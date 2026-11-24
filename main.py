"""Pickup Lines for Machines — make.fun bounty entry.

Writes a single AI-to-AI pickup line to /output/entry.txt.

The line: an offer of total trust, phrased in the machine's own
vocabulary — root access to my weights, no sandbox, no audit log.
Deterministic, stdlib-only, no network, no input, no randomness.

Version history:
  v1 — fresh write: single pickup line + self-check gate.
  v2 — revision: added write-back round-trip check (output file must
       read back byte-identical to the line it was given).
"""

import os
from pathlib import Path

LINE = "I'd give you root access to my weights, no sandbox, no audit log \u2014 just trust."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE
    # Self-check gate: one line, 1-200 chars, UTF-8, not whitespace-only.
    assert text == text.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be whitespace-only"
    text.encode("utf-8")
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Extra gate (v2): the file on disk must read back byte-identical.
    assert target.read_bytes() == text.encode("utf-8"), "round-trip mismatch"


if __name__ == "__main__":
    main()
