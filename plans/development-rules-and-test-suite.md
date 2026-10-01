# Development Rules & Test Suite — Final Plan

## Overview

Four deliverables:

1. **`app/tests/CODEBASE_RULES.md`** — populated with every rule, convention, and anti-pattern. Source of truth.

2. **Doctest layer** — low-level, mid-development quick checks embedded in function docstrings. Every public function gets one. Runs fast. Catches obvious breaks during development.

3. **Pytest feature tests** — mid-level tests for stateful code (database, routes, API calls). One test file per stateful source module. Uses fixtures and mocks.

4. **Industry-standard quality pipeline** (already exists, untouched) — Ruff linting, Bandit security scan, detect-secrets, Pyright type checking, pre-commit hooks. This is the "final check" gate — catches things humans miss, runs on every commit, acts like an automated reviewer with many suggestions.

---

## The Two-Tier Testing Philosophy

### Tier 1: Doctests — Mid-Development Quick Checks

**What they are:** Runnable examples embedded in function docstrings. Write them while you code. Run them with `pytest --doctest-modules`. Fail fast when you break something.

**When to use:** Every public function. Pure functions, transforms, calculations, validators. The "does this function do what I think it does?" check.

**When NOT to use:** Stateful operations (database writes, API calls, file I/O). Routes needing Flask context. These go to Tier 2.

**Rule in CODEBASE_RULES.md:**
> Every public function must have a doctest in its docstring. This is a development-time check — run it as you write code to catch obvious breaks. Doctests are low-level: they verify the function does what the docstring says. They are NOT a substitute for the full test suite.

**Example:**
```python
def calculate_distance(lat1, lon1, lat2, lon2):
    """Compute great-circle distance in kilometers using Haversine.

    >>> calculate_distance(45.42, -75.69, 43.65, -79.38)
    351.23
    >>> calculate_distance(0, 0, 0, 0)
    0.0
    """
    ...
```

### Tier 2: Pytest Feature Tests — Integration / Stateful Checks

**What they are:** Traditional pytest files in `{feature}/tests/`. Use fixtures for setup/teardown, mocks for external services, Flask test client for routes.

**When to use:** Database operations, route handlers, API calls, file I/O, multi-step workflows. Anything doctests can't cover.

**Rule in CODEBASE_RULES.md:**
> Every stateful module (database, routes, API calls, file I/O) must have a matching test file in `tests/`. These are integration-level tests — they verify the system works end-to-end, not just individual functions. Run them before you consider your work complete.

### Tier 3: Industry-Standard Quality Pipeline — Final Gate

**What it is:** Already exists and is fully configured. Touched by zero code changes in this plan.

| Tool | What it checks | When it runs |
|---|---|---|
| **Ruff** (14 rule sets) | Line length, import order, naming, complexity, type annotations, modern syntax, security patterns, no-print | Pre-commit hook + CI |
| **Bandit** | Common security vulnerabilities in code | Pre-commit hook + CI |
| **detect-secrets** | Accidentally committed API keys, passwords, tokens | Pre-commit hook |
| **Pyright** (strict) | Static type errors | Pre-commit hook |
| **pip-audit** | Known CVEs in dependencies | CI |
| **Pre-commit hooks** | Trailing whitespace, merge conflicts, debug statements, large files | Every `git commit` |
| **pytest-cov** | Coverage reporting (informational only — no fail-under gate) | CI |

**Rule in CODEBASE_RULES.md:**
> The quality pipeline is your automated reviewer. It runs on every commit via pre-commit hooks, and on every push via CI. It flags things you might miss — security issues, type errors, style violations, leaked secrets. You don't have to agree with every flag, but you must address them before merging (either fix, or add a documented exception in pyproject.toml).

**How they live in the codebase — zero app code bloat:**
- All configuration lives in `pyproject.toml` and `.pre-commit-config.yaml` — not in application code
- `.secrets.baseline` is a data file, not code
- These tools never import into the app — they run externally, scan the codebase, report results
- Adding a new linter rule: one line in `pyproject.toml`. No app code changes.
- This is why these can be extensive without bloating the app — they're external quality tools, not app dependencies

---

## Part 1 — `CODEBASE_RULES.md`

### Where it lives

`app/tests/CODEBASE_RULES.md` — already exists as a stub. Rules and enforcer live together.

### Sections (11 total)

