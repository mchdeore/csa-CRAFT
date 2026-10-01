# 06 — Permissions and roles: one declarative JSON file

**Status:** planned · depends on `01-config-stdlib-dotenv.md`

## Why

Role levels are duplicated between `app/core/logging.py:507-511` and `storage/store.py:230-234`. Route rules + prefix lists are hardcoded in `app/core/logging.py:515-541`. Public-path checks for `/` and `/favicon.ico` are magic branches inside `_check_permission`. All four live in Python — opaque to readers and awkward to extend.

Pitch §1 shows the Route-gated RBAC container as a plain, declarative concept (`base(1) < power(2) < admin(3)`, route × role matrix). Move role levels, route rules, and public/internal prefix lists into one JSON file loaded at startup.

## Scope

**In**
- `app/core/permissions.json` as the single source for role levels, prefixes, and rules.
- `app/core/permissions.py` as the loader + helpers.
- `app/core/logging.py` keeps only structured request logging (sheds ~150 lines).
- `storage/store.py` imports role helpers from `app.core.permissions` (deletes its duplicate).
- Stale rules dropped (`/tools/read_document`, `/tools/search_documents` — those paths don't exist).

**Out**
- Per-tool RBAC (pitch "per-tool RBAC column staged"; stays staged).
- Row-level data scope beyond `QueryTool.set_user` (not touched here).

## File shape

```json
// app/core/permissions.json
{
  "role_levels": {"base_user": 1, "power_user": 2, "admin": 3},
  "public_route_prefixes": ["/auth/", "/_", "/static/"],
  "public_exact_paths": ["/", "/favicon.ico"],
  "internal_route_prefixes": ["/chat/internal/", "/tools/execute/", "/tools/list"],
  "route_rules": [
    {"pattern": "/chat/send", "min_role": "base_user"},
    {"pattern": "/chat/upload", "min_role": "power_user"},
    {"pattern": "/storage/list/*", "min_role": "base_user"},
    {"pattern": "/storage/create", "min_role": "power_user"},
    {"pattern": "/storage/load/*", "min_role": "base_user"},
    {"pattern": "/storage/save-messages/*", "min_role": "base_user"},
    {"pattern": "/admin/*", "min_role": "admin"}
  ]
}
```

## Loader API

```python
# app/core/permissions.py (sketch)
from __future__ import annotations
import json, fnmatch
from functools import lru_cache
from app.core.config import settings

@lru_cache(maxsize=1)
def _data() -> dict:
    return json.loads(settings.PERMISSIONS_FILE.read_text())

def role_level(role: str) -> int:
    return _data()["role_levels"].get(role, 0)

def is_public(path: str) -> bool:
    d = _data()
    if path in d["public_exact_paths"]:
        return True
    return any(path.startswith(p) for p in d["public_route_prefixes"])

def is_internal(path: str) -> bool:
    return any(path.startswith(p) for p in _data()["internal_route_prefixes"])

def find_matching_rule(path: str) -> dict | None:
    for rule in _data()["route_rules"]:
        if fnmatch.fnmatchcase(path, rule["pattern"]):
            return rule
    return None
```

## Files touched

- **New**
  - `app/core/permissions.json`.
  - `app/core/permissions.py`.
  - `app/tests/test_permissions.py` (basic loader + helper tests).
- **Edit**
  - `app/core/logging.py` — delete `_ROLE_LEVEL`, `_ROUTE_RULES`, `_PUBLIC_ROUTE_PREFIXES`, `_INTERNAL_ROUTE_PREFIXES`, `_find_matching_rule`, and the magic `path == "/" or path == "/favicon.ico"` branch inside `_check_permission`. Replace references with `app.core.permissions` imports.
  - `storage/store.py` — delete the duplicate `_ROLE_LEVEL` dict (lines ~230-239) and the local `_role_level`; import `role_level` from `app.core.permissions`.
- **Delete**
  - Stale rules `/tools/read_document` and `/tools/search_documents` (paths don't exist; the real route is `/tools/execute/<tool_name>` which falls under `internal_route_prefixes`).

## Workflow

**Pre-check**
- Plan 01 shipped so `settings.PERMISSIONS_FILE` is defined.

**Do**
1. Create `app/core/permissions.json`.
2. Write `app/core/permissions.py` with the helpers above.
3. Rip `_ROLE_LEVEL`, `_ROUTE_RULES`, `_PUBLIC_ROUTE_PREFIXES`, `_INTERNAL_ROUTE_PREFIXES` and `_find_matching_rule` out of `app/core/logging.py`. Replace the magic `/` branch with `permissions.is_public(path)`.
4. Delete the duplicate `_ROLE_LEVEL` and `_role_level` in `storage/store.py`; import from `app.core.permissions`.
5. Add `app/tests/test_permissions.py`: JSON loads; `role_level("admin") == 3`; `is_public("/")` True; `is_public("/foo")` False; `find_matching_rule("/admin/users")` returns the admin rule; `find_matching_rule("/nope")` returns `None`.

**Verify**
- `grep -rn "_ROLE_LEVEL\|_ROUTE_RULES\|_PUBLIC_ROUTE_PREFIXES\|_INTERNAL_ROUTE_PREFIXES\|_find_matching_rule" --include='*.py'` returns only the import sites and the loader internals.
- `pytest app/tests/test_permissions.py -q` passes.
- `pytest auth/tests/test_permissions.py -q` route × role matrix still passes.
- Manual: `curl /` returns the login page (public exact path); `curl /debug/routes` with no session returns 403 (internal prefix); logged-in base_user hitting `/admin/foo` returns 403.

**Commit**
`refactor(permissions): declarative JSON, de-dupe role levels`

**Rollback**
`git restore -SW app/core/ storage/store.py app/tests/test_permissions.py`

## Verification checklist

- [ ] One `_ROLE_LEVEL` definition in the tree (inside the JSON loader module).
- [ ] `permissions.json` loads cleanly on import.
- [ ] `_check_permission` no longer contains hardcoded path strings.
- [ ] Public `/` + `/favicon.ico` work.
- [ ] `/admin/*` rejects base_user.
- [ ] Route × role matrix test green.

## Out of scope

- Per-tool RBAC gating (pitch staged).
- Loading permissions over the network (always a local file).
- Hot-reload of `permissions.json` without restart.

---

## Reasoning / justification extracts

**User instructions:**
- "proper routes".
- "no hardcoding anything".

**Pitch commitments honoured:**
- "Route-gated RBAC ⟨I⟩ AuthProvider ... `base (1) read · chat`, `power (2) + upload · tools`, `admin (3) + /admin/*`" (§1 Containers, item 2).
- "Role check · AgentAction audit · HITL interrupt stay fixed" (§3 Use Cases). Keeping the role / route data separate from the gate code lets the gate stay thin and the data auditable in one place.
- "pytest + pyright + ruff + bandit + pip-audit + detect-secrets — Route × role matrix, protocol contracts, audit-envelope present" (§4 Design Decisions, Invariants row). The JSON file makes the matrix a data artefact tests can walk, not a buried literal.

**Why `fnmatch` for patterns:**
Stdlib, no deps. Pattern syntax (`/admin/*`) already matches the current `_find_matching_rule` behaviour. No regex overhead.

**Why delete `/tools/read_document` / `/tools/search_documents` rules:**
Those routes don't exist in `tools/routes.py` — the only tool endpoint is `/tools/execute/<tool_name>`, which is already under `internal_route_prefixes`. The rules are leftover demo noise.
