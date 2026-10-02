# Codebase & Development Rules

The checklist every change must respect. The tests in this directory enforce the rules; this file states them in prose.

Tests that back these rules:

- `test_architecture.py` — folder-structure, root-whitelist, cross-feature import, and tool-canonicalization rules.
- `test_rules.py` — code-quality rules (function length, cyclomatic complexity, TODO attribution, requirements hygiene).
- `test_entry.py` — entry-point boot sanity.

---

## Kanban Board Rules

Every PR must update the kanban board in `docs-depo/plans/kanban-board-files/`. No PR merges without it.

### Rule: Kanban task exists for every PR

- A `kanban_tasks` row must exist before the PR opens, with a title matching the work.
- Populate `github_pr_url` and `github_pr_number` on the task row when the PR is created.

### Rule: Structured PR description populated

When a PR is open, all seven structured fields in `kanban_tasks` must be filled:

| Field | What it holds | Why |
|-------|---------------|-----|
| `pr_change_summary` | One-paragraph summary of the change | Fellow devs can scan the board and understand what changed without reading the PR |
| `pr_scope_affected` | Comma-separated areas touched (database, api, ui, auth, connectors, tools, tests, docs-depo, plans) | Lets devs filter the board by area to find all PRs affecting their subsystem |
| `pr_behavior_changes` | BEFORE/AFTER comparison of every behavior change | Prevents silent regressions — reviewer knows exactly what to look for |
| `pr_test_suite` | Exact test commands and results | Anyone can re-run and confirm the change is safe |
| `pr_validation_criteria` | Checklist of conditions that must be true before merge | Makes review objective — no guessing what "done" means |
| `pr_unfinished_items` | Known gaps, deferred work, edge cases not handled | Transparent about what the PR does NOT do. Prevents follow-up surprises |
| `pr_related_issues` | Linked issues, dependent PRs, blocking PRs | Tracks the full chain of work across the board |

### Rule: PR description synced via template

- Use `.github/pull_request_template.md` to write the PR description.
- Run `python3 docs-depo/plans/kanban-board-files/sync_pr.py <task_id> <pr_description_file.md>` to sync the filled template into the database.
- The `pr_description_hash` field auto-computes a fingerprint of all fields — query it to find stale descriptions.

### Rule: Task moves to `review` when PR opens

- When a PR is opened, move the kanban task from `in-progress` to `review`.
- When the PR merges, move it to `done` and set `completed_at`.

## PR Finalization

Before marking a PR ready for review, follow `docs-depo/plans/markdown-plans/incomplete/finalize-pr-workflow.md`. The `finalize-pr` skill (`.cursor/skills/finalize-pr/SKILL.md`) automates this.

Minimum bar:
- `pytest app/tests/ -v --tb=short` passes with zero failures
- `ruff check app/` and `pyright app/` pass
- PR description fills every section of `.github/pull_request_template.md`
- Kanban task synced via `sync_pr.py`, moved to `review` column
