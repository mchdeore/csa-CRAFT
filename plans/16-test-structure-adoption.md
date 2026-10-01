# 16 — Review and adopt the three-tier test structure from `feat/development-rules-and-test-suite`

**Status:** planned · can run in parallel with plans 02–11 · hard-depends on plan 01 (settings) and plan 08 (weather/news deletion) for the "what fits" review

## Why

A separate branch `feat/development-rules-and-test-suite` (currently 9 commits ahead of `master`) already ships a well-shaped test strategy:

- **`app/tests/CODEBASE_RULES.md`** — the full developer rulebook (11 sections).
- **Doctest layer** — `pytest --doctest-modules` enabled; every public pure function gets a `>>>` example in its docstring.
- **Pytest feature layer** — one test file per stateful module (database, routes, API calls, file I/O), under `<feature>/tests/`.
- **Architecture enforcement** — two new tests in `app/tests/test_architecture.py` that walk the AST and fail CI if (a) a public function in a non-exempt module lacks a doctest, or (b) a stateful module lacks a matching `tests/test_<name>.py`.

Our refactor (plans 01–15) changes the dependency set, deletes `tools/weather` and `tools/news`, swaps the agent runtime (`pydantic-ai` → Azure OpenAI SDK), drops `pydantic`, and reorganises directories (`docs-depo/` → `dev-docs-depo/`). The branch's test suite was written against the old stack. We can't just merge it — we must review, cherry-pick the parts that still apply, and rewrite the parts that reference deleted / replaced modules.

This plan is that review-and-adopt pass.

## Scope

**In**
- Adopt the three-tier model (doctest / pytest / quality pipeline) as the project's testing posture.
- Adopt `app/tests/CODEBASE_RULES.md` with edits to reflect the post-refactor stack (no `pydantic_ai`, no weather/news, Azure SDK direct, dev-docs-depo path).
- Adopt the two new architecture-enforcement tests (`test_doctest_coverage`, `test_pytest_coverage_for_stateful`).
- Adopt `pytest --doctest-modules` opt-in via `pyproject.toml`.
- Cherry-pick the pytest files for modules we keep (`storage/tests/test_connection.py`, `storage/tests/test_runner.py`, `auth/tests/test_routes.py`, `chat/tests/test_routes.py`, `connectors/tests/test_local_files.py`, `tools/documents/tests/*`).
- Cherry-pick the doctests the branch adds to kept source files (charts, documents).

**Out** (deliberately rejected from the branch)
- `tools/weather/tests/*`, `tools/news/tests/*` — their source folders are deleted by plan 08.
- `tools/risks/`, `tools/costing/`, `tools/engineering/` folders the branch introduces — they belong to the pitch's reserved tool slots, but plan 08 already reserves those with stub classes. If the branch's parsers are richer than our stubs we migrate the stub bodies in a follow-up plan; **this plan ships only the stubs**.
- `tools/documents/ingest.py` from the branch — our plan 08 leaves document ingest to the existing `TextAnalysisTool`; evaluate whether to adopt the branch's richer parser as a follow-up.
- `chat/tests/test_agent.py` from the branch — hardcoded against `pydantic-ai`. Plan 03 already rewrites `chat/tests/test_agent.py` against a stub `AsyncAzureOpenAI`; adoption of the branch's version is a `git log` reference only.
- `demo/tests/` and `demo/` — the branch introduces a `demo/` feature folder. We do not adopt it; our demo flow is a seeded instance of the real app, not a parallel code path.
- `DESIGN_JOURNEY.md` at the branch's repo root — labelled "temporary"; we skip it.

## Review of the branch (what fits where)

Mapping every delivered artefact on `feat/development-rules-and-test-suite` to one of {Adopt, Edit then adopt, Reject, Follow-up}:

| Branch artefact | Status | Reason |
|---|---|---|
| `app/tests/CODEBASE_RULES.md` | Edit then adopt | Rewrite §9 Dependency Stack (drop `pydantic-ai`, Azure SDK direct). Rewrite §4 to reference `app/core/permissions.py` not `app/core/logging.py`. Keep everything else. |
| `app/tests/test_architecture.py` (two new methods) | Adopt | `test_doctest_coverage` + `test_pytest_coverage_for_stateful`. Exempt list adjusted to our modules (add `scripts/`, exempt `*/README.md`, exempt reserved tool stubs that intentionally raise `NotImplementedError`). |
| `pyproject.toml` doctest + testpath updates | Adopt | Adds `--doctest-modules` and expands `testpaths` to include `tools/` and `scripts/`. |
| `storage/tests/test_connection.py` | Adopt | Tests SQLite WAL + foreign-key invariants; stack-neutral. |
| `storage/tests/test_runner.py` | Adopt | Migration-runner tests; stack-neutral. |
| `auth/tests/test_routes.py` | Edit then adopt | Needs to use `X-Internal-Secret` from `settings.INTERNAL_API_SECRET` (plan 01) for test_client calls. |
| `chat/tests/test_routes.py` | Edit then adopt | Needs to be rewritten against the Azure SDK stub (plan 03). |
| `chat/tests/test_agent.py` | Reject | Hardcoded against `pydantic-ai`; plan 03 ships a replacement. |
| `connectors/tests/test_local_files.py` | Adopt | Stack-neutral; small path tweaks for `dev-docs-depo/data/` (plan 15). |
| `tools/documents/tests/test_reader.py` | Adopt | File-I/O tests via `tmp_path`. |
| `tools/documents/tests/test_search.py` | Edit then adopt | Needs the data-source registry (plan 07) wiring; drop any references to Guardian / weather. |
| `tools/documents/ingest.py` | Follow-up | Richer ingest parser; evaluate separately. Our refactor keeps the existing `TextAnalysisTool`. |
| `tools/charts/*` doctests | Adopt | Pure functions; the `>>>` examples embed cleanly. |
| `tools/costing/distance.py` | Follow-up | Not needed to satisfy any pitch use case yet. Belongs to UC-F1 cost pipeline. |
| `tools/engineering/compliance.py` | Follow-up | UC-E2 compliance helper. |
| `tools/risks/parser.py` | Follow-up | UC-E2 risk parser; our `ClassifierTool` stub from plan 08 is the pitch-reserved slot. |
| `tools/weather/tests/*` | Reject | `tools/weather/` is deleted by plan 08. |
| `tools/news/tests/*` | Reject | `tools/news/` is deleted by plan 08. |
| `tools/risks/tests/test_parser.py` | Follow-up | Pairs with the parser follow-up. |
| `demo/` + `demo/tests/` | Reject | We do not have a separate `demo/` feature folder. |
| `docs-depo/setup.md` (updated) | Reject | Plan 11 deletes `setup.md` entirely. |
| `DESIGN_JOURNEY.md` | Reject | Labelled temporary on the branch. |

## Adoption method

Three options, lowest-risk first:

1. **Cherry-pick per commit, by file.** For each "Adopt" row, `git checkout origin/feat/development-rules-and-test-suite -- <path>`. For "Edit then adopt", same checkout then patch the deltas in place. This keeps diffs atomic.
2. **Branch merge with resolution.** `git merge --no-ff origin/feat/development-rules-and-test-suite` and resolve conflicts in favour of our refactor for the Reject rows. Larger diff, less clear history.
3. **Rewrite from the branch's intent.** Open the branch's plan file (`plans/development-rules-and-test-suite.md` on that branch) as a reference, write all files fresh. Highest effort, cleanest code.

**Choice: Option 1** — one commit per artefact or per small cluster, so review is straightforward and rollback granular.

## Files touched (summary)

