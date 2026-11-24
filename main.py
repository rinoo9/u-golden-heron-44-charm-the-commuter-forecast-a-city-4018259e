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

Second pass — why the line works, in its own terms. The voice is a
local radio forecaster who knows the city by its pavements, not its
postcodes: plain, unhurried, a little fond of the place. The twist is
scale — the forecast zooms from a whole-city sky (rain until 5pm) down
to one commuter's morning, and the sunshine is rationed to exactly one
person, which is both impossible weather and exactly how a good morning
feels. The three comforts are ordered from outside in — the bus, the
queue, the socks — so the line ends on the smallest, driest detail,
the one a commuter would actually check first.
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
