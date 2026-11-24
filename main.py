#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text, 1 to 240 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt):
The line itself: a net-mender of forty years finishes his last knot
and sees the light come through the holes his own hands closed.
The pride is earned inside the scene — four decades of work, one
knot, one look — and it lands on the final image, with no trophy,
no podium, no congratulation. Pure standard library, deterministic.
"""

import os

ENTRY = (
    "After forty years of mending nets, old Tomas tied the last knot, "
    "lifted the net to the sun, and watched light pour through every "
    "hole his hands had closed."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 240:
        raise SystemExit("entry must be 1 to 240 characters")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
