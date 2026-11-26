#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun bounty entry.

Writes the unsent micro-confession to /output/entry.txt: a To: line naming who it was meant for, and the unsent line itself, exactly as typed. Specific, honest, and it stayed in drafts because it was never said out loud.
"""

import os

ENTRY = 'To: my old team lead\nI never said it, but the night you stayed late to fix my deploy, I stayed too — not for the code, for you.'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 260, f"entry is {len(text)} chars, must be 1-260"
    assert text.strip(), "entry must not be only whitespace"
    parts = text.split("\n")
    assert len(parts) == 2, "entry must be exactly two parts: a To: line and the unsent line"
    assert parts[0].startswith("To: "), "first part must be a To: line"
    assert parts[1].strip(), "unsent line must not be empty"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
