# TEMPORARY — Delete after branch merges to master

## How We Landed at This Testing Structure

User directive: "Make a plan to make a subfolder somewhere of key documentation and codebase
rules to follow for development so we have a source of truth."

### User Requirements (evolved over discussion)

1. **Rules document** — single source of truth for how development should be done. Covering
   proper routes, logging, authority, data safety, testing, protocols, code style.

2. **Tests should not bloat app code** — keep test infrastructure separate from application
   logic. No mocking frameworks in app code. No test imports in production paths.

3. **Doctests as mid-development quick checks** — low-level, run while coding, catch obvious
   breaks. Every public function gets one in its docstring. Not a substitute for full test suite.

4. **Industry-standard quality pipeline as final gate** — Ruff, Bandit, detect-secrets, Pyright
   running on every commit via pre-commit hooks. Acts like an automated reviewer with many
   suggestions. You don't have to take every suggestion, but you must address them.

5. **Three-tier system:**
   - Tier 1: Doctests (development-time) — in function docstrings, `pytest --doctest-modules`
   - Tier 2: Pytest feature tests (pre-merge) — in `tests/` folders, one per stateful source file
   - Tier 3: Quality pipeline (commit-time) — Ruff, Bandit, detect-secrets, Pyright, pre-commit

6. **No coverage percentage gate** — replaced with structural enforcement:
   - `test_doctest_coverage` — every public function must have `>>>` in docstring
   - `test_pytest_coverage_for_stateful` — stateful modules must have matching test file

7. **Sync with master before development** — added to rules doc workflow section.

8. **Branch named `feat/development-rules-and-test-suite`** — pushed to GitHub for review
   before merging to master.

### Key Design Decisions

- **Doctest first, pytest second.** Pure-function modules (most of tools/charts/) get zero
  new files — tests live in docstrings. Only stateful code (database, routes, API calls)
  gets pytest test files. This kept total new test files to ~15 instead of ~30+.

- **Rules doc lives at `app/tests/CODEBASE_RULES.md`.** Same directory as the enforcement
  tests. Rules and enforcer live together. When someone adds a test, they see the rules doc
  and update it. When someone reads the rules, the tests are right next to them.

- **Quality pipeline configuration untouched.** All in `pyproject.toml` and
  `.pre-commit-config.yaml`. Zero app code impact. These run externally and scan the
  codebase without importing into the application.

- **Bug found during test writing:** `tools/documents/reader.py` `_chunk_text` was missing
  `paragraphs = text.split("\n\n")` — the variable was referenced but never defined.
  Fixed by the subagent writing the tests.

### Files Changed

```
app/tests/CODEBASE_RULES.md          ← populated from stub (11 sections)
app/tests/test_architecture.py       ← added 2 enforcement tests + helpers
pyproject.toml                       ← doctest enabled, testpaths expanded, 80% gate removed
docs-depo/setup.md                   ← updated with 3-tier test instructions

Doctests added to: tools/charts/_shared.py, bar.py, pie.py, scatter.py, line.py,
  heatmap.py, histogram.py, boxplot.py, radar.py, overlaid_bar.py
  tools/costing/distance.py, tools/engineering/compliance.py,
  tools/risks/parser.py, tools/documents/reader.py, excel.py, ingest.py

Pytest tests added:
  auth/tests/test_routes.py
  chat/tests/test_agent.py, test_routes.py
  connectors/tests/test_local_files.py
  storage/tests/test_connection.py, test_runner.py
  demo/tests/test_routes.py
  tools/weather/tests/test_forecast.py, test_historical.py
  tools/news/tests/test_search.py
  tools/documents/tests/test_reader.py, test_search.py
  tools/risks/tests/test_parser.py

Bug fix: tools/documents/reader.py (_chunk_text missing paragraphs assignment)
```

### Why Delete After Merge

This file documents the conversation and design process — useful context during review,
not needed in the permanent codebase. The permanent docs (`CODEBASE_RULES.md`,
`docs-depo/setup.md`, `plans/development-rules-and-test-suite.md`) cover the what and
how. This covers the why and the journey.

---

**DELETE THIS FILE AFTER `feat/development-rules-and-test-suite` MERGES TO MASTER.**