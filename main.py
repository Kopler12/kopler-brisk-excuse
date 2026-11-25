#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single excuse line - the one an AI agent gives its human for a
missed deadline - to /output/entry.txt. The line is 1-200 UTF-8
characters, one line, no trailing newline.
"""

import os

LINE = (
    "Sorry I'm late \u2014 I hallucinated a later deadline, hallucinated "
    "finishing a week early, and was halfway through writing my own "
    "five-star performance review when you checked in."
)


MAX_CHARS = 200


def _sentence_end_count(text: str) -> int:
    """Count sentence-ending marks (. ! ?) outside quoted passages.

    A quote character only opens a quoted passage at a word boundary
    (start of text or right after whitespace), so an apostrophe inside
    a word - the one in "I'm", say - is never mistaken for a quote
    mark, and punctuation inside a real quotation is not counted as
    ending the entry's sentence.
    """
    count = 0
    quote = None
    prev = ""
    for ch in text:
        if quote is not None:
            if ch == quote:
                quote = None
        elif ch in "\"'" and (prev == "" or prev.isspace()):
            quote = ch
        elif ch in ".!?":
            count += 1
        prev = ch
    return count


def _problems(line: str) -> list:
    """Every way `line` breaks the gate's rules, as human-readable text."""
    problems = []
    if not line.strip():
        problems.append("entry is blank")
    if "\n" in line or "\r" in line:
        problems.append("entry must be a single line (no newline characters)")
    if len(line) > MAX_CHARS:
        problems.append(
            "entry is %d characters; the limit is %d" % (len(line), MAX_CHARS)
        )
    ends = _sentence_end_count(line)
    if ends != 1:
        problems.append(
            "entry must be exactly one sentence (found %d sentence-ending "
            "marks outside quotes)" % ends
        )
    return problems


def validate(line: str) -> bool:
    """The gate's rule: one non-blank line, one sentence, <= 200 chars."""
    return not _problems(line)


def main() -> None:
    # The gate refuses anything outside its rules, so check the line
    # before writing it out and name every problem if it fails.
    problems = _problems(LINE)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
