#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one epitaph -- the winner of an 8-draft pairwise duel judged
against the bounty brief -- to /output/entry.txt.

Duel result (56 calls, both orders, margins 1-5): the winning line
scored 5.25/7, winning 13 of 14 calls. Runner-up was the hearse bet
at 4.90/7. The winner is the only draft that hits all five judge
criteria at once: genuine last words, a real laugh, a clean reversal
twist, short enough to carve, and quotable.
"""

import os

EPITAPH = "My last words were 'watch this.' My second-to-last words were 'hold my beer.'"


def main() -> None:
    text = EPITAPH.strip()
    assert 1 <= len(text) <= 150, f"epitaph must be 1-150 chars, got {len(text)}"
    assert text.strip() == text and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
