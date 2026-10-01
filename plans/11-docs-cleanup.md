# 11 — Docs cleanup (folder explainers only, no onboarding)

**Status:** planned · depends on `08-delete-weather-news.md`

## Why

User rule: **remove onboarding docs; keep only folder explainers**. A folder explainer is one short paragraph (plus a bullet list of files) that says what belongs in the folder. Not "how to install". Not "how to run". Not "how to contribute". Not "where to look next".

Current state on this branch after merging master:
- Root `README.md` is stale (describes a FastAPI backend that doesn't exist).
- `docs-depo/setup.md` is an onboarding doc (install, run, test, pre-commit).
- Feature folders already have folder-explainer READMEs on master: `storage/README.md`, `tools/README.md`, `tools/charts/README.md`, `tools/documents/README.md`, `tools/news/README.md`, `tools/weather/README.md`.
- Missing folder explainers: `auth/`, `chat/`, `connectors/`, `app/`, `app/core/`, `app/database/`, `storage/database/` (last two may already exist on master — audit when executing).

This plan deletes everything onboarding and ensures every live folder has an explainer, nothing more.

## Scope

**In**
- Delete the stale root `README.md`.
- Delete `docs-depo/setup.md` (onboarding).
- Delete `tools/weather/README.md` and `tools/news/README.md` (orphans after plan 08).
- Add folder-explainer READMEs for `auth/`, `chat/`, `connectors/`, and any other feature folder missing one after audit.
- Add folder-explainer READMEs for the five reserved tool stubs from plan 08 (`tools/classifier/README.md` etc.).
- Spot-check existing `docs-depo/*.md` and feature-folder READMEs for stale terms (`pydantic-ai`, `LangGraph` as prescribed choice, weather / news tools, Montreal, `user1`/`user2`).

**Out**
- `README.md` at the root. Not re-created.
- `CONTRIBUTING.md`.
- Any `CLAUDE.md`, `AGENTS.md`, `.cursorrules`-style agent-instruction file.
- Setup / install docs in any form.
- Architecture overview (pitch PDF in `docs-depo/pitch/` is the source of truth).

## Folder-explainer template

Max ~15 lines. Pattern:

```markdown
# <folder-name>

<One sentence saying what the folder contains and what it is for.>

Files:
- `foo.py` — <one line>
- `bar.py` — <one line>
- `tests/` — <one line>
```

No "how to run", no "requirements", no "example commands". If the reader needs to run something to understand the folder, that is a sign the folder is doing too much, not that the README is too short.

## Files touched

- **Delete**
  - `README.md` (root).
  - `docs-depo/setup.md`.
  - `tools/weather/README.md`.
  - `tools/news/README.md`.
- **New** (folder explainers)
  - `auth/README.md`.
  - `chat/README.md`.
  - `connectors/README.md`.
  - `app/README.md` (if missing on master).
  - `app/core/README.md` (if missing).
  - `app/database/README.md` (if missing).
  - `scripts/README.md` (after plan 05 adds `scripts/`).
  - `tools/classifier/README.md`, `tools/historical_mission/README.md`, `tools/cost_aggregator/README.md`, `tools/vendor_aggregator/README.md`, `tools/code_exec/README.md` (reserved stubs from plan 08).
- **Spot-check / patch**
  - `docs-depo/README.md` — remove the `setup.md` bullet.
  - `docs-depo/exploration/*.md` — grep for stale terms.
  - Any existing feature-folder README on master that mentions weather / news / `pydantic-ai`.

## Workflow

**Pre-check**
- Plan 08 shipped (weather / news folders deleted; reserved tool folders created).
- Plan 05 shipped (`scripts/` exists).

**Do**
1. `git rm README.md docs-depo/setup.md tools/weather/README.md tools/news/README.md` (last two if plan 08 didn't already remove them with the folder).
2. For every folder in the "New" list, write a folder-explainer README following the template above.
3. Update `docs-depo/README.md`: remove the `setup.md` bullet; keep `pitch/`, `demo-data/`, `exploration/` bullets.
4. Grep audit: `grep -rEi "weather|open.?meteo|guardian|cohere|rerank|montreal|pydantic.ai|user1|user2" --include='*.md'` — patch or delete the offending paragraph in any match.

**Verify**
- `find . -name README.md -not -path './.git/*'` returns **only** folder-explainer READMEs — no root `README.md`, no onboarding `setup.md`.
- `grep -rEi "install|how to run|getting started|quickstart|make install|pip install" --include='*.md' .` returns zero outside git history.
- Every live top-level folder has exactly one `README.md` of the folder-explainer shape.
- `grep -rEi "pydantic.ai|user1|user2|montreal" --include='*.md'` returns zero.

**Commit**
`docs: folder explainers only; delete root README and onboarding`

**Rollback**
`git restore -SW .` (then re-check `git status` for new files to remove manually)

## Verification checklist

- [ ] Root `README.md` is gone.
- [ ] `docs-depo/setup.md` is gone.
- [ ] No file contains "install" / "quickstart" / "getting started" sections.
- [ ] Every feature folder has a folder-explainer `README.md`.
- [ ] No stale terms in any `*.md` outside git history.
- [ ] No `CLAUDE.md` / `AGENTS.md` / `.cursorrules` added.

## Out of scope

- Writing a current `README.md` at the root. Explicitly not re-created.
- `CONTRIBUTING.md`.
- Any onboarding or quickstart artefact.

---

## Reasoning / justification extracts

**User instructions:**
- "dont add a current readme remove all readme's unless just explaining what a folder is".
- "remove onboarding docs".
- "I dont want agent instructions".

**Why no root README:**
A root `README.md` is where onboarding naturally accretes ("install", "run", "quickstart", "architecture overview"). The user has explicitly ruled that content out. Deleting the root README removes the gravitational pull toward onboarding content; folder explainers alone give readers (humans and agents) a map of what exists without inviting bitrot.

**Why folder explainers:**
A short, factual "this folder contains X" scales. Each explainer is the stable description of the folder's purpose; it does not go stale when install commands or dev loops change.

**Pitch alignment:**
Pitch has no onboarding section — it describes the architecture, requirements, and blockages. Folder explainers mirror that posture: facts about the system, not instructions to run it.
