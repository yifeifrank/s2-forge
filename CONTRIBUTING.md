# Contributing

Skills live at `skills/<skill-name>/`, where `<skill-name>` matches the `name` field in the skill's `SKILL.md` frontmatter.

Each skill should remain self-contained and include its public documentation, license, validation entry point, and citation metadata when applicable. Do not commit credentials, `.env` files, generated archives, caches, bytecode, private data, or machine-specific absolute paths. Keep `.env.example` files limited to documented placeholders.

Before proposing a change:

1. Run the affected skill's validation from the collection root.
2. Confirm that safe permission defaults remain intact and document any requested expansion.
3. Update the root catalog when adding, renaming, or removing a skill.
4. Describe behavioral, schema, compatibility, and citation changes in the review request.

For Research Workspace Builder, run:

```bash
python3 skills/research-workspace-builder/scripts/release_check.py
```
