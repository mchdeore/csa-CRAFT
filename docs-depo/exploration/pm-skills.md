# phuryn/pm-skills — PM Skills Marketplace

**Source:** https://github.com/phuryn/pm-skills
**License:** MIT
**Last reviewed:** 2026-10-01
**Stars / adoption signal:** 26.7k stars, actively maintained (default branch `main`, last update 2026-10-01)
**Primary language:** Markdown + a small Python validator

## One-line summary

A marketplace of 9 Claude Code / Cowork plugins (68 skills, 42 commands) that
encode product-management frameworks — discovery, strategy, PRDs, launch,
metrics — as agentic skills.

## Why it's here

Two reasons:

1. **Skill-authoring pattern.** The repo is a reference implementation of the
   `.claude-plugin/plugin.json` + `skills/<name>/SKILL.md` + `commands/<name>.md`
   layout. Our chat agent in [chat/agent.py](../../chat/agent.py) wires tools
   through PydanticAI; if we later expose user-authored skills (versus hard-coded
   tools), the SKILL.md shape here is the de-facto convention to copy.
2. **Content library candidate.** If CRAFT ever needs built-in PM workflows for
   mission-engineering planning (discovery → strategy → PRD-equivalent for
   mission concepts), these skills are MIT-licensed and vendorable.

## Structure / key artifacts

- `.claude-plugin/marketplace.json` — root manifest listing all 9 plugins.
- `pm-{area}/` — one directory per plugin (`pm-product-discovery`,
  `pm-product-strategy`, `pm-toolkit`, `pm-execution`, `pm-go-to-market`,
  `pm-marketing-growth`, `pm-market-research`, `pm-data-analytics`,
  `pm-ai-shipping`).
- `pm-<area>/.claude-plugin/plugin.json` — per-plugin manifest.
- `pm-<area>/skills/<skill>/SKILL.md` — one folder per skill; the SKILL.md is
  the agent-facing prompt.
- `pm-<area>/commands/<command>.md` — one file per slash-command.
- `validate_plugins.py` — a plugin-manifest validator (small, auditable).
- `tests/` — unittest-based docs-consistency + validator tests.
- `CLAUDE.md` — single source of truth for repo structure and agent guidance.
- `.github/workflows/tests.yml` + `tag-on-merge.yml` — CI on PR/push, auto-tag on main.

## Integration ideas for CRAFT

- **Copy the SKILL.md convention** for how our chat agent describes tools to
  the LLM. Currently tool descriptions live inline in `tools/*/`
  (e.g. [tools/weather/forecast.py](../../tools/weather/forecast.py)); a sibling
  `SKILL.md` per tool folder would make them human-authorable without touching Python.
- **Mirror `validate_plugins.py`** for our own tool registry
  ([tools/registry.py](../../tools/registry.py)) — a schema-validated manifest
  keeps tools consistent as the catalog grows.
- **Lift the "docs-consistency test"** idea: a pytest that confirms every tool
  in the registry has matching docs. Fits our existing
  [app/tests/test_architecture.py](../../app/tests/test_architecture.py) style.
- **Not for direct dependency.** The repo is content + conventions, not a
  pip-installable library. Any adoption is manual vendoring under MIT attribution.

## Risks / caveats

- Opinionated PM framing — not every workflow transfers to mission engineering.
- Content, not code: no API stability guarantees; vendored copies will drift.
- Large repo (hundreds of markdown files); if we vendor, pick folders deliberately.
- MIT: fine to vendor with attribution; include the LICENSE file alongside any copied content.

## Citations

- Repo root: https://github.com/phuryn/pm-skills/tree/main
- Repo structure overview: https://github.com/phuryn/pm-skills/blob/main/CLAUDE.md
- Plugin manifest example: https://github.com/phuryn/pm-skills/blob/main/pm-toolkit/.claude-plugin/plugin.json
- Validator: https://github.com/phuryn/pm-skills/blob/main/validate_plugins.py
- License: https://github.com/phuryn/pm-skills/blob/main/LICENSE
