# demo-data

Frozen copies of external specification and requirements documents, kept here for reference and demos. Original binaries live under each project's `raw/` subfolder; markdown transcriptions live beside them.

Current contents:

- `craft-requirements/` — the CSA CRAFT UMR, requirements/architecture document (V3), WFS GDIR (EN + FR), HAWC glossary, and the Building-CSA-AI-Capability briefing. The source-of-truth binaries are under `craft-requirements/raw/`; the `*.md` files alongside them are text transcriptions produced for retrieval.

**Not for runtime consumption.** The webapp's connector points at `~/Documents` via `CONNECTORS_ROOT` — not at this folder. Live mission data lives under `data/cadre-missions/` at the repo root.
