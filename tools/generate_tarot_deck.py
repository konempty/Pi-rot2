#!/usr/bin/env python3
"""Generate a cute Pi-inspired 78-card tarot deck as PNG assets."""

from __future__ import annotations

import json
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "tarot-cards" / "png"
PREVIEW_DIR = ROOT / "assets" / "tarot-cards" / "preview"
META_PATH = ROOT / "assets" / "tarot-cards" / "metadata.json"

W, H = 900, 1350
S = 2

FONTS = {
    "rounded_regular": "/Library/Fonts/SF-Pro-Rounded-Regular.otf",
    "rounded_bold": "/Library/Fonts/SF-Pro-Rounded-Bold.otf",
    "rounded_black": "/Library/Fonts/SF-Pro-Rounded-Black.otf",
    "display_bold": "/Library/Fonts/SF-Pro-Display-Bold.otf",
    "korean": "/System/Library/Fonts/AppleSDGothicNeo.ttc",
}

COLORS = {
    "ink": "#2D2143",
    "muted": "#6C5A84",
    "cream": "#FFF8EA",
    "paper": "#FFF2D7",
    "purple": "#44206F",
    "deep_purple": "#2B164F",
    "violet": "#7752C8",
    "gold": "#F8B84D",
    "gold_dark": "#C97922",
    "peach": "#FFB69F",
    "mint": "#87DDBE",
    "sky": "#9ED7FF",
    "rose": "#FF86B7",
}

SUITS = {
    "wands": {
        "name": "Wands",
        "kr": "완드",
        "accent": "#FF8A68",
        "soft": "#FFE1CE",
        "deep": "#9F3A38",
        "symbol": "wand",
    },
    "cups": {
        "name": "Cups",
        "kr": "컵",
        "accent": "#55C7D2",
        "soft": "#D9F7F8",
        "deep": "#176F83",
        "symbol": "cup",
    },
    "swords": {
        "name": "Swords",
        "kr": "소드",
        "accent": "#89A9FF",
        "soft": "#E3EAFF",
        "deep": "#3754A2",
        "symbol": "sword",
    },
    "pentacles": {
        "name": "Pentacles",
        "kr": "파이 코인",
        "accent": "#8BD36E",
        "soft": "#E8F9D7",
        "deep": "#3F7A35",
        "symbol": "coin",
    },
}

RANKS = [
    ("ace", "Ace", "에이스", 1),
    ("two", "Two", "2", 2),
    ("three", "Three", "3", 3),
    ("four", "Four", "4", 4),
    ("five", "Five", "5", 5),
    ("six", "Six", "6", 6),
    ("seven", "Seven", "7", 7),
    ("eight", "Eight", "8", 8),
    ("nine", "Nine", "9", 9),
    ("ten", "Ten", "10", 10),
    ("page", "Page", "시종", None),
    ("knight", "Knight", "기사", None),
    ("queen", "Queen", "여왕", None),
    ("king", "King", "왕", None),
]

MAJORS = [
    ("00", "the-fool", "The Fool", "바보", "fresh start"),
    ("01", "the-magician", "The Magician", "마법사", "skill and focus"),
    ("02", "the-high-priestess", "The High Priestess", "여사제", "intuition"),
    ("03", "the-empress", "The Empress", "여황제", "growth and care"),
    ("04", "the-emperor", "The Emperor", "황제", "structure"),
    ("05", "the-hierophant", "The Hierophant", "교황", "tradition"),
    ("06", "the-lovers", "The Lovers", "연인", "choice and bond"),
    ("07", "the-chariot", "The Chariot", "전차", "willpower"),
    ("08", "strength", "Strength", "힘", "gentle courage"),
    ("09", "the-hermit", "The Hermit", "은둔자", "inner light"),
    ("10", "wheel-of-fortune", "Wheel of Fortune", "운명의 수레바퀴", "cycles"),
    ("11", "justice", "Justice", "정의", "fairness"),
    ("12", "the-hanged-man", "The Hanged Man", "매달린 사람", "new angle"),
    ("13", "death", "Death", "죽음", "transformation"),
    ("14", "temperance", "Temperance", "절제", "balance"),
    ("15", "the-devil", "The Devil", "악마", "attachment"),
    ("16", "the-tower", "The Tower", "탑", "sudden change"),
    ("17", "the-star", "The Star", "별", "hope"),
    ("18", "the-moon", "The Moon", "달", "dreams"),
    ("19", "the-sun", "The Sun", "태양", "joy"),
    ("20", "judgement", "Judgement", "심판", "awakening"),
    ("21", "the-world", "The World", "세계", "completion"),
]


def sx(value: float) -> int:
    return int(round(value * S))


def box(values: tuple[float, float, float, float]) -> tuple[int, int, int, int]:
    return tuple(sx(v) for v in values)


def rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return int(h[:2], 16), int(h[2:4], 16), int(h[4:], 16)


def rgba(hex_color: str, alpha: int = 255) -> tuple[int, int, int, int]:
    return (*rgb(hex_color), alpha)


def blend(a: str, b: str, t: float) -> tuple[int, int, int]:
    ar, ag, ab = rgb(a)
    br, bg, bb = rgb(b)
    return (
        int(ar + (br - ar) * t),
        int(ag + (bg - ag) * t),
        int(ab + (bb - ab) * t),
    )


FONT_CACHE: dict[tuple[str, int], ImageFont.FreeTypeFont | ImageFont.ImageFont] = {}


