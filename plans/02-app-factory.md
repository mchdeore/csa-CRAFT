# 02 — Application factory

**Status:** planned · depends on `01-config-stdlib-dotenv.md`

## Why

`app.py` + `app/entry.py` do all their work at module import time (routes registered, callbacks imported, Dash instance constructed, secret key set, middleware registered). That makes tests hard (can't build two app instances cleanly), prevents swapping config at construction time, and spreads side effects across files. The Flask + Dash community standard is a `create_app()` factory — one function, called from the entry point.

## Scope

**In**
- `app/factory.py` with `create_app(overrides=None) -> Dash` and `main()` for the console script.
- `app.py` becomes a 5-line entry point calling `create_app()`.
- `app/core/dash_app.py` keeps a transitional module-level singleton that the factory initialises (so `@app.callback` decorators keep working).

**Out**
- Rewriting every `@app.callback` to accept the app as an argument. Transitional singleton is fine for now; full decoupling is a follow-up.

## Files touched

- **New**: `app/factory.py`.
- **Rewrite**: `app.py`.
- **Edit**: `app/entry.py` — collapse module-level side effects into `create_app`.
- **Keep (transitional)**: `app/core/dash_app.py` — module-level `app` singleton that the factory sets up on first call.

## Implementation sketch

```python
# app/factory.py
from __future__ import annotations
from dash import Dash
from app.core.config import settings

def create_app(overrides: dict | None = None) -> Dash:
    from app.core import dash_app
    from app.core.logging import register_middleware, get_structured_logger
    from app.core.routes import register_all
    from app.core.services import auth
    from app.templates import make_layout

    if dash_app.app is None:
        dash_app.app = Dash(__name__, suppress_callback_exceptions=True)
    da = dash_app.app
    server = da.server
    server.secret_key = settings.SECRET_KEY

    get_structured_logger()
    auth.init_app(server)
    register_all(server)
    register_middleware(server)

    da.layout = make_layout()
    _register_callbacks(da)
    return da

def _register_callbacks(da):
    # Importing registers decorated callbacks against the singleton.
    import auth.callbacks  # noqa: F401
    import chat.callbacks  # noqa: F401
    import storage.callbacks  # noqa: F401

def main() -> None:
    app = create_app()
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
```

```python
# app.py
from app.factory import main
if __name__ == "__main__":
    main()
```

```python
# app/core/dash_app.py (transitional)
app = None  # set by factory on first call
```

## Workflow

**Pre-check**
- `01-config-stdlib-dotenv.md` shipped.
- `python -c "from app.core.config import settings"` works with a filled `.env`.

**Do**
1. Write `app/factory.py` as above.
2. Change `app/core/dash_app.py` to `app = None` (no module-level `Dash(...)` call).
3. Rewrite `app.py` to the two-line entry point.
4. Delete the module-level side effects at the top of `app/entry.py`; keep it as a thin shim or delete.

**Verify**
- `python app.py` boots the dev server and the login UI renders.
- `pytest -q` passes. Add a fixture that builds a fresh app in a scratch Flask app context — two calls to `create_app()` in the same session should not raise.
- `grep -nE "^app\s*=\s*Dash\(" --include='*.py' .` returns only inside `create_app`.

**Commit**
`refactor(app): create_app factory pattern`

**Rollback**
`git restore -SW app/`

## Verification checklist

- [ ] `python app.py` boots.
- [ ] `pytest` passes.
- [ ] No module-level `Dash(...)` outside `create_app`.
- [ ] Tests can build two `create_app()` instances without collision.

## Out of scope

- Removing the transitional `dash_app.app` singleton — callback decorators depend on it. Full decoupling is a later cleanup.
- Introducing Flask Blueprints — not needed yet.

---

## Reasoning / justification extracts

**User instruction:**
- "we are using good developer practices like... proper routes, etc".

**Pattern reference:**
Flask application factory is the long-standing community pattern for non-trivial apps. See [Plotly community thread](https://community.plotly.com/t/recommended-project-structure-mvc-pattern/27868) and [Flask best practices](https://tessl.io/registry/tessl-labs/flask-best-practices). Advantages: prevents circular imports, enables per-test app isolation, lets config vary at construction time, matches how larger Flask / Dash projects are structured.

**Pitch alignment:**
Pitch §1 shows the "Route-gated RBAC" + "Primary Agent (entry point)" containers as independent concerns; the factory function is the one place they get wired together. Keeps the pitch's seams honest.