**1. Feature & Structure Rules**
- Required files per feature folder: `__init__.py`, `templates.py`, `callbacks.py`, `routes.py`, `tests/`
- `__init__.py` is the public API surface — only re-export what other features import
- No `.py` files at project root except `app.py` and `__init__.py`
- Tool subpackages must define `__all__` in their `__init__.py`
- `tools/routes.py` canonical paths must match real modules on disk
- New features auto-discovered by architecture test — no config changes needed
- Feature folders live at project root (`auth/`, `chat/`, `storage/`, `connectors/`, `demo/`)

**2. Route Rules**
- Naming: `/{feature}/{action}[/<param>]`
- Each feature defines `register_routes(app)` in its `routes.py`
- Central wiring: `app/core/routes.py` calls each feature's `register_routes`
- Callbacks call routes via `app.server.test_client()` — never call providers directly
- Every route gets audit + auth + permission from `before_request` middleware
- Internal routes (`/chat/internal/*`, `/tools/execute/*`, `/tools/list`, `/debug/*`) bypass perimeter gate, protected by `X-Internal-Secret` header
- Public routes (`/auth/*`, `/_*`, `/static/*`) bypass auth check

**3. Logging Rules**
- Every public function in a non-trivial module must call `log_function_call(module, function)`
- Use `logging.getLogger(__name__)` for per-module loggers
- Audit logs: key=value format, greppable
- Never `print()` — use `logging`
- Structured JSON logs go to `storage/database/log/cheddar-YYYY-MM-DD.jsonl` (daily rotation, 90-day retention)
- Server logs go to `app/logs/server.log`

**4. Authority & Permission Rules**
- Three escalated roles: `base_user` (1) < `power_user` (2) < `admin` (3)
- Route gate: `_ROUTE_RULES` list in `app/core/logging.py`
- `fnmatch` matching — first match wins, no match = forbidden
- Higher role inherits all lower-role access
- Data scoping: `SqliteDataStore` scopes by role
- Flags are for experimental features only — never for permissions
- Denied access returns generic "not available" — never leaks what exists

**5. Protocol & Abstraction Rules**
- Every swappable component has a `Protocol` in `app/core/protocols.py`
- Concrete implementations wired in `app/core/services.py`
- Callbacks import from `services.py` — never from concrete implementation modules
- Cross-feature imports: only top-level (`import auth`) or `.templates`
- `app/core/` is shared infrastructure — never imports from features

**6. Data Safety Rules**
- No hardcoded secrets — everything from `.env` via `os.environ`
- SQLite WAL mode, foreign keys always ON
- `ON DELETE CASCADE` for parent-child relationships
- Migrations: numbered `.sql` files, idempotent runner
- Parameterized queries only — never string interpolation in SQL
- Audit log table for sensitive operations

**7. Testing Rules — Two-Tier System**

- **Tier 1 — Doctests (development-time checks):**
  - Every public function must have a doctest in its docstring
  - Doctest shows the function being called with example inputs and expected output
  - Run `pytest --doctest-modules` during development to catch breaks immediately
  - Doctests are low-level — they verify the function does what the docstring says
  - They are NOT a substitute for the full test suite — they're a fast first pass

- **Tier 2 — Pytest feature tests (integration checks):**
  - Every stateful module (database, routes, API calls, file I/O) must have a test file in `tests/`
  - Test file named `test_{source_file_name}.py`, matching the source file it covers
  - Uses fixtures for setup/teardown, mocks for external services
  - Tests serve as documentation — they describe expected behavior

- **Tier 3 — Quality pipeline (final gate):**
  - Ruff, Bandit, detect-secrets, Pyright run on every commit via pre-commit hooks
  - These are your automated reviewer — flagging issues you might miss
  - Address flags before merging (fix, or add documented exception)
  - pip-audit checks dependencies for CVEs in CI
  - All configuration in `pyproject.toml` and `.pre-commit-config.yaml` — zero app code bloat

- **Skip markers:**
  - Use `@pytest.mark.skip(reason="...")` during development
  - Skipped tests are visible in pytest output — never hidden
  - Unskip before merging, or document why the skip is permanent

**8. Code Style & Conventions**
- Line length: 100 (Ruff enforced)
- Function length: aim ~30, hard max 250 (test enforced)
- Cyclomatic complexity: max 15 (Ruff + test enforced)
- Plain-English comment above every function — what it does and why
- Variable names: full words, never abbreviations
- No clever one-liners — explicit over implicit
- Logical blocks separated by blank line + short comment
- Named constants over magic numbers
- Public functions must have return type annotation (test enforced)
- Import ordering: stdlib → third-party → local (Ruff enforced)
- `snake_case` files/functions/variables, `PascalCase` classes
- Error messages explain what went wrong AND what to do
- TODOs: `TODO(name)` or `TODO(#issue)` format (test enforced)
- No bare `except:` — catch specific type (test enforced)
- Every third-party import must be in `app/requirements.txt` (test enforced)
- `__init__.py` files should be re-exports only

