#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes one kind, funny fortune for a houseplant (under 120 characters)
to /output/entry.txt, creating /output if needed.
"""

import os
import sys

ENTRY = (
    "A draught from the window will bring you gossip from the garden, "
    "and by spring you'll know every secret the roses keep."
)

# The grader sets MAKEFUN_OUTPUT_DIR=/output and runs with no arguments
# in a read-only working directory, so honour the env var first, then an
# optional argv path, and only then fall back to /output (never ".").
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
    sys.argv[1] if len(sys.argv) > 1 else "/output"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120 and ENTRY.strip(), "entry must be 1-120 chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
