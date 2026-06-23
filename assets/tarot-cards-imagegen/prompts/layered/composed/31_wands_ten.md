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

# arcanaPrompt - 31 Ten of Wands

Source archive: `../ratio-regeneration/by-card/31_wands_ten.md`
Card file: `31_wands_ten.png`
Arcana: `minor`

Use case: precise-object-edit
Input images: Image 1 is the edit target, the current Wands 10 image with exactly ten staffs and aspect ratio about 0.805. Image 2 is only an age/style reference showing the desired younger teenage character feeling.

Primary edit request: Keep the current image canvas, crop, composition, and exactly ten staffs unchanged, but make only the central character look like a 15-17 year old adolescent mage again instead of a 25-year-old adult. Preserve the same character identity, purple-gold outfit, cloak, pendant, pose, lighting, and fantasy tarot style, but soften the facial structure and proportions to read as a teenage boy: smaller/softer jaw, rounder youthful face, slightly larger expressive eyes, less mature cheekbones, slimmer adolescent body frame, narrower shoulders, less adult masculine build.

Critical preservation rules:
- Keep the same canvas ratio as the edit target: width/height about 0.805, not 0.667.
- Do NOT change the ten staffs. Keep exactly five staffs on the left and exactly five staffs on the right.
- Do NOT add, remove, duplicate, crop, or redraw any staff.
- Count the purple crystal tips: exactly 10 crystal-tipped staffs total.
- Keep the mountain sunset background, road, flowers, castle, sky, and magic circles unchanged.
- Keep all Pi emblems on round coin medallions only; no square Pi icons.

Character age target: adolescent male mage, around 15-17 years old. He should look determined and powerful but still clearly youthful. Avoid adult 20s face, mature jaw, broad adult shoulders, beard, stubble, rugged older expression, or overly tall adult proportions.

Hard constraints: edit only character age/proportions; preserve current aspect ratio about 0.805; exactly 10 staffs total; exactly five left and five right; one human character only; natural anatomy; no extra limbs; no swords or blades; no horizontal stretching; no square Pi icons.

Avoid: narrow 2:3 output, adult man, 25-year-old look, mature masculine face, changed staff count, 8 staffs, 9 staffs, 11 staffs, 12 staffs, extra staff-like objects, changed background, readable text.