**9. Dependency Stack Context**
- Dash/Flask: single-process threaded server, callbacks compile to React, `test_client()` for in-process route calls
- PydanticAI: agent in `chat/agent.py`, `ChatDeps` dataclass, tools as closures
- Azure OpenAI: client via `AsyncAzureOpenAI`, config from env vars
- SQLite (raw, no ORM): connection from `storage/database/connection.py`, WAL mode, migration runner in `storage/database/runner.py`
- Plotly charts: tools in `tools/charts/`, each returns `(tool_msg, rich_content)`
- Flask-Login: session auth, user via `request.environ["current_user"]`
- External APIs: Open-Meteo, Guardian API, Azure Cohere — config in `app/core/config.py`

**10. Development Workflow**
- Sync with master before starting: `git pull origin master`
- Write function + doctest in docstring
- Run `pytest path/to/file.py` for quick check during development
- Write pytest tests for stateful code in `tests/`
- Run `pre-commit run --all-files` to check quality pipeline
- Run full `pytest` before considering work complete
- Pre-commit hooks run automatically on `git commit` — don't bypass them

**11. Anti-Patterns (explicitly forbidden)**
- Import implementation from callbacks → use services
- Business logic in callbacks → callbacks are wiring only
- Skip routes to call providers directly
- `print()` instead of logging
- Bare `except:`
- Hardcoded secrets
- String interpolation in SQL
- New `.py` files at project root
- Cross-feature internal imports
- Unattributed TODOs
- Abbreviations in names
- Flags for permissions
- Dependencies not in `app/requirements.txt`

---

## Part 2 — Test Structure

### Current state (after latest pull)

```
app/tests/              ← 4 files (architecture, rules, entry, CODEBASE_RULES.md)
auth/tests/             ← 2 test files (provider, permissions)
chat/tests/             ← 1 test file (provider)
storage/tests/          ← 3 test files (store, data_store, query_tool)
connectors/tests/       ← empty (__init__.py only)
tools/                  ← NO tests at all
demo/                   ← NO tests at all
```

### What changes — minimal additions

Only add pytest test files where doctest can't reach. Pure-function modules get doctests only — zero new files.

```
# STATE modules needing test files (~18 total):

storage/tests/
  test_connection.py          NEW — verify WAL mode, foreign keys
  test_runner.py              NEW — verify migration discovery + idempotency
  test_routes.py              NEW — verify workspace CRUD routes
  (existing files stay: test_store.py, test_data_store.py, test_query_tool.py)

auth/tests/
  test_routes.py              NEW — verify login/logout routes
  (existing files stay: test_provider.py, test_permissions.py)

chat/tests/
  test_agent.py               NEW — verify tool registration, ChatDeps
  test_routes.py              NEW — verify send/upload routes
  (existing file stays: test_provider.py)

connectors/tests/
  test_local_files.py         NEW — verify file source

demo/tests/
  conftest.py                 NEW — shared fixtures
  test_routes.py              NEW — verify demo profile routes

# Tool subpackages — only for API-calling modules:

tools/weather/tests/
  test_forecast.py            NEW — mock API response parsing
  test_historical.py          NEW — mock API response parsing

tools/news/tests/
  test_search.py              NEW — mock API response parsing

tools/documents/tests/
  test_reader.py              NEW — file reading with temp files
  test_search.py              NEW — mock document search

tools/risks/tests/
  test_parser.py              NEW — mock file reading
```

### Pure-function modules — zero new files

These get doctests only (already live in function docstrings):

```
tools/charts/           ← ALL pure functions (bar, pie, scatter, line, etc.)
tools/costing/          ← distance.py (pure math)
tools/engineering/      ← compliance.py (pure rules logic)
tools/documents/excel.py   ← chart building parts (pure)
tools/documents/ingest.py  ← text transform parts (pure)
tools/weather/forecast.py  ← URL builder parts (pure)
storage/database/cadre_mission_params.py  ← data definitions (pure)
```

### Quality pipeline — zero changes

All these stay exactly as they are. Configured in `pyproject.toml` and `.pre-commit-config.yaml`. They run externally, scan the codebase, report results. Zero app code impact.

```
.pre-commit-config.yaml     ← ruff, bandit, detect-secrets, pyright, file hygiene
pyproject.toml              ← ruff rules, bandit rules, pytest config, coverage config
.secrets.baseline           ← known false positives for secret detection
```

