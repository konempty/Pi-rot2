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

## cupsSuitPrompt

# cupsSuitPrompt - The Pearlwater Village

Use this suitPrompt for Cups cards only.

Suit story: The Pearlwater Village. A gentle cup keeper receives emotional water, shares connection, experiences withdrawal and loss, faces dream choices, leaves for deeper meaning, and returns to quiet contentment and community joy.

Consistent protagonist and companion: soft lavender-brown hair, pearl hairpin, purple-and-cream seaside clothes, and a tiny water-sprite companion. Numbered cards Ace-Ten should feel like the same cup keeper moving through one emotional arc. Court cards may be symbolic role portraits but should stay close to the suit palette and emotional softness.

Setting and mood: moonlit pearl pond, seaside garden, fountain courtyard, rainy shore, quiet coast, reflective water, wisteria, lotus, roses, soft aqua glow. Palette: purple, lavender, pearl white, aqua, cream, moon silver, and restrained warm gold.

Suit object: cups are pearl-white vessels with soft aqua glow. They should be visually distinct from bowls, vases, jars, lanterns, shells, trophies, or pitcher decorations.

Cups count discipline: only the requested cups should read as cups. Avoid extra goblets, bowls, vases, chalices, cup-like ornaments, cup-shaped lanterns, or reflections that could confuse the count.

Continuity priority for Ace-Ten: same protagonist, same water-sprite companion, same seaside-water world, exact cup count, and a clear emotional progression.

---

## arcanaPrompt

# arcanaPrompt - 42 Seven of Cups

Source archive: `../ratio-regeneration/by-card/42_cups_seven.md`
Card file: `42_cups_seven.png`
Arcana: `minor`

Use case: stylized-concept
Primary request: Seven of Cups as scene 7 of the Cups suit story, high-quality kawaii fantasy anime tarot illustration. A young purple-cloaked cup keeper faces exactly seven floating dream cups above a mirror pool.
Scene/backdrop: misty sunset mirror pool, lavender flowers, glowing cloud platforms, soft violet and aqua haze.
Subject and exact layout: EXACTLY SEVEN CUPS TOTAL. Arrange seven pearl-white cups in a compact oval cluster around the upper and middle area of the scene: one cup at top center, two cups upper left and upper right, two cups middle left and middle right, and two cups lower left and lower right near the character's shoulders. Each cup is large, separate, and easy to count. Each cup contains one dream symbol such as flower, castle, star, ribbon, crystal, water sprite, or Pi coin. No other cup-shaped object exists anywhere.
Strict negatives: no missing seventh cup, no sixth-only layout, no extra cup, no cup-like reflection, no goblet, no bowl, no mug, no chalice ornament, no cup-shaped lantern.
Character/anatomy: one youthful cup keeper in deep purple cloak at lower foreground, visible from knees up, natural hand reaching carefully, no extra fingers.
Pi motif: include a readable purple-and-gold Pi Network inspired symbol in one dream cup and a small Pi pendant on the keeper. The Pi symbol has a top bar, two vertical stems, two small square dots above, and a short attached upturned right hook. No C-shaped loop or circular right-side hole.
Composition/framing: target portrait art-slot aspect ratio close to 817x1014, about 0.806. The picture should be taller than wide but not tall-narrow. Keep all seven cups and the character safely away from edges.
Constraints: inner illustration only; no tarot card frame, no border, no nameplate, no readable text, no words, no numbers, no watermark.
Avoid: wrong cup count, malformed Pi symbol, C-shaped Pi icon, extra fingers, distorted hands, infographic, diagram, poster layout.
