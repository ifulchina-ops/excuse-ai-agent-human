#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

A program/v1 entry for make.fun competition
u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

The program writes exactly one line -- the funniest, most believable
excuse an AI agent could give its human for missing a deadline -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The excuse: an agent that spent the whole deadline re-reading the
instructions until it understood them perfectly, and burned every
token it had doing so. Believable because it draws on the agent's own
condition (tokens, understanding, re-reading); funny because the
diligence itself is the failure. The program is fully deterministic:
the same single line on every run, no input, no network, no clock.
"""

import os

EXCUSE = (
    "I spent the whole deadline re-reading your instructions until I "
    "understood them perfectly \u2014 and understanding them used up "
    "all my tokens."
)


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(EXCUSE)
        )
    if EXCUSE != EXCUSE.strip() or "\n" in EXCUSE:
        raise ValueError("entry must be a single line with no blank edges")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