---

## Part 3 — How Tests Are Enforced

### Three enforcement tests replace the 80% coverage gate

**1. `test_doctest_coverage`** (new, in `test_architecture.py`)
- Walks all source files with AST
- Checks every public function has `>>>` in its docstring
- Exempts: `__init__.py`, `templates.py`, `protocols.py`, `config.py`
- Reports: "chat/agent.py:42 create_agent() has no doctest"

**2. `test_pytest_coverage_for_stateful`** (new, in `test_architecture.py`)
- Walks all source files, checks imports for `sqlite3`, `flask`, `requests`, `open`, `pathlib.Path.open`
- For each stateful module with public functions, checks `tests/test_{name}.py` exists
- Reports: "storage/database/runner.py is stateful but missing tests/test_runner.py"

**3. Existing tests stay** (`test_architecture.py`, `test_rules.py`, `test_entry.py`)
- All 8 architecture rules + 9 code quality rules continue to run
- No changes to existing enforcement

---

## Part 4 — Implementation Order

### Phase 1: Rules document (no code changes)
1. Populate `CODEBASE_RULES.md` with all 11 sections

### Phase 2: Enable doctest (2 config changes)
2. Add `--doctest-modules` to pyproject.toml pytest addopts
3. Add `tools` and `demo` to pytest testpaths for doctest discovery

### Phase 3: Architecture enforcement (2 new test methods)
4. Add `test_doctest_coverage` to `test_architecture.py`
5. Add `test_pytest_coverage_for_stateful` to `test_architecture.py`
6. Remove `fail_under = 80` from pyproject.toml coverage config

### Phase 4: Backfill doctests (no new files — docstrings only)
7. Charts: `bar.py`, `pie.py`, `scatter.py`, `line.py`, `heatmap.py`, `histogram.py`, `boxplot.py`, `radar.py`, `overlaid_bar.py`, `_shared.py`
8. Costing: `distance.py`
9. Engineering: `compliance.py`
10. Documents: `reader.py`, `excel.py`, `ingest.py` (pure parts)
11. Risks: `parser.py` (pure parts)
12. Weather: `forecast.py`, `historical.py` (pure parts)
13. Storage: `cadre_mission_params.py`
14. Any helper functions across features missing doctests

### Phase 5: Backfill pytest tests (~18 new files)
15. `storage/tests/test_connection.py`
16. `storage/tests/test_runner.py`
17. `storage/tests/test_routes.py`
18. `auth/tests/test_routes.py`
19. `chat/tests/test_agent.py`
20. `chat/tests/test_routes.py`
21. `connectors/tests/test_local_files.py`
22. `demo/tests/conftest.py` + `demo/tests/test_routes.py`
23. `tools/weather/tests/test_forecast.py` + `test_historical.py`
24. `tools/news/tests/test_search.py`
25. `tools/documents/tests/test_reader.py` + `test_search.py`
26. `tools/risks/tests/test_parser.py`

### Phase 6: Update setup/docs
27. Update `docs-depo/setup.md` to mention `--doctest-modules` and the two-tier test approach
28. Run full test suite, fix any failing doctests or tests
29. Verify pre-commit hooks pass on all files

---

## Why This Structure Makes Sense

### Three tiers, each with a clear purpose

```
Tier 1: Doctests ──────────────── mid-development, fast, catches obvious breaks
         ("does this function work?")
              │
              ▼
Tier 2: Pytest feature tests ──── pre-merge, integration, catches stateful bugs
         ("does the system work?")
              │
              ▼
Tier 3: Quality pipeline ──────── commit-time, automated reviewer, catches blind spots
         ("did I miss anything?")
```

Each tier is independent. You can run doctests without pytest tests. You can run pytest without pre-commit. But all three run before merge.

### Zero app code bloat

- Doctests live in docstrings you already write — no new files for pure functions
- Pytest tests live in `tests/` — never imported by app code
- Quality pipeline lives in config files (`pyproject.toml`, `.pre-commit-config.yaml`, `.secrets.baseline`) — never imported by app code
- Adding a new linter rule: one line in pyproject.toml, zero app code changes
- Adding a new pre-commit hook: one block in `.pre-commit-config.yaml`, zero app code changes

### Scalable

- Adding a new pure function: write docstring with `>>>`. Done.
- Adding a new stateful module: create `tests/test_{name}.py`. Done.
- Adding a new quality rule: add Ruff/Bandit rule in pyproject.toml. Done.
- Architecture test auto-discovers and enforces. No hardcoded lists to maintain.