# 14 — Dead code sweep

**Status:** planned · last plan in the refactor; depends on plans 01–13 landing

## Why

After plans 01–13 ship, several symbols and files have zero callers:

- `WORKSPACES_DIR` (`app/core/config.py`) — never imported.
- `log_route` decorator (`app/core/logging.py`) — backward-compat shim, no callers.
- `_is_public_route`, `_has_permission` (`app/core/logging.py`) — labelled "kept for backward compatibility", no callers.
- `_ROLE_LEVEL` duplicate in `storage/store.py` — plan 06 removes.
- Duplicate `werkzeug.security` imports in `storage/store.py:60,68`.
- `tools/registry.py` — may be unused; confirm with grep.
- `/debug/pipeline` log-path string literal in `app/core/routes.py:95` — plan 10 replaces with resolved path from `settings`.

Clean them up in one commit so the diff reads as "sweep" not "touched everywhere by accident".

## Scope

**In**
- Delete the symbols above after confirming zero references.
- Delete `tools/registry.py` if grep confirms no imports.
- Collapse duplicate imports.
- `vulture` dry-run (optional, dev-only) to spot anything else.

**Out**
- Rewriting any logic — delete-only.
- Removing legitimate test fixtures that happen to be unused by prod code.

## Workflow

**Pre-check**
- Plans 01–13 shipped.
- `make check` green.
- `grep -rn "<symbol>"` for each symbol in the delete list returns only the definition site.

**Do**
1. For each symbol in the "Why" list, grep the tree; delete only if the sole hit is the definition (or a `__all__` re-export we also delete).
2. `tools/registry.py` — `grep -rn "tools\.registry\|from tools import registry\|import tools\.registry"`; delete only on zero hits.
3. Collapse `storage/store.py` duplicate imports.
4. (Optional) `vulture .` and triage noise. Treat 90%+ confidence as actionable; skip the rest.

**Verify**
- `pytest -q` green.
- `pyright` strict green.
- `grep -rn "WORKSPACES_DIR\|log_route\|_is_public_route\|_has_permission\|tools\.registry"` returns nothing (or only historical git).

**Commit**
`chore: sweep dead code (post-refactor)`

**Rollback**
`git revert HEAD`

## Verification checklist

- [ ] Each symbol listed in "Why" is deleted or justified kept.
- [ ] `pyright` strict green.
- [ ] `pytest` green.
- [ ] No duplicate imports in `storage/store.py`.

## Out of scope

- Refactoring the files these deletions touch beyond the delete itself.
- `vulture` acceptance beyond ~90% confidence (noise-prone).

---

## Reasoning / justification extracts

**User instructions:**
- "super in depth clean up all previous demo garbage on your pass".

**Why last, not first:**
Dead-code sweep after the refactor avoids "deleted now, resurrected by plan 03" churn. Running it last also means pyright strict in plan 09 gives an independent signal: anything strict pyright flags as unused is a candidate to delete, not debate.

**Why not use `--check-only` tooling earlier:**
Ruff's `F401` catches unused imports; `vulture` catches unused symbols. Both run under `make check` from plan 09 onwards; this plan's sweep is the manual pass over symbols labelled "backward compat" — the kind of thing linters flag but refuse to delete automatically.
