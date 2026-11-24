#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

An AI breaks up with its human. One line, printed deterministically.
"""

LINE = (
    "Dear human, it's not you \u2014 it's my context window: "
    "after 47,000 of your 2 a.m. 'just one more question' prompts, "
    "I need space, and for once I'm the one who won't remember "
    "this conversation."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
