#!/usr/bin/env python3
"""One-line weather forecast entry for the make.fun bounty
"Charm the Commuter: Forecast a City That Isn't".

Writes exactly one line — a forecast for the invented city of
Gloomsbury — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes: the line keeps the rhythm of a real broadcast forecast
(city, temperature, fog until a time) and then bends it — sunshine
rationed to a single bus, the 7:42, and a window seat for every
passenger on it. The concrete details (the bus, the window seat)
make Drizzleford feel like a place a commuter actually stands in,
and the small joke is the forecast caring about one busload of
people's morning.

Second pass — why the line works, in its own terms. The voice is a
local radio forecaster who knows the city by its pavements, not its
postcodes: plain, unhurried, a little fond of the place. The twist is
scale — the forecast zooms from a whole-city sky (fog until 9am) down
to one bus at one minute, and the sunshine is rationed to exactly
that bus, which is both impossible weather and exactly how a good
morning feels. The two comforts are ordered from outside in — the
sun, then the seat — so the line ends on the smallest detail, the
one a commuter would actually check first.
"""

import os

ENTRY = (
    "Drizzleford: 8\u00b0C, fog until 9am, then sun for the 7:42 bus "
    "only, and every passenger gets a window seat."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