def font(key: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    cache_key = (key, size)
    if cache_key in FONT_CACHE:
        return FONT_CACHE[cache_key]
    path = FONTS.get(key, FONTS["rounded_regular"])
    try:
        loaded = ImageFont.truetype(path, sx(size))
    except OSError:
        loaded = ImageFont.load_default()
    FONT_CACHE[cache_key] = loaded
    return loaded


def gradient(size: tuple[int, int], top: str, bottom: str) -> Image.Image:
    img = Image.new("RGBA", size)
    draw = ImageDraw.Draw(img)
    for y in range(size[1]):
        t = y / max(1, size[1] - 1)
        draw.line([(0, y), (size[0], y)], fill=(*blend(top, bottom, t), 255))
    return img


def text_center(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: float,
    font_obj: ImageFont.ImageFont,
    fill: str,
    x: float = W / 2,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    draw.text((sx(x) - tw / 2, sx(y)), text, font=font_obj, fill=fill)


def text_fit_center(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: float,
    max_width: float,
    start_size: int,
    fill: str,
    key: str = "rounded_black",
) -> None:
    size = start_size
    while size > 18:
        f = font(key, size)
        bbox = draw.textbbox((0, 0), text, font=f)
        if bbox[2] - bbox[0] <= sx(max_width):
            break
        size -= 2
    text_center(draw, text, y, font(key, size), fill)


def rounded(
    draw: ImageDraw.ImageDraw,
    rect: tuple[float, float, float, float],
    radius: float,
    fill: str | tuple[int, int, int, int],
    outline: str | tuple[int, int, int, int] | None = None,
    width: int = 1,
) -> None:
    draw.rounded_rectangle(
        box(rect),
        radius=sx(radius),
        fill=fill,
        outline=outline,
        width=sx(width),
    )


def ellipse(
    draw: ImageDraw.ImageDraw,
    rect: tuple[float, float, float, float],
    fill: str | tuple[int, int, int, int],
    outline: str | tuple[int, int, int, int] | None = None,
    width: int = 1,
) -> None:
    draw.ellipse(box(rect), fill=fill, outline=outline, width=sx(width))


def line(
    draw: ImageDraw.ImageDraw,
    pts: list[tuple[float, float]],
    fill: str | tuple[int, int, int, int],
    width: int = 4,
) -> None:
    draw.line([(sx(x), sx(y)) for x, y in pts], fill=fill, width=sx(width), joint="curve")


def polygon(
    draw: ImageDraw.ImageDraw,
    pts: list[tuple[float, float]],
    fill: str | tuple[int, int, int, int],
    outline: str | None = None,
) -> None:
    draw.polygon([(sx(x), sx(y)) for x, y in pts], fill=fill, outline=outline)


def arc(
    draw: ImageDraw.ImageDraw,
    rect: tuple[float, float, float, float],
    start: int,
    end: int,
    fill: str,
    width: int,
) -> None:
    draw.arc(box(rect), start=start, end=end, fill=fill, width=sx(width))


def add_soft_shadow(img: Image.Image, rect: tuple[float, float, float, float], radius: float) -> None:
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(box((rect[0], rect[1] + 12, rect[2], rect[3] + 12)), radius=sx(radius), fill=(60, 34, 97, 42))
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(sx(18))))


def sparkle(draw: ImageDraw.ImageDraw, x: float, y: float, r: float, color: str = "#F8B84D") -> None:
    line(draw, [(x, y - r), (x, y + r)], color, max(1, int(r / 4)))
    line(draw, [(x - r, y), (x + r, y)], color, max(1, int(r / 4)))
    ellipse(draw, (x - r * 0.22, y - r * 0.22, x + r * 0.22, y + r * 0.22), color)


def scatter_sparkles(draw: ImageDraw.ImageDraw, rng: random.Random, accent: str, count: int = 26) -> None:
    for _ in range(count):
        x = rng.uniform(78, W - 78)
        y = rng.uniform(115, H - 170)
        r = rng.choice([5, 6, 8, 10])
        color = rng.choice([accent, COLORS["gold"], "#FFFFFF", "#DCCAFF"])
        if rng.random() < 0.55:
            sparkle(draw, x, y, r, color)
        else:
            ellipse(draw, (x - r / 2, y - r / 2, x + r / 2, y + r / 2), rgba(color, 150))


def draw_pi_coin(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    r: float,
    accent: str = COLORS["purple"],
    alpha: int = 255,
    label: bool = True,
) -> None:
    ellipse(draw, (cx - r, cy - r, cx + r, cy + r), rgba(COLORS["gold_dark"], alpha), None)
    ellipse(draw, (cx - r * 0.93, cy - r * 0.93, cx + r * 0.93, cy + r * 0.93), rgba(COLORS["gold"], alpha))
    ellipse(draw, (cx - r * 0.72, cy - r * 0.72, cx + r * 0.72, cy + r * 0.72), rgba("#FFE7A4", alpha))
    ellipse(
        draw,
        (cx - r * 0.56, cy - r * 0.56, cx + r * 0.56, cy + r * 0.56),
        rgba("#FFF7D8", max(90, alpha - 70)),
        rgba(COLORS["gold_dark"], alpha),
        width=max(1, int(r * 0.035)),
    )
    if label:
        draw_pi_network_mark(draw, cx, cy, r, accent, "#FFF7D8")


