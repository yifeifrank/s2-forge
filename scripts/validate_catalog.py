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

    vendored_skills = ROOT / "skills"
    if vendored_skills.exists() and any(vendored_skills.rglob("SKILL.md")):
        raise SystemExit("S² Forge catalogs canonical repositories; do not vendor skill copies")

    print(f"OK: {len(skills)} catalog entry validated; canonical sources remain external")


if __name__ == "__main__":
    main()
