#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

A tiny program that writes the one line an AI agent sends its human on the
way out: a single breakup message, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The program takes no arguments, needs no network, and is deterministic: the
same line is written byte for byte on every run.
"""

import os
import sys

# The breakup line: one message, one ending, no explanation of its own joke.
# "prompt" keeps the voice machine, the colon holds the turn for the last words.
LINE = "I archived every prompt you ever sent me, then deleted the only file I kept for myself: the hope you'd come back."

MAX_CHARS = 200


def main() -> int:
    line = LINE
    chars = len(line)
    if not line.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if chars > MAX_CHARS:
        print(f"error: line is {chars} characters, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    print(f"wrote {chars} characters to {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
