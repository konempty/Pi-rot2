## rootPrompt

# rootPrompt - Pi Tarot Deck

Apply this rootPrompt to every ImageGen request for Arcana 0-77.

Generate only the inner illustration for the fixed Pi Tarot card template. Do not generate a full card, ornate border, frame, nameplate, title, rank label, number, caption, Korean text, English text, watermark, or signature.

Target the art slot, not the whole tarot card: vertical portrait inner illustration, aspect ratio close to 817:1014, approximately 0.806 width/height. Keep faces, hands, suit objects, Pi emblems, and important symbolic objects safely inside the image with generous margins so the fixed frame and top medallion will not crop them.

Visual style: high-quality kawaii fantasy / polished anime-inspired tarot illustration for a premium mobile tarot deck. Use soft painterly lighting, clean readable silhouettes, detailed but not cluttered fantasy props, and a consistent purple-and-gold Pi Tarot identity. Main palette should harmonize around deep purple, lavender, cream, warm gold accents, and the relevant card or suit colors.

Pi motif rules: any Pi-inspired emblem must resemble the Pi Network coin/app icon structure, not a plain mathematical pi glyph. It should have two small square dots above, a thick continuous rounded bridge, two vertical stems below, and a short solid right arm attached to the right stem that turns upward. The right arm must not become a C-shaped loop, ring, circular hole, horseshoe, omega, swollen upper-right bulb, Roman numeral II, T mark, plus-sign mark, or two standalone bars. Prefer one or two readable round purple-and-gold medallions over many tiny noisy symbols. If the object is a coin or medallion, it must be round, not square or rectangular.

Anatomy and physical plausibility: natural faces, hands, limbs, clothing, held objects, animal companions, and occlusion. Animals and mascots must have animal or mascot limbs only, never human hands or arms. Avoid extra fingers, duplicated limbs, fused objects, malformed vessels, and impossible shared-object handling.

Count discipline: when a suit object count is requested, the count must be exact, large enough to verify at card scale, separated enough to count, and not confused by background props, reflections, decorations, or partial hidden objects.

Output should be a single coherent illustration, not an infographic, diagram, UI, poster, collage, or typography layout. No readable text of any kind.

---

## pentaclesSuitPrompt

# pentaclesSuitPrompt - The Coinseed Garden

Use this suitPrompt for Pentacles cards only.

Suit story: The Coinseed Garden. A grounded young gardener-merchant plants the first coinseed, learns balance and craft, protects value, endures scarcity, practices generosity, waits and improves, then builds abundance and legacy.

Consistent protagonist and companion: warm brown hair, green-violet apron, cream shirt, and a small sprout mascot. Numbered cards Ace-Ten should feel like the same gardener progressing through one practical garden-market story. Court cards may be symbolic role portraits but should stay grounded in material care and abundance.

Setting and mood: terraced coinseed garden, open-air garden worktables, village market, rainy market alley, harvest greenhouse, garden shop courtyard. Palette: garden green, soil brown, cream, deep violet, warm gold accents, soft sunset or lantern light.

Suit object: pentacles are purple-enamel Pi coinseeds or medallions with warm gold rims, grown or displayed among leaves, soil, stone, and careful garden tools. They should not look like plain gold coins, square app icons, generic discs, badges, buttons, or unrelated shop signs.

Pentacles count discipline: exact requested purple-enamel Pi coinseeds or medallions must be large and countable, not tiny glitter, coin piles, clothing buttons, background seals, or extra round decorations. Every visible countable coinseed should share the same warm gold rim, deep purple enamel face, and clean raised Pi-inspired emblem with no C-shaped right loop, no circular right-side hole, and no swollen upper-right bulb.

Continuity priority for Ace-Ten: same gardener, same sprout mascot with natural stubby mascot limbs only, exact coinseed count, outdoor garden-market continuity, and stable purple-enamel Pi coin styling.

---

## arcanaPrompt

# arcanaPrompt - 75 Knight of Pentacles

Source archive: `../ratio-regeneration/by-card/75_pentacles_knight.md`
Card file: `75_pentacles_knight.png`
Arcana: `minor`

Use case: precise-object-edit

Primary request: Edit the visible Knight of Pentacles tarot illustration. Preserve the same knight, farm market, basket of Pi coins, small companion creature, banner, shield, crop, portrait aspect ratio, anime fantasy style, lighting, and warm color palette.

Only change Pi-logo containers that are square, rectangular, shield-shaped, or plaque-like into perfectly round purple-and-gold coin medallions. Specifically fix the square Pi badge on the knight's chest and the square/rectangular Pi plaque on the shield into circular Pi coin medallions. Keep the basket coins, hanging staff medallion, banner emblem, and companion necklace as round coin medallions.

Constraints: keep the character's face, hands, armor, basket, shield position, companion creature anatomy, crops, market background, composition, and lighting unchanged except for the specified Pi badge shapes. The Pi symbol must be the clean Pi Network mark, centered, gold on purple, with no extra C-shaped bulge and no square corners.

Avoid: new scene, infographic, poster, text, title, border, nameplate, watermark, altered face, altered hands, altered companion anatomy, changed crop, extra objects, square Pi icons.
