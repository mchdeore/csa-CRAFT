# Finalize PR Workflow

End-to-end process for shipping a PR in csa-CRAFT. Run this checklist before asking for review.

---

## 1. Run the full test suite

```bash
# From repo root. One command runs everything.
cd /Users/cheddar/Documents/CODE/csa-cheddar
pytest app/tests/ -v --tb=short
```

Three test files run:
- `test_architecture.py` — folder structure, imports, tool canonicalization
- `test_rules.py` — code quality, function length, complexity, TODOs, secrets
- `test_entry.py` — app server boot and layout

**On failure**: Read the assertion message. Each test is self-documenting — the error tells you which file, which line, and what rule was violated.

## 2. Handle test failures

| Common failure | What to do |
|----------------|------------|
| `Missing return annotation` | Add `-> None` or proper return type to public function |
| `Functions too long` | Split into smaller helpers, each under 250 lines |
| `Functions too complex` | Flatten nested conditionals, extract early-return blocks |
| `Imports not listed in requirements.txt` | Add the missing package to `app/requirements.txt` |
| `Missing logging` | Add `log_function_call` decorator to public functions |
| `print()` found | Replace with `logging.info(...)` |
| `TODO without owner` | Change to `# TODO(username)` or `# TODO(#issue)` |
| `Bare except:` | Catch a specific exception type: `except ValueError:` |
| `Circular or broken imports` | Fix the import path — test shows the exact error |
| `Cross-feature internal import` | Import from the feature's public API instead of internals |
| `Root file not whitelisted` | Move the .py file into a feature folder or add to whitelist |
| `Feature folder missing required files` | Create the missing `__init__.py`, `templates.py`, etc. |

## 3. Lint and type-check

```bash
ruff check app/
pyright app/
```

Fix all errors before proceeding. Ruff errors are usually formatting; pyright errors are type mismatches.

## 4. Build the PR description

Copy `.github/pull_request_template.md` to a working file:

```bash
cp .github/pull_request_template.md pr-descriptions/your-feature-name.md
```

Fill every section completely. See `docs-depo/plans/kanban-board-files/example-pr-description.md` for an example.

## 5. Open the PR on GitHub

Push your branch, open the PR, paste the filled template as the description.

## 6. Update the kanban board

```bash
# Sync the structured PR fields into the database
python3 docs-depo/plans/kanban-board-files/sync_pr.py <kanban_task_id> pr-descriptions/your-feature-name.md
```

Then move the task to `review`:

```bash
sqlite3 app/database/cheddar.db "UPDATE kanban_tasks SET column_id = (SELECT id FROM kanban_columns WHERE name = 'review'), updated_at = datetime('now') WHERE id = <task_id>;"
```

Also populate `github_pr_url` and `github_pr_number` if not already set:

```bash
sqlite3 app/database/cheddar.db "UPDATE kanban_tasks SET github_pr_url = 'https://github.com/mchdeore/csa-CRAFT/pull/NNN', github_pr_number = NNN WHERE id = <task_id>;"
```

## 7. Verify the board is current

```bash
sqlite3 app/database/cheddar.db ".headers on" ".mode column" < docs-depo/plans/kanban-board-files/queries_v2.sql
```

Confirm your task appears in `review` column with all structured fields populated and `pr_description_hash` is non-empty.

## 8. Request review

Tag a reviewer on the PR. The PR template gives them everything they need — summary, scope, behavior changes, test commands, validation criteria, known gaps.

## 9. After merge

Move task to `done`:

```bash
sqlite3 app/database/cheddar.db "UPDATE kanban_tasks SET column_id = (SELECT id FROM kanban_columns WHERE name = 'done'), completed_at = datetime('now'), updated_at = datetime('now') WHERE id = <task_id>;"
```

## Quick reference: one shell block

```bash
# === Finalize PR: run from repo root ===

# 1. Test
pytest app/tests/ -v --tb=short

# 2. Lint + type
ruff check app/ && pyright app/

# 3. Build PR desc
cp .github/pull_request_template.md pr-descriptions/my-feature.md
# → edit pr-descriptions/my-feature.md now

# 4. Sync to kanban
python3 docs-depo/plans/kanban-board-files/sync_pr.py TASK_ID pr-descriptions/my-feature.md

# 5. Move to review + set PR link
sqlite3 app/database/cheddar.db "
  UPDATE kanban_tasks
  SET column_id = (SELECT id FROM kanban_columns WHERE name = 'review'),
      github_pr_url = 'https://github.com/mchdeore/csa-CRAFT/pull/PR_NUM',
      github_pr_number = PR_NUM,
      updated_at = datetime('now')
  WHERE id = TASK_ID;
"

# 6. Verify
sqlite3 app/database/cheddar.db ".headers on" ".mode column" < docs-depo/plans/kanban-board-files/queries_v2.sql
```