#!/usr/bin/env python3
"""One-line weather forecast entry for the make.fun bounty
"Charm the Commuter: Forecast a City That Isn't".

Writes exactly one line — a forecast for the invented city of
Gloomsbury — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes: the line keeps the rhythm of a real broadcast forecast
(city, temperature, rain until a time) and then bends it — sunshine
for exactly one commuter, a warm bus, a short queue, dry socks. The
concrete details (the bus, the queue, the socks) make Gloomsbury feel
like a place a commuter actually stands in, and the small joke is the
forecast caring about one person's morning.
"""

import os

ENTRY = (
    "Gloomsbury: 10\u00b0C, rain until 5pm, then sunshine for exactly one "
    "commuter \u2014 the bus is warm, the queue is short, and your socks "
    "stay dry."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
