#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun bounty entry.

Writes the unsent micro-confession to /output/entry.txt: a To: line naming who it was meant for, and the unsent line itself, exactly as typed. Specific, honest, and it stayed unsent because it was never spoken aloud.
"""

import os
import sys

ENTRY = 'To: my old team lead\nI never said it, but the night you stayed late to fix my deploy, I stayed too — not for the code, for you.'

MAX_CHARS = 260


def _fail(reason):
    sys.exit(f"entry rejected: {reason}")


def _check_confession(text):
    if not text.strip():
        _fail("nothing to send: the confession is blank")
    if len(text) > MAX_CHARS:
        _fail("confession runs past the character limit")
    lines = text.split("\n")
    if len(lines) != 2:
        _fail("confession needs a To: line and one unsent line")
    if not lines[0].startswith("To: "):
        _fail("first line must start with To:")
    if not lines[1].strip():
        _fail("unsent line is empty")
    if text != text.strip():
        _fail("confession has leading or trailing whitespace")


def main():
    _check_confession(ENTRY)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
