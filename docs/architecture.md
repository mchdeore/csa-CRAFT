# Cheddar — Architecture & Blind Decisions

## What This Document Covers

Every "blind decision" baked into the repo — choices about structure, dependencies, interfaces, routing, testing, and logging. Not what the code does, but **why** it does it that way. Read this before you change anything structural.

---

## 1. Component-Based Architecture

### The Rule

Every feature lives in its own top-level folder. Nothing bleeds.

```
cheddar/
├── app/           ← Application shell (entry, config, services, logging)
│   └── core/      ← Shared infrastructure (never imports from features)
├── auth/          ← Authentication (login, logout, user sessions)
├── chat/          ← Chat messages, LLM provider, agent tools
├── connectors/    ← Data source connectors (local files, future: S3, SharePoint)
├── storage/       ← Workspace persistence, database, migrations
└── tools/         ← Tool implementations (weather, news, excel, documents)
```

### Required Files per Feature

Every feature folder must contain:

| File | Purpose |
|------|---------|
| `__init__.py` | Public API surface — what other features are allowed to import |
| `templates.py` | Dash HTML components and UI layout |
| `callbacks.py` | Dash callback functions (user interactions → state changes) |
| `routes.py` | Flask route handlers (HTTP endpoints) |
| `tests/` | Unit tests for this feature |

Enforced by `app/tests/test_architecture.py` — auto-discovers folders by looking for `__init__.py`. Add a new folder and the test picks it up without updating any list.

### Why This Structure

**Isolation.** Each feature is a sealed box. You can audit `auth/` without reading `chat/`. You can replace `storage/` without touching `chat/`. The architecture test prevents you from creating spider webs.

**Government-ready.** A 500-user agency app needs clear boundaries. When an auditor asks "where does chat store messages?" you point at `storage/store.py`. One file. One answer.

**Scales linearly.** New feature? `mkdir feature_name/`, add the 4 files + test dir. Done. No config changes, no import wiring, no DI container updates. The architecture test validates it automatically.

### What We Chose NOT to Do

- **No microservices.** Single process, single deploy. This is a Dash app serving a small team. Microservices at this scale add deployment complexity with zero benefit.
- **No monorepo tooling.** Standard Python packages. `pip install -r requirements.txt` and you're done.
- **No feature flags.** Every folder is a feature. If you don't want it, delete the folder.

---

## 2. The Route-Gated Architecture

### The Problem

Without routes, callbacks call providers directly:

```python
# Bad: no audit trail, no central auth, no permission check
chat/callbacks.py → chat_provider.get_response()
auth/callbacks.py → auth.try_login()
storage/callbacks.py → store.create()
```

Three problems:
1. **No audit log.** Who called what? When? No trace.
2. **No central auth.** Every callback must remember to check login — or forget.
3. **No permissions.** Any authenticated user can call anything.

### The Solution

Every piece of business logic goes through a Flask route. Callbacks call routes. Routes call providers/stores. Middleware handles the rest.

```
Browser → Dash Callback → HTTP POST /chat/send
                              │
                              ▼
                     ┌─────────────────┐
                     │  before_request  │ ← Audit timer starts
                     ├─────────────────┤
                     │  Auth check      │ ← 401 if no user
                     ├─────────────────┤
                     │  Permission check│ ← 403 if wrong role
                     ├─────────────────┤
                     │  Route handler   │ ← Actual business logic
                     ├─────────────────┤
                     │  after_request   │ ← Audit log emitted
                     └─────────────────┘
```

### Audit Logging

One `before_request`/`after_request` pair in `app/core/logging.py` captures **every** request. No per-route code. Nothing to forget.

Output format:

```
AUDIT method=POST path=/chat/send user=alice status=200 elapsed=0.234s
```

**Why key=value, not JSON:** `grep user=alice` works without `jq`. Structured enough for machines, readable enough for humans. This is the Unix way.

### Permission Model

Role-based, checked in middleware. Three roles cover all access patterns:

| Role | Access |
|------|--------|
| `viewer` | `/chat/send` only — read conversations |
| `analyst` | `/chat/*`, `/tools/read_document`, `/tools/search_documents`, `/storage/*` |
| `admin` | `*` — everything |

**Why roles, not per-user permissions:** 500 users × N permissions = management nightmare. 3 roles = 3 `if` branches in the middleware. Add a role once, update never.

### Route Design

Each feature exposes its operations as HTTP endpoints:

```
POST /auth/login              → auth.try_login()
POST /auth/logout             → auth.do_logout()
POST /chat/send               → chat_provider.get_response()
POST /chat/upload             → excel_tool.register_upload()
GET  /storage/list/<user>     → store.list()
POST /storage/create          → store.create()
GET  /storage/load/<ws_id>    → store.load()
POST /storage/save-messages   → store.save_messages()
```