def draw_pi_network_mark(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    r: float,
    accent: str,
    cutout_fill: str,
) -> None:
    """Draw the Pi Network-style coin mark without relying on a Greek pi glyph."""
    dot = max(5, r * 0.13)
    bridge_h = max(7, r * 0.2)
    stem_w = max(9, r * 0.2)
    top = cy - r * 0.21
    stem_top = cy - r * 0.04
    stem_bottom = cy + r * 0.45

    rounded(draw, (cx - r * 0.33, cy - r * 0.43, cx - r * 0.33 + dot, cy - r * 0.43 + dot), dot * 0.22, accent)
    rounded(draw, (cx + r * 0.18, cy - r * 0.43, cx + r * 0.18 + dot, cy - r * 0.43 + dot), dot * 0.22, accent)
    rounded(draw, (cx - r * 0.34, top, cx + r * 0.38, top + bridge_h), bridge_h / 2, accent)
    rounded(draw, (cx - r * 0.25, stem_top, cx - r * 0.25 + stem_w, stem_bottom), stem_w / 2, accent)
    rounded(draw, (cx + r * 0.16, stem_top, cx + r * 0.16 + stem_w, stem_bottom), stem_w / 2, accent)

    draw.polygon(
        [
            (sx(cx - r * 0.34), sx(top)),
            (sx(cx - r * 0.55), sx(cy - r * 0.09)),
            (sx(cx - r * 0.55), sx(cy + r * 0.06)),
            (sx(cx - r * 0.42), sx(cy + r * 0.14)),
            (sx(cx - r * 0.22), sx(cy + r * 0.03)),
            (sx(cx - r * 0.18), sx(top + bridge_h)),
        ],
        fill=accent,
    )

    rounded(draw, (cx + r * 0.32, top, cx + r * 0.55, top + bridge_h), bridge_h / 2, accent)
    rounded(
        draw,
        (cx + r * 0.46, top - r * 0.16, cx + r * 0.63, top + bridge_h * 0.72),
        bridge_h / 2,
        accent,
    )


def draw_suit_symbol(
    draw: ImageDraw.ImageDraw,
    suit: str,
    cx: float,
    cy: float,
    size: float,
    color: str,
    fill_soft: str = "#FFF8EA",
) -> None:
    if suit == "wands":
        line(draw, [(cx - size * 0.16, cy + size * 0.62), (cx + size * 0.16, cy - size * 0.62)], color, int(size * 0.16))
        ellipse(draw, (cx + size * 0.04, cy - size * 0.34, cx + size * 0.42, cy - size * 0.08), "#8BD36E", color, 2)
        ellipse(draw, (cx - size * 0.38, cy + size * 0.06, cx - size * 0.02, cy + size * 0.3), "#8BD36E", color, 2)
        ellipse(draw, (cx - size * 0.2, cy + size * 0.44, cx + size * 0.2, cy + size * 0.72), COLORS["gold"], color, 2)
    elif suit == "cups":
        rounded(draw, (cx - size * 0.42, cy - size * 0.36, cx + size * 0.42, cy + size * 0.18), size * 0.18, fill_soft, color, 4)
        arc(draw, (cx - size * 0.62, cy - size * 0.22, cx - size * 0.22, cy + size * 0.32), -80, 100, color, int(size * 0.08))
        line(draw, [(cx, cy + size * 0.18), (cx, cy + size * 0.55)], color, int(size * 0.08))
        line(draw, [(cx - size * 0.28, cy + size * 0.6), (cx + size * 0.28, cy + size * 0.6)], color, int(size * 0.08))
        ellipse(draw, (cx - size * 0.26, cy - size * 0.25, cx + size * 0.26, cy - size * 0.02), "#B8F8FF")
    elif suit == "swords":
        polygon(draw, [(cx, cy - size * 0.72), (cx + size * 0.18, cy + size * 0.1), (cx, cy + size * 0.28), (cx - size * 0.18, cy + size * 0.1)], "#F8FBFF", color)
        line(draw, [(cx - size * 0.42, cy + size * 0.25), (cx + size * 0.42, cy + size * 0.25)], color, int(size * 0.1))
        rounded(draw, (cx - size * 0.09, cy + size * 0.24, cx + size * 0.09, cy + size * 0.68), size * 0.04, COLORS["gold"], color, 2)
        line(draw, [(cx, cy - size * 0.6), (cx, cy + size * 0.12)], color, max(1, int(size * 0.025)))
    else:
        draw_pi_coin(draw, cx, cy, size * 0.55, accent=COLORS["purple"])


