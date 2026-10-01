# 12 — Test and guardrail hardening

**Status:** planned · depends on plans 01–11

## Why

The pitch calls out "Route × role matrix · protocol contracts · audit-envelope invariants" as the test posture (§4 Design Decisions, Invariants row; §8 System-Health Tooling). After the refactor the invariants grow: `os.environ` reads must be centralised, `pydantic`/`langchain` must be absent, `DEFAULT_USERS` must not come back, the hash chain must verify. These are things humans forget to re-check during review — put them in the test suite so pre-commit catches them.

## Scope

**In**
- `app/tests/test_config.py` — settings loader behaviour.
- `app/tests/test_permissions.py` — JSON loader + role / rule helpers.
- `app/tests/test_audit.py` — hash chain integrity.
- `app/tests/test_imports.py` — forbidden-import guardrail.
- `app/tests/test_rules.py` extensions — codebase scans.
- `auth/tests/test_permissions.py` — full route × role matrix.
- `chat/tests/*` rewritten against a stub `AsyncAzureOpenAI` (also covered in plan 03; this plan audits coverage).

**Out**
- Load testing / performance.
- Fuzz testing the audit chain.
- UI (Dash) E2E tests beyond the ones that already live under feature `tests/`.

## Guardrail tests

### `app/tests/test_rules.py` (extend)

```python
# pseudo-code; current file already does codebase scanning for route rules.
# Add:
def test_os_environ_centralised():
    hits = run_grep(r"os\.environ|os\.getenv", include="*.py")
    allowed = {Path("app/core/config.py")}
    offenders = {h for h in hits if h.file not in allowed}
    assert not offenders, f"os.environ outside config.py: {offenders}"

def test_no_default_users():
    hits = run_grep(r"\bDEFAULT_USERS\b", include="*.py")
    assert not hits, f"DEFAULT_USERS resurrected: {hits}"

def test_no_demo_hardcoded_strings():
    for needle in ("cheddar-internal-dev",
                   "CHE-DSV4P",
                   "cheddar-dev-secret-key-change-in-production",
                   "echo — Azure OpenAI not configured"):
        hits = run_grep(re.escape(needle), include="*.py")
        assert not hits, f"demo string resurrected: {needle} → {hits}"

def test_no_weather_news():
    for mod in ("tools.weather", "tools.news"):
        hits = run_grep(fr"\b{mod.replace('.', r'\.')}\b", include="*.py")
        assert not hits
```

### `app/tests/test_imports.py` (new)

```python
from importlib.metadata import distributions

FORBIDDEN = {"pydantic", "pydantic_core", "pydantic-ai", "langchain", "langchain-core",
             "langchain-openai", "langgraph"}

def test_forbidden_packages_not_installed():
    installed = {d.metadata["Name"].lower() for d in distributions()}
    hits = FORBIDDEN & installed
    assert not hits, f"forbidden packages installed: {hits}"

def test_forbidden_imports_not_in_source():
    offenders = []
    for py in Path(".").rglob("*.py"):
        if ".git" in py.parts or "/.venv/" in str(py):
            continue
        text = py.read_text()
        for mod in FORBIDDEN:
            if re.search(fr"^\s*(from|import)\s+{re.escape(mod)}(\s|\.|$)", text, re.M):
                offenders.append((py, mod))
    assert not offenders, offenders
```

### `app/tests/test_config.py` (new)

- missing required env var raises `RuntimeError` with the field name
- `CHAT_PROVIDER=azure` with any Azure field empty raises with the field name
- every field in `Settings` appears in `app/.env.example`
- `DEBUG=1` / `DEBUG=true` / `DEBUG=yes` all parse `True`
- Path fields resolve relative to cwd

### `app/tests/test_permissions.py` (new)

- `permissions.json` loads
- `role_level("admin") == 3`, `role_level("unknown") == 0`
- `is_public("/")`, `is_public("/favicon.ico")`, `is_public("/auth/login")`
- `find_matching_rule("/admin/users")` → admin rule
- `find_matching_rule("/no-such-path")` → `None`

### `app/tests/test_audit.py` (new)

- empty log + first emit uses the seed as `previous_hash`
- chain remains valid across 100 serial writes
- tampering with any field of any line breaks `verify` and names the offending `trace_id`
- two threads writing under the file lock both land cleanly; chain verifies

### `auth/tests/test_permissions.py` (extend or replace)

Full route × role matrix. For every registered route and every role, assert:
- 200 if role meets or exceeds `min_role`
- 403 if role is below `min_role`
- 404 if route is not registered
- public and internal prefixes behave per `permissions.json`

Implementation: enumerate `app.url_map.iter_rules()`, cross-join with role list, drive via `test_client` sessions.

## Files touched

- **New**
  - `app/tests/test_config.py`.
  - `app/tests/test_permissions.py`.
  - `app/tests/test_audit.py`.
  - `app/tests/test_imports.py`.
- **Extend**
  - `app/tests/test_rules.py` — guardrails above.
  - `auth/tests/test_permissions.py` — full matrix.
- **Rewrite** (ensure coverage)
  - `chat/tests/test_agent.py` — stub `AsyncAzureOpenAI` scenarios (also in plan 03).

## Workflow

**Pre-check**
- Plans 01–11 shipped.
- `make check` otherwise passes.

**Do**
1. Write the four new test files.
2. Extend `app/tests/test_rules.py` with the four new guardrails.
3. Extend `auth/tests/test_permissions.py` to drive the full matrix.
4. Audit `chat/tests/*` for coverage of ReAct branches: tool-less reply, single-tool reply, recursion-limit guard, HITL pause.

**Verify**
- `pytest -q` green across the whole suite.
- `pytest app/tests/test_imports.py` fails loudly if someone `pip install pydantic`s.
- `pytest app/tests/test_rules.py` fails loudly if someone sneaks an `os.environ.get` into `chat/foo.py`.

**Commit**
`test: config / permissions / audit / imports guardrails + full route×role matrix`

**Rollback**
`git restore -SW app/tests/ auth/tests/ chat/tests/`

## Verification checklist

- [ ] Four new test files exist and pass.
- [ ] `test_rules.py` fails on seeded demo strings.
- [ ] `test_imports.py` fails if any forbidden package is installed.
- [ ] Route × role matrix covers every registered rule.
- [ ] `make check` is green on a scratch clone.

## Out of scope

- Load tests.
- Fuzz tests.
- UI E2E beyond the current Playwright smoke.

---

## Reasoning / justification extracts

**Pitch commitments honoured:**
- "Route × role matrix · protocol contracts · audit-envelope invariants (156 tests, 91% cov)" (§8 System-Health Tooling).
- "Invariants" row of §4 Design Decisions names pytest + pyright + ruff + bandit + pip-audit + detect-secrets — the guardrails make these tests specific to this codebase, not just generic linting.

**User instructions:**
- "no hardcoding anything though clean that up I think that's going to cause a lot of cleanup issues later" — the guardrail tests are the long-term enforcement so cleanup stays done.

**Why `test_imports.py` goes beyond source grep:**
A dep can be pulled in transitively by a well-intentioned new package. Walking `importlib.metadata.distributions()` catches that at the first `make check` after someone adds the new dep, not months later during a dep audit.
