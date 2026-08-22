# Contributing

S² Forge curates agent skills that materially improve social-science research. A skill may be maintained by Yifei Zhu, another researcher, a research group, or an independent developer. Its source remains in its canonical upstream repository.

## Propose a catalog entry

Add or update one object in `catalog.json` and, when appropriate, the catalog table in `README.md`. Do not vendor, fork, or copy the skill into this repository merely to list it.

Every proposal should identify:

- the stable skill ID, name, canonical repository, and `SKILL.md` path;
- the maintainer, license, version or reviewed commit, and maturity level;
- the research tasks for which the skill is and is not a good fit;
- supported agents and required software;
- filesystem, command, network, credential, and external-action requirements;
- the evidence, provenance, missingness, and contradiction policy;
- a worked end-to-end case, deterministic validation command, and known limitations;
- software citation and related scholarly work, when applicable.

External skills remain governed and released by their upstream maintainers. S² Forge records the exact revision it reviewed and should not imply endorsement of later changes automatically.

## Review standard

Review has two parts:

1. **Technical review** checks the Agent Skills structure, declared capabilities, least-privilege behavior, credential handling, reproducible validation, licensing, and provenance.
2. **Research-method review** checks whether the skill’s evidence and output contracts are suitable for its stated social-science use, including boundaries, conflicting evidence, missing values, and failure cases.

The catalog uses `experimental`, `preview`, and `stable` maturity levels. These describe the amount of public testing and review; they are not safety guarantees or claims of substantive validity. See `docs/curation.md` for the complete criteria.

## Validate a change

Run:

```bash
python3 scripts/validate_catalog.py
```

The validator checks the catalog schema, unique IDs, canonical URLs, immutable reviewed revisions, documentation links, and accidental vendoring. It intentionally performs no network calls, so CI remains deterministic.
