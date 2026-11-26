#!/usr/bin/env python3
"""One-line weather forecast entry for the make.fun bounty
"Charm the Commuter: Forecast a City That Isn't".

Writes exactly one line — a forecast for the invented city of
Brollyton — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes: the line keeps the rhythm of a real broadcast forecast
(city, temperature, rain with a precise pause time) and then bends
it — the weather itself cooperates with the morning rush. The rain
pauses at 8:03, the puddles part for the commuter's shoes, and the
bus arrives two minutes early: three small kindnesses, each one
concrete, each one something a commuter at a wet bus stop actually
wishes for. The joke is that the forecast is not describing weather
at all, but a city being polite.

Second pass — why the line works, in its own terms. The voice is a
local radio forecaster who knows the city by its pavements, not its
postcodes: plain, unhurried, a little fond of the place. The twist
is courtesy — the weather behaves like a good neighbour, pausing
its rain and parting its puddles on schedule, and the line ends on
the smallest, most welcome detail of all, a bus that is early
instead of late. The three kindnesses are ordered from sky to
street to timetable, so the line lands on the one a commuter would
actually check first.
"""

import os

ENTRY = (
    "Brollyton: 9\u00b0C, rain pauses at 8:03 for the morning rush, "
    "puddles part for your shoes, and the bus arrives two minutes early."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
