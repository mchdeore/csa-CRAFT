# Cheddar Development Rules

Quality is enforced by three tools. All must pass before merging.

## pyright (type checking)

- Every function parameter must have a type annotation.
- Every function must have a return type annotation (use `-> None` for void).
- Run: `pyright`

## ruff (linting)

- `snake_case` for variables and functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for module-level constants.
- Standard library imports first, then third-party, then local. One blank line between groups.
- No unused imports.
- Run: `ruff check .`

## pytest (code quality)

- Functions must not exceed 30 lines.
- Every third-party import must be listed in `requirements.txt`.
- Run: `pytest tests/ -v`

## Guidelines (human review)

- Error messages must explain what went wrong AND what to do about it.
- Don't extract string literals to constants unless reused across files or genuinely configurable.
- Don't write docstrings that restate the function signature — only when behavior is non-obvious.
