# Codebase & Development Rules

The checklist every change must respect. The tests in this directory enforce the rules; this file states them in prose.

Tests that back these rules:

- `test_architecture.py` — folder-structure, root-whitelist, cross-feature import, tool-canonicalization, doctest coverage, pytest file coverage.
- `test_rules.py` — code-quality rules (function length, cyclomatic complexity, TODO attribution, requirements hygiene, type annotations).
- `test_entry.py` — entry-point boot sanity.

---

## 1. Feature & Structure Rules

### Required files per feature folder

Every feature at the project root (`auth/`, `chat/`, `storage/`, `connectors/`, `demo/`) must contain:

| File | Purpose |
|------|---------|
| `__init__.py` | Public API surface — only re-export what other features are allowed to import |
| `templates.py` | Dash HTML components and UI layout |
| `callbacks.py` | Dash callback functions (user interactions → state changes) |
| `routes.py` | Flask route handlers (HTTP endpoints) |
| `tests/` | Unit and integration tests for this feature |

Enforced by `test_architecture.py` → `test_feature_folders_have_required_files`.

### Root-level restrictions

Only `app.py` and `__init__.py` allowed at project root. All other code lives in feature folders or `app/core/`.

Enforced by `test_architecture.py` → `test_root_files_whitelisted`.

### Tool subpackages

Every folder under `tools/` must define `__all__` in its `__init__.py`. This declares what the subpackage exports.

Enforced by `test_architecture.py` → `test_tool_subpackages_have_all`.

### Canonical tool paths

Tool paths declared in `tools/routes.py` must match real modules on disk. If you add a tool, update the path map.

Enforced by `test_architecture.py` → `test_canonical_tool_paths`.

### Auto-discovery

New features are auto-discovered by the architecture test — no config changes, no hardcoded lists. Just create the folder with the required files and `tests/`.

---

## 2. Route Rules

### Naming convention

Routes follow `/{feature}/{action}[/<param>]`. Examples:

```
POST /auth/login
POST /auth/logout
POST /chat/send
POST /chat/upload
GET  /storage/list/<username>
POST /storage/create
GET  /storage/load/<username>/<workspace_id>
POST /storage/save-messages/<username>/<workspace_id>
```

### Registration pattern

Each feature defines a `register_routes(app)` function in its `routes.py`. The central `app/core/routes.py` calls each feature's `register_routes` at startup.

### Route-gated flow

Callbacks must call routes via `app.server.test_client()` — never call providers or stores directly.

```
Browser → Dash Callback → HTTP POST (via test_client) → before_request middleware
    → Route handler → Provider/Store → after_request middleware → Response
```

Every route gets audit logging, auth check, and permission check from `before_request` middleware — no per-route code needed.

### Internal routes

Routes prefixed with `/chat/internal/`, `/tools/execute/`, `/tools/list`, `/debug/` bypass the perimeter gate. They are called by other route handlers (not the browser). Protected by `X-Internal-Secret` header for defense in depth.

### Public routes

Routes prefixed with `/auth/`, `/_*`, `/static/` bypass auth check entirely — needed for login page and static assets.

---

## 3. Logging Rules

### Function-level logging

Every public function in a non-trivial module must call `log_function_call(module, function)` at the top. This creates a traceable trail of function calls tied to the request's trace ID.

Enforced by `test_rules.py` → `test_logging_coverage`.

Exempt files: `__init__.py`, `templates.py`, `protocols.py`, `config.py`, `dash_app.py`, `logging.py`, `_shared.py`, `connection.py`, `runner.py`, `registry.py`, `entry.py`, `app.py`, `auth/callbacks.py`, `app/routes.py`.

### Module-level loggers

Use `logging.getLogger(__name__)` for per-module loggers. Standard Python `logging` — no custom framework needed.

### Audit logs

Audit logs use key=value format for grep-friendliness:

```
AUDIT method=POST path=/chat/send user=alice status=200 elapsed=0.234s
```

Structured enough for machines, readable enough for humans. No JSON parsing needed.

### Structured JSON logs

Written to `storage/database/log/cheddar-YYYY-MM-DD.jsonl`. One file per day, auto-rotated at midnight, 90-day retention. Every line is a valid JSON object.

