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

# arcanaPrompt - 02 The High Priestess

Source archive: `../ratio-regeneration/by-card/02_major_02_the-high-priestess.md`
Card file: `02_major_02_the-high-priestess.png`
Arcana: `major`

Use case: precise-object-edit
Input image: the provided High Priestess tarot inner illustration is the edit target.
Primary request: Keep the exact same canvas aspect ratio and framing as the input image. Change only Pi Network symbols drawn as square app icons, square badges, rectangular patches, or flat square plaques into circular Pi coin medallions.
Specific targets in this image: the square Pi plaque on the right stone pillar, plus any other Pi symbol container that reads as a square app icon or rectangular badge. Keep already-round medallions round and unchanged except for minor polish.
Invariants: Preserve the original composition, crop, woman, face, pose, moon crown, scroll, robes, pillars, lake, flowers, curtains, lighting, color palette, image ratio, and tarot symbolism. Do not redraw the scene. Do not add or remove people, moons, scrolls, pillars, flowers, or background details.
Canvas constraint: output must match the input image's portrait art-slot framing, approximately 817:1014 ratio. Do not convert it into a full tarot-card ratio, do not add a border, and do not add a nameplate.
Pi coin requirement: every Pi symbol must sit inside a perfectly round purple-and-gold coin or medallion. No square icon, no rectangle patch, no app-icon tile, no flat square plaque, no C-shaped right side.
Avoid: changing anything except the shape/material of Pi-symbol containers; no text, no border, no new objects, no count changes, no style shift.
