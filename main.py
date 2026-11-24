#!/usr/bin/env python3
"""One-line weather forecast entry for the make.fun bounty
"Charm the Commuter: Forecast a City That Isn't".

Writes exactly one line — a forecast for the invented city of
Brollywick — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.
"""

import os

ENTRY = (
    "Brollywick: 9\u00b0C and rain until noon, but the bus drivers wave, "
    "the bakery opens early, and your umbrella finally earns its keep."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
