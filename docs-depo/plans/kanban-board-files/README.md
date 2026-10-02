# kanban-board-files

Kanban board for tracking csa-CRAFT project development. Lives inside the existing `app/database/cheddar.db` — no separate database needed.

Every card links to:
- **GitHub PR** — `github_pr_url` + `github_pr_number`
- **Development plan** — file path to a plan in `plans/`
- **Development description** — file path to a detailed design doc or spec

## Setup

```bash
# From repo root — creates tables + seeds default columns
bash docs-depo/plans/kanban-board-files/setup.sh

# If upgrading from v1 schema — apply v2 additions
sqlite3 app/database/cheddar.db < docs-depo/plans/kanban-board-files/schema_v2_additions.sql

# Load example cards
python3 docs-depo/plans/kanban-board-files/load_cards.py
```

## Files

All files that make up the kanban board system. Grouped by purpose.

### Core: this directory (`docs-depo/plans/kanban-board-files/`)

| File | Absolute path | Purpose |
|------|---------------|---------|
| `schema.sql` | `docs-depo/plans/kanban-board-files/schema.sql` | Table definitions — `kanban_columns`, `kanban_tasks`, `kanban_comments`, `kanban_moves` |
| `schema_v2_additions.sql` | `docs-depo/plans/kanban-board-files/schema_v2_additions.sql` | Adds structured PR description columns to `kanban_tasks` (summary, scope, behavior, tests, validation, unfinished, related, hash) |
| `seed.sql` | `docs-depo/plans/kanban-board-files/seed.sql` | Default columns (backlog → todo → in-progress → review → done) + one example task |
| `cards.json` | `docs-depo/plans/kanban-board-files/cards.json` | Task definitions in JSON. Edit this to add tasks, then run `load_cards.py` |
| `load_cards.py` | `docs-depo/plans/kanban-board-files/load_cards.py` | Reads `cards.json` and inserts rows into `kanban_tasks` |
| `sync_pr.py` | `docs-depo/plans/kanban-board-files/sync_pr.py` | Parses a filled `.github/pull_request_template.md` copy and syncs structured fields into `kanban_tasks` |
| `setup.sh` | `docs-depo/plans/kanban-board-files/setup.sh` | One-shot: applies `schema.sql` + `seed.sql` against `app/database/cheddar.db` |
| `queries.sql` | `docs-depo/plans/kanban-board-files/queries.sql` | Common queries: board overview, open PRs, stalled tasks, WIP limits, recent moves |
| `queries_v2.sql` | `docs-depo/plans/kanban-board-files/queries_v2.sql` | Extended queries: PR sync status, scope summary, unfinished items, validation criteria |
| `example-pr-description.md` | `docs-depo/plans/kanban-board-files/example-pr-description.md` | Filled example of the PR template — reference for what a complete description looks like |
| `kanban_server.py` | `docs-depo/plans/kanban-board-files/kanban_server.py` | Standalone Flask server — browse the board at `http://localhost:8051` |

### Database

| File | Absolute path | Purpose |
|------|---------------|---------|
| `cheddar.db` | `app/database/cheddar.db` | The SQLite database. Kanban tables live inside this alongside app tables. No separate DB. |

### PR workflow integration

| File | Absolute path | Purpose |
|------|---------------|---------|
| Pull request template | `.github/pull_request_template.md` | Template for every PR. Fill this, then sync to kanban via `sync_pr.py` |
| Finalize-PR skill | `.cursor/skills/finalize-pr/SKILL.md` | Agent skill that automates the full finalize-PR-to-kanban pipeline |
| Finalize-PR runbook | `docs-depo/plans/finalize-pr-workflow.md` | Step-by-step human/agent runbook for finalizing a PR (tests → lint → template → kanban sync → review) |

### Governance

| File | Absolute path | Purpose |
|------|---------------|---------|
| Codebase rules | `app/tests/CODEBASE_RULES.md` | Kanban board rules — every PR must update the board, no merge without it. Structured fields required. |
| Board README | `docs-depo/plans/kanban-board-files/README.md` | This file. Complete file map and usage guide. |

## File dependencies (what uses what)

```
app/database/cheddar.db
  ← schema.sql (creates tables)
  ← seed.sql (inserts default data)
  ← schema_v2_additions.sql (upgrades to v2)
  ← load_cards.py (inserts task cards)
  ← sync_pr.py (updates PR description fields)
  ← queries.sql / queries_v2.sql (reads data)

cards.json → load_cards.py → kanban_tasks

.github/pull_request_template.md → (copy → edit) → sync_pr.py → kanban_tasks

app/tests/CODEBASE_RULES.md → enforces board update rule
  .cursor/skills/finalize-pr/SKILL.md → automates the workflow
  docs-depo/plans/finalize-pr-workflow.md → step-by-step runbook
```

## Migration between environments

To recreate the board on a fresh clone or new machine:

```bash
# 1. Create tables + seed columns
bash docs-depo/plans/kanban-board-files/setup.sh

# 2. Apply v2 schema if upgrading
sqlite3 app/database/cheddar.db < docs-depo/plans/kanban-board-files/schema_v2_additions.sql

# 3. Load all tasks
python3 docs-depo/plans/kanban-board-files/load_cards.py
```

The only state that lives outside source control is `app/database/cheddar.db`. All schema, seeds, cards, and queries are versioned in the repo. To migrate, copy `cards.json` and re-run setup — everything else is reproducible.

## Columns

| Column | WIP limit | Meaning |
|--------|-----------|---------|
| backlog | none | Ideas and future work, not yet prioritized |
| todo | none | Ready to pick up |
| in-progress | 3 | Actively being worked on |
| review | 2 | PR open, awaiting review |
| done | none | Merged and shipped |

## Adding a task

Edit `cards.json` with this shape:

```json
{
  "title": "Short task name",
  "description": "What needs to happen and why.",
  "column": "backlog",
  "github_pr_url": "https://github.com/owner/repo/pull/42",
  "github_pr_number": 42,
  "development_plan_file": "plans/my-feature-plan.md",
  "development_description_file": "specs/my-feature-design.md",
  "priority": "high",
  "assignee": "username",
  "tags": ["frontend", "api"],
  "estimated_hours": 8
}
```

Then run `python3 docs-depo/plans/kanban-board-files/load_cards.py` to insert it.

## Syncing a PR description

When a PR is open, fill out `.github/pull_request_template.md` and sync it into the kanban board:

```bash
python3 docs-depo/plans/kanban-board-files/sync_pr.py <task_id> <path-to-filled-pr-template.md>
```

This populates all structured PR fields: `pr_change_summary`, `pr_scope_affected`, `pr_behavior_changes`, `pr_test_suite`, `pr_validation_criteria`, `pr_unfinished_items`, `pr_related_issues`, and auto-computes a `pr_description_hash` for staleness detection.

## Querying

```bash
# Full board overview
sqlite3 app/database/cheddar.db ".headers on" ".mode column" < docs-depo/plans/kanban-board-files/queries.sql

# Extended overview with PR description sync status
sqlite3 app/database/cheddar.db ".headers on" ".mode column" < docs-depo/plans/kanban-board-files/queries_v2.sql
```

## Workflow (required per CODEBASE_RULES.md)

1. Create task in `cards.json` → run `load_cards.py`
2. Start work → move task to `in-progress`
3. Open PR → populate `github_pr_url` + `github_pr_number`
4. Fill `.github/pull_request_template.md`
5. Run `sync_pr.py <task_id> pr-descriptions/my-feature-pr.md`
6. Move task to `review`
7. After merge → move to `done`