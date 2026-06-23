#!/usr/bin/env python3
"""Render tarot card nameplate text directly onto blank final cards."""

from __future__ import annotations

import argparse
import os
import json
import math
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "tarot-cards-imagegen"
META_PATH = BASE / "metadata.json"
NO_TEXT_DIR = BASE / "final" / "blank"
WEBP_OUT_DIR = BASE / "final" / "cards"
PREVIEW_DIR = BASE / "preview"

DEFAULT_FONT = Path("/System/Library/Fonts/Supplemental/Didot.ttc")

ROMAN = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
    16: "XVI",
    17: "XVII",
    18: "XVIII",
    19: "XIX",
    20: "XX",
    21: "XXI",
}


def load_metadata() -> dict:
    return json.loads(META_PATH.read_text(encoding="utf-8"))


def load_cards() -> list[dict]:
    return load_metadata()["cards"]


def card_by_selector(selector: str) -> dict:
    for card in load_cards():
        stem = Path(card["filename"]).stem
        if selector in {card["id"], card["filename"], stem, card["slug"]}:
            return card
    raise SystemExit(f"Unknown card selector: {selector}")


def marker_for(card: dict) -> str:
    if card["arcana"] == "major":
        number = int(card["number"])
        return "0" if number == 0 else ROMAN[number]
    rank_value = card.get("rank_value")
    if rank_value:
        return ROMAN[int(rank_value)]
    return card["rank"].upper()


def title_for(card: dict) -> str:
    return card["name"].title()


def load_font(font_path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not font_path.exists():
        raise FileNotFoundError(font_path)
    return ImageFont.truetype(str(font_path), size)


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, stroke_width: int) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    return box[2] - box[0], box[3] - box[1]


def fit_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: Path,
    max_width: int,
    start_size: int,
    min_size: int,
    stroke_width: int,
) -> tuple[ImageFont.FreeTypeFont, int, int]:
    for size in range(start_size, min_size - 1, -1):
        font = load_font(font_path, size)
        width, height = text_size(draw, text, font, stroke_width)
        if width <= max_width:
            return font, width, height
    font = load_font(font_path, min_size)
    width, height = text_size(draw, text, font, stroke_width)
    return font, width, height


