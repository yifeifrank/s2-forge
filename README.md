# S² Forge

**Expand what social science can study.**

S² Forge is a curated collection of agent skills for valid, transparent, and auditable social science research.

The collection is deliberately small. Each skill remains in its own canonical repository, with independent releases, issues, tests, licensing, and citation metadata. S² Forge reviews and describes those skills without copying their source code. This lets the catalog include both first-party projects and strong work maintained by other researchers.

## Catalog

| Skill | Best for | Status | Canonical source |
|---|---|---|---|
| **S² Searcher** | Searching once or studying at scale while preserving evidence in a validated research workspace | Preview · first-party | [`yifeifrank/s2-searcher`](https://github.com/yifeifrank/s2-searcher) |

The machine-readable record is [catalog.json](catalog.json). It includes stable identifiers, reviewed revisions, task fit, permissions, evidence contracts, validation, authorship, and citation metadata.

## Install S² Searcher

For a no-code installation, tell your agent:

> Install S² Searcher from `https://github.com/yifeifrank/s2-searcher` and tell me when it is ready.

After installation, describe your research question or repeated-case design in ordinary language. The skill’s [beginner guide](https://github.com/yifeifrank/s2-searcher/blob/main/docs/getting-started.md) provides copyable prompts for setup, dry runs, live research, review, and resumption.

## What S² Forge reviews

Catalog inclusion is an editorial decision, not a blanket claim that a skill is universally safe or that its substantive conclusions are valid. Reviews distinguish several questions:

- Does the skill follow an open, inspectable Agent Skills structure?
- Does it state what it is and is not appropriate for?
- Are permissions, network services, credential names, and unsafe modes declared?
- Can a reviewer reproduce a worked case and run deterministic checks?
- Are evidence, missingness, contradiction, and provenance policies explicit?
- Are authorship, licensing, limitations, and scholarly lineage documented?

See [the curation policy](docs/curation.md) for status levels and the full admission standard.

## Add a skill

S² Forge can catalog a skill from any public canonical repository; the maintainer does not need to transfer ownership or duplicate the code here. Proposals should add one catalog entry and explain how the skill improves social-science research practice. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing an entry.

Validate catalog changes locally with:

```bash
python3 scripts/validate_catalog.py
```

## Collection and distribution

GitHub is the source of truth for this public catalog and for each linked skill. Installers and packs may provide additional distribution later, but they should resolve back to the canonical repositories recorded here rather than become competing copies.
