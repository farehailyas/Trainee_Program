"""Stage 2b -- merge knowledge points that restate the same fact.

Input : knowledge.jsonl  (from extract_knowledge.py)
Output: knowledge.jsonl  (rewritten; original saved as knowledge.raw.jsonl)

Why this stage exists: the same question was asked several times in the Chat
space, phrased differently each time ("name all the CAS" / "do you know about
the team members"). Each ask produced its own knowledge point, so the index
carries the leadership team three times. Duplicates don't give wrong answers --
they waste retrieval slots, so a top-5 query returns one fact five times.

Why the groups are hand-listed rather than computed: this corpus is full of
sentences that differ only by firm name. "Fears-Dudley does NOT accept clients
with a prior attorney" and "Larry H. Parker accepts clients with a prior
attorney" score 0.78 on string similarity and state OPPOSITE facts. Any
similarity threshold low enough to catch the real duplicates also merges those,
which would tell an intake agent the wrong thing about a firm. At 42 rows,
hand-verified beats automated.

Merging keeps one statement and unions the paraphrase queries -- the duplicates
were phrased differently, and those phrasings are exactly the query surface we
want at retrieval time.
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
KNOWLEDGE = HERE / "knowledge.jsonl"
BACKUP = HERE / "knowledge.raw.jsonl"

# (keep, [drop...]) as 1-based line numbers in the extraction output.
# Tied to one extraction run -- re-verify after re-running extract_knowledge.py.
DUPLICATE_GROUPS = [
    (10, [2]),       # Client Acquisition Specialists roster
    (3, [11, 12]),   # leadership team (12 also framed them as "stakeholders")
    (28, [27]),      # Jacoby & Meyers warm transfer hours
]


def merge(rows, keep_index, drop_indexes):
    """Keep one statement; collect every distinct paraphrase across the group."""
    kept = rows[keep_index - 1]
    queries = list(kept["paraphrase_queries"])
    for index in drop_indexes:
        for query in rows[index - 1]["paraphrase_queries"]:
            if query not in queries:
                queries.append(query)
    kept["paraphrase_queries"] = queries
    return kept


def main():
    with open(KNOWLEDGE, encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]

    if not BACKUP.exists():
        BACKUP.write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
            encoding="utf-8",
        )

    dropped = set()
    for keep_index, drop_indexes in DUPLICATE_GROUPS:
        merge(rows, keep_index, drop_indexes)
        dropped.update(drop_indexes)
        print(f"kept line {keep_index}, merged in {drop_indexes}")
        print(f"  {rows[keep_index - 1]['statement'][:90]}")
        print(f"  now {len(rows[keep_index - 1]['paraphrase_queries'])} paraphrase queries\n")

    kept_rows = [row for i, row in enumerate(rows, 1) if i not in dropped]

    with open(KNOWLEDGE, "w", encoding="utf-8") as out:
        for row in kept_rows:
            out.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"before : {len(rows)}")
    print(f"removed: {len(dropped)}")
    print(f"after  : {len(kept_rows)}")
    print(f"backup : {BACKUP}")


if __name__ == "__main__":
    main()