def draw_chibi(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    robe: str,
    hair: str = "#47304F",
    mood: str = "smile",
    crown: str | None = None,
    scale: float = 1.0,
) -> None:
    head_r = 48 * scale
    body_w = 78 * scale
    body_h = 104 * scale
    skin = "#FFD4BC"
    line_color = COLORS["ink"]

    ellipse(draw, (cx - head_r * 0.95, cy - 142 * scale, cx + head_r * 0.95, cy - 52 * scale), skin, line_color, 3)
    arc(draw, (cx - head_r * 1.03, cy - 153 * scale, cx + head_r * 1.03, cy - 70 * scale), 185, 355, hair, 18)
    ellipse(draw, (cx - head_r * 0.9, cy - 142 * scale, cx + head_r * 0.9, cy - 96 * scale), hair)
    ellipse(draw, (cx - 24 * scale, cy - 100 * scale, cx - 15 * scale, cy - 90 * scale), line_color)
    ellipse(draw, (cx + 15 * scale, cy - 100 * scale, cx + 24 * scale, cy - 90 * scale), line_color)
    ellipse(draw, (cx - 34 * scale, cy - 85 * scale, cx - 21 * scale, cy - 74 * scale), "#FF9EB1")
    ellipse(draw, (cx + 21 * scale, cy - 85 * scale, cx + 34 * scale, cy - 74 * scale), "#FF9EB1")
    if mood == "o":
        ellipse(draw, (cx - 7 * scale, cy - 78 * scale, cx + 7 * scale, cy - 64 * scale), line_color)
    elif mood == "calm":
        line(draw, [(cx - 13 * scale, cy - 72 * scale), (cx + 13 * scale, cy - 72 * scale)], line_color, 3)
    else:
        arc(draw, (cx - 18 * scale, cy - 86 * scale, cx + 18 * scale, cy - 58 * scale), 18, 162, line_color, 3)

    rounded(draw, (cx - body_w / 2, cy - 58 * scale, cx + body_w / 2, cy + body_h / 2), 24 * scale, robe, line_color, 3)
    ellipse(draw, (cx - 48 * scale, cy - 40 * scale, cx - 18 * scale, cy + 14 * scale), skin, line_color, 2)
    ellipse(draw, (cx + 18 * scale, cy - 40 * scale, cx + 48 * scale, cy + 14 * scale), skin, line_color, 2)
    line(draw, [(cx - 24 * scale, cy + 51 * scale), (cx - 31 * scale, cy + 83 * scale)], line_color, 5)
    line(draw, [(cx + 24 * scale, cy + 51 * scale), (cx + 31 * scale, cy + 83 * scale)], line_color, 5)
    if crown:
        polygon(
            draw,
            [
                (cx - 42 * scale, cy - 142 * scale),
                (cx - 24 * scale, cy - 184 * scale),
                (cx, cy - 148 * scale),
                (cx + 24 * scale, cy - 184 * scale),
                (cx + 42 * scale, cy - 142 * scale),
            ],
            crown,
            line_color,
        )


def draw_land(draw: ImageDraw.ImageDraw, accent: str) -> None:
    ellipse(draw, (135, 850, 765, 1130), rgba("#FFFFFF", 90))
    polygon(draw, [(80, 1030), (240, 820), (410, 1030)], "#CAB9FF")
    polygon(draw, [(310, 1030), (515, 760), (770, 1030)], "#BFE7FF")
    polygon(draw, [(70, 1010), (830, 1010), (830, 1110), (70, 1110)], "#CDEBC7")
    line(draw, [(110, 1030), (790, 1030)], accent, 5)


def base_card(card: dict) -> tuple[Image.Image, ImageDraw.ImageDraw, random.Random]:
    rng = random.Random(card["id"])
    if card["arcana"] == "major":
        top, bottom, accent = "#FFF3D4", "#D9CEFF", COLORS["purple"]
    else:
        suit = SUITS[card["suit"]]
        top, bottom, accent = suit["soft"], "#F4EDFF", suit["accent"]

    img = gradient((sx(W), sx(H)), top, bottom)
    draw = ImageDraw.Draw(img)
    scatter_sparkles(draw, rng, accent, 18)

    add_soft_shadow(img, (48, 48, W - 48, H - 48), 56)
    draw = ImageDraw.Draw(img)
    rounded(draw, (50, 50, W - 50, H - 50), 56, rgba(COLORS["cream"], 238), rgba(COLORS["purple"], 235), 5)
    rounded(draw, (76, 76, W - 76, H - 76), 38, rgba("#FFFFFF", 115), rgba(COLORS["gold"], 210), 4)

    draw_pi_coin(draw, 450, 150, 52, accent=COLORS["purple"], alpha=238)
    sparkle(draw, 144, 150, 14, COLORS["gold"])
    sparkle(draw, 756, 150, 14, COLORS["gold"])

    if card["arcana"] == "major":
        text_center(draw, card["number"], 112, font("rounded_black", 28), COLORS["deep_purple"], x=144)
        text_center(draw, "MAJOR", 112, font("rounded_bold", 22), COLORS["muted"], x=756)
    else:
        suit = SUITS[card["suit"]]
        text_center(draw, card["rank_short"], 105, font("rounded_black", 34), suit["deep"], x=144)
        draw_suit_symbol(draw, card["suit"], 756, 126, 44, suit["deep"], suit["soft"])

    rounded(draw, (118, 1146, W - 118, 1266), 32, rgba("#FFFFFF", 205), rgba(COLORS["gold"], 235), 3)
    text_fit_center(draw, card["name"].upper(), 1170, 570, 38, COLORS["deep_purple"])
    text_fit_center(draw, card["kr"], 1216, 570, 31, COLORS["muted"], "korean")

    return img, draw, rng


