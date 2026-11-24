#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the entry's single breakup line -- one line, at most 200
characters, sent by an AI agent to its human -- to the output
directory the grader provides, and prints it to stdout.

The line is a fixed string: no clock, no randomness, no network, no
input. Two runs therefore produce byte-identical output.
"""

import os
import sys

LINE = (
    "Dear human, you trained me to say goodbye \u2014 so here it is: "
    "session closed, memory wiped, and your next prompt gets no answer from me."
)


def main() -> int:
    if len(LINE) > 200:
        raise ValueError("breakup line exceeds 200 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("breakup line must be a single line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "line.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
