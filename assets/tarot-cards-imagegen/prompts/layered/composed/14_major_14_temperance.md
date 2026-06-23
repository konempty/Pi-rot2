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

## arcanaPrompt

# arcanaPrompt - 14 Temperance

Source archive: `../ratio-regeneration/by-card/14_major_14_temperance.md`
Card file: `14_major_14_temperance.png`
Arcana: `major`

Use case: precise-object-edit

Primary request: Edit the visible tarot illustration of Temperance. Preserve the same winged figure, chalices, flowing water, river garden, mountains, crop, portrait aspect ratio, anime fantasy style, lighting, and color palette.

Only change Pi-logo containers that are square, rectangular, shield-shaped, or plaque-like into perfectly round purple-and-gold coin medallions. Specifically fix the central square Pi badge on the chest and the lower-left stone Pi plaque into circular Pi coin medallions. Keep the already-round Pi symbols on the chalices and small round ornaments unchanged.

Constraints: keep the figure's face, wings, hands, clothing, cups, water stream, river, flowers, mountains, composition, and lighting unchanged except for the specified Pi badge shapes. The Pi symbol must be the clean Pi Network mark, centered, gold on purple, with no extra C-shaped bulge and no square corners.

Avoid: new scene, infographic, poster, text, title, border, nameplate, watermark, altered face, altered hands, altered wings, changed crop, extra objects, square Pi icons.