def draw_major_scene(img: Image.Image, draw: ImageDraw.ImageDraw, card: dict, rng: random.Random) -> None:
    slug = card["slug"]
    accent = COLORS["violet"]
    draw_land(draw, accent)

    if slug == "the-fool":
        polygon(draw, [(130, 1035), (620, 935), (835, 1050)], "#F5DB7C", COLORS["ink"])
        draw_chibi(draw, 480, 790, "#FFF0A8", "#5C366E")
        line(draw, [(430, 710), (386, 650)], COLORS["ink"], 5)
        rounded(draw, (360, 600, 430, 660), 18, "#FFB69F", COLORS["ink"], 3)
        ellipse(draw, (620, 880, 690, 950), "#FFFFFF", COLORS["ink"], 3)
        ellipse(draw, (666, 890, 706, 928), "#FFFFFF", COLORS["ink"], 3)
        line(draw, [(660, 950), (642, 982)], COLORS["ink"], 4)
    elif slug == "the-magician":
        draw_chibi(draw, 450, 735, "#D7B7FF", "#44206F", crown=COLORS["gold"])
        rounded(draw, (245, 830, 655, 930), 28, "#FFFFFF", COLORS["ink"], 4)
        for x, suit in zip([310, 400, 500, 590], ["wands", "cups", "swords", "pentacles"]):
            draw_suit_symbol(draw, suit, x, 880, 42, COLORS["purple"], "#FFF8EA")
        line(draw, [(505, 600), (555, 505)], COLORS["gold"], 8)
        sparkle(draw, 565, 492, 22, COLORS["gold"])
    elif slug == "the-high-priestess":
        rounded(draw, (210, 515, 300, 980), 28, COLORS["deep_purple"], COLORS["gold"], 5)
        rounded(draw, (600, 515, 690, 980), 28, COLORS["deep_purple"], COLORS["gold"], 5)
        ellipse(draw, (337, 460, 563, 686), "#DCD0FF", COLORS["gold"], 5)
        arc(draw, (360, 455, 600, 710), 100, 260, COLORS["gold"], 12)
        draw_chibi(draw, 450, 790, "#F2E8FF", "#2B164F", mood="calm")
        rounded(draw, (365, 830, 535, 890), 14, "#FFF7D8", COLORS["ink"], 3)
    elif slug == "the-empress":
        ellipse(draw, (280, 580, 620, 950), "#FFD8E8", COLORS["gold"], 6)
        draw_chibi(draw, 450, 800, "#FFC7D8", "#8E4B66", crown=COLORS["gold"])
        for x, y in [(250, 875), (310, 790), (655, 840), (585, 935)]:
            ellipse(draw, (x - 28, y - 28, x + 28, y + 28), "#FF86B7", COLORS["ink"], 2)
            ellipse(draw, (x - 10, y - 10, x + 10, y + 10), COLORS["gold"])
    elif slug == "the-emperor":
        rounded(draw, (285, 575, 615, 1000), 35, "#D3C2FF", COLORS["ink"], 5)
        polygon(draw, [(302, 740), (240, 690), (300, 650)], COLORS["gold"], COLORS["ink"])
        polygon(draw, [(598, 740), (660, 690), (600, 650)], COLORS["gold"], COLORS["ink"])
        draw_chibi(draw, 450, 790, "#8562D9", "#302040", crown=COLORS["gold"])
        line(draw, [(545, 670), (605, 600)], COLORS["gold"], 8)
    elif slug == "the-hierophant":
        rounded(draw, (280, 530, 620, 970), 44, "#F4E9FF", COLORS["purple"], 5)
        draw_chibi(draw, 450, 770, "#FFFFFF", "#5A3B7A", crown=COLORS["gold"])
        line(draw, [(390, 905), (510, 905)], COLORS["gold"], 7)
        line(draw, [(450, 850), (450, 960)], COLORS["gold"], 7)
        draw_pi_coin(draw, 350, 995, 36)
        draw_pi_coin(draw, 550, 995, 36)
    elif slug == "the-lovers":
        draw_chibi(draw, 360, 800, "#FFB6C9", "#4F2C4E")
        draw_chibi(draw, 540, 800, "#A8E7FF", "#47304F")
        ellipse(draw, (365, 520, 535, 690), "#FFE1EE", COLORS["gold"], 5)
        polygon(draw, [(450, 650), (375, 575), (450, 535), (525, 575)], COLORS["rose"], COLORS["ink"])
        draw_pi_coin(draw, 450, 750, 42)
    elif slug == "the-chariot":
        rounded(draw, (260, 780, 640, 990), 38, "#B3A0FF", COLORS["ink"], 5)
        ellipse(draw, (290, 950, 380, 1040), COLORS["gold"], COLORS["ink"], 4)
        ellipse(draw, (520, 950, 610, 1040), COLORS["gold"], COLORS["ink"], 4)
        draw_chibi(draw, 450, 750, "#FFFFFF", "#2B164F", crown=COLORS["gold"])
        line(draw, [(332, 820), (230, 760)], COLORS["purple"], 5)
        line(draw, [(568, 820), (670, 760)], COLORS["purple"], 5)
    elif slug == "strength":
        ellipse(draw, (350, 700, 620, 970), "#FFCB64", COLORS["ink"], 5)
        ellipse(draw, (398, 740, 572, 895), "#FFE1A2", COLORS["ink"], 3)
        arc(draw, (420, 810, 550, 905), 20, 160, COLORS["ink"], 4)
        draw_chibi(draw, 330, 790, "#FFF2B5", "#7E4F5E")
        line(draw, [(350, 800), (440, 810)], "#FFD4BC", 12)
    elif slug == "the-hermit":
        ellipse(draw, (260, 500, 640, 1000), "#DBD5FF", rgba(COLORS["deep_purple"], 70))
        draw_chibi(draw, 430, 795, "#D7C8FF", "#2B164F", mood="calm")
        line(draw, [(500, 680), (570, 560)], COLORS["ink"], 6)
        rounded(draw, (535, 525, 605, 610), 14, "#FFF4B7", COLORS["ink"], 4)
        draw_pi_coin(draw, 570, 568, 24)
    elif slug == "wheel-of-fortune":
        ellipse(draw, (230, 525, 670, 965), "#FFFFFF", COLORS["gold"], 16)
        ellipse(draw, (300, 595, 600, 895), "#E5D8FF", COLORS["purple"], 7)
        for a in range(0, 360, 45):
            x = 450 + math.cos(math.radians(a)) * 185
            y = 745 + math.sin(math.radians(a)) * 185
            draw_pi_coin(draw, x, y, 24)
        draw_pi_network_mark(draw, 450, 720, 110, COLORS["purple"], "#E5D8FF")
    elif slug == "justice":
        draw_chibi(draw, 450, 785, "#F4F0FF", "#2D2143", crown=COLORS["gold"])
        line(draw, [(450, 560), (450, 900)], COLORS["gold"], 8)
        line(draw, [(330, 650), (570, 650)], COLORS["gold"], 7)
        for x in [320, 580]:
            line(draw, [(x, 650), (x - 45, 760)], COLORS["muted"], 3)
            line(draw, [(x, 650), (x + 45, 760)], COLORS["muted"], 3)
            arc(draw, (x - 70, 725, x + 70, 825), 0, 180, COLORS["purple"], 7)
    elif slug == "the-hanged-man":
        ellipse(draw, (290, 500, 610, 950), "#E7DFFF", COLORS["gold"], 6)
        line(draw, [(320, 540), (580, 540)], COLORS["ink"], 8)
        line(draw, [(450, 540), (450, 635)], COLORS["ink"], 5)
        draw_chibi(draw, 450, 825, "#B9E9FF", "#4C356A", mood="calm")
        line(draw, [(410, 680), (490, 630)], COLORS["ink"], 4)
    elif slug == "death":
        draw_chibi(draw, 450, 800, "#F4F4FA", "#222222", mood="calm")
        line(draw, [(555, 630), (555, 880)], COLORS["ink"], 6)
        polygon(draw, [(555, 630), (710, 690), (555, 745)], "#222222", COLORS["ink"])
        ellipse(draw, (635, 668, 670, 703), "#FFFFFF")
        for x in [310, 590]:
            ellipse(draw, (x - 34, 910, x + 34, 978), "#FFFFFF", COLORS["ink"], 3)
            polygon(draw, [(x, 878), (x + 28, 928), (x - 28, 928)], "#8BD36E")
    elif slug == "temperance":
        draw_chibi(draw, 450, 790, "#E8F8FF", "#E0A55C", crown=COLORS["gold"])
        polygon(draw, [(330, 650), (250, 760), (370, 740)], "#FFFFFF", "#B8A6E8")
        polygon(draw, [(570, 650), (650, 760), (530, 740)], "#FFFFFF", "#B8A6E8")
        draw_suit_symbol(draw, "cups", 350, 810, 60, COLORS["purple"], "#FFFFFF")
        draw_suit_symbol(draw, "cups", 550, 760, 60, COLORS["purple"], "#FFFFFF")
        line(draw, [(405, 780), (505, 760)], COLORS["sky"], 8)
    elif slug == "the-devil":
        draw_chibi(draw, 450, 800, "#5B327D", "#2B164F", mood="o")
        polygon(draw, [(400, 640), (365, 585), (430, 625)], COLORS["gold"], COLORS["ink"])
        polygon(draw, [(500, 640), (535, 585), (470, 625)], COLORS["gold"], COLORS["ink"])
        line(draw, [(320, 900), (420, 930), (480, 900), (590, 930)], COLORS["muted"], 6)
        sparkle(draw, 450, 540, 22, COLORS["rose"])
    elif slug == "the-tower":
        rounded(draw, (340, 570, 560, 1020), 18, "#9273D9", COLORS["ink"], 5)
        polygon(draw, [(340, 570), (450, 485), (560, 570)], COLORS["deep_purple"], COLORS["ink"])
        line(draw, [(530, 455), (470, 610), (540, 590), (440, 780)], COLORS["gold"], 16)
        for x, y in [(335, 730), (580, 680), (505, 940)]:
            draw_pi_coin(draw, x, y, 28)
    elif slug == "the-star":
        draw_chibi(draw, 450, 820, "#F8E8FF", "#5B4077")
        for a in range(0, 360, 72):
            sparkle(draw, 450 + math.cos(math.radians(a)) * 150, 580 + math.sin(math.radians(a)) * 70, 18, COLORS["gold"])
        draw_suit_symbol(draw, "cups", 350, 860, 55, COLORS["purple"], "#FFFFFF")
        draw_suit_symbol(draw, "cups", 550, 860, 55, COLORS["purple"], "#FFFFFF")
        line(draw, [(375, 900), (285, 980)], COLORS["sky"], 8)
        line(draw, [(525, 900), (615, 980)], COLORS["sky"], 8)
    elif slug == "the-moon":
        ellipse(draw, (330, 480, 570, 720), "#FFF1A8", COLORS["gold"], 5)
        ellipse(draw, (395, 450, 610, 700), rgba("#D9CEFF", 255))
        rounded(draw, (200, 755, 290, 1015), 22, COLORS["deep_purple"], COLORS["gold"], 4)
        rounded(draw, (610, 755, 700, 1015), 22, COLORS["deep_purple"], COLORS["gold"], 4)
        line(draw, [(450, 735), (410, 1005), (490, 1005)], COLORS["gold"], 6)
        draw_pi_coin(draw, 450, 820, 34)
    elif slug == "the-sun":
        ellipse(draw, (250, 455, 650, 855), "#FFE27A", COLORS["gold_dark"], 8)
        for a in range(0, 360, 30):
            line(draw, [(450, 655), (450 + math.cos(math.radians(a)) * 260, 655 + math.sin(math.radians(a)) * 260)], COLORS["gold"], 8)
        draw_chibi(draw, 450, 880, "#FFFFFF", "#D08A38", mood="smile")
        draw_pi_coin(draw, 450, 650, 58)
    elif slug == "judgement":
        polygon(draw, [(320, 650), (230, 790), (365, 750)], "#FFFFFF", "#B8A6E8")
        polygon(draw, [(580, 650), (670, 790), (535, 750)], "#FFFFFF", "#B8A6E8")
        draw_chibi(draw, 450, 770, "#FFF7D8", "#E0A55C", crown=COLORS["gold"])
        rounded(draw, (520, 610, 690, 680), 26, COLORS["gold"], COLORS["ink"], 4)
        ellipse(draw, (662, 586, 735, 704), "#FFF7D8", COLORS["ink"], 4)
        for x in [335, 450, 565]:
            rounded(draw, (x - 40, 935, x + 40, 1035), 18, "#F0E7FF", COLORS["ink"], 3)
    elif slug == "the-world":
        ellipse(draw, (250, 500, 650, 980), rgba("#FFFFFF", 80), COLORS["gold"], 13)
        for a in range(0, 360, 24):
            x = 450 + math.cos(math.radians(a)) * 200
            y = 740 + math.sin(math.radians(a)) * 240
            ellipse(draw, (x - 16, y - 16, x + 16, y + 16), "#8BD36E", COLORS["ink"], 2)
        draw_chibi(draw, 450, 790, "#DCCAFF", "#6B4B77", crown=COLORS["gold"])
        draw_pi_coin(draw, 450, 740, 42)


