# Pi Tarot Prompt Archive

This directory stores prompt material for the 78-card ImageGen tarot deck.

- `layered/`: current prompt source for future ImageGen requests.
  - `root.md`: rules shared by all 78 Arcana.
  - `suits/*.md`: suit-level continuity and count rules for minor Arcana only.
  - `arcana/<group>/*.md`: card-specific Arcana prompts.
  - `composed/*.md`: generated request prompts built as root + optional suit + Arcana.
- `ratio-regeneration/by-card/`: historical one-file-per-card prompt archive.
- `targeted-round-pi-edits-20260619/`: historical targeted edit prompts.

Build current request prompts with:

```bash
python3 tools/compose_layered_imagegen_prompt.py
python3 tools/compose_layered_imagegen_prompt.py --stdout 31_wands_ten
```

Current rendering uses the transparent no-text template and does not place title text directly on cards.
