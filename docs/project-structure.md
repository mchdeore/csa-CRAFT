# Project Structure

## Root

- `app.py` — thin entry point, delegates to `app.entry`
- `tests/` — architecture enforcement + code quality tests

## app/ — Application Shell

- `entry.py` — Dash server setup, layout, clientside callbacks
- `templates.py` — `make_layout()` returns root page HTML
- `routes.py` — app-level Flask routes (stub)
- `core/` — shared infrastructure
  - `config.py` — settings, constants, environment variables
  - `dash_app.py` — `Dash()` application instance
  - `protocols.py` — interfaces (AuthProvider, WorkspaceStore, ChatProvider, Tool, ChatResponse)
  - `services.py` — wires protocols to concrete implementations (singletons)
  - `routes.py` — central Flask route registrar

## auth/ — Authentication

- `provider.py` — `InMemoryAuth` class (flask-login integration)
- `templates.py` — `build_login()` UI
- `callbacks.py` — login/logout/page render callbacks
- `routes.py` — auth Flask routes (stub)

## chat/ — Chat & Tools

- `provider.py` — `DeepSeekChat` class (Azure OpenAI with tool-calling loop)
- `templates.py` — message bubbles, charts, news cards, chat area, input bar
- `callbacks.py` — send message, file upload, chart navigation
- `routes.py` — future tool endpoints (code sandbox, chart generation)

## storage/ — Workspace Storage

- `store.py` — `SqliteStore` business logic (CRUD operations)
- `templates.py` — sidebar, workspace list, chart navigation
- `callbacks.py` — create/select workspace
- `routes.py` — storage Flask routes (stub)
- `database/` — database infrastructure
  - `connection.py` — SQLite connection factory (WAL mode, foreign keys)
  - `runner.py` — migration runner (discovers and applies numbered .sql files)
  - `migrations/` — numbered SQL migration files (001_initial.sql, 002_*.sql, ...)

## tools/ — Chat Tools

- `registry.py` — `ToolRegistry` manages tool definitions and execution
- `weather.py` — weather forecast tool (Open-Meteo API)
- `historical_weather.py` — historical weather data tool
- `news.py` — news search tool (Guardian API + Cohere rerank)
- `excel_tool.py` — Excel/CSV file upload and charting