### Server logs

Written to `app/logs/server.log`. Survives terminal clears and restarts.

### No print()

Never use `print()` in production code — use `logging`.

Enforced by `test_rules.py` → `test_no_print_statements`.

---

## 4. Authority & Permission Rules

### Role model

Three escalated roles: levels represent privilege, higher inherits lower.

| Role | Level | Access |
|------|-------|--------|
| `base_user` | 1 | Chat, own workspace data, public datasets, all tools |
| `power_user` | 2 | base_user + upload files, manage workspaces, all datasets |
| `admin` | 3 | Everything — all users, all workspaces, all datasets |

Defined in `app/core/logging.py` → `_ROLE_LEVEL` dict. Add new tiers by appending to this dict.

### Route gate

`_ROUTE_RULES` list in `app/core/logging.py` maps route patterns to minimum role:

```python
{"pattern": "/chat/send", "min_role": "base_user"},
{"pattern": "/chat/upload", "min_role": "power_user"},
{"pattern": "/storage/create", "min_role": "power_user"},
{"pattern": "/admin/*", "min_role": "admin"},
```

Patterns use `fnmatch`. First match wins. No match = forbidden. Optional `required_flag` field gates experimental features.

### Data scoping

`SqliteDataStore` scopes data by role automatically. Same tool call, different results per user:

- `base_user`: own workspace data + public datasets
- `admin`: all workspaces, all datasets, all users

Denied access returns generic "not available" — never leaks what exists.

### Flags

Flags (`required_flag` field) are for experimental features only — never for permissions. When an experiment ships, remove the flag from the route rule and user configs, not the gate.

---

## 5. Protocol & Abstraction Rules

### Protocol pattern

Every swappable component has a `Protocol` in `app/core/protocols.py`. Current protocols: `AuthProvider`, `WorkspaceStore`, `ChatProvider`, `Tool`, `ChatResponse`.

No ABCs, no inheritance — just `Protocol` from `typing`. The protocol IS the contract.

### Wiring

Concrete implementations are wired once in `app/core/services.py`:

```python
auth: AuthProvider = InMemoryAuth()
store: WorkspaceStore = SqliteStore()
chat_provider: ChatProvider = DeepSeekChat(...)
```

Callbacks import from `services.py` — never from concrete implementation modules.

### Cross-feature imports

Only two forms allowed:

```python
# Allowed:
import auth                           # top-level import
from auth.templates import login_form  # UI composition

# Blocked:
from auth.provider import InMemoryAuth  # internal implementation
from chat.provider import DeepSeekChat  # internal implementation
from storage.store import SqliteStore   # internal implementation
```

Enforced by `test_architecture.py` → `test_no_cross_feature_internal_imports`.

### Shared infrastructure

`app/core/` is shared infrastructure — it never imports from features. Features import from `app.core`, never the reverse.

---

## 6. Data Safety Rules

### Secrets

No hardcoded secrets. Everything comes from `.env` via `os.environ` or `os.getenv`. Secrets never touch source code.

Enforced by `test_rules.py` → `test_no_hardcoded_secrets`.

### Database

- SQLite with WAL mode: `PRAGMA journal_mode=WAL` — readers don't block writers
- Foreign keys always ON: `PRAGMA foreign_keys=ON`
- `ON DELETE CASCADE` for parent-child (workspace → messages)
- Connection factory in `storage/database/connection.py`
- No ORM — raw sqlite3 from stdlib
- No connection pooling needed (single process)

### Migrations

Numbered `.sql` files in `storage/database/migrations/`. Applied idempotently by `storage/database/runner.py`:

```
001_initial.sql
002_unified_data.sql
003_audit_log.sql
004_stream_buffer.sql
```

Adding a migration: create `005_description.sql`, write SQL, done. Runner reads `schema_version` table and applies only pending migrations.

### Queries

Parameterized queries only — never string interpolation:

```python
# Correct:
conn.execute("SELECT * FROM users WHERE username = ?", (username,))

# Wrong — never do this:
conn.execute(f"SELECT * FROM users WHERE username = '{username}'")
```

### Audit trail

