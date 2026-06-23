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

## swordsSuitPrompt

# swordsSuitPrompt - The Moonwind Academy

Use this suitPrompt for Swords cards only.

Suit story: The Moonwind Academy. A clever sky student seeks clarity, confronts conflict and strategy, recognizes self-made limitation and anxiety, then reaches a symbolic dawn ending without gore.

Consistent protagonist and companion: silver-black bobbed hair, violet academy cloak, cream scarf, and a small owl-like wind familiar. Numbered cards Ace-Ten should feel like one academy student's mental journey. Court cards may be symbolic role portraits but should match the same moonlit academy polish.

Setting and mood: moonlit academy, misty shore, windy hill, archive, quiet chapel-like room, river crossing, dawn training hall. Palette: silver blue, moon blue, deep violet, pearl cream, pale wind light, restrained dawn gold.

Suit object: elegant silver practice swords with blue wind light. The suit should feel intellectual and nonviolent, not like a battlefield.

Swords count discipline: show only the requested readable sword or swords. Avoid extra blades, daggers, weapon piles, blade-shaped window bars, sword-like ribbons, sharp reflections, or background ornaments that can be counted as swords.

Continuity priority for Ace-Ten: same student, same owl familiar with animal anatomy only, exact sword count, non-gory symbolism, and a readable progression from clarity to dawn rebirth.

---

## arcanaPrompt

# arcanaPrompt - 63 King of Swords

Source archive: `../ratio-regeneration/by-card/63_swords_king.md`
Card file: `63_swords_king.png`
Arcana: `minor`

Use case: precise-object-edit

Primary request: Edit the visible King of Swords tarot illustration. Preserve the same king, owl, throne, sword, scroll, sky, castle, crop, portrait aspect ratio, anime fantasy style, lighting, and color palette.

Only change Pi-logo containers that are square, rectangular, shield-shaped, or plaque-like into perfectly round purple-and-gold coin medallions. Specifically fix the square Pi plaque on the sword hilt, the owl's square necklace Pi plaque, and the square Pi plaque on the lower scroll into circular Pi coin medallions. Keep the already-round Pi emblem on the right flag unchanged.

Constraints: keep the king's face, hands, crown, robe, sword blade, owl anatomy, throne, scroll, background, composition, and lighting unchanged except for the specified Pi badge shapes. The Pi symbol must be the clean Pi Network mark, centered, gold on purple, with no extra C-shaped bulge and no square corners.

Avoid: new scene, infographic, poster, text, title, border, nameplate, watermark, altered face, altered hands, altered owl anatomy, changed crop, extra objects, square Pi icons.
