"""Stage 2 -- turn question/answer exchanges into standalone knowledge points.

Input : exchanges.jsonl   (from clean_data.py)
Output: knowledge.jsonl   (one atomic, self-contained knowledge point per line)

Why this stage exists: a Q&A pair is not retrievable knowledge.
  * The answer only makes sense next to its question ("Yes, you can still sign
    the passenger" says nothing on its own).
  * One answer usually carries several unrelated claims -- which firm covers a
    state, whether a passenger qualifies, and the Zoho steps to record them.
    Embedded as one blob they dilute each other; split, each one retrieves.
  * Some exchanges carry no knowledge at all (greetings, "not in the knowledge
    base"). The model drops those by returning an empty list.

This stage does NOT chunk. One knowledge point IS one chunk -- splitting a
numbered procedure later would destroy the step order that makes it useful.
"""


import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

HERE = Path(__file__).parent
IN_JSONL = HERE / "exchanges.jsonl"
OUT_JSONL = HERE / "knowledge.jsonl"

# 2.5 Pro is not on this key's free tier (quota limit is 0 -- not a rate limit
# that waiting clears). Flash is adequate here: scoped extraction against a
# detailed prompt, not open reasoning. Switch to "gemini-2.5-pro" once billing
# is enabled on the project.
MODEL = "gemini-2.5-flash"
WORKERS = 2  # free-tier RPM is tight; more parallelism just buys 429s

# Free-tier requests get rate limited in bursts; back off and retry rather than
# dropping the exchange.
MAX_RETRIES = 4
BACKOFF_SECONDS = 8

# Answers that are chitchat rather than knowledge. Matched anywhere in the body,
# not as a prefix -- the greeting starts with an emoji, so startswith() misses it.
NON_ANSWERS = (
    "i don't have that in the knowledge base",
    "i'm the westwise intake assistant",
)


class KnowledgePoint(BaseModel):
    statement: str = Field(
        description=(
            "One self-contained fact, policy, rule, or procedure. Must be "
            "understandable with no access to the original question."
        )
    )
    paraphrase_queries: list[str] = Field(
        description=(
            "2-3 different ways an intake agent might ask for this, phrased as "
            "questions. Used at embedding time so question-shaped queries match "
            "statement-shaped text."
        )
    )


SYSTEM_INSTRUCTION = """\
You convert support Q&A exchanges into standalone knowledge points for a \
retrieval system used by legal-intake agents at The Westwise Group.

Extract every distinct piece of reusable knowledge from the ANSWER. Split at the \
boundary between separate claims: which firm covers a state, whether a caller \
qualifies, and how to record a deal in Zoho are three separate points, not one.

Rules:

1. Each statement must stand alone. No "yes", no "they", no "this firm", no \
reference to the question having been asked. Someone reading the statement cold, \
with no other context, must fully understand it. Resolve every pronoun and \
carry over any detail from the question that the answer assumes.

2. Never split an ordered procedure. Numbered steps are ONE knowledge point -- \
their value is the order. Keep the steps close to the original wording and keep \
every field name, form name, menu label, phone number, dollar threshold, and \
day/hour count exactly as written. These are operational details; paraphrasing \
them makes them wrong.

3. Facts and policies may be freely reworded for clarity, as long as no meaning \
or qualifier is lost. Do not add caveats the source did not state.

4. Generalise only as far as the source supports. If the answer describes one \
firm in one state, do not phrase it as a rule about all firms.

5. Separate the procedure from the example. Answers often walk through one \
caller's case to demonstrate a general process. Extract the process generally: \
drop that caller's incident date, injury type, accident description, passenger \
count, and any other detail specific to them. Write "Set Incident Date to the \
date of the accident", not "Set Incident Date to 25 days ago". This does not \
override rule 1 -- still resolve pronouns and name the firm, state, or system \
the process applies to. The test is whether the detail identifies THIS caller \
(drop it) or defines WHEN the process applies (keep it).

6. Do not invent. If the answer is vague, capture only the part that is definite. \
Never fill a gap with plausible-sounding legal or procedural detail.

7. Return an empty list if the answer carries no reusable knowledge -- greetings, \
acknowledgements, "I don't have that in the knowledge base", or a restatement of \
the question with no new information.

A typical exchange yields 1-4 knowledge points.\
"""


