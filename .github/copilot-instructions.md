# Copilot instructions for this repo

This repository stores Irish Gaelic vocabulary and study notes for learning support. The main source file is `vocab.csv`, and the derived files are generated from it.

## Key rules
- Use `vocab.csv` as the canonical vocabulary source.
- Do not manually edit generated files unless the task explicitly requires regenerating them.
- Keep entries consistent with the existing schema and naming conventions.
- When adjusting vocabulary data, run the conversion script and confirm it succeeds.

## Regeneration
Run this from the repo root or inside the `python` directory:

```bash
cd python
python convert.py
```

This validates the vocabulary data, rebuilds `vocab_conv.csv`, and regenerates `vocab.md`.

## Scope
Focus on Irish-language learning workflows: vocabulary maintenance, note organization, study material indexing, and small data-quality improvements.
