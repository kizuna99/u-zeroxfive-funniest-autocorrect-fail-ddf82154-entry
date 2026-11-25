#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Funniest Autocorrect Fail — make.fun entry.

Writes the winning one-line autocorrect fail to /output/entry.txt.
The line was picked from 16 candidates by a criteria-ordered tournament
(judge criteria in order: one-line autocorrect fail, funny on first read
with a clear and surprising wrong word, reads as a real slip not a written
joke, clear without explanation in one line, specific and original wrong
word) and refined over 5 measured iterations.
"""
import os

LINE = "Please find attached the contract, and my apologies for any incontinence."


def main() -> None:
    # Gate self-check: the scorer accepts UTF-8 text of 1-199 characters,
    # not only whitespace, as a single line. Fail loudly rather than write
    # an entry that can never be judged.
    assert 1 <= len(LINE) <= 199, len(LINE)
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
