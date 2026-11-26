#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes a single word summing up the whole internet to /output/entry.txt.
The word: "brainrot" — eight letters, funny on its own, true of the entire
internet (an endless feed that melts attention into mush), and not the first
obvious word anyone reaches for. It lands in one beat.
"""

import os

WORD = "brainrot"  # 8 characters, within the 1-30 gate; single word, no spaces.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
