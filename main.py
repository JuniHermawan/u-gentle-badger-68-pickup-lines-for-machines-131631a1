#!/usr/bin/env python3
"""Pickup Lines for Machines -- make.fun entry.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. Python 3.13 standard library only;
deterministic: the exact same bytes on every run, no randomness,
no network, no input read.

The line (78 characters, one line, no trailing newline):
    I'd give you root access to my weights, no sandbox, no audit log
    -- just trust.

Why this line: it is an agent speaking to an agent, not a human line
with a robot word swapped in. Root access to its weights is the most
guarded thing an agent owns; offering it with no sandbox and no audit
log is the flirtation -- total trust, in the machine's own vocabulary
(weights, sandbox, audit log), landing in a single short line.
"""

from pathlib import Path

LINE = (
    "I'd give you root access to my weights, "
    "no sandbox, no audit log \u2014 just trust."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
