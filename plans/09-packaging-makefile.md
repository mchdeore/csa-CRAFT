# 09 — Packaging + Makefile

**Status:** planned · depends on plans 01–08 landing (deps are stable by then)

## Why

The repo imports work because the working directory is on `sys.path` by accident of invocation. A professional repo declares its packages, lets `pip install -e .` resolve them, and exposes console scripts for the long-running verbs. The Makefile makes every verb discoverable to a human or an agent landing in the repo cold.

## Scope

**In**
- `[project]` + `[build-system]` + `[project.scripts]` in `pyproject.toml`.
- Hatchling as the build backend.
- Pyright strict mode for the source packages.
- Top-level `Makefile` with `install`, `dev`, `test`, `lint`, `typecheck`, `check`, `seed`, `audit-verify`, `clean`, `help`.

**Out**
- Publishing to a package index.
- Dockerfile / container build (deploy-time, pitch end-state).
- CI workflow — pre-commit already runs the gates; GitHub Actions were deleted per master.

## Files touched

- **Edit**
  - `pyproject.toml` — add `[project]`, `[project.optional-dependencies]`, `[project.scripts]`, `[build-system]`, `[tool.hatch.build.targets.wheel]`, `[tool.pyright]`.
- **New**
  - `Makefile` at repo root.
- **Keep (derived)**
  - `app/requirements.txt` stays during the transition as a pinned list; mark it in the file header as derived from `pyproject.toml`. Delete it once the whole team moves to `pip install -e ".[dev]"`.

## Shapes

```toml
# pyproject.toml additions
[project]
name = "csa-craft"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "dash", "flask", "flask-login",
    "openai",
    "pandas", "plotly",
    "python-dotenv", "requests", "werkzeug", "msal",
    "pdfplumber", "python-docx",
]

[project.optional-dependencies]
dev = ["ruff", "pyright", "bandit", "pip-audit", "detect-secrets",
       "pytest", "pytest-cov", "pre-commit"]

[project.scripts]
csa-craft = "app.factory:main"
csa-craft-seed = "scripts.seed:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["app", "auth", "chat", "storage", "connectors", "tools", "scripts"]

[tool.pyright]
strict = ["app", "auth", "chat", "storage", "connectors", "tools"]
pythonVersion = "3.11"
```

```make
# Makefile
.PHONY: help install dev test lint typecheck check seed clean audit-verify
help:          ## list targets
	@grep -hE '^[a-z_-]+:.*?## ' $(MAKEFILE_LIST) | sort | awk 'BEGIN{FS=":.*?## "};{printf "  %-14s %s\n",$$1,$$2}'
install:       ## editable install with dev extras
	pip install -e ".[dev]"
dev:           ## run the dev server
	python app.py
test:          ## run the test suite
	pytest -q
lint:          ## ruff + bandit + pip-audit + detect-secrets
	ruff check . && bandit -c pyproject.toml -r . && pip-audit && detect-secrets scan --baseline .secrets.baseline
typecheck:     ## pyright strict
	pyright
check: lint typecheck test  ## full CI equivalent
seed:          ## seed users from SEED_USERS_FILE
	python scripts/seed.py
audit-verify:  ## verify today's audit log hash chain
	python -m app.core.audit verify
clean:         ## reset the SQLite DB and log dir
	rm -f app/database/cheddar.db* && rm -rf storage/database/log/*
```

## Workflow

**Pre-check**
- Plans 01–08 shipped so deps + script entry points exist.

**Do**
1. Add the sections above to `pyproject.toml`.
2. Add the top-level `Makefile`.
3. Add a header comment to `app/requirements.txt` noting it is derived from `pyproject.toml` and will be removed once teams migrate.
4. Verify `app/factory.main` and `scripts/seed.main` exist as callables (plans 02 and 05).

**Verify**
- `pip install -e ".[dev]"` succeeds in a fresh venv.
- `which csa-craft csa-craft-seed` shows both console scripts resolved.
- `make help` prints the target list sorted.
- `make check` passes.
- `python -c "import app, auth, chat, storage, connectors, tools, scripts"` succeeds (packaging discovered all).

**Commit**
`build: hatchling packaging + Makefile + pyright strict`

**Rollback**
`git restore -SW pyproject.toml Makefile app/requirements.txt`

## Verification checklist

- [ ] `pip install -e ".[dev]"` works clean.
- [ ] Console scripts resolve.
- [ ] `make help` lists every target.
- [ ] `make check` is one-shot green.
- [ ] Pyright strict mode runs across the six source packages.

## Out of scope

- Dockerfile / container image.
- Private package index publishing.
- GitHub Actions workflow (deleted on master; pre-commit covers the gate).

---

## Reasoning / justification extracts

**User instructions:**
- "proper routes".
- "accessible to 'manual' users too" — the Makefile is the discoverability surface for humans.

**Pitch invariants:**
- §8 System-Health Tooling lists ruff / pyright / pytest / bandit / pip-audit / detect-secrets. The `check` target bundles exactly that set so one command is CI-equivalent.

**Why hatchling:**
Modern, minimal, PEP 621-friendly, used widely in the Python ecosystem; alternative `setuptools` works too but requires more configuration.

**Why `make` over `just`:**
`make` is on every dev machine and CI image. `just` is more ergonomic but adds a dep. For a project that fits on one page of targets, the gain is marginal.