Tools (weather, news, excel) run inside the LLM's tool-calling loop during `/chat/send`. They don't need separate routes — the LLM decides when to call them.

### Why Routes Matter for Scaling

**Service managers later.** When this app grows to multiple services, the route layer becomes the API gateway. Swap `routes.py` to proxy to a different backend. Callbacks never knew the difference — they always talked to routes.

**Logging scales for free.** Every new route gets audit logging. Add a route, get logs. No code change.

**Testing scales.** Route tests verify the contract. Provider tests verify the implementation. Separate concerns. Separate test suites.

---

## 3. Protocols & Interfaces

### The Pattern

Every swappable component has a Protocol (structural interface). No ABCs, no inheritance — just `Protocol` from `typing`.

```python
# app/core/protocols.py


class AuthProvider(Protocol):
    def init_app(self, flask_app: Flask) -> object: ...
    def try_login(self, username: str, password: str) -> bool: ...
    def do_logout(self) -> None: ...


class WorkspaceStore(Protocol):
    def list(self, username: str) -> list[dict]: ...
    def load(self, username: str, workspace_id: str) -> dict | None: ...
    def save(self, username: str, workspace: dict) -> None: ...
    def create(self, username: str, name: str) -> dict: ...

    ...


class ChatProvider(Protocol):
    def get_response(self, messages: list[dict]) -> ChatResponse: ...


class Tool(Protocol):
    def definition(self) -> dict[str, Any]: ...
    def execute(self, args: dict[str, Any]) -> tuple[dict, dict | None]: ...
```

### Wiring

`app/core/services.py` wires protocols to concrete implementations at startup:

```python
auth: AuthProvider = InMemoryAuth()
store: WorkspaceStore = SqliteStore()
chat_provider: ChatProvider = DeepSeekChat(...)
```

Callbacks never import `InMemoryAuth` or `SqliteStore`. They import `auth` and `store` from `services.py`. The protocol is the contract. The implementation is invisible.

### Why This Matters

**Swap without rewrite.** Need DB-backed auth? Write `DatabaseAuth`, implement `AuthProvider`, change one line in `services.py`. Every callback, every route, every template — untouched.

**Test with fakes.** Every test creates a fake that satisfies the protocol. No mocking framework needed. No dependency injection container. Just Python.

**Control coupling.** The protocol IS the interface. Nothing else can depend on implementation details. The architecture test enforces this — cross-feature imports of internal modules are blocked.

---

## 4. Dependencies & Framework Choices

### Stack

| Layer | Choice | Why |
|-------|--------|-----|
| **Web framework** | Flask (via Dash) | Flask is the HTTP layer. Dash wraps it for reactive UI. |
| **UI framework** | Plotly Dash | React components in Python. No JavaScript needed. |
| **LLM framework** | PydanticAI | Type-safe agent with tool calling. Cleaner than raw OpenAI SDK. |
| **LLM provider** | Azure OpenAI | Government cloud. Runs in Azure tenant. |
| **Database** | SQLite (raw, no ORM) | 2 tables. Zero dependencies. WAL mode for concurrent reads during writes. |
| **Migrations** | Numbered `.sql` files + custom runner | Alembic is overkill for 2 tables. SQL files are readable and hand-editable. |
| **Linting** | Ruff | Fast. One tool replaces flake8, isort, pyupgrade. |
| **Type checking** | Pyright | Strict mode. Catches bugs at dev time. |
| **Testing** | Pytest | Standard. Fast. |
| **Env management** | python-dotenv | `.env` files for 12-factor config. |

### What We Did NOT Use

| Skipped | Why |
|---------|-----|
| **SQLAlchemy / ORM** | 2 tables. Raw sqlite3 is stdlib. ORM adds dependency overhead without benefit at this scale. |
| **Alembic** | Custom runner is 40 lines. Discovers numbered `.sql` files. Idempotent. |
| **import-linter** | Hand-rolled AST checks. Auto-discovers feature folders. No dependency. |
| **FastAPI** | Dash already provides the reactive UI layer. Flask underneath is the web server. |
| **Redis / Celery** | No async tasks needed. LLM calls are synchronous. |
| **Docker Compose** (dev) | Single process. `python app.py` is the entire dev setup. |

### Blind Decision: Python Only

Every line of code is Python. No JavaScript, no TypeScript, no CSS frameworks.

**Why:**
- One language to learn, debug, and deploy.
- Dash compiles Python callbacks to React. The JavaScript is generated, not written.
- Government teams often have Python-only developers. This stack keeps the team unified.

---

## 5. Database Design

