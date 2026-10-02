---
name: finalize-pr
description: Run full test suite, lint, type-check, format a PR description from the template, sync it to the kanban board, and prepare a branch for review. Use when the user says "finalize", "ship it", "ready for review", "prepare PR", or wants to open a pull request.
---

# Finalize PR

## Quick Start

Follow `docs-depo/plans/markdown-plans/incomplete/finalize-pr-workflow.md` step by step. The plan has every command and troubleshooting table.

## The steps in order

1. **Run tests**: `pytest app/tests/ -v --tb=short`
2. **Fix failures**: Read the error — each test self-documents the rule it enforces
3. **Lint + type**: `ruff check app/ && pyright app/`
4. **Build PR description**: Copy `.github/pull_request_template.md` → `pr-descriptions/<feature>.md` and fill every section
5. **Open PR** on GitHub with the filled template
6. **Sync kanban**: `python3 docs-depo/plans/kanban-board-files/sync_pr.py <task_id> pr-descriptions/<feature>.md`
7. **Move to review**: Set `column_id` to `review`, populate `github_pr_url` + `github_pr_number`
8. **Verify board**: Run `docs-depo/plans/kanban-board-files/queries_v2.sql` — confirm all structured fields populated
9. **Request review** from a teammate
10. **After merge**: Move task to `done`, set `completed_at`

## Troubleshooting guide

| Test failure | Fix |
|-------------|------|
| Missing return annotation | Add `-> None` or proper return type |
| Function too long (>250 lines) | Split into smaller helpers |
| Complexity too high (>15) | Flatten nested conditionals, extract early returns |
| Import not in requirements.txt | Add to `app/requirements.txt` |
| Missing `log_function_call` | Add decorator to public functions |
| `print()` in code | Replace with `logging.info()` |
| `TODO` without owner | Change to `# TODO(name)` or `# TODO(#issue)` |
| Bare `except:` | Catch a specific type: `except ValueError:` |
| Circular import | Fix path — test shows exact error |
| Cross-feature import | Import from feature's public API, not internals |
| Root `.py` not whitelisted | Move into feature folder or add to whitelist |

## PR description template

The template at `.github/pull_request_template.md` requires these sections filled:
- **Summary** — one paragraph, what and why
- **Scope Affected** — checkboxes for areas touched
- **Behavior Changes** — BEFORE/AFTER for each change
- **Test Suite** — exact commands and results
- **Validation Criteria** — checklist of merge conditions
- **Unfinished Items** — known gaps, deferred work
- **Related Issues** — linked issues, dependent/blocking PRs

Do not skip any section. Empty sections break the kanban sync.

## Kanban sync

After syncing, the kanban task stores all structured fields plus a `pr_description_hash` for staleness detection. The `pr_summary`, `pr_scope_affected`, `pr_behavior_changes`, `pr_test_suite`, `pr_validation_criteria`, `pr_unfinished_items`, and `pr_related_issues` columns must all be non-empty for the sync to be valid.

## All-in-one shell block

```bash
# Run from repo root
pytest app/tests/ -v --tb=short
ruff check app/ && pyright app/
cp .github/pull_request_template.md pr-descriptions/my-feature.md
# → EDIT the file now, then:
python3 docs-depo/plans/kanban-board-files/sync_pr.py TASK_ID pr-descriptions/my-feature.md
sqlite3 app/database/cheddar.db "
  UPDATE kanban_tasks
  SET column_id = (SELECT id FROM kanban_columns WHERE name = 'review'),
      github_pr_url = 'https://github.com/mchdeore/csa-CRAFT/pull/N',
      github_pr_number = N,
      updated_at = datetime('now')
  WHERE id = TASK_ID;
"
sqlite3 app/database/cheddar.db ".headers on" ".mode column" < docs-depo/plans/kanban-board-files/queries_v2.sql
```

Replace `TASK_ID` and `N` with actual values.