def render_card_image(
    card: dict,
    font_path: Path = DEFAULT_FONT,
    output_scale: int = 1,
    supersample: int = 8,
) -> Image.Image:
    if output_scale < 1:
        raise ValueError("output_scale must be 1 or greater")
    if supersample < 1:
        raise ValueError("supersample must be 1 or greater")

    metadata = load_metadata()
    plate = metadata["nameplate"]
    src_path = NO_TEXT_DIR / card["filename"]
    if not src_path.exists():
        raise FileNotFoundError(src_path)

    with Image.open(src_path).convert("RGBA") as card_img:
        if output_scale > 1:
            card_img = card_img.resize(
                (card_img.width * output_scale, card_img.height * output_scale),
                Image.Resampling.LANCZOS,
            )
        scale = output_scale * supersample
        card_x = plate["x"] * output_scale
        card_y = plate["y"] * output_scale
        plate_w = plate["width"] * output_scale
        plate_h = plate["height"] * output_scale
        overlay = Image.new("RGBA", (plate_w * supersample, plate_h * supersample), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        w = plate_w * supersample
        h = plate_h * supersample

        title = title_for(card)
        marker = marker_for(card)

        text_max_width = int(w * 0.82)
        title_stroke = max(2, round(0.65 * scale))
        marker_stroke = max(2, round(0.55 * scale))

        title_font, title_width, title_height = fit_font(
            draw,
            title,
            font_path,
            text_max_width,
            start_size=62 * scale,
            min_size=32 * scale,
            stroke_width=title_stroke,
        )
        marker_start_size = 54 * scale if marker == "0" else 38 * scale
        marker_min_size = 34 * scale if marker == "0" else 24 * scale
        marker_font, marker_width, marker_height = fit_font(
            draw,
            marker,
            font_path,
            int(w * 0.28),
            start_size=marker_start_size,
            min_size=marker_min_size,
            stroke_width=marker_stroke,
        )

        center_x = w // 2
        marker_y = int(h * 0.17)
        title_y = int(h * 0.47)

        fill = (69, 38, 107, 255)
        stroke = (122, 78, 33, 85)

        def draw_layered(text: str, font: ImageFont.FreeTypeFont, width: int, top_y: int, stroke_width: int) -> None:
            left = center_x - width // 2
            draw.text(
                (left, top_y),
                text,
                font=font,
                fill=fill,
                stroke_fill=stroke,
                stroke_width=stroke_width,
            )
            if text == "0":
                box = draw.textbbox((left, top_y), text, font=font, stroke_width=stroke_width)
                bx1, by1, bx2, by2 = box
                bw = bx2 - bx1
                bh = by2 - by1
                slash_width = max(2, round(0.55 * scale))
                draw.line(
                    (
                        bx1 + int(bw * 0.30),
                        by2 - int(bh * 0.24),
                        bx2 - int(bw * 0.26),
                        by1 + int(bh * 0.22),
                    ),
                    fill=fill,
                    width=slash_width,
                )

        draw_layered(marker, marker_font, marker_width, marker_y, marker_stroke)
        draw_layered(title, title_font, title_width, title_y, title_stroke)

        overlay = overlay.resize((plate_w, plate_h), Image.Resampling.LANCZOS)
        card_img.alpha_composite(overlay, (card_x, card_y))
        return card_img.copy()


def render_card_webp(
    card: dict,
    font_path: Path = DEFAULT_FONT,
    output_dir: Path = WEBP_OUT_DIR,
    output_scale: int = 1,
    supersample: int = 8,
    quality: int = 88,
    method: int = 6,
    lossless: bool = False,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{Path(card['filename']).stem}.webp"
    image = render_card_image(card, font_path, output_scale, supersample)
    image.save(out_path, "WEBP", quality=quality, method=method, lossless=lossless, exact=True)
    return out_path


def default_workers() -> int:
    cpus = os.cpu_count() or 2
    return max(1, min(4, cpus - 1))


def render_card_webp_task(args: tuple[dict, str, str, int, int, int, int, bool]) -> str:
    card, font_path, output_dir, output_scale, supersample, quality, method, lossless = args
    return str(
        render_card_webp(
            card,
            Path(font_path),
            Path(output_dir),
            output_scale,
            supersample,
            quality,
            method,
            lossless,
        )
    )


def render_all_webp(
    font_path: Path = DEFAULT_FONT,
    output_dir: Path = WEBP_OUT_DIR,
    output_scale: int = 1,
    supersample: int = 8,
    quality: int = 88,
    method: int = 6,
    lossless: bool = False,
    workers: int | None = None,
) -> list[Path]:
    cards = load_cards()
    worker_count = default_workers() if workers is None else workers
    if worker_count <= 1:
        return [
            render_card_webp(card, font_path, output_dir, output_scale, supersample, quality, method, lossless)
            for card in cards
        ]
    tasks = [
        (card, str(font_path), str(output_dir), output_scale, supersample, quality, method, lossless)
        for card in cards
    ]
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        return [Path(path) for path in executor.map(render_card_webp_task, tasks)]


def make_contact_sheet(source_dir: Path = WEBP_OUT_DIR, out_name: str = "cards-contact-sheet.png") -> Path:
    paths = sorted(source_dir.glob("*.png")) or sorted(source_dir.glob("*.webp"))
    if not paths:
        raise SystemExit(f"No cards in {source_dir}")
    cols, rows = 8, math.ceil(len(paths) / 8)
    thumb_w, thumb_h = 160, 240
    pad = 18
    sheet = Image.new("RGB", (cols * thumb_w + (cols + 1) * pad, rows * thumb_h + (rows + 1) * pad), "#eee6ff")
    for index, path in enumerate(paths):
        with Image.open(path).convert("RGB") as im:
            thumb = im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        px = pad + (index % cols) * (thumb_w + pad)
        py = pad + (index // cols) * (thumb_h + pad)
        sheet.paste(thumb, (px, py))
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = PREVIEW_DIR / out_name
    sheet.save(out, quality=94)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    final_cmd = sub.add_parser("final")
    final_cmd.add_argument("--font", default=str(DEFAULT_FONT))
    final_cmd.add_argument("--webp-dir", default=str(WEBP_OUT_DIR))
    final_cmd.add_argument("--output-scale", type=int, default=1)
    final_cmd.add_argument("--supersample", type=int, default=8)
    final_cmd.add_argument("--quality", type=int, default=88)
    final_cmd.add_argument("--method", type=int, default=6)
    final_cmd.add_argument("--lossless", action="store_true")
    final_cmd.add_argument("--workers", type=int, default=None)

    sheet_cmd = sub.add_parser("contact-sheet")
    sheet_cmd.add_argument("--source-dir", default=str(WEBP_OUT_DIR))
    sheet_cmd.add_argument("--out-name", default="cards-contact-sheet.png")

    args = parser.parse_args()
    if args.command == "final":
        webp_paths = render_all_webp(
            Path(args.font),
            Path(args.webp_dir),
            args.output_scale,
            args.supersample,
            args.quality,
            args.method,
            args.lossless,
            args.workers,
        )
        print(f"rendered_webp: {len(webp_paths)}")
        print(f"webp_dir: {Path(args.webp_dir)}")
    elif args.command == "contact-sheet":
        print(make_contact_sheet(Path(args.source_dir), args.out_name))


if __name__ == "__main__":
    main()
