# Irish study repo instructions

## Project purpose
This repository is a learning workspace for Irish Gaelic vocabulary and notes, mainly focused on the Ulster dialect and material from multiple learning sources. The goal is to keep a clean, repeatable workflow for vocabulary study and note-taking.

## Important files
- `README.md` - high-level project overview.
- `vocab.csv` - canonical source for vocabulary entries.
- `vocab_conv.csv` - generated conversion output; do not manually edit unless you are intentionally regenerating the dataset.
- `vocab.md` - generated markdown view of the vocabulary table.
- `python/convert.py` - conversion script used to validate and regenerate the derived files.
- `index.md` - notes index for study content.

## Working conventions
- Treat `vocab.csv` as the source of truth.
- If you change vocabulary data, regenerate the derived files by running the conversion script.
- Prefer small, targeted edits instead of broad rewrites.
- Keep entries consistent with the existing structure and naming patterns already used in the CSV.
- Preserve the existing study workflow: add vocabulary, notes, or examples without disrupting the conversion pipeline.

## Regeneration workflow
When vocabulary data is changed, validate and regenerate outputs with:

```bash
cd python
python convert.py
```

This script checks the CSV for quality issues, creates `vocab_conv.csv`, and then generates `vocab.md`.

## Guidance for AI assistants
- Do not silently rewrite the vocabulary dataset without checking the surrounding structure.
- If a task touches vocabulary or conversion logic, verify the script still runs successfully afterward.
- Keep changes focused on the repo’s purpose: learning support, vocabulary tracking, and Irish-language study materials.
- When adding notes or docs, keep them concise and practical for study rather than generic explanatory prose.
