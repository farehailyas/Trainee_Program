"""Stage 1 — clean the Google Chat export and pair questions with their answers.

Input : chat_messages_YYYY-MM-DD.csv  (dlt export of the Chat space, originally ClickHouse)
Output: exchanges.jsonl              (one resolved question/answer exchange per line)

Why this stage exists: the raw export cannot be embedded as-is.
  * A bot answer lives in `cards_v2` JSON, not in `text` (56/139 rows have empty text).
  * In most of the history the bot answered at room level, so the answer sits in a
    DIFFERENT thread than the question -- 53 of 55 pairs. Thread grouping alone loses them.
    Only messages after 2026-07-23 16:53 use real thread replies.
  * Acks, greetings and "not in the knowledge base" replies carry no knowledge.
"""

import csv
import html
import json
import re
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
IN_CSV = HERE / "chat_messages_2026-07-29.csv"
OUT_JSONL = HERE / "exchanges.jsonl"

# A bot reply this long after a question is not an answer to it.
MAX_PAIR_GAP_S = 180

ACK_MARKERS = ("Looking into that",)
NON_ANSWERS = (
    "i don't have that in the knowledge base",
    "i'm the westwise intake assistant",
)
GREETINGS = {"hi", "hey", "hello", "yo", "thanks", "thank you", "ok", "okay", ""}
TS_FMT = "%Y-%m-%d %H:%M:%S"


def strip_html(text):
    """Card bodies are HTML: <b>, <br>, entities. Keep the line breaks, drop the tags."""
    text = re.sub(r"<br\s*/?>", "\n", text or "")
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def parse_card(cards_v2):
    """Split an answer card into (body, sources, reasoning).

    Only the header-less section is the answer. The '📚 Sources' and '🧠 How I got this'
    sections are provenance -- kept as metadata, never embedded as answer text.
    """
    if not (cards_v2 or "").strip():
        return None, None, None
    try:
        cards = json.loads(cards_v2)
    except json.JSONDecodeError:
        return None, None, None

    body, sources, reasoning = [], [], []
    for card in cards:
        for section in card.get("card", {}).get("sections", []):
            header = section.get("header", "") or ""
            if "Sources" in header:
                bucket = sources
            elif "How I got" in header:
                bucket = reasoning
            elif header:
                continue  # unknown titled section -- ignore rather than pollute the answer
            else:
                bucket = body
            for widget in section.get("widgets", []):
                paragraph = widget.get("textParagraph", {}).get("text")
                if paragraph:
                    bucket.append(strip_html(paragraph))

    return (
        "\n".join(body) or None,
        "\n".join(sources) or None,
        "\n".join(reasoning) or None,
    )


def load_messages(path):
    messages = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            sender = json.loads(row["sender"])
            body, sources, reasoning = parse_card(row["cards_v2"])
            # argument_text is the human text with the @mention already removed.
            plain = strip_html(row["argument_text"] or row["text"])
            messages.append(
                {
                    "id": row["name"].split("/")[-1],
                    "at": row["create_time"][:19],
                    "who": sender["type"],  # HUMAN | BOT
                    "user": sender["name"],
                    "thread": json.loads(row["thread"])["name"].split("/")[-1],
                    "is_thread_reply": row["thread_reply"] == "true",
                    "body": body or plain,
                    "sources": sources,
                    "reasoning": reasoning,
                    "from_card": bool(body),
                }
            )
    messages.sort(key=lambda m: m["at"])
    return messages


def is_ack(message):
    return any(marker in (message["body"] or "") for marker in ACK_MARKERS)


def is_question(message):
    """Chitchat and operator notes are not questions worth answering."""
    body = (message["body"] or "").strip()
    if body.lower() in GREETINGS:
        return False
    if body.lower().endswith("-- ignore") or "@Kamal" in body or "@Kennedy" in body:
        return False  # team announcements about the bot itself
    return len(body.split()) >= 4


def is_real_answer(message):
    body = (message["body"] or "").strip()
    if not body or is_ack(message):
        return False
    return not any(body.lower().startswith(prefix) for prefix in NON_ANSWERS)


def pair_exchanges(messages):
    """Answer = the next non-ack reply, either a real thread reply or a room-level
    reply close in time. Anyone may answer, bot or human -- the knowledge counts either way."""
    exchanges, used = [], set()

    for i, question in enumerate(messages):
        if question["who"] != "HUMAN" or not is_question(question):
            continue

        asked_at = datetime.strptime(question["at"], TS_FMT)
        for candidate in messages[i + 1 :]:
            if candidate["id"] in used or is_ack(candidate):
                continue
            gap = (datetime.strptime(candidate["at"], TS_FMT) - asked_at).total_seconds()
            in_thread = candidate["is_thread_reply"] and candidate["thread"] == question["thread"]
            if not in_thread and gap > MAX_PAIR_GAP_S:
                break
            # Another human asking their own question is not an answer to this one.
            if candidate["who"] == "HUMAN" and is_question(candidate):
                break
            if not is_real_answer(candidate):
                continue

            used.add(candidate["id"])
            exchanges.append(
                {
                    "exchange_id": question["id"],
                    "asked_at": question["at"],
                    "asker": question["user"],
                    "question": question["body"],
                    "answer": candidate["body"],
                    "answered_by": candidate["who"],
                    "answerer": candidate["user"],
                    "pairing": "thread" if in_thread else "adjacent",
                    "gap_seconds": gap,
                    "sources": candidate["sources"],
                    "reasoning": candidate["reasoning"],
                }
            )
            break

    return exchanges


def main():
    messages = load_messages(IN_CSV)
    exchanges = pair_exchanges(messages)

    with open(OUT_JSONL, "w", encoding="utf-8") as handle:
        for exchange in exchanges:
            handle.write(json.dumps(exchange, ensure_ascii=False) + "\n")

    humans = sum(1 for m in messages if m["who"] == "HUMAN")
    by_human = sum(1 for e in exchanges if e["answered_by"] == "HUMAN")
    print(f"messages       : {len(messages)} ({humans} human, {len(messages) - humans} bot)")
    print(f"questions kept : {sum(1 for m in messages if m['who'] == 'HUMAN' and is_question(m))}")
    print(f"exchanges      : {len(exchanges)}  ({by_human} answered by a human)")
    print(f"pairing        : {sum(1 for e in exchanges if e['pairing'] == 'thread')} thread, "
          f"{sum(1 for e in exchanges if e['pairing'] == 'adjacent')} adjacent")
    print(f"wrote          : {OUT_JSONL}")


if __name__ == "__main__":
    main()