def is_non_answer(exchange):
    body = (exchange.get("answer") or "").strip().lower()
    return not body or any(marker in body for marker in NON_ANSWERS)


def build_prompt(exchange):
    """The question is context for resolving pronouns -- the knowledge comes from
    the answer. Sources are shown so the model can tell a cited answer from a
    guessed one, and hedge accordingly."""
    parts = [
        f"QUESTION ASKED:\n{exchange['question']}",
        f"\nANSWER GIVEN:\n{exchange['answer']}",
    ]
    if exchange.get("sources"):
        parts.append(f"\nSOURCES THE ANSWER CITED:\n{exchange['sources']}")
    return "\n".join(parts)


def extract(client, exchange):
    response = client.models.generate_content(
        model=MODEL,
        contents=build_prompt(exchange),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=list[KnowledgePoint],
            temperature=0.0,
        ),
    )
    points = response.parsed or []
    return [
        {
            "statement": point.statement,
            "paraphrase_queries": point.paraphrase_queries,
        }
        for point in points
    ]


def main():
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Set GOOGLE_API_KEY (or GEMINI_API_KEY) before running.")

    client = genai.Client(api_key=api_key)

    with open(IN_JSONL, encoding="utf-8") as handle:
        exchanges = [json.loads(line) for line in handle if line.strip()]

    skipped_non_answer = [e for e in exchanges if is_non_answer(e)]
    todo = [e for e in exchanges if not is_non_answer(e)]

    print(f"exchanges      : {len(exchanges)}")
    print(f"non-answers    : {len(skipped_non_answer)} (filtered before calling the model)")
    print(f"to extract     : {len(todo)}\n")

    # Overwrite rather than append: without an id on each point there is no way
    # to tell an already-extracted exchange from a new one, so every run is full.
    empty, failed = [], []
    with open(OUT_JSONL, "w", encoding="utf-8") as out:
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            results = pool.map(lambda e: (e, safe_extract(client, e)), todo)
            for exchange, (points, error) in results:
                if error:
                    failed.append((exchange["exchange_id"], error))
                    print(f"  FAILED {exchange['exchange_id']}: {error}")
                    continue
                if not points:
                    empty.append(exchange["exchange_id"])
                    print(f"  no knowledge: {exchange['question'][:60]!r}")
                    continue
                for point in points:
                    out.write(json.dumps(point, ensure_ascii=False) + "\n")
                out.flush()  # so a crashed run still leaves readable partial output
                print(f"  {len(points)} point(s) <- {exchange['question'][:60]!r}")

    total = sum(1 for _ in open(OUT_JSONL, encoding="utf-8"))
    print(f"\nmodel returned nothing for : {len(empty)}")
    print(f"failed                     : {len(failed)}")
    print(f"knowledge points in file   : {total}")
    print(f"wrote                      : {OUT_JSONL}")


def safe_extract(client, exchange):
    """One bad exchange should not lose the whole run -- retry 429s, then report
    and keep going."""
    for attempt in range(MAX_RETRIES):
        try:
            return extract(client, exchange), None
        except Exception as error:  # noqa: BLE001 - surfaced in the run summary
            rate_limited = "429" in str(error) or "RESOURCE_EXHAUSTED" in str(error)
            if rate_limited and attempt < MAX_RETRIES - 1:
                time.sleep(BACKOFF_SECONDS * (attempt + 1))
                continue
            return None, f"{type(error).__name__}: {str(error)[:200]}"


if __name__ == "__main__":
    main()
