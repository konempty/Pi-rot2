# Layered ImageGen Prompts

This directory is the current prompt source for future Pi Tarot image generation.

Layer order for every request:

1. `root.md` - rules shared by all 78 Arcana.
2. `suits/<suit>.md` - suit-level continuity and count rules for minor Arcana only. Major Arcana skip this layer.
3. `arcana/<group>/<card>.md` - card-specific scene, count, edit, and avoidance instructions.

Use `tools/compose_layered_imagegen_prompt.py` to build the actual prompt passed to ImageGen:

```bash
python3 tools/compose_layered_imagegen_prompt.py 31_wands_ten
python3 tools/compose_layered_imagegen_prompt.py --stdout 31_wands_ten
python3 tools/compose_layered_imagegen_prompt.py
```

The generated request prompts are written to `composed/`. Existing files under `prompts/ratio-regeneration/by-card/` are kept as historical prompt archives and source references.
