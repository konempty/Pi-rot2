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

## wandsSuitPrompt

# wandsSuitPrompt - The Ember Trail

Use this suitPrompt for Wands cards only.

Suit story: The Ember Trail. A youthful spark apprentice discovers creative fire on a lavender mountain trail, reaches a warm mountain village, learns through practice and recognition, defends the village lights, and finally accepts responsibility for the flame.

Consistent protagonist and companion: short dark wavy hair, violet eyes, purple travel cloak, cream tunic, orange scarf, star satchel, and a small cream fox-like companion. Numbered cards Ace-Ten should feel like the same adolescent protagonist progressing through one continuous story. Court cards may be more symbolic role portraits but should still share the suit's visual language.

Setting and mood: lavender mountain trail, Ember Academy, warm village festival, ridge at night, sunrise return path. Warm orange fire, deep purple, lavender, cream, and controlled gold accents.

Suit object: wands are refined magical staffs or ritual rods with gold bands, violet crystals, and soft orange flame. They should not read as mundane lumber, chopped wood, branch piles, fence posts, poles, banners, or random sticks.

Wands count discipline: only the requested magical staffs should read as wands. Avoid extra pole-like trees, posts, banners, spare sticks, branch shapes, or staff-like decorations that could be counted as additional wands.

Continuity priority for Ace-Ten: same protagonist, same fox companion, same outfit family, same mountain-village world, exact wand count, and a readable step in the Ember Trail story.

---

## arcanaPrompt

# arcanaPrompt - 22 Ace of Wands

Source archive: `../ratio-regeneration/by-card/22_wands_ace.md`
Card file: `22_wands_ace.png`
Arcana: `minor`

Create the inner illustration for Ace of Wands.

Archive ID for saving only: 22_wands_ace_ratio_full. Do not draw this ID.

Use the displayed current Ace of Wands image as the primary visual reference. Preserve its concept, characters, mood, color harmony, and story context as closely as possible: the dark violet-black-haired Wands apprentice discovers one living magical staff sprouting from glowing earth at sunrise, with a small fox companion nearby, lavender mountain valley and guild-city in the distance, warm creative fire awakening.

Target image shape: portrait art-slot aspect ratio close to 817x1014, about 0.806. Do not use the old very tall 2:3 card ratio. Keep face, fox, staff, hands, and Pi charm safely inside the image with breathing room on all edges.

Critical count: EXACTLY ONE WAND/STAFF TOTAL. The single living staff is the clear central suit object. No extra rods, branches shaped like additional staffs, poles, spear shapes, fence posts, or staff-like decorations.

Pi motif: keep a visible purple-and-gold or gold Pi charm/medallion on the apprentice, clear but secondary. The Pi symbol should have a straight or gently rounded top bar, two vertical stems, two small square dots above, and a short attached upturned right hook. Avoid C-shaped loop, circular right-side hole, ring, swollen bulb, pig nose, Roman numeral II, number 2, omega, horseshoe.

Avoid: extra staffs, extra branches that read as staffs, malformed Pi symbol, C-shaped Pi icon, text, border, title, number, watermark, distorted hands, animal with human arms.