- **New** (ported from the branch, with edits for rejects + stack changes)
  - `app/tests/CODEBASE_RULES.md` (editable rewrite of the branch's version).
  - `app/tests/test_architecture.py` — append `test_doctest_coverage` and `test_pytest_coverage_for_stateful`.
  - `pyproject.toml` — `--doctest-modules` in `addopts`; `testpaths` extended.
  - `storage/tests/test_connection.py`.
  - `storage/tests/test_runner.py`.
  - `auth/tests/test_routes.py`.
  - `chat/tests/test_routes.py`.
  - `connectors/tests/test_local_files.py`.
  - `tools/documents/tests/test_reader.py`.
  - `tools/documents/tests/test_search.py`.
  - Doctest additions in `tools/charts/*`, `tools/documents/excel.py`, `tools/documents/reader.py`, `storage/database/*` modules.

- **Edit** (post-port patches)
  - `app/tests/CODEBASE_RULES.md` §9 (Azure SDK direct, no `pydantic-ai`, no `pydantic`), §4 (`app/core/permissions.py`), §6 (`settings.*` via `app.core.config`), §11 (append the forbidden-package rule from plan 12).
  - Any test using `cheddar-internal-dev` → `settings.INTERNAL_API_SECRET`.
  - Any test referencing `tools.weather`, `tools.news`, `tools.risks.parser`, `tools.costing.distance`, `tools.engineering.compliance` → removed or marked `@pytest.mark.skip(reason="reserved — see plan 08")` depending on whether the module exists as a stub.
  - `app/tests/test_architecture.py` exempt lists updated for the reserved tool stubs (so a stub raising `NotImplementedError` doesn't trip `test_pytest_coverage_for_stateful`).

- **Do NOT port**
  - `tools/weather/tests/`, `tools/news/tests/`, `tools/risks/`, `tools/costing/`, `tools/engineering/`, `demo/`, `DESIGN_JOURNEY.md`, `tools/documents/ingest.py`.

## Workflow

**Pre-check**
- Plans 01, 03, 05, 07, 08, 09 shipped (settings, Azure SDK agent, users, data-sources registry, weather/news delete + reserved stubs, packaging).
- `origin/feat/development-rules-and-test-suite` fetched (`git fetch origin feat/development-rules-and-test-suite`).
- `git log --oneline origin/master..origin/feat/development-rules-and-test-suite` understood.

**Do**
1. Fetch the branch (if not already): `git fetch origin feat/development-rules-and-test-suite`.
2. Port `app/tests/CODEBASE_RULES.md` from the branch; edit §4, §6, §9, §11 as above.
3. Port the two new architecture-enforcement test methods into `app/tests/test_architecture.py`; adjust exempt lists for our module set.
4. Port the `pyproject.toml` doctest + testpath additions.
5. Port the stack-neutral test files (`storage/tests/test_{connection,runner}.py`, `connectors/tests/test_local_files.py`, `tools/documents/tests/test_reader.py`).
6. Port the stack-adjacent tests with edits (`auth/tests/test_routes.py`, `chat/tests/test_routes.py`, `tools/documents/tests/test_search.py`).
7. Port the doctest additions on kept source files (`tools/charts/*`, `tools/documents/reader.py`, `tools/documents/excel.py`, chosen storage helpers).
8. Run `pytest --doctest-modules -q`. Fix any doctest failures (edit expected outputs, not source behaviour).
9. Run the new `test_doctest_coverage` and `test_pytest_coverage_for_stateful`; add any missing doctests or test files for our own modules introduced by plans 01–15 (`app/core/config.py`, `app/core/permissions.py`, `app/core/audit.py`, `app/core/data_sources.py`, `scripts/seed.py`, `storage/approvals.py`).
10. Add any new tests the enforcement surfaces, iteratively.

**Verify**
- `make check` green on a scratch clone.
- `pytest -q` runs doctests + pytest; green.
- `pytest app/tests/test_architecture.py -q` reports zero missing doctests and zero missing stateful tests across the live module set.
- `git log --oneline origin/feat/development-rules-and-test-suite..HEAD -- app/tests/CODEBASE_RULES.md` shows our edit on top of the ported file.

**Commit boundaries** (suggested)
- `test: port CODEBASE_RULES.md from feat/development-rules-and-test-suite with post-refactor edits`
- `test: port doctest+coverage architecture tests`
- `test: enable --doctest-modules in pyproject`
- `test: port stateful module tests (storage, auth, chat, connectors, documents)`
- `test: port doctests on kept pure-function modules (charts, documents)`
- `test: fill coverage gaps for refactor-introduced modules (config, permissions, audit, data_sources, seed, approvals)`

**Rollback**
Each commit is one scope → `git revert <sha>` per boundary. Full rollback: `git revert` across all boundaries.

## Verification checklist

- [ ] `app/tests/CODEBASE_RULES.md` lives in-tree and reflects the post-refactor stack (no `pydantic-ai`, Azure SDK direct, `app/core/permissions.py`, `settings.*`).
- [ ] `test_doctest_coverage` and `test_pytest_coverage_for_stateful` run under `make test` and pass.
- [ ] `pytest --doctest-modules` picks up our doctests across kept modules.
- [ ] No ported test imports `tools.weather`, `tools.news`, or `pydantic_ai`.
- [ ] Reserved tool stubs (plan 08) are either exempted from the stateful-coverage check or have a trivial `test_schema.py` asserting the raised `NotImplementedError`.
- [ ] `make check` is one-shot green.

## Out of scope

- Porting `tools/costing/`, `tools/engineering/`, `tools/risks/` from the branch — each gets a dedicated follow-up plan once the pitch use case lands.
- Porting `demo/` — not adopted.
- Replacing `TextAnalysisTool` with the branch's `tools/documents/ingest.py` — follow-up.
- Reaching 100% doctest coverage on legacy modules (`app/core/logging.py` structured JSON helpers, etc.) — exempt lists are allowed per the branch's convention.

---

## Reasoning / justification extracts

**User instruction:**
- "also make another plan to review and implement this branches test structure feat/development-rules-and-test-suite".

**Why review rather than merge:**
The branch was built against the pre-refactor stack: `pydantic-ai` agent, `tools/weather/`, `tools/news/`, `data/cadre-missions/` at root, `docs-depo/`. Merging whole would resurrect deleted modules and reintroduce pydantic. Cherry-picking the stack-neutral parts and rewriting the stack-adjacent parts preserves the test-strategy intent without regressing plans 01–15.

**Why keep the three-tier model intact:**
- Pitch §8 names the exact quality pipeline the branch's Tier 3 relies on (ruff / pyright / bandit / pip-audit / detect-secrets / pytest + coverage) — no change needed to that layer.
- Doctest layer (Tier 1) catches pure-function regressions during development without a run cost — matches the pitch's "Industry-standard, maintained" posture.
- Pytest feature layer (Tier 2) is where stateful behaviour (routes, SQLite, audit chain, approval queue) gets exercised. Pitch §4 Invariants explicitly calls out "Route × role matrix, protocol contracts, audit-envelope present" — all three sit in Tier 2.

**Why the two architecture tests over coverage %:**
The branch's own plan file argues the coverage % gate ("fail_under = 80") is a lagging indicator — a file can be 80% covered and still miss the one path that matters. The two AST walkers (doctest coverage, stateful-coverage) are leading indicators: they say "this public function is undocumented" or "this stateful module has nowhere to be exercised". We adopt the same logic.

**Why `demo/` is not adopted:**
Our refactor's position (plan 00 and plan 05): the demo is a running instance of the real app seeded with demo users, not a parallel code path. Introducing a `demo/` feature folder reintroduces a separate codepath to maintain. The branch's `demo/` was reasonable for its lineage; it is not for ours.

**Pitch alignment:**
- §4 "Protocol contracts" row and §4 "Invariants" row — our `test_architecture.py` extensions make the protocol conformance and the route × role matrix enforcement data-driven.
- §8 System-Health Tooling table — Tier 3 remains unchanged, matching pitch commitments exactly (ruff, pyright strict, pytest, bandit, pip-audit, detect-secrets).

**References**
- Branch's own plan: `origin/feat/development-rules-and-test-suite:plans/development-rules-and-test-suite.md`.
- Branch's rulebook deliverable: `origin/feat/development-rules-and-test-suite:app/tests/CODEBASE_RULES.md`.
- Branch's enforcement tests: `origin/feat/development-rules-and-test-suite:app/tests/test_architecture.py`.
