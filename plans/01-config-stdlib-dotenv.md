# 01 — Config via stdlib + `python-dotenv`

**Status:** planned · prerequisite for every later plan

## Why

`os.environ.get("…", "default")` is scattered across at least five files, including demo-shaped defaults (`"cheddar-dev-secret-key-change-in-production"`, `"cheddar-internal-dev"`, `"CHE-DSV4P"`, `~/Documents`). Config needs one source of truth, type-safe, fails at startup when a required var is missing. No new deps.

## Scope

**In**
- One `app/core/config.py` that reads every env var.
- A frozen `Settings` dataclass instance (`settings`) imported everywhere else.
- `.env` loaded via existing `python-dotenv`.
- Rewrite `app/.env.example` with inline comments and required / optional marks.
- Delete every hardcoded fallback for identity, secrets, paths.
- Guardrail test asserting `os.environ`/`os.getenv` lives only in `config.py`.

**Out**
- Pydantic / pydantic-settings / environs. Stdlib only.
- Converting UI copy strings to env (they stay in Python templates).

## Env schema (final)

| Env var | Purpose | Required | Fallback |
|---|---|---|---|
| `SECRET_KEY` | Flask session signing | yes | raise at startup |
| `INTERNAL_API_SECRET` | header for server-side callback `test_client` calls | yes | raise at startup |
| `HOST` | bind host | no | `127.0.0.1` |
| `PORT` | bind port | no | `8050` |
| `DEBUG` | debug mode | no | `0` |
| `DATABASE_URL` | SQLite file (`sqlite:///…`) | no | `sqlite:///app/database/cheddar.db` |
| `LOG_DIR` | audit + structured log directory | no | `storage/database/log` |
| `LOG_RETENTION_DAYS` | retention days | no | `90` |
| `AUDIT_HASH_SEED` | starting hash for AgentAction chain | no | `"0" * 64` |
| `CONNECTORS_ROOT` | local-file source root | yes | raise |
| `DATA_SOURCES_FILE` | JSON file listing data sources | no | `app/core/data_sources.json` |
| `PERMISSIONS_FILE` | JSON file with role levels + route rules | no | `app/core/permissions.json` |
| `SEED_USERS_FILE` | JSON file consumed by the seeder | no | `scripts/users.example.json` |
| `SYSTEM_PROMPT_FILE` | plain-text agent prompt | no | `app/core/system_prompt.txt` |
| `CHAT_PROVIDER` | provider dispatch (`azure` only today) | no | `azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure endpoint | yes if `CHAT_PROVIDER=azure` | raise |
| `AZURE_OPENAI_API_KEY` | Azure key | yes if `CHAT_PROVIDER=azure` | raise |
| `AZURE_OPENAI_API_VERSION` | API version | no | `2024-10-21` |
| `AZURE_OPENAI_DEPLOYMENT` | deployment name | yes if `CHAT_PROVIDER=azure` | raise |
| `AGENT_RECURSION_LIMIT` | max tool-call loop iterations | no | `25` (pitch invariant) |
| `ENABLE_DEBUG_ROUTES` | gate `/debug/*` | no | `0` |
| `ENABLE_HITL` | enable risky-tool interrupt | no | `0` |
| `GUARDRAIL_HOOK` | reserved; `""` = no-op | no | `""` |

## Files touched

- **Rewrite**
  - `app/core/config.py` — `Settings` dataclass + loader + validator.
  - `app/.env.example` — full schema with inline comments.
- **Edit** (replace `os.environ.get` with `from app.core.config import settings`)
  - `app/core/logging.py:597`
  - `chat/callbacks.py:28`
  - `storage/callbacks.py:13`
  - `chat/provider.py:76,77,84,86`
  - `app/entry.py:12`
- **Delete** (hardcoded fallbacks)
  - `"cheddar-dev-secret-key-change-in-production"` in `app/entry.py`
  - `"cheddar-internal-dev"` wherever it appears (3 places)
  - `"CHE-DSV4P"` in `chat/provider.py`
  - the `~/Documents` default in `app/core/config.py`
  - `app/core/config.py:10` `WORKSPACES_DIR` (unused dead constant)

## Implementation sketch

```python
# app/core/config.py
from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

_MISSING = object()
def _str(name, default=_MISSING):
    v = os.environ.get(name, default)
    if v is _MISSING:
        raise RuntimeError(f"missing required env var: {name}")
    return v
def _int(name, default): return int(os.environ.get(name, default))
def _bool(name, default): return os.environ.get(name, str(int(default))).lower() in ("1","true","yes","on")
def _path(name, default=_MISSING): return Path(_str(name, default))

@dataclass(frozen=True)
class Settings:
    SECRET_KEY: str
    INTERNAL_API_SECRET: str
    HOST: str
    PORT: int
    DEBUG: bool
    DATABASE_URL: str
    LOG_DIR: Path
    LOG_RETENTION_DAYS: int
    AUDIT_HASH_SEED: str
    CONNECTORS_ROOT: Path
    DATA_SOURCES_FILE: Path
    PERMISSIONS_FILE: Path
    SEED_USERS_FILE: Path
    SYSTEM_PROMPT_FILE: Path
    CHAT_PROVIDER: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_API_VERSION: str
    AZURE_OPENAI_DEPLOYMENT: str
    AGENT_RECURSION_LIMIT: int
    ENABLE_DEBUG_ROUTES: bool
    ENABLE_HITL: bool
    GUARDRAIL_HOOK: str

def _load() -> Settings:
    s = Settings(
        SECRET_KEY=_str("SECRET_KEY"),
        INTERNAL_API_SECRET=_str("INTERNAL_API_SECRET"),
        HOST=_str("HOST", "127.0.0.1"),
        PORT=_int("PORT", 8050),
        DEBUG=_bool("DEBUG", False),
        DATABASE_URL=_str("DATABASE_URL", "sqlite:///app/database/cheddar.db"),
        LOG_DIR=_path("LOG_DIR", "storage/database/log"),
        LOG_RETENTION_DAYS=_int("LOG_RETENTION_DAYS", 90),
        AUDIT_HASH_SEED=_str("AUDIT_HASH_SEED", "0" * 64),
        CONNECTORS_ROOT=_path("CONNECTORS_ROOT"),
        DATA_SOURCES_FILE=_path("DATA_SOURCES_FILE", "app/core/data_sources.json"),
        PERMISSIONS_FILE=_path("PERMISSIONS_FILE", "app/core/permissions.json"),
        SEED_USERS_FILE=_path("SEED_USERS_FILE", "scripts/users.example.json"),
        SYSTEM_PROMPT_FILE=_path("SYSTEM_PROMPT_FILE", "app/core/system_prompt.txt"),
        CHAT_PROVIDER=_str("CHAT_PROVIDER", "azure"),
        AZURE_OPENAI_ENDPOINT=_str("AZURE_OPENAI_ENDPOINT", ""),
        AZURE_OPENAI_API_KEY=_str("AZURE_OPENAI_API_KEY", ""),
        AZURE_OPENAI_API_VERSION=_str("AZURE_OPENAI_API_VERSION", "2024-10-21"),
        AZURE_OPENAI_DEPLOYMENT=_str("AZURE_OPENAI_DEPLOYMENT", ""),
        AGENT_RECURSION_LIMIT=_int("AGENT_RECURSION_LIMIT", 25),
        ENABLE_DEBUG_ROUTES=_bool("ENABLE_DEBUG_ROUTES", False),
        ENABLE_HITL=_bool("ENABLE_HITL", False),
        GUARDRAIL_HOOK=_str("GUARDRAIL_HOOK", ""),
    )
    if s.CHAT_PROVIDER == "azure":
        for n in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_DEPLOYMENT"):
            if not getattr(s, n):
                raise RuntimeError(f"CHAT_PROVIDER=azure requires {n}")
    return s

settings = _load()
```

## Workflow

**Pre-check**
- `git status` clean on the branch.
- `python -c "import dotenv"` works (already in requirements).

**Do**
1. Write new `app/core/config.py` as above.
2. Rewrite `app/.env.example` listing every var with inline comments and required/optional notes.
3. Grep for every `os.environ.get`/`os.getenv` in the tree; convert each call site to `from app.core.config import settings`.
4. Delete the hardcoded fallback strings listed above.
5. Delete `WORKSPACES_DIR` and any imports of it.

**Verify**
- `grep -rE "os\.environ|os\.getenv" --include='*.py'` returns only `app/core/config.py`.
- `grep -rn "cheddar-internal-dev\|cheddar-dev-secret-key-change-in-production\|CHE-DSV4P"` returns zero.
- `python -c "from app.core.config import settings"` with no `.env` raises `RuntimeError: missing required env var: SECRET_KEY`.
- With a filled `.env` (dummy values for required), the import succeeds.
- `pytest` still passes (fixtures may need `monkeypatch.setenv` tweaks).

**Commit**
`refactor(config): stdlib Settings + dotenv, delete scattered os.environ and demo defaults`

**Rollback**
`git restore -SW app/core/ app/.env.example app/entry.py chat/ storage/`

## Verification checklist

- [ ] One `os.environ`/`os.getenv` grep match (in `config.py`).
- [ ] Missing required var raises at import.
- [ ] `CHAT_PROVIDER=azure` with any Azure field empty raises with the field name.
- [ ] `app/.env.example` lists every field in `Settings`.
- [ ] `WORKSPACES_DIR` is gone and unimported.
- [ ] No hardcoded `"cheddar-*"` fallback strings remain.

## Out of scope

- Converting UI copy to env.
- Replacing `python-dotenv` with anything else.
- Vendor API-version default (`2024-10-21`) — keep as a declarative constant.

---

## Reasoning / justification extracts

**User instructions:**
- "no hardcoding anything though clean that up".
- "we are using good developer practices like abstract var names in the env".
- "don't prefix stuff with CHEDDAR, make it real dev names".
- "all vars should be env driven".

**Why stdlib + dotenv instead of pydantic-settings / environs:**
- User wants pydantic removed from the install. Pydantic-settings pulls pydantic.
- Environs is a nice library but still a new dep; stdlib + a `_MISSING` sentinel is 30 lines and does the same job for this scope.
- `python-dotenv` is already a direct dep — reuse it.

**Why fail-fast at import time:**
- 12-factor principle: config errors surface before the server accepts traffic (see [FastAPI settings guide](https://fastapi.tiangolo.com/advanced/settings/)).
- Matches the pitch's "Invariants" posture (§8 System-Health Tooling): config misses are caught by startup, not production.

**Pitch commitments this plan honours:**
- Startup validation — pitch §8 lists "ruff · pyright · pytest · bandit · pip-audit · detect-secrets" as invariants; a typed `Settings` lets pyright-strict verify callers.