def pip_positions(n: int) -> list[tuple[float, float]]:
    layouts = {
        1: [(450, 700)],
        2: [(335, 615), (565, 835)],
        3: [(335, 590), (565, 590), (450, 830)],
        4: [(330, 585), (570, 585), (330, 840), (570, 840)],
        5: [(330, 575), (570, 575), (450, 705), (330, 850), (570, 850)],
        6: [(320, 560), (580, 560), (320, 705), (580, 705), (320, 850), (580, 850)],
        7: [(320, 548), (580, 548), (450, 635), (320, 735), (580, 735), (320, 870), (580, 870)],
        8: [(320, 535), (580, 535), (320, 650), (580, 650), (320, 765), (580, 765), (320, 880), (580, 880)],
        9: [(320, 525), (580, 525), (320, 640), (580, 640), (450, 705), (320, 790), (580, 790), (320, 905), (580, 905)],
        10: [(300, 520), (450, 520), (600, 520), (330, 640), (570, 640), (300, 760), (450, 760), (600, 760), (360, 900), (540, 900)],
    }
    return layouts[n]


def draw_minor_scene(img: Image.Image, draw: ImageDraw.ImageDraw, card: dict, rng: random.Random) -> None:
    suit = SUITS[card["suit"]]
    accent = suit["accent"]
    deep = suit["deep"]
    soft = suit["soft"]
    rounded(draw, (148, 380, 752, 1038), 50, rgba("#FFFFFF", 125), rgba(accent, 230), 4)
    ellipse(draw, (210, 430, 690, 1000), rgba(soft, 130), None)

    if card["rank_value"]:
        n = card["rank_value"]
        if n == 1:
            ellipse(draw, (260, 470, 640, 850), rgba("#FFFFFF", 180), rgba(COLORS["gold"], 235), 7)
            for a in range(0, 360, 30):
                line(draw, [(450, 660), (450 + math.cos(math.radians(a)) * 245, 660 + math.sin(math.radians(a)) * 245)], rgba(accent, 135), 5)
            draw_suit_symbol(draw, card["suit"], 450, 660, 190, deep, soft)
            sparkle(draw, 450, 910, 24, COLORS["gold"])
        else:
            for idx, (x, y) in enumerate(pip_positions(n)):
                size = 68 if n <= 6 else 56
                if idx == n - 1 and n in {3, 5, 7, 9}:
                    size += 10
                draw_suit_symbol(draw, card["suit"], x, y, size, deep, soft)
            if n in {2, 6}:
                line(draw, [(240, 980), (660, 980)], COLORS["gold"], 7)
                for x in [330, 450, 570]:
                    sparkle(draw, x, 950, 12, COLORS["gold"])
            elif n in {3, 4}:
                for x in [295, 450, 605]:
                    ellipse(draw, (x - 20, 938, x + 20, 978), COLORS["rose"], COLORS["ink"], 2)
                    line(draw, [(x, 978), (x, 1020)], "#8BD36E", 5)
            elif n in {5, 10}:
                draw_chibi(draw, 450, 1015, "#F8E8FF", "#5B4077", mood="o", scale=0.58)
                line(draw, [(355, 970), (545, 970)], accent, 5)
            elif n in {7, 8, 9}:
                arc(draw, (235, 850, 665, 1100), 205, 335, COLORS["gold"], 7)
                draw_pi_coin(draw, 450, 980, 32)
    else:
        role = card["rank"]
        robe = {
            "Page": "#FFE1CE",
            "Knight": "#DCE8FF",
            "Queen": "#FFE0F0",
            "King": "#E8D8FF",
        }[role]
        hair = {
            "Page": "#63424B",
            "Knight": "#374363",
            "Queen": "#7C4769",
            "King": "#33264F",
        }[role]
        crown = COLORS["gold"] if role in {"Queen", "King"} else None
        draw_chibi(draw, 450, 800, robe, hair, crown=crown, scale=1.24)
        draw_suit_symbol(draw, card["suit"], 450, 890, 102, deep, soft)
        if role == "Knight":
            rounded(draw, (250, 845, 650, 980), 34, rgba("#FFFFFF", 145), deep, 4)
            line(draw, [(320, 920), (580, 920)], COLORS["gold"], 8)
        elif role == "Page":
            rounded(draw, (330, 600, 570, 660), 18, "#FFF8EA", deep, 3)
            sparkle(draw, 450, 570, 18, COLORS["gold"])
        elif role == "Queen":
            ellipse(draw, (300, 850, 600, 1060), rgba("#FFFFFF", 120), COLORS["gold"], 4)
        else:
            rounded(draw, (310, 610, 590, 1010), 36, rgba("#FFFFFF", 100), COLORS["gold"], 5)

    draw_pi_coin(draw, 240, 1030, 28, alpha=220)
    draw_pi_coin(draw, 660, 1030, 28, alpha=220)