Audit log table (`003_audit_log.sql`) for tracking sensitive operations. Audit logs written via structured JSON logging alongside.

---

## 7. Testing Rules — Three-Tier System

### Tier 1: Doctests — Mid-Development Quick Checks

**Purpose:** Catch obvious breaks while you code. Fast first pass. Run with `pytest --doctest-modules`.

**Requirement:** Every public function must have a doctest in its docstring. The doctest shows the function being called with example inputs and expected output.

**Example:**
```python
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Compute great-circle distance in kilometers.

    >>> calculate_distance(45.42, -75.69, 43.65, -79.38)
    351.23
    >>> calculate_distance(0, 0, 0, 0)
    0.0
    """
    ...
```

**What they are not:** Doctests are NOT a substitute for the full test suite. They verify the function does what the docstring says — a single call with known inputs. They don't test edge cases, error paths, stateful operations, or multi-step workflows.

**Enforcement:** Architecture test checks every public function has `>>>` in its docstring.

### Tier 2: Pytest Feature Tests — Integration Checks

**Purpose:** Verify the system works end-to-end. Run before you consider work complete.

**Requirement:** Every stateful module (database operations, route handlers, API calls, file I/O) must have a matching test file in `tests/`. Test file named `test_{source_file_name}.py`, matching the source file it covers.

**What they cover:**
- Database CRUD with fixtures and temp databases
- Route handlers with Flask test client
- External API calls with mocks
- File I/O with temp files
- Multi-step workflows (login → create → read → verify)

**Organization:**
```python
# tests/test_store.py
class TestCreate:
    def test_create_returns_required_fields(self, store): ...
    def test_create_then_load_returns_same_data(self, store): ...

class TestLoad:
    def test_load_nonexistent_returns_none(self, store): ...
```

Shared fixtures live in `tests/conftest.py`. Tests serve as documentation — they describe expected behavior.

**Enforcement:** Architecture test checks stateful modules have matching test files.

### Tier 3: Quality Pipeline — Final Gate

**Purpose:** Automated reviewer. Catches things humans miss. Runs on every commit.

**What runs:**

| Tool | What it checks | When |
|------|---------------|------|
| Ruff (14 rule sets) | Line length, import order, naming, complexity, type annotations, modern syntax, security patterns, no-print | Pre-commit + CI |
| Bandit | Common security vulnerabilities | Pre-commit + CI |
| detect-secrets | Accidentally committed API keys, passwords, tokens | Pre-commit |
| Pyright (strict) | Static type errors | Pre-commit |
| pip-audit | Known CVEs in dependencies | CI |
| Pre-commit hooks | Trailing whitespace, merge conflicts, debug statements, large files | Every commit |

**Configuration:** All in `pyproject.toml` and `.pre-commit-config.yaml`. Zero app code impact.

**Workflow:** Run `pre-commit run --all-files` before pushing. Address all flags before merging — either fix the issue or add a documented exception in the config file.

### Skip markers

During development, skip incomplete tests with a clear reason:

```python
@pytest.mark.skip(reason="WIP: implementing data scoping for power_user")
def test_power_user_cannot_see_admin_data(self, store):
    ...
```

Skipped tests appear in pytest output as `s SKIPPED` — always visible, never hidden. Unskip before merging.

---

## 8. Code Style & Conventions

### Formatting
- Line length: 100 (Ruff enforced)
- Import ordering: stdlib → third-party → local (Ruff isort enforced)
- Modern Python: f-strings, `pathlib`, type hints (Ruff pyupgrade enforced)
- `snake_case` for files, functions, variables
- `PascalCase` for classes

### Function design
- Aim for ~30 lines per function where practical
- Hard max: 250 lines (test enforced)
- Cyclomatic complexity: max 15 (Ruff + test enforced)
- Plain-English comment above every function — what it does and why
- Separate logical blocks with blank line + short comment describing the block
- No clever one-liners — explicit over implicit
- Named constants over magic numbers

### Naming
- Variable and function names: full words, never abbreviations
- Examples: `price_history` not `pH`, `connection_pool` not `cp`, `user_profile` not `up`

### Type annotations
- Public functions must have return type annotations (test enforced)
- Use `from __future__ import annotations` for forward references

