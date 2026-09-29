# Permissions

## Design Philosophy

**Roles handle everything gate-related.** Escalated levels (`base_user` < `power_user` < `admin`). Higher roles inherit all lower-role access. Every route, tool, and data query checks the user's role — one axis, simple.

**Flags are for experiments only.** Use them to gate half-built features behind a flag like `beta_charts_v2`. Give the flag to one tester. No flag-check code in production paths. When the feature ships, remove the flag — not the gate.

**Data scoping is automatic.** `base_user` sees their own workspace data + public datasets. `admin` sees everything — all workspaces, all datasets, all users. The store enforces this. The tool and model never know about other users' data existing.

**Tiers come later.** When you need `super_admin` or `auditor` or `readonly_admin`, add a new role to `_ROLE_LEVEL`. The abstraction handles it — no rewrite needed.

---

## Role Levels (Escalated)

```python
_ROLE_LEVEL = {
    "base_user": 1,
    "power_user": 2,
    "admin": 3,
}
```

Higher role level inherits all lower-role access. Route check: `_ROLE_LEVEL[user.role] >= _ROLE_LEVEL[min_role]`.

### Role Catalog

| Role | Level | Access |
|------|-------|--------|
| `base_user` | 1 | Chat, own workspace data, public datasets, all tools |
| `power_user` | 2 | base_user + upload files, manage workspaces, all datasets |
| `admin` | 3 | Everything — all users, all workspaces, all datasets, user management |

---

## Flags — Experimental Features Only

Flags are NOT used for permissions. They gate half-built or beta features.

Example route rule with experimental flag:

```python
# Experimental route — requires both role AND flag
"/chat/beta_charts": {"min_role": "base_user", "required_flag": "beta_charts_v2"},
```

When `beta_charts_v2` ships, remove the flag from the route rule and user configs. Route stays gated by `min_role`.

---

## Two-Layer Permission Model

```
Browser → Route Gate (before_request) → Route Handler → Agent → Store Gate → Data
                  │                                                      │
            check role (+flag if experiment)                      scope by role
            401/403 if blocked                               base_user: own+public
                                                            admin: everything
```

### Layer 1 — Route Gate (perimeter)

Every user-facing route checked in `before_request`. Role escalation. Optional experimental flag. Fast deny at the door.

### Layer 2 — Store Gate (internal)

`SqliteDataStore.query()` scopes data by role. Same tool call, different results per user.

### Internal Routes

`/chat/internal/*`, `/tools/execute/*`, `/tools/list`, `/debug/*` bypass the perimeter gate. They are called by other route handlers (not the browser). They keep the parent route's `trace_id` so audit stays intact.

Optionally protected by a shared secret header (`X-Internal-Secret`) for defense in depth — even with full network access, an attacker can't hit internal routes without knowing the secret.

---

## Route Rules

```python
_ROUTE_RULES = {
    "/chat/send":               {"min_role": "base_user"},
    "/chat/upload":             {"min_role": "power_user"},
    "/storage/list":            {"min_role": "base_user"},
    "/storage/create":          {"min_role": "power_user"},
    "/storage/load":            {"min_role": "base_user"},
    "/storage/save-messages":   {"min_role": "base_user"},
    "/tools/read_document":     {"min_role": "base_user"},
    "/tools/search_documents":  {"min_role": "base_user"},
    "/admin/*":                 {"min_role": "admin"},
}

_INTERNAL_ROUTE_PREFIXES = (
    "/chat/internal/",
    "/tools/execute/",
    "/tools/list",
    "/debug/",
)

_PUBLIC_ROUTE_PREFIXES = ("/auth/", "/_", "/static/")
```

---

## Users Table

Migration 002 adds role, division, region, and flags columns to the existing `users` table:

```sql
ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'base_user';
ALTER TABLE users ADD COLUMN division TEXT NOT NULL DEFAULT '';
ALTER TABLE users ADD COLUMN region TEXT NOT NULL DEFAULT '';
ALTER TABLE users ADD COLUMN flags TEXT NOT NULL DEFAULT '[]';
```

The `InMemoryAuth` provider seeds users into the DB. `SqliteDataStore` reads role directly from `users` — one query, no separate table.

---

## Data Scoping

`SqliteDataStore.query()` resolves keys against three namespaces, all scoped by role:

1. **Workspace user data** — scoped to `(username, workspace_id)` pair. Only the owning user sees their data unless admin.
2. **User profile metadata** — scoped to the requesting user. Admin can read any user's profile with `profile:<otheruser>` key.
3. **Global datasets** — gated by `min_role` column. `base_user` datasets visible to all. `power_user`+ datasets only visible at that level.

base_user queries `workspace_id=123`: returns ONLY workspace 123's data + public datasets.
admin queries: returns all workspaces, all datasets, all users.

---

## QueryTool

Single tool for the model: `query_data(key, action, value?)`.

- `action="query"` — needs base_user role. Returns scoped data.
- `action="store"` — needs power_user role. Writes to user_data.
- `action="list"` — needs base_user role. Returns accessible keys.
- `action="delete"` — needs power_user role. Removes from user_data.

Returns generic "not available" when denied — never leaks what exists.

---

## ChatDeps

```python
@dataclass
class ChatDeps:
    username: str = ""
    workspace_id: str = ""
    user_role: str = "base_user"
    user_flags: list[str] = field(default_factory=list)
    # ... existing tool fields ...
    query_tool: QueryTool | None = None
    rich_contents: list[dict] = field(default_factory=list)
```