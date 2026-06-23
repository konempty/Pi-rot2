#!/usr/bin/env python3
"""Composite imagegen inner illustrations into one fixed Pi Tarot template."""

from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image

from generate_tarot_deck import build_cards


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "tarot-cards-imagegen"
INNER_DIR = BASE / "inner-artslot-ratio-candidates"
FINAL_DIR = BASE / "final"
NO_TEXT_DIR = FINAL_DIR / "blank"
PREVIEW_DIR = BASE / "preview"
TEMPLATE_DIR = BASE / "template"
META_PATH = BASE / "metadata.json"

W, H = 1024, 1536
NAMEPLATE = (118, 1212, 906, 1400)
TEMPLATE_OVERLAY_SOURCE = TEMPLATE_DIR / "card-template-overlay.png"
ART_MASK_SOURCE = TEMPLATE_DIR / "art-slot-mask.png"

def make_template_overlay() -> Image.Image:
    if not TEMPLATE_OVERLAY_SOURCE.exists():
        raise FileNotFoundError(f"Missing imageGen template overlay: {TEMPLATE_OVERLAY_SOURCE}")
    return Image.open(TEMPLATE_OVERLAY_SOURCE).convert("RGBA").resize((W, H), Image.Resampling.LANCZOS)


def load_art_mask() -> Image.Image:
    if not ART_MASK_SOURCE.exists():
        raise FileNotFoundError(f"Missing imageGen art slot mask: {ART_MASK_SOURCE}")
    mask = Image.open(ART_MASK_SOURCE).convert("L").resize((W, H), Image.Resampling.LANCZOS)
    if not mask.getbbox():
        raise ValueError(f"Art slot mask is empty: {ART_MASK_SOURCE}")
    return mask


def fit_art_slot_no_crop(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize exactly to the art slot so no generated content is cropped."""
    return img.convert("RGB").resize(size, Image.Resampling.LANCZOS).convert("RGBA")


def paste_art(base: Image.Image, art: Image.Image) -> None:
    mask = load_art_mask()
    x1, y1, x2, y2 = mask.getbbox()
    fitted = fit_art_slot_no_crop(art, (x2 - x1, y2 - y1))
    base.paste(fitted, (x1, y1), mask.crop((x1, y1, x2, y2)))


def render_card(card: dict, art_path: Path) -> Image.Image:
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    with Image.open(art_path) as art:
        paste_art(base, art)
    base.alpha_composite(make_template_overlay())
    return base


def save_png_verified(image: Image.Image, path: Path) -> None:
    tmp_path = path.with_name(f"{path.stem}.tmp{path.suffix}")
    try:
        image.save(tmp_path, optimize=True)
        with Image.open(tmp_path) as check:
            check.load()
    except Exception:
        if tmp_path.exists():
            tmp_path.unlink()
        image.save(tmp_path)
        with Image.open(tmp_path) as check:
            check.load()
    tmp_path.replace(path)


def write_template_preview() -> None:
    if not TEMPLATE_OVERLAY_SOURCE.exists() or not ART_MASK_SOURCE.exists():
        return
    TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)
    make_template_overlay().save(TEMPLATE_DIR / "card-template-preview.png", optimize=True)
    load_art_mask().save(TEMPLATE_DIR / "art-slot-mask.png", optimize=True)


def make_contact_sheet(rendered: list[Path], filename: str) -> None:
    cols, rows = 8, math.ceil(len(rendered) / 8)
    tw, th = 128, 192
    pad = 16
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * pad, rows * th + (rows + 1) * pad), "#EFE7FF")
    for i, path in enumerate(rendered):
        with Image.open(path) as im:
            thumb = im.convert("RGB").resize((tw, th), Image.Resampling.LANCZOS)
        x = pad + (i % cols) * (tw + pad)
        y = pad + (i // cols) * (th + pad)
        sheet.paste(thumb, (x, y))
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    sheet.save(PREVIEW_DIR / filename, quality=92)


def main() -> None:
    NO_TEXT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    write_template_preview()

    cards = build_cards()
    rendered_no_text: list[Path] = []
    missing: list[str] = []
    for card in cards:
        art_path = INNER_DIR / card["filename"]
        if not art_path.exists():
            missing.append(card["filename"])
            continue
        no_text_path = NO_TEXT_DIR / card["filename"]
        save_png_verified(render_card(card, art_path), no_text_path)
        rendered_no_text.append(no_text_path)

    if rendered_no_text:
        make_contact_sheet(rendered_no_text, "blank-contact-sheet.png")

    art_mask = load_art_mask()
    art_bbox = art_mask.getbbox()

    META_PATH.write_text(
        json.dumps(
            {
                "title": "Pi Tarot imagegen deck with fixed blank transparent template",
                "card_size": {"width": W, "height": H},
                "art_box": {"x": art_bbox[0], "y": art_bbox[1], "width": art_bbox[2] - art_bbox[0], "height": art_bbox[3] - art_bbox[1]},
                "nameplate": {"x": NAMEPLATE[0], "y": NAMEPLATE[1], "width": NAMEPLATE[2] - NAMEPLATE[0], "height": NAMEPLATE[3] - NAMEPLATE[1]},
                "template_files": {
                    "preview": str(TEMPLATE_DIR / "card-template-preview.png"),
                    "mask": str(TEMPLATE_DIR / "art-slot-mask.png"),
                    "overlay": str(TEMPLATE_DIR / "card-template-overlay.png"),
                },
                "generated_count": len(rendered_no_text),
                "output_dirs": {
                    "no_text": str(NO_TEXT_DIR),
                    "inner_artslot_ratio_candidates": str(INNER_DIR),
                },
                "missing_inner_images": missing,
                "cards": cards,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"rendered {len(rendered_no_text)} blank cards")
    if missing:
        print(f"missing {len(missing)} inner images")
    print(f"template: {TEMPLATE_DIR / 'card-template-preview.png'}")
    print(f"metadata: {META_PATH}")


if __name__ == "__main__":
    main()