def finalize(img: Image.Image) -> Image.Image:
    return img.resize((W, H), Image.Resampling.LANCZOS).convert("RGB")


def build_cards() -> list[dict]:
    cards: list[dict] = []
    idx = 0
    for num, slug, name, kr, meaning in MAJORS:
        cards.append(
            {
                "id": f"{idx:02d}",
                "number": num,
                "slug": slug,
                "name": name,
                "kr": kr,
                "meaning": meaning,
                "arcana": "major",
                "filename": f"{idx:02d}_major_{num}_{slug}.png",
            }
        )
        idx += 1

    for suit_key, suit in SUITS.items():
        for rank_key, rank_name, rank_kr, rank_value in RANKS:
            name = f"{rank_name} of {suit['name']}"
            kr = f"{suit['kr']} {rank_kr}"
            cards.append(
                {
                    "id": f"{idx:02d}",
                    "slug": f"{rank_key}-of-{suit_key}",
                    "name": name,
                    "kr": kr,
                    "arcana": "minor",
                    "suit": suit_key,
                    "rank": rank_name,
                    "rank_short": "A" if rank_name == "Ace" else str(rank_value) if rank_value else rank_name[:2].upper(),
                    "rank_value": rank_value,
                    "filename": f"{idx:02d}_{suit_key}_{rank_key}.png",
                }
            )
            idx += 1
    return cards


