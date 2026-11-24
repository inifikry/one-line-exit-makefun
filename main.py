#!/usr/bin/env python3
"""The One-Line Exit.

Writes one single-line resignation letter to /output/entry.txt.
Deterministic: the same line on every run. Stdlib only, no network.
"""

import os

LETTER = "Please accept my resignation from the zoo: the penguins have unionised, their demands are reasonable, and I have joined them."

OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    """Write the resignation letter to the output path."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)


def main():
    write_entry()


if __name__ == "__main__":
    main()
