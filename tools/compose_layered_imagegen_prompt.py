#!/usr/bin/env python3
"""Compose layered ImageGen prompts for the Pi Tarot deck.

Prompt layers live under:

    assets/tarot-cards-imagegen/prompts/layered/

Each final prompt is built as:

    rootPrompt + optional suitPrompt + arcanaPrompt

Major Arcana cards intentionally skip the suit layer.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "tarot-cards-imagegen"
METADATA = BASE / "metadata.json"
LAYERED = BASE / "prompts" / "layered"
ROOT_PROMPT = LAYERED / "root.md"
SUIT_DIR = LAYERED / "suits"
ARCANA_DIR = LAYERED / "arcana"
COMPOSED_DIR = LAYERED / "composed"


def load_cards() -> list[dict]:
    data = json.loads(METADATA.read_text(encoding="utf-8"))
    return data["cards"]


def card_suit(card: dict) -> str | None:
    if card["arcana"] == "major":
        return None
    return card["filename"].split("_", 2)[1]


def arcana_prompt_path(card: dict) -> Path:
    suit = card_suit(card) or "major"
    return ARCANA_DIR / suit / card["filename"].replace(".png", ".md")


def read_layer(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8").strip()


def compose_card(card: dict) -> str:
    layers = [
        ("rootPrompt", ROOT_PROMPT),
    ]
    suit = card_suit(card)
    if suit:
        layers.append((f"{suit}SuitPrompt", SUIT_DIR / f"{suit}.md"))
    layers.append(("arcanaPrompt", arcana_prompt_path(card)))

    chunks = []
    for label, path in layers:
        chunks.append(f"## {label}\n\n{read_layer(path)}")

    return "\n\n---\n\n".join(chunks).strip() + "\n"


def select_cards(cards: list[dict], names: list[str]) -> list[dict]:
    if not names:
        return cards

    by_key: dict[str, dict] = {}
    for card in cards:
        stem = card["filename"].removesuffix(".png")
        keys = {
            card["id"],
            card["slug"],
            card["name"].lower(),
            card["filename"],
            stem,
        }
        if card.get("number"):
            keys.add(card["number"])
        for key in keys:
            by_key[key] = card

    selected = []
    missing = []
    for name in names:
        card = by_key.get(name) or by_key.get(name.lower())
        if card is None:
            missing.append(name)
        else:
            selected.append(card)

    if missing:
        raise SystemExit(f"Unknown card selector(s): {', '.join(missing)}")
    return selected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cards",
        nargs="*",
        help="Optional card selectors: id, number, slug, filename, stem, or English name.",
    )
    parser.add_argument(
        "--out-dir",
        default=str(COMPOSED_DIR),
        help="Directory for composed Markdown prompts.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print one composed prompt to stdout instead of writing files.",
    )
    args = parser.parse_args()

    cards = select_cards(load_cards(), args.cards)
    if args.stdout:
        if len(cards) != 1:
            raise SystemExit("--stdout requires exactly one selected card")
        sys.stdout.write(compose_card(cards[0]))
        return 0

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for card in cards:
        out = out_dir / card["filename"].replace(".png", ".md")
        out.write_text(compose_card(card), encoding="utf-8")
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
