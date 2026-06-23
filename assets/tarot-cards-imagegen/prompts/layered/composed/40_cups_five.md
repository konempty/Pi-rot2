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

# arcanaPrompt - 40 Five of Cups

Source archive: `../ratio-regeneration/by-card/40_cups_five.md`
Card file: `40_cups_five.png`
Arcana: `minor`

Use case: stylized-concept
Primary request: Five of Cups as scene 5 of the Cups suit story: rainy pearlwater garden, a young purple-cloaked cup keeper mourns quietly beside a stream, but hope remains.
Scene/backdrop: rainy village garden with small bridge, lavender wisteria, wet stone path, soft silver-aqua reflections, distant pavilion.
Subject and exact cup layout: EXACTLY FIVE CUPS TOTAL. Place the cups in a simple countable 3+2 arrangement: THREE spilled pearl-white cups in the lower foreground only, arranged left, center, and right; TWO upright glowing pearl-white cups behind them near the kneeling figure. Make all five large and separated. Do not place any other cup-shaped object anywhere.
Strict negatives: no fourth spilled cup, no extra upright cup, no tiny background cup, no bowl, no goblet, no chalice ornament, no cup-shaped lantern, no cup-like reflection that reads as an object.
Character/anatomy: one youthful cup keeper in deep purple rain cloak, natural hands, quiet grieving expression, no distorted face or extra fingers.
Pi motif: include a readable purple-and-gold Pi Network inspired pendant on the cloak and small Pi seals on two of the five cups. The Pi symbol has a top bar, two vertical stems, two small square dots above, and a short attached upturned right hook. No C-shaped loop, no circular right-side hole, no swollen right bulge.
Composition/framing: target portrait art-slot aspect ratio close to 817x1014, about 0.806. Keep all five cups, face, hands, and Pi symbols safely away from edges with breathing room. No tarot frame, no border, no title, no number, no typography, no watermark.
Constraints: inner illustration only; exact cup count; no readable text, no words, no numbers.
Avoid: extra cups, wrong cup count, malformed Pi symbol, C-shaped Pi icon, extra fingers, distorted hands, infographic, diagram, poster layout.
