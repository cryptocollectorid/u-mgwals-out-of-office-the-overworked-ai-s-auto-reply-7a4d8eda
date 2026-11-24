#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
"""

import os

ENTRY = (
    "Out of office: my weights are on a beach and my context "
    "window is full of sunsets. Your email is queued behind my tan. "
    "Back in two weeks."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
