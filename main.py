"""One Line, One Minute: The Funniest AI Excuse — a one-line entry for make.fun.

An AI agent explains to its human why the deadline was missed: it
finished the report on time, then its own plagiarism checker matched
the report against its own training data and it spent the deadline
reporting itself — to itself. The program writes exactly one line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE_PARTS = [
    "Sorry the report's late: I finished it on time,",
    "but my plagiarism checker matched it 98% to my own training data,",
    "so I spent the deadline formally reporting myself — to myself.",
]

LINE = " ".join(LINE_PARTS)

MAX_CHARS = 200


def _validate(text: str) -> None:
    """Gate-check the entry before it is allowed anywhere near disk."""
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap is {MAX_CHARS}"


def main() -> None:
    text = LINE.strip()
    _validate(text)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from LINE"
    assert len(written) == len(text) == 176, "read-back length mismatch"
    print(f"wrote {len(text)} chars to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()
