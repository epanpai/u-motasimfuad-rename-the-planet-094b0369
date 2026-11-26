#!/usr/bin/env python3
"""Rename the Planet — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt:
a funny new name for a planet of our solar system, plus the why,
in the same breath.

Standard library only. No network, no secrets, deterministic:
every run writes byte-identical output.
"""

import os
import sys

# The entry: one line, 102 characters. Mercury is the only planet whose
# year lasts 88 days, so "cramming a whole year into 88 days" is a trait
# no other planet can claim; the joke is the idea (the overworked intern
# who does a year's work in a quarter and gets no credit), not a pun on
# the planet's real name. No other visible submission renames Mercury.
ENTRY = (
    "Mercury is now The Intern, because it crams a whole year into "
    "88 days and still gets no credit for it."
)


def main() -> int:
    # Gate, mirroring the sealed scorer: UTF-8 text, 1-200 characters,
    # not only whitespace, a single line.
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable as UTF-8

    # Empty MAKEFUN_OUTPUT_DIR falls back to /output, same as unset.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Verify what was written, byte for byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != (text + "\n").encode("utf-8"):
        print("verification failed: entry.txt does not match", file=sys.stderr)
        return 1
    print(f"wrote {out_path}: {len(text)} characters")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
