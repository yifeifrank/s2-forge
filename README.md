# S² Forge

**Expand what social science can study.**

S2 Forge provides agent skills for ambitious, transparent, and auditable research.

Each skill is self-contained under `skills/` and includes its own behavior, documentation, validation, and license metadata.

## Skill catalog

| Skill | Description | Status |
|---|---|---|
| [Research Workspace Builder](skills/research-workspace-builder/README.md) | Preserves reusable sources and task-specific evidence for repeated-case studies and open-ended inquiries. | `v0.1.0` friend preview |

Research Workspace Builder generalizes the research workflow associated with Yifei Zhu, Songpo Yang, Jiangnan Zhu, and Junyan Jiang, [“Agentic Framework for Political Biography Extraction”](https://doi.org/10.48550/arXiv.2603.18010) (arXiv:2603.18010). The preprint remains under review. Yifei Zhu is the software author; see the subskill's [CITATION.cff](skills/research-workspace-builder/CITATION.cff) for versioned citation metadata.

## Install a skill

For an agent-first installation, tell your runtime:

> Install the Research Workspace Builder skill from `https://github.com/yifeifrank/s2-forge/tree/main/skills/research-workspace-builder`, then tell me when to reload the session.

After installation, describe an Inquiry or repeated-case Study in ordinary language. The agent should create and validate the workspace; beginners do not need to write codebooks, manifests, or terminal commands. The [no-code getting-started guide](skills/research-workspace-builder/docs/getting-started.md) provides copyable prompts.

For manual installation, clone this collection and link the selected skill into the runtime's skill directory:

```bash
git clone https://github.com/yifeifrank/s2-forge.git
ln -s /absolute/path/to/s2-forge/skills/research-workspace-builder \
  ~/.codex/skills/research-workspace-builder
```

For Claude Code, install the same directory under `~/.claude/skills/research-workspace-builder`. Reload the runtime after installing or updating a skill.

## Safety

Research Workspace Builder uses least-privilege defaults: Codex uses `workspace-write` with network access and no approval escalation, while Claude Code uses its sandbox and fails closed. Its `--unsafe-unattended` option bypasses runtime permission enforcement and must be used only inside an externally isolated, disposable container or virtual machine. Read the subskill's [security guidance](skills/research-workspace-builder/SECURITY.md) before live research runs.

## Validate

Run the credential-free release check from the collection root:

```bash
python3 skills/research-workspace-builder/scripts/release_check.py
```

The root GitHub Actions workflow runs the same check on supported Python versions.
