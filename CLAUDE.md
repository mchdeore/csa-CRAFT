# CLAUDE.md

## What is this project

Cheddar is a chat application built with Dash (single process, frontend + backend).

### File structure
- `app.py` — Dash app entry point: sets layout, imports callbacks, runs server
- `dash_app.py` — creates the Dash app instance (imported by callbacks and app.py)
- `protocols.py` — interfaces (AuthProvider, WorkspaceStore, ChatProvider)
- `config.py` — settings and constants
- `services.py` — wires protocols to concrete implementations
- `auth.py` — DictAuth implementation
- `storage.py` — JsonFileStore (JSON files on disk)
- `chat.py` — DeepSeekChat (OpenAI SDK → DeepSeek)
- `layouts.py` — Dash UI builder functions
- `callbacks/` — Dash callback handlers (auth, workspaces, chat)

## Running

- App: `python app.py` (runs on http://localhost:8050)
- Type check: `pyright`
- Lint: `ruff check .`
- Tests: `pytest tests/ -v`

All three checks must pass before committing.

## Code standards

### Dependencies
- Every third-party package the code imports must be listed in `requirements.txt`.
- pytest enforces this — missing packages fail the build.

### Types
- Type-annotate function parameters and return values — pyright enforces this.

### Documentation
- Don't write docstrings on functions where the name + signature tells the full story.
- DO write a one-line docstring when behavior or side effects are non-obvious.
- Never write "Parameters: x: The x" boilerplate.

### Style
- ruff enforces naming (snake_case, PascalCase) and import ordering.
- Functions over 30 lines should be split — pytest enforces this.
- Keep string literals inline. Don't extract "role" to MSG_ROLE or "password" to INPUT_TYPE_PW.
- Constants are for values that are: reused across files, configurable, or genuinely unexplained.

## What NOT to do

These patterns make the codebase worse. Don't introduce them:
- Don't create a constant for every string literal.
- Don't add docstrings that restate the function signature.
- Don't wrap a single function call in another function.
- Don't split a clear 20-line function into three 8-line functions.
- Don't add error handling for impossible conditions.
- Don't add `# removed: ...` comments or backwards-compatibility shims.
- Don't add `type: ignore` comments to suppress pyright — fix the actual type issue.
- Don't add a dependency without listing it in `requirements.txt`.

## Before creating a new endpoint or function

1. Search the codebase for existing implementations first.
2. If similar functionality exists, extend it rather than creating a parallel version.
3. Don't duplicate what already exists under a different name.
