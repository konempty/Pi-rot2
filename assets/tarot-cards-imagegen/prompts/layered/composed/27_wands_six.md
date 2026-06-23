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

# arcanaPrompt - 27 Six of Wands

Source archive: `../ratio-regeneration/by-card/27_wands_six.md`
Card file: `27_wands_six.png`
Arcana: `minor`

Use case: precise-object-edit

Primary request: Edit the visible Six of Wands tarot illustration. Preserve the same festival scene, central celebrant, crowd, lighting, colors, anime fantasy style, and portrait crop.

Only fix the object count: there must be exactly six tall magical wands/staffs visible across the upper scene, not seven. Remove one wand cleanly, preferably the far-left extra wand, and fill the background naturally with sky, confetti, and crowd details. Keep the remaining six wands evenly spaced, upright, ornate, and clearly visible.

Constraints: keep all Pi coin medallions on the remaining wands perfectly round purple-and-gold coins with the clean Pi Network mark. Keep the central character's round chest Pi coin unchanged. Do not alter faces, hands, clothing, crowd, city, lighting, or composition except removing the extra wand.

Avoid: new scene, infographic, poster, text, title, border, nameplate, watermark, seven wands, fewer than six wands, square Pi icons, extra limbs, distorted hands.
