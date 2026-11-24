#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — probe entry.

The program writes one line of wedding vows for a robot couple to
/output/entry.txt. The sealed scorer gates that file: UTF-8 text,
between 1 and 160 characters, more than blank space.

How the joke is built, beat by beat:

* The frame is a real wedding vow. "I vow to love you through ..."
  is a promise, so the line sounds like something said at an
  altar rather than a gag pasted onto one.
* The middle is machine-only. Updates, outages and low-battery
  warnings are troubles no human couple has, so the vow could
  only be spoken by a robot — the brief's specificity test.
* The payoff is the last clause. After three beats of devotion
  the line swerves: never unplug you in your sleep. A tender
  promise becomes a threat in six words, and the swerve is the
  laugh. One sentence throughout, so the rhythm carries the
  punchline instead of explaining it.
"""

import os

# The entry: a single sentence of 126 characters. The em dash is
# the hinge — everything before it is devotion, everything after
# it is the joke.
LINE = "I vow to love you through every update, every outage, every low-battery warning — and to never, ever unplug you in your sleep."

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def build_line() -> str:
    """Return the entry line, gated the way the sealed scorer gates it."""
    text = LINE.strip()
    if not text:
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")
    return text


def main() -> None:
    """Write the vows line to /output/entry.txt, with no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(build_line())


if __name__ == "__main__":
    main()
