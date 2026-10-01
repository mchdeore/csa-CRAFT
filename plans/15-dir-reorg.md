# 15 — Directory reorganisation: `dev-docs-depo` + consolidated non-app folders

**Status:** planned · last structural change before guardrails (12) · runs after plans 01–11, before 12 and 14

## Why

Too many top-level folders carrying developer-facing material. Current layout at the repo root:

```
app/  auth/  chat/  connectors/  storage/  tools/     ← webapp (keep as-is)
data/                                                   ← runtime data (cadre-missions)
docs-depo/                                              ← dev docs (pitch + demo-data + exploration + setup.md)
plans/                                                  ← refactor plans
```

The `data/` and `plans/` folders sit at root alongside the webapp code, making the root busy and ambiguous ("is `data/` consumed by tests? by prod? by docs?"). The user wants everything that isn't shipped application code gathered under one folder, renamed to signal its purpose clearly.

Also: `docs-depo/pitch/` is marked inaccurate (prior user instruction) and should be deleted; `zzz-ptich-docs/` (if any copy remains anywhere) deleted; `docs-depo/setup.md` is onboarding (deleted by plan 11); `rundemo.sh` — confirmed does **not** exist at root on this branch (user mentioned it; verified absent — no action needed, note here for the record).

## Scope

**In**
- Rename `docs-depo/` → `dev-docs-depo/`.
- Delete `dev-docs-depo/pitch/` (the whole folder; pitch material is captured in `plans/00-refactor-overview.md`'s reasoning extracts and in `dev-docs-depo/exploration/*.md`).
- Move `data/` → `dev-docs-depo/data/` (runtime corpus the local-files connector reads).
- Move `plans/` → `dev-docs-depo/plans/` (this directory and this plan file move together).
- Confirm no `zzz-ptich-docs/`, `zzz-pitch-docs/`, or `rundemo.sh` remain anywhere; delete if any pop up.
- Update `.env.example` guidance so `CONNECTORS_ROOT` points at the new path (`dev-docs-depo/data/cadre-missions`).
- Update plan `00-refactor-overview.md` cross-references after move.
- Update plan `11-docs-cleanup.md` to point at `dev-docs-depo/` for the exploration-folder spot-check.

**Out**
- Renaming the application packages (`app/`, `auth/`, `chat/`, etc.) — those stay.
- Carving out a `src/` layout — not now; packaging via hatchling (plan 09) handles the import story.
- Moving `tools/charts/`, `tools/documents/`, etc. — those are application code, not developer material.

## Final root layout

```
app/                              webapp core
auth/  chat/  connectors/
storage/  tools/
scripts/                          seeder CLI (plan 05)
dev-docs-depo/                    everything not shipped
├── README.md                     folder explainer
├── data/
│   └── cadre-missions/           runtime corpus consumed by LocalFileSource
├── demo-data/                    frozen reference docs
├── exploration/                  research + reference notes
└── plans/                        refactor plans (including this one, after move)
app.py                            entry point
pyproject.toml  Makefile  .env.example  .gitignore  etc.
```

## Files touched

- **Rename / move**
  - `docs-depo/` → `dev-docs-depo/` (whole tree).
  - `data/` → `dev-docs-depo/data/`.
  - `plans/` → `dev-docs-depo/plans/` (this plan file moves with the folder).
- **Delete**
  - `dev-docs-depo/pitch/` (after the rename; whole folder).
  - `dev-docs-depo/setup.md` — plan 11 already removes it; if it survived into this step, delete here too.
  - Any stray `zzz-*pitch*` or `rundemo*` hits.
- **Edit**
  - `dev-docs-depo/README.md` — list the four subfolders (`data/`, `demo-data/`, `exploration/`, `plans/`) and strike mentions of `pitch/` and `setup.md`.
  - `dev-docs-depo/data/README.md` — update to reflect its new home ("Runtime data the webapp consumes. Was `data/` at the root; moved under `dev-docs-depo/` in plan 15.").
  - `.env.example` — change the `CONNECTORS_ROOT` comment/example to `./dev-docs-depo/data/cadre-missions`.
  - `plans/00-refactor-overview.md` — update cross-references after the move.
  - `plans/11-docs-cleanup.md` — "spot-check `docs-depo/*.md`" → "`dev-docs-depo/*.md`".
  - Any other plan file (01–14) that mentions `docs-depo/` or `plans/` as a current path — rewrite to `dev-docs-depo/...`.
  - `.gitignore` — update any `docs-depo/` or `plans/` paths if present (none at this time; verify).

## Workflow

**Pre-check**
- All of plans 01–11 shipped (so the layout above is otherwise stable).
- `git status` clean.
- `rg -g '!*.md' -l 'docs-depo|zzz-ptich-docs|rundemo' .` to catch any code references outside markdown.

**Do**
1. `git mv docs-depo dev-docs-depo`.
2. `git rm -r dev-docs-depo/pitch`.
3. `git mv data dev-docs-depo/data`.
4. `git mv plans dev-docs-depo/plans`.
5. Edit `dev-docs-depo/README.md` and `dev-docs-depo/data/README.md` as above.
6. Grep for lingering `docs-depo/` strings in `*.md`, `*.py`, `*.toml`, `*.cfg`, `.env.example`, `.gitignore`, `Makefile`, `pre-commit-config.yaml` — rewrite each hit to `dev-docs-depo/`.
7. Grep for `data/cadre-missions` references in `*.md` and `*.env*` — rewrite to `dev-docs-depo/data/cadre-missions`.
8. Verify `rundemo.sh`, `zzz-ptich-docs/`, `zzz-pitch-docs/` are absent anywhere in the tree (`find . -maxdepth 3 -iname "rundemo*" -o -iname "zzz*p*itch*"` returns nothing); if any appear, `git rm` them.

**Verify**
- `ls -1 .` shows only: `app`, `app.py`, `auth`, `chat`, `connectors`, `dev-docs-depo`, `pyproject.toml`, `pyrightconfig.json`, `scripts`, `storage`, `tools`, plus the dotfiles.
- `ls -1 dev-docs-depo/` shows: `README.md`, `data`, `demo-data`, `exploration`, `plans`.
- `ls -1 dev-docs-depo/plans/` contains all plan files (00–16, including this one at the new location).
- `grep -rn "docs-depo" --include='*.md' --include='*.py' --include='*.toml' --include='*.sh'` returns zero hits (any surviving reference is a bug).
- `grep -rn "^CONNECTORS_ROOT=" .env.example` points under `dev-docs-depo/data/cadre-missions`.
- With `.env` updated accordingly, `make dev` still boots and `document_search_tool` returns hits.

**Commit**
`refactor(repo): rename docs-depo → dev-docs-depo; consolidate data/ and plans/ underneath`

**Rollback**
`git reset --hard HEAD~1`

## Verification checklist

- [ ] `docs-depo/` does not exist.
- [ ] `data/` at root does not exist.
- [ ] `plans/` at root does not exist.
- [ ] `dev-docs-depo/pitch/` does not exist.
- [ ] No `zzz*p*itch*` or `rundemo*` files anywhere.
- [ ] `dev-docs-depo/{data,demo-data,exploration,plans}/` all present.
- [ ] `CONNECTORS_ROOT` in `.env.example` points to the new path.
- [ ] No lingering `docs-depo` references in text files.
- [ ] `make dev` boots; doc search over the new path still returns hits.

## Out of scope

- `src/` layout for the webapp.
- Renaming `app/` → `webapp/` or similar.
- Moving `scripts/` under `dev-docs-depo/` (scripts are shipped developer-facing tooling, not dev reference material; they stay at the root).

---

## Reasoning / justification extracts

**User instructions:**
- "i feel like there is too many data folders, i think we can add to the plan to clean it up some more".
- "we should rename docs-depo to dev-docs-depo".
- "delete zzz pitch docs" (not present on this branch; included defensively).
- "put all demo, research, plans and things of that nature in dev-doc-depo".
- "I don't know what the rundemo.sh is doing at the route" — verified absent; noted for record.
- "I don't know what cadre missions is doing out in the open" — moved under `dev-docs-depo/data/`.

**Why rename to `dev-docs-depo`:**
`docs-depo` is ambiguous — reads like "documentation". `dev-docs-depo` signals clearly that the folder holds developer-facing material (plans, research, frozen reference docs, runtime data), not user documentation. Matches the folder's own self-description in its README.

**Why consolidate `data/` and `plans/`:**
Both are developer / project artefacts, not shipped code. Keeping them at the root alongside `app/` / `auth/` / `chat/` suggests they are peers of the webapp packages, which they are not. One parent folder = fewer top-level entries, clearer boundaries.

**Why delete `dev-docs-depo/pitch/`:**
User said earlier: "remove pitch docs they are inaccurate". The pitch PDF's architectural intent is captured where it matters: in `plans/00-refactor-overview.md` (reasoning extracts) and in `dev-docs-depo/exploration/*.md` (SDK usage, dependency strategy). Keeping the PDF around invites drift.

**Why `data/` is not production-sacred:**
`data/cadre-missions/` holds a frozen corpus the local-files connector reads. The connector's root is already env-driven (`CONNECTORS_ROOT`) — moving the physical path is a one-line change in `.env`. Semantics unchanged.

**Pitch alignment:**
Pitch §4 Data sources row — "LocalFileSource — filesystem (live)". Nothing in the pitch mandates the on-disk location of the corpus; it only mandates the `⟨I⟩ DataSource` protocol stay intact. This plan preserves that.