### Error handling
- Error messages explain what went wrong AND what to do about it
- No bare `except:` — always catch a specific exception type (test enforced)

### Comments & TODOs
- TODOs must reference owner or issue: `TODO(name)` or `TODO(#issue)` (test enforced)
- `__init__.py` files should be re-exports only — no logic

### Imports
- Every third-party import must be listed in `app/requirements.txt` (test enforced)
- No circular imports — enforced by subprocess import check in architecture test

---

## 9. Dependency Stack Context

### Dash & Flask
- Single-process threaded Flask server under Dash
- Callbacks are Python functions compiled to React — no JavaScript needed
- Dash singleton in `app/core/dash_app.py`
- In-process route calls via `app.server.test_client()` — no HTTP overhead
- Root layout in `app/templates.py`, feature templates compose into it

### PydanticAI & Azure OpenAI
- Agent definition in `chat/agent.py`
- `ChatDeps` dataclass holds user context + all tool references
- Tools registered as closures with logging and rich content collection
- System prompt built in `app/core/config.py` with user context injection
- Agent runs synchronously inside asyncio event loop
- Azure OpenAI client via `AsyncAzureOpenAI`
- Configuration: `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_DEPLOYMENT`

### SQLite (Raw, No ORM)
- Connection factory: `storage/database/connection.py`
- WAL mode for concurrent reads during writes
- Single process — no connection pooling needed
- Migration runner: `storage/database/runner.py`
- Schema tables: users, workspaces, messages, unified_data, schema_version, audit_log, stream_buffer

### Plotly Charts
- Chart tools in `tools/charts/`
- Each tool returns `(tool_msg: dict, rich_content: dict)`
- Rich content rendered in `chat/templates.py` via `dcc.Graph`
- Shared utilities in `tools/charts/_shared.py`

### Flask-Login
- Session-based authentication
- User object accessed via `request.environ["current_user"]`
- `InMemoryAuth` provider in `auth/provider.py`
- Auth managed by `before_request` middleware, not `@login_required` decorators

### External APIs
- Open-Meteo: weather forecast and historical data (free, no key)
- Guardian API: news article search (requires API key)
- Azure Cohere: semantic rerank for search results (requires API key)
- All configuration in `app/core/config.py` via environment variables

---

## 10. Development Workflow

### Before starting
1. Sync with master: `git pull origin master`
2. Create feature branch: `git checkout -b feat/your-feature-name`
3. Read the relevant README.md in the feature folder you're modifying

### During development
1. Write function + doctest in docstring
2. Run `pytest path/to/file.py --doctest-modules` for quick feedback
3. Write pytest tests for stateful code in `tests/`
4. Use `@pytest.mark.skip(reason="...")` for incomplete tests

### Before committing
1. Run `pre-commit run --all-files` to check quality pipeline
2. Run full `pytest` to verify all tests pass
3. Address all Ruff/Bandit/detect-secrets/Pyright flags (fix or document exception)
4. Unskip any tests that were skipped during development

### Before merging
1. Verify all tiers pass: doctests, pytest tests, quality pipeline
2. Verify no skipped tests remain without documented permanent reason
3. Verify architecture tests pass (structure, imports, test coverage)

---

## 11. Anti-Patterns — Explicitly Forbidden

| Don't | Do instead |
|-------|-----------|
| Import implementations from callbacks | Import from `app/core.services` |
| Put business logic in callbacks | Callbacks are wiring only — logic lives in routes/providers |
| Skip routes to call providers directly | Routes give audit, auth, and permissions for free |
| Use `print()` | Use `logging` |
| Use bare `except:` | Catch a specific exception type |
| Hardcode secrets | Use `.env` + `os.environ` |
| String interpolation in SQL | Parameterized queries with `?` placeholders |
| Add `.py` files at project root | Put code in feature folders or `app/core/` |
| Import from another feature's internals | Use top-level import or `.templates` |
| Leave unattributed TODOs | Use `TODO(name)` or `TODO(#issue)` |
| Use abbreviations in names | Full words: `price_history` not `pH` |
| Use flags for permissions | Flags are for experimental features only |
| Add dependencies without requirements.txt | Every third-party import must be listed |