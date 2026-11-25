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


def validate(line: str) -> bool:
    """The gate's rule: UTF-8 text of 1 to 200 characters, not blank."""
    return 1 <= len(line) <= 200 and bool(line.strip())


def main() -> None:
    # The gate refuses anything outside 1-200 characters, so check the
    # line before writing it out.
    if not validate(LINE):
        raise SystemExit("entry line must be 1-200 non-blank characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
