# Architecture Restructure — Research Decisions

## 1. Dash App Entry Pattern

**Decision:** Keep global `app` from `dash_app.py`, configure in `app/entry.py`. No factory function.

**Why:** Dash apps are singletons by nature. The `app` instance must be the same object that callbacks register on. A factory pattern would break callback registration or require passing `app` to every callback file. The current pattern (`dash_app.py` creates the instance, everything else imports it) is the standard Dash convention.

**Thin root `app.py`:** Does `from app.entry import *`. Keeps `python app.py` working as the entry point. No `python -m app.entry` needed.

## 2. Callback Registration

**Decision:** Import callbacks directly in `app/entry.py` via `import auth.callbacks`, `import chat.callbacks`, `import storage.callbacks`. Do NOT put callbacks in `__init__.py`.

**Why:** Dash callbacks register via decorator side effects on `@app.callback`. They must be imported after `app` exists. Putting them in `__init__.py` causes circular imports because `services.py` → `auth.provider` → `auth/__init__.py` → `auth.callbacks` → `services`. By importing callbacks only in `app/entry.py` (after services are wired), we break the cycle.

## 3. Auth: Class-Based Provider

**Decision:** Keep `InMemoryAuth` as a class, not module-level functions. `services.py` wires `auth = InMemoryAuth()` as a singleton.

**Why:** Already protocol-compatible (`AuthProvider` Protocol). Callbacks use `auth.try_login()` via the singleton. This pattern scales to DB-backed auth later — just swap the class.

**User model:** Stays in `auth/provider.py` with the class. No separate `models.py` needed for a single dataclass.

**Cross-feature import:** `auth/callbacks.py` imports `build_main` from `storage.templates`. This is allowed because it's a template-level import (UI composition). Blocked by architecture test if it imported `storage.store` directly.

## 4. Chat Provider + Tool Architecture

**Decision:** Keep `DeepSeekChat` as a single class with tool-calling loop. No split into `LLMClient` + `ChatProvider`.

**Why:** The current class already handles both API connection and response orchestration. Splitting would add indirection without benefit at this scale. The tool-calling loop (up to 5 iterations) is self-contained. When function calling support is needed later, the `_handle_tool_calls` method is the single extension point.

**AzureOpenAI client:** Lazily initialized via `_get_client()`. Singleton in `services.py` as `chat_provider = DeepSeekChat(tool_registry)`. This is clean enough — no need to extract client initialization to services.py.

**Template organization:** All 8 chat UI functions + 6 style constants in `chat/templates.py` (~200 lines). This is OK because they're all UI markup for one feature. The 30-line function limit test is for logic, not declarative HTML-in-Python.

## 5. SQLite Storage

**Decision:** Raw `sqlite3` with WAL mode, no ORM.

**Why:** The app has 2 tables, simple CRUD. SQLAlchemy adds dependency overhead and boilerplate without benefit at this scale. Raw sqlite3 is stdlib, zero dependencies.

### Production Schema

```sql
-- WAL mode for concurrent reads during writes
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- Migration tracking
CREATE TABLE schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
);

-- Users (ready for DB-backed auth)
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- Workspaces
CREATE TABLE workspaces (
    id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    last_accessed TEXT NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);
CREATE INDEX idx_workspaces_username ON workspaces(username);

-- Messages with structured content support
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workspace_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    content_json TEXT,  -- JSON for charts, news cards, etc.
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE
);
CREATE INDEX idx_messages_workspace ON messages(workspace_id, id);
```

### Key Design Decisions

- **WAL mode:** Dash/Flask uses threaded server. WAL lets reads happen during writes without blocking.
- **content_json:** Chart dicts and news card data serialize to JSON. On load, deserialize back to dict. Simple text stays in `content` column.
- **`with self._conn:`:** Transaction context manager. Auto-commit on success, auto-rollback on exception. Prevents half-written data.
- **`ON DELETE CASCADE`:** Delete workspace → messages go with it. No orphaned messages.
- **`schema_version` table:** Hook for future migrations without Alembic or manual scripts.
- **Thread safety:** `check_same_thread=False` plus WAL mode. One connection object, shared across threads — safe for Dash's single-worker Flask dev server.