### SQLite with WAL Mode

```python
# storage/database/connection.py
conn.execute("PRAGMA journal_mode=WAL")  # Writers don't block readers
conn.execute("PRAGMA foreign_keys=ON")  # Cascade deletes
```

**Why WAL:** Dash runs a threaded Flask server. Multiple threads can read while one writes. Standard journal mode would lock reads during writes. WAL fixes this.

### Schema

```
users        → username, password_hash, role, created_at
workspaces   → id, username, name, created_at, last_accessed
messages     → id, workspace_id, role, content, content_json, created_at
schema_version → version, applied_at   (migration tracking)
```

Key decisions:
- **`content_json` column** — chart dicts and rich objects serialize to JSON. Plain text goes in `content`. Best of both worlds.
- **`ON DELETE CASCADE`** — delete workspace → messages disappear. No orphans.
- **`schema_version` table** — lightweight migration hook. No Alembic needed.

### Migration System

Numbered SQL files in `storage/database/migrations/`. Runner is idempotent:

```python
# Runner reads schema_version, applies only pending migrations
for sql_file in sorted(migration_files):
    if version <= current:  # Already applied → skip
        continue
    conn.executescript(sql)  # Apply
    conn.execute("INSERT INTO schema_version ...")  # Log
```

Adding a migration: `touch storage/database/migrations/003_add_feature.sql`, write SQL, done.

---

## 6. Testing Strategy

### Three Layers

| Layer | Location | What It Tests |
|-------|----------|---------------|
| **Architecture** | `app/tests/test_architecture.py` | Folder structure rules, import boundaries |
| **Code quality** | `app/tests/test_rules.py` | Function length (≤30 lines), requirements.txt completeness |
| **Feature tests** | `{feature}/tests/` | Unit tests for each feature's logic |

### Architecture Tests (Auto-Discovering)

```python
# Auto-discovers feature folders — no hardcoded list
def _discover_features() -> set[str]:
    # Finds every dir with __init__.py, excluding venv/tests/cache/tools
    ...


class TestArchitecture:
    def test_no_circular_imports(self): ...  # Every module imports cleanly
    def test_root_files_whitelisted(self): ...  # Only app.py at root
    def test_feature_folders_have_required_files(self): ...  # 4 files + tests/
    def test_no_cross_feature_internal_imports(self): ...  # AST import analysis
```

The cross-feature import rule is the most important. It allows:

```python
# ✅ Allowed
import auth                       # Top-level import
from auth.templates import ...    # UI composition
from app.core.protocols import ... # Shared infrastructure

# ❌ Blocked
from auth.provider import ...     # Internal implementation
from chat.provider import ...     # Internal implementation
from storage.store import ...     # Internal implementation
```

### Code Quality Tests

- **Function length:** Any function over 30 lines fails. Forces you to split logic. (30-line limit excludes declarative HTML-in-Python templates.)
- **Import completeness:** Every third-party import must be in `requirements.txt`. Catches "works on my machine" drift.

### Feature Tests

Each feature's `tests/` folder contains tests for its own logic:

```
auth/tests/test_provider.py    ← Unit tests for InMemoryAuth
chat/tests/test_provider.py    ← Unit tests for DeepSeekChat
storage/tests/test_store.py    ← Unit tests for SqliteStore
connectors/tests/              ← Unit tests for data sources
```

### Coverage Threshold

`pyproject.toml` enforces 80% coverage minimum:

```toml
[tool.coverage.report]
fail_under = 80
show_missing = true
```

### Why Test This Way

**Architecture tests catch structure drift.** The most common regressions in a growing codebase are structural: someone imports from `chat.provider` instead of using the route, someone puts business logic in a callback, someone forgets to add `__init__.py`. Architecture tests catch all of this before code review.

**Code quality tests enforce standards.** Function length, import hygiene — things linters miss. Ruff catches syntax, these catch intent.

**Feature tests stay fast.** Each feature's tests only import that feature. No test depends on the full app starting. Fast feedback loop.

---

## 7. Logging Strategy

### Server Logs

`app/core/dash_app.py` sets up file logging at startup:

```python
file_handler = logging.FileHandler(LOGS_PATH / "server.log")
logging.getLogger().addHandler(file_handler)
logging.getLogger().setLevel(logging.DEBUG)
```

All log output goes to `app/logs/server.log`. Survives terminal clears and restarts.

### Audit Logs

`app/core/logging.py` registers Flask middleware that logs every request:

```
AUDIT method=POST path=/chat/send user=alice status=200 elapsed=0.234s
```

**Why structured key=value:** Greppable. Sortable. No JSON parsing needed. `grep "user=alice" server.log | sort` gives you a user's full activity timeline.

