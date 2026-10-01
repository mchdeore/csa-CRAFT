# 05 — DB-backed users + seeder script

**Status:** planned · depends on `01-config-stdlib-dotenv.md`

## Why

`auth/provider.py` currently defines `DEFAULT_USERS = {"demo": {"password": "demo", "role": "admin"}}` — a hardcoded identity baked into the module. `storage/store._seed_users` reads it on startup. That is demo state in production code. The user asked: "can you just make a seeder for it?" The right place for users is the SQLite `users` table; a seeder script writes rows into it.

## Scope

**In**
- Delete `DEFAULT_USERS` from `auth/provider.py` and `auth/__init__.py`.
- Delete `_seed_users` from `storage/store.py`.
- Add `SqliteStore.list_users()` and `SqliteStore.upsert_user(...)`.
- `InMemoryAuth.load_from_store(store)` hydrates from the DB on `init_app`.
- `scripts/seed.py` — argparse CLI that upserts users from `settings.SEED_USERS_FILE`.
- `scripts/users.example.json` — field-shape template, no real passwords.
- `scripts/users.demo.json` — gitignored; real demo users; built from the example.
- `.gitignore` additions.

**Out**
- Entra ID / MSAL swap (pitch end-state).
- Password rotation CLI.
- UI for user management.

## Files touched

- **New**
  - `scripts/__init__.py` (empty, so the module is import-safe).
  - `scripts/seed.py` — the CLI.
  - `scripts/users.example.json` — template.
- **Rewrite**
  - `auth/provider.py` — remove `DEFAULT_USERS`; `__init__(users=None)` keeps the test kwarg; `init_app` calls `load_from_store(store)`.
  - `auth/__init__.py` — stop re-exporting `DEFAULT_USERS`.
- **Edit**
  - `storage/store.py` — delete `_seed_users` and the `DEFAULT_USERS` import; add `list_users()`, `upsert_user(...)`; drop duplicate `werkzeug.security` imports.
  - `app/core/services.py` — `InMemoryAuth()` still takes no args; the factory calls `load_from_store(store)` during `init_app`.
  - `.gitignore` — add `scripts/users.demo.json`, `*.db-shm`, `*.db-wal` (and confirm `.env` is already present).
- **Test rewrites**
  - `auth/tests/test_provider.py` — delete `test_init_with_no_users_uses_defaults` and `TestDefaultUsers`; add `test_init_from_store_hydrates_users` and `test_init_with_no_users_rejects_login`.

## File shapes

```json
// scripts/users.example.json
[
  {
    "username": "admin",
    "password": "CHANGE_ME",
    "role": "admin",
    "division": "",
    "region": "",
    "flags": []
  }
]
```

```python
# scripts/seed.py (sketch)
from __future__ import annotations
import argparse, json, sys
from app.core.config import settings
from storage.store import SqliteStore

def main() -> int:
    p = argparse.ArgumentParser("csa-craft-seed")
    p.add_argument("--reset", action="store_true", help="wipe users table before seeding")
    p.add_argument("--dump", action="store_true", help="print current users (no password hashes) and exit")
    p.add_argument("--file", default=str(settings.SEED_USERS_FILE), help="JSON file (default: SEED_USERS_FILE)")
    args = p.parse_args()
    store = SqliteStore()
    if args.dump:
        for u in store.list_users():
            print(json.dumps({k: v for k, v in u.items() if k != "password_hash"}))
        return 0
    if args.reset:
        store.wipe_users()
    rows = json.loads(open(args.file).read())
    n = 0
    for row in rows:
        store.upsert_user(**row)
        n += 1
    print(f"{n} user(s) seeded from {args.file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Workflow

**Pre-check**
- Plan 01 shipped.
- SQLite migrations run (startup already does this).

**Do**
1. Add `list_users()`, `upsert_user(...)`, `wipe_users()` to `SqliteStore`.
2. Delete `_seed_users` and the `DEFAULT_USERS` import from `storage/store.py`.
3. Rewrite `auth/provider.py` to remove `DEFAULT_USERS` and add `load_from_store(store)`.
4. Update `app/core/services.py` so `init_app` hydrates from the store.
5. Write `scripts/__init__.py` (empty), `scripts/seed.py`, `scripts/users.example.json`.
6. Update `.gitignore`.
7. Rewrite `auth/tests/test_provider.py` tests per Scope.

**Verify**
- `python scripts/seed.py --dump` on an empty DB prints nothing (exits 0).
- `python scripts/seed.py` with the example file (`CHANGE_ME` password) seeds the admin row; second run is idempotent (same count, no duplicates).
- `python scripts/seed.py --dump` after seeding prints the row(s) without `password_hash`.
- `python app.py` without `scripts/users.demo.json` and without having seeded → login endpoint rejects every attempt with "no users configured".
- `python app.py` after seeding → `admin` / `CHANGE_ME` logs in.
- `pytest auth/tests -q` passes.

**Commit**
`refactor(auth): DB-backed users, seeder script, delete DEFAULT_USERS`

**Rollback**
`git restore -SW auth/ storage/ scripts/ .gitignore`

## Verification checklist

- [ ] `DEFAULT_USERS` grep returns zero matches.
- [ ] `_seed_users` is deleted.
- [ ] `scripts/seed.py --dump` works on empty and seeded DB.
- [ ] Seeder is idempotent on re-run.
- [ ] `scripts/users.demo.json` is gitignored.
- [ ] Login flow works end-to-end with a seeded user.

## Out of scope

- Entra ID / MSAL identity.
- User self-registration.
- Password reset flow.

---

## Reasoning / justification extracts

**User instructions:**
- "can you just make a seeder for it?"
- "no hardcoding anything though clean that up".

**Pitch alignment:**
- Pitch §4 Identity row: today "Local AuthProvider stub"; end-state "Entra ID + MSAL". The seeder populates the local stub's backing store. The same `⟨I⟩ AuthProvider` protocol accepts an Entra implementation later with no change to routes or sessions.
- Pitch §6 RBAC + data scope: `_ROUTE_RULES` + `_ROLE_LEVEL` + `SqliteDataStore` + `QueryTool.set_user`. The DB-backed `users` table is the backing for both auth and the data-store scope.

**Why SQLite is the single source of truth:**
Avoids drift between the auth provider's in-memory dict and the data store's `users` table. One table, one truth; `InMemoryAuth` becomes a cache populated at startup.