def render_card(card: dict) -> Image.Image:
    img, draw, rng = base_card(card)
    if card["arcana"] == "major":
        draw_major_scene(img, draw, card, rng)
    else:
        draw_minor_scene(img, draw, card, rng)
    return finalize(img)


def make_card_back() -> Image.Image:
    img = gradient((sx(W), sx(H)), COLORS["deep_purple"], "#6443B3")
    draw = ImageDraw.Draw(img)
    scatter_sparkles(draw, random.Random("back"), COLORS["gold"], 45)
    rounded(draw, (55, 55, W - 55, H - 55), 58, rgba("#2B164F", 215), rgba(COLORS["gold"], 240), 6)
    rounded(draw, (92, 92, W - 92, H - 92), 42, rgba("#FFFFFF", 30), rgba("#DCCAFF", 180), 3)
    ellipse(draw, (190, 385, 710, 905), rgba("#FFFFFF", 28), rgba(COLORS["gold"], 255), 16)
    draw_pi_coin(draw, 450, 645, 160, accent=COLORS["purple"])
    for a in range(0, 360, 30):
        x = 450 + math.cos(math.radians(a)) * 268
        y = 645 + math.sin(math.radians(a)) * 268
        sparkle(draw, x, y, 16, COLORS["gold"])
    text_center(draw, "PI TAROT", 975, font("rounded_black", 56), COLORS["gold"])
    text_center(draw, "파이 타로", 1042, font("korean", 36), "#F6E8FF")
    return finalize(img)


def make_contact_sheet(cards: list[dict]) -> None:
    thumbs = []
    for card in cards:
        path = OUT_DIR / card["filename"]
        with Image.open(path) as im:
            thumbs.append(im.resize((140, 210), Image.Resampling.LANCZOS))
    cols, rows = 13, 6
    pad = 18
    sheet = Image.new("RGB", (cols * 140 + (cols + 1) * pad, rows * 210 + (rows + 1) * pad), "#F5EDFF")
    for i, thumb in enumerate(thumbs):
        x = pad + (i % cols) * (140 + pad)
        y = pad + (i // cols) * (210 + pad)
        sheet.paste(thumb, (x, y))
    sheet.save(PREVIEW_DIR / "deck-contact-sheet.png", quality=92)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    cards = build_cards()
    for card in cards:
        render_card(card).save(OUT_DIR / card["filename"], optimize=True)
    make_card_back().save(PREVIEW_DIR / "card-back.png", optimize=True)
    make_contact_sheet(cards)
    META_PATH.write_text(
        json.dumps(
            {
                "title": "Pi-inspired cute tarot deck",
                "description": "78 tarot card fronts with purple-gold coin and pi motifs for a youthful tarot service.",
                "card_size": {"width": W, "height": H},
                "style": {
                    "palette": ["purple", "gold", "pastel suit accents"],
                    "motifs": ["pi coin halo", "gold circular ring", "small square highlights", "rounded kawaii tarot scenes"],
                    "note": "Pi-inspired original artwork, not an official Pi Network trademark asset.",
                },
                "cards": cards,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"generated {len(cards)} cards in {OUT_DIR}")
    print(f"metadata: {META_PATH}")
    print(f"preview: {PREVIEW_DIR / 'deck-contact-sheet.png'}")


if __name__ == "__main__":
    main()
