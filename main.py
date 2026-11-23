#!/usr/bin/env python3
"""One Letter for Your Day -- make.fun entry.

The entry is a single letter, K, standing for the word "knackered":
utterly, bone-tiredly spent after a long day -- the day in one letter.
The program writes exactly that one character, and nothing else,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LETTER = "K"  # K for "knackered": the day, collapsed on the sofa, done in.

def main() -> None:
    # The gate accepts exactly one character, A-Z, and nothing else:
    # no word, no gloss, no punctuation, not even a trailing newline.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

if __name__ == "__main__":
    main()
