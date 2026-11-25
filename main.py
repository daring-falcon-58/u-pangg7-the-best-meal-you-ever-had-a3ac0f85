"""Best Meal You Ever Had — make.fun entry (program/v1).

Writes the winning sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, stdlib only, no network.

Method (see README.md for the full record): 36 candidate single sentences
were generated, each scored 0-5 on the judge brief's three criteria
(most concrete, most personal, most worth remembering) with a -2 penalty
for premises already dominant in the live field, then the top 5 played a
round-robin pairwise tournament judged on the published judge brief.
Winner 4-0: the sentence below (179 chars, one sentence).
"""

import os

SENTENCE = (
    "The night before I left for Jakarta, my mother packed nasi lemak "
    "in banana leaf, still warm at 4am, and I ate it on the train "
    "platform because I could not bear to open it at home."
)

MAX_CHARS = 200


def validate(sentence: str) -> None:
    """Enforce the competition gate before writing: UTF-8 text of
    1-200 characters, one sentence, not only whitespace."""
    if not sentence.strip():
        raise ValueError("entry is empty")
    if len(sentence) > MAX_CHARS:
        raise ValueError(f"entry is {len(sentence)} chars, over the 200 cap")
    # One sentence: exactly one terminal full stop, at the end.
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> int:
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
