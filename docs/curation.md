# S² Forge curation policy

S² Forge is an editorial collection, not a crawler, popularity leaderboard, or security certification. It favors a small number of inspectable skills that make social-science research more capable while preserving evidence, limitations, and scholarly accountability.

## Canonical-source rule

Every skill has one canonical upstream repository. S² Forge stores catalog metadata and a reviewed Git revision, not another maintained copy of the skill. First-party and external skills follow the same rule. External maintainers retain ownership, release control, and responsibility for their repositories.

## Admission criteria

A cataloged skill should provide:

1. a valid, self-contained `SKILL.md` with an accurate trigger description;
2. a public license and named maintainer;
3. clear best-fit and out-of-scope cases;
4. declared filesystem, command, network, credential, and external-action capabilities;
5. a worked end-to-end example with inspectable artifacts;
6. deterministic validation that does not require credentials;
7. an evidence policy appropriate to the claimed research task;
8. explicit handling of missing, conflicting, and uncertain information;
9. citation and scholarly lineage where relevant;
10. documented limitations, unsafe options, and human review points.

Meeting these criteria does not establish that every output is valid or that every deployment is safe. Technical reproducibility, least-privilege design, evidence traceability, and substantive validity are related but separate judgments.

## Maturity levels

- **Experimental**: a promising public implementation with a worked case, but limited independent use or incomplete boundary testing.
- **Preview**: the core workflow, documentation, deterministic checks, permissions, and known limitations are reviewable; broader field testing is still needed.
- **Stable**: versioned releases have survived repeated real research use, boundary cases, and substantive-method review with documented results.

A maturity change requires a new catalog review. A reviewed commit remains immutable even when the upstream default branch changes.

## Review and removal

Reviewers assess both implementation quality and fitness for the stated research method. Entries may be corrected, downgraded, or removed when an upstream project becomes unavailable, changes its licensing, weakens declared protections, or no longer meets the collection standard. Catalog history remains visible through Git.