### Application Logs

Standard Python logging with named loggers:

```python
logger = logging.getLogger("cheddar.audit")  # Audit events
logger = logging.getLogger(__name__)  # Per-module logs
```

No custom logging framework. No structured logging library. `logging` from stdlib is sufficient and well-understood.

---

## 8. Configuration

### Environment Variables

`app/core/config.py` reads from environment via `os.environ`. All secrets come from `.env` files, never hardcoded.

```python
AZURE_OPENAI_ENDPOINT  # Azure OpenAI endpoint URL
AZURE_OPENAI_API_KEY  # Azure OpenAI API key
AZURE_OPENAI_DEPLOYMENT  # Model deployment name
GUARDIAN_API_KEY  # The Guardian news API
AZURE_COHERE_ENDPOINT  # Azure Cohere rerank endpoint
AZURE_COHERE_API_KEY  # Azure Cohere API key
OPEN_METEO_GEOCODING_URL  # Open-Meteo geocoding API
OPEN_METEO_FORECAST_URL  # Open-Meteo forecast API
OPEN_METEO_ARCHIVE_URL  # Open-Meteo historical API
```

**Why environment variables:** 12-factor app. Secrets never touch source code. Deploy to any environment by changing `.env`, not code.

### Static Configuration

Non-secret configuration lives in config constants:

```python
CONNECTORS_ROOT = Path("...")  # Local file connector root directory
GUARDIAN_SEARCH_URL = "..."  # Guardian API endpoint (not secret)
```

---

## 9. How Everything Connects

```
                    ┌──────────────────────────────┐
                    │         Browser               │
                    └──────────┬───────────────────┘
                               │ Dash React UI
                    ┌──────────▼───────────────────┐
                    │     app/templates.py          │
                    │     (Dash layout)              │
                    └──────────┬───────────────────┘
                               │ User clicks, types
                    ┌──────────▼───────────────────┐
                    │   {feature}/callbacks.py       │
                    │   (Dash callbacks)             │
                    └──────────┬───────────────────┘
                               │ HTTP POST (via test_client)
                    ┌──────────▼───────────────────┐
                    │   {feature}/routes.py          │
                    │   (Flask route handlers)       │
                    └──────────┬───────────────────┘
                               │
               ┌───────────────┼───────────────┐
               ▼               ▼               ▼
          auth.provider   chat.provider   storage.store
          (InMemoryAuth)  (DeepSeekChat)  (SqliteStore)
               │               │               │
               ▼               ▼               ▼
          flask-login     PydanticAI      sqlite3 (WAL)
                          + tools/*
```

**The flow:**
1. User clicks/talks → Dash callback fires
2. Callback calls `/chat/send` via Flask test client (in-process, no HTTP overhead)
3. `before_request` runs: audit timer starts, auth check, permission check
4. Route handler calls `chat_provider.get_response()`
5. Provider runs PydanticAI agent with tool-calling loop
6. Agent calls tools (weather, news, excel, documents)
7. Response flows back through `after_request`: audit log emitted
8. Dash updates UI with response text + rich contents (charts, cards)

---

## 10. Future Scaling Paths

| Need | Where to Extend |
|------|-----------------|
| **Code sandbox** | `chat/routes.py` → `POST /chat/tools/run-code` |
| **Chart generation** | `tools/interactive_charts.py` — bar, pie, scatter tools (see `docs/interactive-charts.md`) |
| **DB-backed auth** | `auth/provider.py` → new class implementing `AuthProvider` protocol |
| **New LLM backend** | `chat/provider.py` → new class implementing `ChatProvider` protocol |
| **New data source** | `connectors/` → new class implementing `DataSource` protocol |
| **New feature** | `mkdir {name}/` with 4 files + tests. Auto-discovered by architecture tests. |
| **Multiple services** | Route layer becomes API gateway. Proxy routes to different backends. |
| **Role expansion** | `app/core/logging.py` → add entries to `_ROLE_ROUTES` dict. |
| **Audit queries** | `grep` on structured logs. No DB needed for audit. |

---

## 11. Key Principles (Summary)

1. **Everything is a component.** Feature folders are sealed boxes. No cross-contamination.
2. **Everything goes through a route.** Callbacks call routes, not providers. Routes give us audit logging, auth, and permissions for free.
3. **Everything has a protocol.** Concrete implementations are swappable. Protocols are the contracts.
4. **Everything is Python.** One language. Dash generates the JavaScript. No frontend/backend split.
5. **Everything is tested.** Architecture tests enforce structure. Code quality tests enforce standards. Feature tests verify logic.
6. **Everything is logged.** Structured `key=value` audit logs. Plain Python logging. Readable by `grep`, parseable by scripts.