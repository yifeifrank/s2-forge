#!/usr/bin/env python3
"""Validate the deterministic, link-based S² Forge catalog."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
HEX_SHA = re.compile(r"^[0-9a-f]{40}$")
MATURITY_LEVELS = {"experimental", "preview", "stable"}
RELATIONSHIPS = {"first-party", "external"}
BUNDLED_WRITING_SKILLS = {"academic-humanizer", "humanizer"}


def require(mapping: dict, key: str, context: str):
    value = mapping.get(key)
    if value in (None, "", []):
        raise SystemExit(f"{context} is missing {key}")
    return value


def validate_https_github_url(value: str, context: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme != "https" or parsed.netloc != "github.com" or len(parsed.path.strip("/").split("/")) != 2:
        raise SystemExit(f"{context} must be a canonical https://github.com/<owner>/<repo> URL")


def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0":
        raise SystemExit("Unsupported catalog schema_version")

    collection = require(data, "collection", "catalog")
    validate_https_github_url(require(collection, "repository", "collection"), "collection.repository")
    collection_repo = collection["repository"].rstrip("/")

    skills = require(data, "skills", "catalog")
    if not isinstance(skills, list):
        raise SystemExit("catalog.skills must be a list")

    seen: set[str] = set()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for index, skill in enumerate(skills):
        context = f"skills[{index}]"
        skill_id = require(skill, "id", context)
        if skill_id in seen:
            raise SystemExit(f"Duplicate skill id: {skill_id}")
        seen.add(skill_id)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
            raise SystemExit(f"Invalid skill id: {skill_id}")

        for key in ("name", "description", "version", "skill_path", "license", "authors"):
            require(skill, key, context)
        if skill.get("maturity") not in MATURITY_LEVELS:
            raise SystemExit(f"Invalid maturity for {skill_id}")
        if skill.get("relationship") not in RELATIONSHIPS:
            raise SystemExit(f"Invalid relationship for {skill_id}")

        upstream = require(skill, "canonical_repository", context).rstrip("/")
        validate_https_github_url(upstream, f"{context}.canonical_repository")
        if upstream == collection_repo:
            raise SystemExit(f"{skill_id} must use a standalone canonical repository")
        if not HEX_SHA.fullmatch(str(require(skill, "reviewed_ref", context))):
            raise SystemExit(f"{skill_id} reviewed_ref must be a full lowercase Git SHA")
        for key in ("reviewed_on",):
            date.fromisoformat(str(require(skill, key, context)))

        capabilities = require(skill, "capabilities", context)
        for key in ("filesystem", "network", "commands", "credential_names", "external_actions", "unsafe_flag"):
            require(capabilities, key, f"{context}.capabilities")
        validation = require(skill, "validation", context)
        require(validation, "command", f"{context}.validation")
        if validation.get("status") not in {"passed", "partial", "not-run"}:
            raise SystemExit(f"Invalid validation status for {skill_id}")
        date.fromisoformat(str(require(validation, "checked_on", f"{context}.validation")))

        if skill["name"] not in readme or upstream not in readme:
            raise SystemExit(f"README catalog is missing {skill_id}")

    # Explicit writing-skill exceptions do not relax the external catalog rule.
    bundled = ROOT / "skills"
    found = set()
    for path in bundled.rglob("SKILL.md"):
        relative = path.relative_to(bundled)
        if len(relative.parts) != 2 or relative.parts[0] not in BUNDLED_WRITING_SKILLS:
            raise SystemExit(f"Unlisted bundled skill: {relative}; research skills belong in the catalog")
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            raise SystemExit(f"Missing skill frontmatter: {relative}")
        name = re.search(r"^name:\s*([^\n]+)$", parts[1], re.MULTILINE)
        if not name or name.group(1).strip() != relative.parts[0]:
            raise SystemExit(f"Skill name does not match directory: {relative}")
        if not re.search(r"^description:\s*\S", parts[1], re.MULTILINE):
            raise SystemExit(f"Missing skill description: {relative}")
        found.add(relative.parts[0])
    if found != BUNDLED_WRITING_SKILLS:
        raise SystemExit(f"Missing bundled writing skills: {sorted(BUNDLED_WRITING_SKILLS - found)}")

    print(f"OK: {len(skills)} catalog entry validated; canonical sources remain external")


if __name__ == "__main__":
    main()
