# Route-Gated Architecture — Design Decisions

## Problem

Callbacks call providers, stores, and tools directly:

```
chat/callbacks.py → chat_provider.get_response()     # direct
auth/callbacks.py → auth.try_login()                  # direct
storage/callbacks.py → store.create()                 # direct
```

This has three problems:

1. **No audit trail.** A government app with 500+ users needs to know who did what and when. Direct calls leave no trace.
2. **No centralized auth.** Every callback checks (or forgets to check) auth on its own. Adding a new feature means remembering to add auth checks.
3. **No permission model.** Cannot restrict tool access per user role. An analyst and an admin can both call any tool.

## Solution: Route-Gated Architecture

Every piece of business logic must be triggered through a Flask route. Callbacks call routes; routes call providers/tools/stores. One audit middleware logs everything. One auth middleware checks permissions.

```
Request → Audit log → Auth check → Permission check → Route handler → Response
              ↓                ↓                  ↓
          logged always     401 if no user    403 if no permission
```

## Audit Logging

A single `before_request`/`after_request` listener in `app/core/logging.py` captures every request:

- Timestamp
- HTTP method and path
- User ID (from flask-login session)
- Status code
- Response time (ms)

No per-route logging code needed. Nothing to forget.

**Format:** Structured key=value for grep/awk parsing:
```
AUDIT method=POST path=/chat/send user=alice status=200 elapsed=0.234s
```

**Why key=value not JSON:** grep `user=alice` works without jq. Structured enough for parsing, human-readable for tailing logs.

## Permission Model

Role-based access control via the `users` table. Each user has a `role` column. Roles map to route patterns.

```sql
-- Added to existing users table via migration
ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'viewer';
```

**Built-in roles:**

| Role | Allowed routes |
|------|---------------|
| `admin` | `*` (everything) |
| `analyst` | `/chat/*`, `/tools/read_document`, `/tools/search_documents`, `/storage/*` |
| `viewer` | `/chat/*` (read only — no tool execution, no workspace creation) |

**Why roles not per-user permissions:** 500 users means 500 permission rows to manage. Roles mean 3 rows to manage. Add a role, update once. The auth middleware has 3 `if` branches, not a DB lookup per request.

**Permission check in middleware:**

```python
ROLE_ROUTES = {
    "viewer": ["/chat/send"],
    "analyst": ["/chat/*", "/tools/read_document", "/tools/search_documents", "/storage/*"],
    "admin": ["*"],
}


def _check_permission(role: str, path: str) -> bool:
    patterns = ROLE_ROUTES.get(role, [])
    return any(fnmatch.fnmatch(path, p) for p in patterns)
```

## Route Design

Each feature's `routes.py` is no longer a stub. It exposes the feature's operations as Flask endpoints:

### auth/routes.py
```
POST /auth/login     → auth.try_login()
POST /auth/logout    → auth.do_logout()
```

### chat/routes.py
```
POST /chat/send      → chat_provider.get_response()
POST /chat/upload    → excel_tool.register_upload()
```

### storage/routes.py
```
GET  /storage/list/<username>       → store.list()
POST /storage/create                → store.create()
GET  /storage/load/<ws_id>          → store.load()
POST /storage/save-messages/<ws_id> → store.save_messages()
```

### tools routes (via chat/routes.py)
Tool execution happens inside the chat route — the LLM calls tools during `chat_provider.get_response()`. No separate tool routes needed.

## Callback Rewrites

Each callback that currently calls a provider/store directly must call the route instead.

**Before:**
```python
# auth/callbacks.py
if auth.try_login(username, password):
    ...
```

**After:**
```python
# auth/callbacks.py
import requests

resp = requests.post(f"http://localhost:{port}/auth/login", json={...})
if resp.json()["success"]:
    ...
```

**Problem:** Dash callbacks run in the same process but don't share the Flask request context. Calling `http://localhost` from inside the server is an extra HTTP hop — negligible latency for an internal call.

**Alternative for dev simplicity:** Use Flask's `test_client()` in-process. No HTTP hop, same route handlers fire, audit middleware still runs.

```python
from flask import current_app

client = current_app.test_client()
resp = client.post("/auth/login", json={...})
```

## Authentication via Session

Callbacks currently check a client-side Dash `dcc.Store` session dict. This is NOT secure — the client can modify it. With route-gated architecture, auth moves server-side:

1. User logs in → `POST /auth/login` sets flask-login session cookie
2. Every route hits `before_request` → checks `current_user` from cookie
3. Callback calls route → route checks auth → 401 if not authenticated

The `dcc.Store` session becomes a cache for UI state (workspace_id, messages), not a security boundary.

**What changes in callbacks:** They pass the Flask session cookie, not a username string. Or better: they don't pass identity at all — the route reads `current_user` from the cookie.

## Architecture Enforcement

The existing architecture test requires `routes.py` per feature. No new rule needed.

A new rule: "Callbacks may not import provider/store modules directly." They import only `requests` or use `current_app.test_client()`. Enforced by the existing `test_no_cross_feature_internal_imports` test — callbacks importing from `auth.provider`, `chat.provider`, or `storage.store` is already blocked. The test only allows imports from `auth`, `auth.templates`, etc. — which means callbacks can't reach the internals.

## What we did NOT do

- **No OAuth/SSO yet.** InMemoryAuth + flask-login is sufficient for now. Routes don't care how auth works — the middleware just checks `current_user`.
- **No fine-grained per-user permissions.** Roles handle this. Per-user overrides can be added later via a `user_permissions` table without changing the middleware.
- **No API versioning.** Routes are simple `/feature/action` for now. Versioned routes (`/v1/chat/send`) add overhead without benefit at this scale.
- **No request validation schema.** Flask routes accept JSON and pass to providers. Validation happens in providers (they already handle missing fields).
- **No async.** Flask is synchronous. Internal `test_client()` calls are synchronous. Keeping it simple.

## Migration Impact

- `auth/provider.py` — no change (already has `try_login`, `do_logout`)
- `chat/provider.py` — no change (already has `get_response`)
- `storage/store.py` — no change (already has CRUD)
- `auth/callbacks.py` — rewrite to call `/auth/login` route
- `chat/callbacks.py` — rewrite to call `/chat/send` route
- `storage/callbacks.py` — rewrite to call `/storage/*` routes
- `auth/routes.py` — implement login/logout handlers
- `chat/routes.py` — implement send/upload handlers
- `storage/routes.py` — implement CRUD handlers
- `app/core/logging.py` — new: audit middleware + permission middleware
- `app/entry.py` — wire audit + permission middleware
- `app/tests/test_routes.py` — new: test audit logging, test permission checks
- `storage/database/migrations/` — new migration: add `role` column to users