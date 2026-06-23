#!/usr/bin/env python3
"""Build the remaining Pi Tarot imageGen prompt queue.

The prompts intentionally target inner illustrations only. The fixed card
frame, labels, and final variants are produced later by render_imagegen_deck.py.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from generate_tarot_deck import build_cards


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "tarot-cards-imagegen"
INNER_DIR = BASE / "inner"
DEFAULT_OUT = BASE / "imagegen-prompt-queue.md"

REPLACE_FILENAMES: set[str] = set()

SUIT_CONTINUITY = {
    "wands": (
        "a youthful spark apprentice protagonist with short dark wavy hair, violet eyes, "
        "a purple travel cloak, cream tunic, orange scarf, star satchel, and a small cream "
        "fox-like companion; lavender mountain trail, Ember Academy, and warm mountain "
        "village festival; wands are refined magical staffs or ritual rods with gold bands, "
        "violet crystals, and soft orange flame, not mundane lumber or chopped wood; "
        "the protagonist stays visually central, while faceless hands, partial bodies, or a few "
        "supporting villagers/helpers may appear when they make the action more natural"
    ),
    "cups": (
        "a gentle young cup keeper with soft lavender-brown hair, a pearl hairpin, "
        "purple-and-cream seaside clothes, and a tiny water-sprite companion; moonlit "
        "pearl pond, seaside garden, fountain courtyard, and quiet shore; cups are "
        "pearl-white vessels with soft aqua glow; the protagonist stays visually central, "
        "while faceless hands, partial bodies, or a few supporting figures may appear when useful"
    ),
    "swords": (
        "a clever young sky student with silver-black bobbed hair, violet academy cloak, "
        "cream scarf, and a small owl-like wind familiar; moonlit academy, misty shore, "
        "windy hill, quiet chapel-like room, and river crossing; elegant silver practice "
        "swords carry blue wind light; the protagonist stays visually central, while faceless "
        "hands, partial bodies, or a few supporting academy figures may appear when useful"
    ),
    "pentacles": (
        "a grounded young coin gardener-merchant with warm brown hair, green-violet apron, "
        "cream shirt, and a small sprout mascot; terraced coinseed garden, open-air garden "
        "worktables, village market, and harvest greenhouse; pentacles are purple-enamel Pi "
        "coinseeds with warm gold rims set among leaves, soil, stone, and careful garden tools; the protagonist stays "
        "visually central, while faceless hands, partial bodies, or a few supporting market "
        "figures may appear when useful"
    ),
}

SUIT_GENERATION_RULES = {
    "wands": (
        "Wands count discipline: only the requested magical staffs should read as wands. "
        "Avoid extra pole-like trees, posts, banners, branch piles, or spare sticks that could "
        "be mistaken for additional wands."
    ),
    "cups": (
        "Cups count discipline: only the requested pearl-white cups should read as cups. "
        "Avoid extra goblets, bowls, shells shaped like cups, vases, pitchers, or cup-like "
        "decorations that could confuse the count."
    ),
    "swords": (
        "Swords discipline: keep the scene intellectual and nonviolent. Show only the requested "
        "readable silver practice sword or swords; avoid battlefields, blood, injuries, horror, "
        "weapon piles, extra blades, and readable text-like wind glyphs."
    ),
    "pentacles": (
        "Pentacles discipline: the exact requested purple-enamel Pi coinseeds or medallions must "
        "be large and countable, not tiny glitter or coin piles. Each visible coinseed should "
        "have a warm gold rim, deep purple enamel face, and simplified raised Pi Network "
        "icon-like embossing with no C-shaped right loop, no circular right-side hole, and no "
        "swollen upper-right bulb. Keep earthy greens, soil browns, cream, and violet as the "
        "broad color fields; gold is a controlled accent on the countable coinseeds/medallions."
    ),
}

SCENES = {
    "22_wands_ace.png": {
        "scene": (
            "dawn on the lavender mountain trail below Ember Academy, roots and moss in "
            "the foreground, distant academy roofs softly visible"
        ),
        "subject": (
            "the spark apprentice discovers exactly one living wooden wand awakening from "
            "an ember root; the wand has green leaves and soft orange flame petals. The "
            "small cream fox companion watches in surprise. This is the first moment of "
            "the Ember Trail story."
        ),
        "composition": "low close-up near the soil, exactly one wand large and unmistakable, same apprentice and fox introduced clearly",
    },
    "23_wands_two.png": {
        "scene": (
            "a fork in the lavender mountain trail, one path bending back toward Ember "
            "Academy and one path leading toward distant mountain village lights"
        ),
        "subject": (
            "the apprentice studies a blank map with no readable marks while exactly two "
            "living wooden wands stand as path markers at the fork. The fox sniffs the "
            "path toward the village, creating a clear choice after the Ace discovery."
        ),
        "composition": "over-the-shoulder view of the map and fork, exactly two separated wands, quiet decision mood",
    },
    "24_wands_three.png": {
        "scene": (
            "high ridge above the same lavender valley, distant warm village festival "
            "lights visible beyond winding mountain paths"
        ),
        "subject": (
            "the apprentice plants exactly three living wooden wands as signal staffs on "
            "the ridge and looks toward the village. The fox sits beside the satchel. "
            "This is departure and expectation after choosing the road."
        ),
        "composition": "wide horizon shot, three signal wands framing the valley, protagonist and fox remain central",
    },
    "25_wands_four.png": {
        "scene": (
            "arrival at the cozy mountain village festival seen from the previous ridge, "
            "sunset lanterns, lavender hills, and a warm village gate; celebratory but not "
            "crowded, with no pole-like objects near the arch"
        ),
        "subject": (
            "exactly four large living wooden wands must be clearly visible at card scale, "
            "no more and no fewer. Use a clean simple arch made only from these four wands: "
            "one left upright wand, one right upright wand, one top-front horizontal wand, "
            "and one top-back horizontal wand. The two top wands may gently cross, but they "
            "must remain countable. Leave open sky around each wand so the count is unmistakable. "
            "The same apprentice and cream fox enter beneath the arch with quiet joy, making "
            "this the arrival payoff after Three of Wands. Include one clear larger golden "
            "medallion hanging at the center of the four-wand arch; do not scatter many tiny "
            "Pi marks. No other wands, no hidden staffs, no extra stick-like poles, no branch "
            "posts, no spare wood."
        ),
        "composition": "centered clean four-wand arch, exactly four separated countable wands, protagonist and fox remain central",
    },
    "26_wands_five.png": {
        "scene": (
            "the morning after arrival, a quiet village practice meadow near the festival "
            "square, lavender grasses, distant mountain houses, and warm training light; "
            "avoid standing stones, carved stones, wall markings, signs, and background symbols"
        ),
        "subject": (
            "exactly five living wooden wands must be clearly visible and countable at card "
            "scale. The apprentice holds one wand, while faceless training helpers' hands or "
            "arms hold the other four wands into a star-like practice clash. The apprentice "
            "struggles but stays focused, and the small cream fox watches beside them. This "
            "is guided training conflict, not a crowd fight. Include one or two clear larger "
            "golden coin charms or medallions only, with the Pi Network icon-like emblem "
            "readable; do not scatter many tiny Pi marks. No extra wands."
        ),
        "composition": "protagonist centered slightly low, faceless helper hands/arms allowed, five wands with clear separation, energetic but uncluttered",
    },
    "27_wands_six.png": {
        "scene": (
            "the same mountain village square after the training, warm lanterns and lavender "
            "banners kept low and soft, distant festival stalls without pole-like clutter"
        ),
        "subject": (
            "the apprentice is quietly recognized by the village. Exactly six living wooden "
            "wands line the path in three pairs, each topped with a small orange flame petal. "
            "A small ember wreath or ribbon marks recognition, while the fox trots proudly "
            "beside the apprentice."
        ),
        "composition": "low path perspective through six paired wands, recognition mood, protagonist and fox remain central",
    },
    "28_wands_seven.png": {
        "scene": (
            "night on the windy ridge above the village, the same mountain trail now dark, "
            "village lanterns glowing below"
        ),
        "subject": (
            "a cold night wind threatens the village lights, and the apprentice defends the "
            "ridge with exactly seven living wooden wands forming a staggered barrier. The "
            "fox guards a lantern behind the barrier. This begins the crisis turn of the story."
        ),
        "composition": "dramatic diagonal ridge barrier, seven countable wands, defensive stance without extra weapons",
    },
    "29_wands_eight.png": {
        "scene": (
            "open sky above the lavender valley between the ridge, Ember Academy, and the "
            "mountain village, dawn beginning at the horizon"
        ),
        "subject": (
            "exactly eight living wooden wands are carried relay-style between the defended "
            "ridge, the village, and Ember Academy. The apprentice points the route or passes "
            "the first wand, while a few faceless or back-turned helpers/messengers carry the "
            "remaining wands along the path. The wands should not float unsupported in the sky."
        ),
        "composition": "wide relay motion shot, eight separated handheld or carried wands, clear direction from ridge to village, no crowd",
    },
    "30_wands_nine.png": {
        "scene": (
            "the last hour before dawn on the same ridge, wind fading, village lanterns still "
            "alive below, cool violet shadows"
        ),
        "subject": (
            "the tired apprentice keeps final watch behind exactly nine living wooden wands "
            "set like a protective palisade. The scarf is dusty or slightly torn but there is "
            "no blood. The fox curls near the apprentice's boots, still awake."
        ),
        "composition": "close night-watch scene behind nine countable wands, fatigue and resilience, no extra pole shapes",
    },
    "31_wands_ten.png": {
        "scene": (
            "early dawn descending from the ridge back toward the mountain village hearth, "
            "the same trail now warm with first light"
        ),
        "subject": (
            "the apprentice accepts responsibility by magically controlling exactly ten refined "
            "staffs floating around them in two groups of five, rather than physically carrying "
            "bundles. The fox walks beside them. The burden feels heavy but hopeful, completing "
            "the Ember Trail numbered arc."
        ),
        "composition": "full-body downhill journey, ten hovering staffs clearly countable as 5+5, dawn resolution",
    },
    "41_cups_six.png": {
        "scene": (
            "memory garden beside the moonlit pearl pond, soft seaside flowers, a low cream "
            "stone table, gentle aqua reflections"
        ),
        "subject": (
            "the cup keeper remembers childhood kindness. Exactly six pearl-white cups sit "
            "on the low stone table in two clean rows of three, each cup holding a small "
            "flower or shell. The present-day protagonist watches a soft translucent memory "
            "of a younger self or one childhood friend, while the tiny water-sprite glows nearby."
        ),
        "composition": "front view of a low table with six cups in 3+3 arrangement, memory mood, cups unobscured and countable",
    },
    "56_swords_seven.png": {
        "scene": (
            "moonlit Moonwind Academy wind archive after the river crossing, high shelves "
            "and blue wind ribbons, no readable scrolls or labels"
        ),
        "subject": (
            "the sky student secretly moves exactly seven elegant silver practice swords to "
            "solve an approaching academy crisis. This should read as strategy and a risky "
            "plan, not random theft. The owl-like wind familiar guides the safest path."
        ),
        "composition": "quiet stealth-like diagonal composition, seven swords countable in the student's arms and nearby rack, no violence",
    },
    "57_swords_eight.png": {
        "scene": (
            "a circular wind-trial room in Moonwind Academy, the consequence of the Seven of "
            "Swords plan, moonlight through tall windows"
        ),
        "subject": (
            "the sky student stands in a self-made trial circle where exactly eight silver "
            "practice swords and blue wind ribbons form a loose cage around them. The owl "
            "familiar points toward a narrow opening, showing that the limit can be understood."
        ),
        "composition": "centered trial circle, eight swords evenly spaced and countable, restrained nonviolent tension",
    },
    "58_swords_nine.png": {
        "scene": (
            "night before the final trial, a quiet Moonwind Academy dormitory or chapel room, "
            "rain on the window and blue moonlight"
        ),
        "subject": (
            "the sky student cannot sleep. Exactly nine silver sword-shaped shadows or practice "
            "swords loom above the bed and wall like anxious thoughts, foreshadowing the Ten "
            "of Swords. The owl familiar stays close, worried but protective."
        ),
        "composition": "intimate night interior, nine swords clearly aligned above or behind the bed, anxiety without horror",
    },
    "59_swords_ten.png": {
        "scene": (
            "dawn in the Moonwind Academy training chapel, the final consequence of the Seven, "
            "Eight, and Nine sequence, first sunlight entering through tall windows"
        ),
        "subject": (
            "a symbolic heroic ending: the student's old cloak lies in the center while exactly "
            "ten silver swords of light are planted around it like a ceremonial final trial. "
            "The student may be shown kneeling or collapsed peacefully with no blood and no "
            "injury detail; the owl familiar and sunrise imply rebirth after the old self ends."
        ),
        "composition": "heroic symbolic death-and-dawn composition, ten swords countable, solemn but not violent",
    },
    "61_swords_knight.png": {
        "scene": "Moonwind Academy courtyard opening to a bright windy sky, long ribbons of blue wind light crossing the scene",
        "subject": (
            "the maturing sky student as Knight of Swords, moving forward with determined "
            "clarity on a swift wind path, holding one elegant silver practice sword angled "
            "upward; the owl-like wind familiar flies beside them. No violence, no battlefield."
        ),
        "composition": "dynamic forward motion, one human protagonist, one sword as the main blade",
    },
    "62_swords_queen.png": {
        "scene": "quiet moonlit academy terrace above clouds, pale blue wind glyphs made of light, calm clear air",
        "subject": (
            "the sky student matured into Queen of Swords, seated or standing with serene "
            "authority, holding one upright silver practice sword; the owl-like wind familiar "
            "rests nearby. The mood is wisdom, honesty, and clean perception."
        ),
        "composition": "calm centered portrait, one human protagonist, one readable sword, refined and spacious",
    },
    "63_swords_king.png": {
        "scene": "high Moonwind Academy observatory with open sky, clouds below, moonlit columns and blue wind light",
        "subject": (
            "the sky student matured into King of Swords, composed and thoughtful, holding "
            "one silver practice sword like a symbol of fair judgment; the owl-like familiar "
            "circles above. The tone is intellect, stability, and clarity."
        ),
        "composition": "regal vertical composition, one human protagonist, one readable sword, no combat",
    },
    "64_pentacles_ace.png": {
        "scene": "terraced coinseed garden at sunrise, soil surface seen very close, dew on leaves, greenhouse roof blurred in the background",
        "subject": (
            "the young gardener's hands plant exactly one large purple-enamel Pi coinseed into rich soil, "
            "with the sprout mascot peeking in from the side. This is the first capital seed "
            "of the quiet merchant-gardener story."
        ),
        "composition": "macro low-angle planting close-up, one prominent coinseed, hands and soil emphasized",
    },
    "65_pentacles_two.png": {
        "scene": "village market stall beside the garden, a simple wooden scale, herbs and folded cloth, morning trade beginning",
        "subject": (
            "the gardener learns balance by placing exactly two purple-enamel Pi coinseeds on the two "
            "pans of a plain wooden-and-iron scale. The sprout mascot watches from the stall. "
            "No other gold discs or coin-like weights."
        ),
        "composition": "side-view market scale composition, two coinseeds equal and separated, practical daily-life mood",
    },
    "66_pentacles_three.png": {
        "scene": "open-air garden worktable beside the coinseed beds, top-down view of seedlings, soil, stone, and careful tools around the edges",
        "subject": (
            "the gardener studies cultivation with exactly three purple-enamel Pi coinseeds on the "
            "garden worktable. One mentor or helper is allowed only as subtle hands at the table edge, "
            "not a full second focal character."
        ),
        "composition": "high-angle garden worktable view, three coinseeds easy to count, cultivation-learning focus",
    },
    "67_pentacles_four.png": {
        "scene": "front of a tiny garden shop gate, cream stone threshold, violet awning, protected storage box beside a small plot",
        "subject": (
            "the gardener protects exactly four purple-enamel Pi coinseeds in a simple open storage box "
            "and close to their chest, showing care and caution without greed. The sprout mascot "
            "sits like a tiny shop guard."
        ),
        "composition": "straight-on storefront composition, four coinseeds clearly visible, protective mood",
    },
    "68_pentacles_five.png": {
        "scene": "rainy market alley outside the cozy garden shop and greenhouse, warm rectangular window glowing in the distance, wet stone path and folded stall cloth",
        "subject": (
            "the gardener and sprout mascot endure a difficult trading day, sheltering exactly "
            "five purple-enamel Pi coinseeds under a damp cloth. The shop window suggests help and "
            "hope, not despair."
        ),
        "composition": "side-distance rainy alley view, five coinseeds countable under shelter, quiet resilience",
    },
    "69_pentacles_six.png": {
        "scene": "village market stall after the rain, baskets of herbs, purple cloth, warm community light, no busy crowd",
        "subject": (
            "the gardener practices generosity by sharing exactly six purple-enamel Pi coinseeds arranged "
            "as two groups of three: three kept on the stall cloth and three being offered to "
            "one neighbor or child. The sprout mascot holds the edge of the cloth."
        ),
        "composition": "low close view of hands exchanging coinseeds, six readable in 3+3 groups, kind exchange",
    },
    "70_pentacles_seven.png": {
        "scene": "wide terraced garden at late afternoon, long rows of soil, growing vines, soft green shadows, market stall far below",
        "subject": (
            "seen from behind, the gardener waits thoughtfully beside exactly seven purple-enamel Pi "
            "coinseeds growing across one terrace row. The sprout mascot sits on the stone wall. "
            "This is patience after generosity."
        ),
        "composition": "wide rear-view terrace shot, seven coinseeds clearly visible across the row, spacious waiting mood",
    },
    "71_pentacles_eight.png": {
        "scene": "late-afternoon terraced coinseed farm, neat garden rows, irrigation channels, greenhouse in the distance, leaf shadows, tools kept matte iron and wood",
        "subject": (
            "the gardener carefully prunes, waters, or checks exactly eight purple-enamel Pi "
            "coinseeds growing from the soil in two garden rows of four. The sprout mascot "
            "watches near the irrigation channel."
        ),
        "composition": "slightly high-angle garden-row view, eight coinseeds countable as 4+4, focused cultivation mastery",
    },
    "72_pentacles_nine.png": {
        "scene": "lush harvest greenhouse aisle with vines, purple flowers, cream stone path, afternoon glow",
        "subject": (
            "the gardener walks alone through the greenhouse enjoying self-sufficient abundance. "
            "Exactly nine purple-enamel Pi coinseeds are arranged among the plants as three groups of "
            "three along both sides of the aisle, with the sprout mascot proudly nearby."
        ),
        "composition": "full-body greenhouse aisle shot, nine coinseeds readable as 3+3+3, elegant independence",
    },
    "73_pentacles_ten.png": {
        "scene": "wide courtyard where the small shop, workshop, and garden meet, mature greenery, village rooftops in the distance",
        "subject": (
            "a legacy scene: exactly ten purple-enamel Pi coinseeds are displayed on one low garden bed "
            "or raised bed in two rows of five. The gardener stands with the sprout mascot and "
            "at most one elder/helper in the background, showing the shop and garden can last."
        ),
        "composition": "wide courtyard legacy shot, ten coinseeds countable in 5+5 display, sense of home and continuity",
    },
    "74_pentacles_page.png": {
        "scene": "first morning in the coinseed garden, soft soil, tiny sprouts, notebook-like tool with no readable writing",
        "subject": "the young gardener as Page of Pentacles, carefully studying one purple-enamel Pi coinseed with curious devotion, sprout mascot beside them",
        "composition": "gentle youthful study, one prominent coinseed, one human protagonist",
    },
    "75_pentacles_knight.png": {
        "scene": "garden path between terraces and market fields, steady warm afternoon, practical tools packed neatly",
        "subject": "the gardener as Knight of Pentacles, carrying a sturdy basket with purple-enamel Pi coinseeds and tending the path with patient reliability; no horse required",
        "composition": "steady grounded forward movement, coinseeds visible but not glittery, one human protagonist",
    },
    "76_pentacles_queen.png": {
        "scene": "abundant greenhouse throne-like garden bench, leaves, soil, purple flowers, cream stonework",
        "subject": "the gardener matured into Queen of Pentacles, nurturing a purple-enamel Pi coinseed plant with warm practical grace, sprout mascot at their side",
        "composition": "nurturing centered portrait, earthy greens and creams dominate, readable golden plant accents",
    },
    "77_pentacles_king.png": {
        "scene": "terraced coinseed garden at golden late afternoon, sturdy workshop, harvest baskets, stone steps",
        "subject": "the gardener matured into King of Pentacles, calmly overseeing a thriving garden with purple-enamel Pi coinseed medallions integrated into soil, leaves, and tools",
        "composition": "stable regal garden composition, one human protagonist, grounded abundance without gold clutter",
    },
}


def sentence(value: str) -> str:
    return value.rstrip(".") + "."


def common_prompt(card: dict, scene: dict) -> str:
    suit = card["suit"]
    if suit == "pentacles":
        pi_motif = (
            "Pi motif: the Pentacles suit object is a purple-enamel Pi coinseed. Each visible "
            "coinseed should have a warm gold rim, deep purple enamel face, and a readable "
            "gold Pi-inspired emblem: two small square dots above, a thick continuous rounded "
            "bridge, two vertical stems, and a short solid upturned right arm attached to the "
            "right stem. The right side must look like the official app icon's filled upward "
            "hook, not a C-shaped loop, ring, circular hole, or swollen upper-right bulb. "
            "Make the motif larger or use fewer motifs if needed so the icon shape is readable. "
            "It should feel like original fantasy ornamentation inspired by the Pi coin icon, "
            "not a flat exact official vector copy."
        )
    else:
        pi_motif = (
            "Pi motif: do not add Pi coin badges, round Pi medallions, chest emblems, bag charms, "
            "or background Pi logos inside this non-Pentacles inner illustration; the fixed card "
            "template will supply the deck's Pi identity. If tiny ornamental geometry appears, it "
            "must not resemble a C-shaped Pi icon, coin emblem, or readable logo."
        )
    return "\n".join(
        [
            "Use case: stylized-concept",
            "Asset type: inner illustration only for a Pi-inspired tarot card; fixed frame and English text will be added later.",
            (
                "Reference image guidance: if the official Pi Network App Store icon reference "
                "has been shown in the conversation, use only its emblem structure for coin or "
                "medallion engravings: two dots, rounded bridge, two stems, and a solid upturned "
                "right hook with no C-shaped loop or circular hole. Do not copy the full reference "
                "image, flat-vector style, layout, border, or palette."
            ),
            f"Primary request: {card['name']} as a scene of the {suit.title()} suit story, high-quality kawaii fantasy anime-inspired tarot illustration.",
            f"Suit continuity: {SUIT_CONTINUITY[suit]}.",
            f"Scene/backdrop: {sentence(scene['scene'])}",
            f"Subject: {sentence(scene['subject'])}",
            f"Suit-specific discipline: {SUIT_GENERATION_RULES[suit]}",
            pi_motif,
            (
                "Gold usage: readable golden ornaments, medallions, and coin charms "
                "are welcome, but avoid gold-dust spray, all-over glitter, and tiny dense "
                "clothing speckles; suit colors dominate."
            ),
            f"Composition: vertical 1024x1536 full-bleed inner art, {scene['composition']}, enough breathing room for later crop into a fixed card template.",
            (
                "Style/medium: polished kawaii fantasy anime concept art, soft painterly lighting, "
                "crisp readable silhouettes, premium tarot illustration."
            ),
            (
                "Constraints: inner illustration only; no tarot card frame, no border, no nameplate, "
                "no readable text, no Latin or Greek words, no numbers, no watermark; keep the protagonist visually central. "
                "Faceless hands, arms, or partial bodies do not count as extra characters, and a few supporting "
                "figures are allowed when the scene needs them."
            ),
            (
                "Avoid: readable text, alphabet letters or numbers outside the Pi coin icon-like motif, "
                "extra suit objects beyond the requested count, "
                "oversized or distracting Pi logos that dominate the background, excessive "
                "metallic gold dust, all-over glitter, plain mathematical Greek pi glyphs, "
                "typed pi symbols, T-shaped coin marks, plus-sign coin marks, plain/no-emblem coins, Roman numeral II coin marks, "
                "two standalone vertical-bar coin marks, straight-horizontal-cap coin marks, C-shaped right loops, right-side circular holes, "
                "many tiny repeated Pi marks, official-logo-perfect flat vector copy, malformed two-oval smiley coins, clutter, and unrelated characters."
            ),
        ]
    )


def build_queue() -> list[dict]:
    cards = {card["filename"]: card for card in build_cards()}
    wanted = sorted(REPLACE_FILENAMES | {name for name in SCENES if not (INNER_DIR / name).exists()})
    queue = []
    for filename in wanted:
        card = cards[filename]
        scene = SCENES[filename]
        action = "replace" if filename in REPLACE_FILENAMES else "create"
        queue.append(
            {
                "filename": filename,
                "card_name": card["name"],
                "action": action,
                "prompt": common_prompt(card, scene),
            }
        )
    return queue


def as_markdown(queue: list[dict]) -> str:
    lines = [
        "# Pi Tarot ImageGen Prompt Queue",
        "",
        "Generate only inner illustrations. Save selected PNGs into `assets/tarot-cards-imagegen/inner/` with the exact filenames below, then run `tools/render_imagegen_deck.py`.",
        "",
        "Before prompts where the Pi coin emblem matters, show `assets/tarot-cards-imagegen/references/pi-network-appstore-icon-512.jpg` with `view_image` and tell built-in imageGen to use the official app icon's two dots, bridge, two stems, and solid upturned right hook as the medallion emblem reference. Do not use the deprecated `pi-network-icon-shape-reference.png` because its right side can read as a C-shaped hole.",
        "",
        f"Total prompts: {len(queue)}",
        "",
    ]
    for item in queue:
        lines.extend(
            [
                f"## {item['filename']} - {item['card_name']} ({item['action']})",
                "",
                "```text",
                item["prompt"],
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    parser.add_argument("--write", nargs="?", const=str(DEFAULT_OUT), help="Write Markdown to a path.")
    args = parser.parse_args(argv)

    queue = build_queue()
    if args.json:
        print(json.dumps(queue, ensure_ascii=False, indent=2))
        return 0

    markdown = as_markdown(queue)
    if args.write:
        out = Path(args.write)
        if not out.is_absolute():
            out = ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(markdown, encoding="utf-8")
        print(out)
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