## 6. Architecture Enforcement Tests

**Decision:** Hand-rolled AST checks, auto-discovering feature folders.

**Why:** `import-linter` adds a dependency for what's essentially 3 test functions. Auto-discovering feature folders means new folders (like `tools/`) get validated automatically without updating a hardcoded list.

### Rules Enforced

1. **Root file whitelist:** Only `app.py`, `config.py`, `dash_app.py`, `protocols.py`, `services.py`, `routes.py` allowed at root.
2. **Feature folder required files:** Every feature folder must have `__init__.py`, `templates.py`, `callbacks.py`, `routes.py`, `tests/__init__.py`. Exception: `app/` doesn't need `callbacks.py` (it imports callbacks from other features).
3. **Cross-feature imports:** Feature internals cannot be imported directly. Allowed: `import feature` (via `__init__.py`), `from feature.templates import ...` (UI composition), shared modules (`protocols`, `services`, `config`, `dash_app`).

### Test Organization

- `tests/test_architecture.py` — structure enforcement
- `tests/test_rules.py` — function length limit (30 lines), requirements.txt completeness
- Feature `tests/` folders — unit tests for that feature (future)

## 7. Flask Routes (Internal Tools)

**Decision:** Each feature has `routes.py` with `register_routes(flask_app)`. Central `routes.py` calls all of them. Currently stubs.

**Why:** Routes are co-located with the feature they serve. When tool endpoints are added later (code sandbox, chart generation), they go in the relevant feature's `routes.py`. No restructuring needed.

**Pattern:**
```python
# chat/routes.py
from flask import Flask


def register_routes(flask_app: Flask) -> None:
    # Future: POST /chat/tools/run-code, POST /chat/tools/chart, etc.
    pass
```

## 8. What We Did NOT Do

- **No ORM:** Raw sqlite3 is sufficient for 2 tables and simple CRUD.
- **No factory pattern:** Dash apps are singletons by design.
- **No import-linter:** Hand-rolled AST checks are simpler and dependency-free.
- **No Alembic:** `schema_version` table is a lightweight migration hook for future use.
- **No separate models.py files:** Single dataclass per feature doesn't justify a separate file.
- **No `type: ignore` comments:** All type issues fixed at the source.
- **No backwards-compatibility shims:** Old paths deleted cleanly.

## 9. Future Extension Points

| Feature | Where to add |
|---------|-------------|
| Code sandbox tool | `chat/routes.py` → `POST /chat/tools/run-code` |
| Plotly chart generation | `chat/routes.py` → `POST /chat/tools/chart` |
| DB-backed auth | `auth/provider.py` → new class implementing `AuthProvider` |
| New feature folder | Create `{name}/` with `__init__.py`, `templates.py`, `callbacks.py`, `routes.py`, `tests/` — architecture test auto-discovers it |

## 10. Database Migrations

**Decision:** Numbered SQL files in `storage/database/migrations/`, applied by a runner that checks `schema_version`.

**Why:**
- No dependency on Alembic or other migration frameworks
- Each migration is a plain SQL file — easy to read, review, and hand-edit
- The runner is idempotent: checks `schema_version` table, only applies pending migrations
- Adding a new table or index is: `touch storage/database/migrations/002_add_feature_x.sql`, write SQL, done
- Works with SQLite-specific features (WAL, foreign keys, indexes) that ORM abstractions often hide

**Pattern:**
```sql
-- 002: Add feature X
ALTER TABLE workspaces ADD COLUMN tags TEXT DEFAULT '[]';
CREATE INDEX IF NOT EXISTS idx_workspaces_tags ON workspaces(tags);
```

The runner extracts the version number from the filename prefix (e.g. `002` from `002_add_feature_x.sql`), compares with `schema_version` table, skips already-applied migrations, applies new ones in order.