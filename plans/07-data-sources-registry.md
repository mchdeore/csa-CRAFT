# 07 — Data sources: declarative registry

**Status:** planned · depends on `01-config-stdlib-dotenv.md`, `06-permissions-declarative.md`

## Why

`app/core/services.py` currently hardcodes a single data source:

```python
data_sources: dict[str, DataSource] = {"local_documents": LocalFileSource(CONNECTORS_ROOT)}
```

That is the only call site; adding another connector means editing Python. Pitch §1 names `DataSource Registry ⟨I⟩ DataSource` with LocalFile live and SharePoint / SAP / STK / MATLAB / Vector-index as reserved slots. Pitch's "cutover is a config change, not a rewrite" (§5 Solving the Problems) means the registry needs to be a config file.

User instruction: *"we also only have local sql and no external data connectors for now but make sure to keep abstractions so it can be added later"*. This plan builds the abstraction.

## Scope

**In**
- `app/core/data_sources.json` — declarative list of sources.
- A `kind` registry in `app/core/services.py` mapping `kind` → class (today only `local_files` → `LocalFileSource`).
- Loop over the config to build `data_sources: dict[str, DataSource]`.
- Variable substitution for `${CONNECTORS_ROOT}` (and future vars like `${SHAREPOINT_URL}`).

**Out**
- SharePoint / SAP / STK / MATLAB / AI Search implementations (reserved; cutover later).
- Hot-reload of the JSON without restart.

## File shape

```json
// app/core/data_sources.json
[
  {
    "name": "local_documents",
    "kind": "local_files",
    "root": "${CONNECTORS_ROOT}"
  }
]
```

Future rows (not shipped in this plan; shape documented so later plans copy):
```json
{"name": "mission_corpus_sharepoint", "kind": "sharepoint", "site_url": "${SHAREPOINT_URL}", "library": "Documents"}
{"name": "sap_vendor_lines",          "kind": "sap",        "base_url": "${SAP_URL}", "oauth_scope": "..."}
{"name": "retrieval_index",           "kind": "azure_ai_search", "endpoint": "${AZURE_SEARCH_ENDPOINT}", "index_name": "craft-rag"}
```

## Protocol (unchanged)

`connectors/protocols.py` already defines `⟨I⟩ DataSource` with `search(query)`, `list_files()`, `read_file(path)`. New kinds satisfy the same interface.

## Loader + registry

```python
# app/core/data_sources.py (new tiny module)
from __future__ import annotations
import json, re
from app.core.config import settings
from connectors.local_files import LocalFileSource
from connectors.protocols import DataSource

_KIND_REGISTRY: dict[str, type[DataSource]] = {
    "local_files": LocalFileSource,
    # future: "sharepoint": SharePointSource, "sap": SAPSource, "azure_ai_search": AzureAISearchSource, ...
}

_VAR_PATTERN = re.compile(r"\$\{([A-Z_][A-Z0-9_]*)\}")

def _subst(value):
    if not isinstance(value, str):
        return value
    def repl(m):
        name = m.group(1)
        return str(getattr(settings, name, ""))
    return _VAR_PATTERN.sub(repl, value)

def load_data_sources() -> dict[str, DataSource]:
    rows = json.loads(settings.DATA_SOURCES_FILE.read_text())
    out: dict[str, DataSource] = {}
    for row in rows:
        kind = row["kind"]
        if kind not in _KIND_REGISTRY:
            raise RuntimeError(f"unknown data-source kind: {kind}; known: {sorted(_KIND_REGISTRY)}")
        cls = _KIND_REGISTRY[kind]
        kwargs = {k: _subst(v) for k, v in row.items() if k not in ("name", "kind")}
        out[row["name"]] = cls(**kwargs)
    return out
```

Then `app/core/services.py` replaces the hardcoded dict with `data_sources = load_data_sources()`.

## Files touched

- **New**
  - `app/core/data_sources.json`.
  - `app/core/data_sources.py` — loader + kind registry.
- **Edit**
  - `app/core/services.py` — swap the hardcoded dict for `load_data_sources()`.
  - `connectors/local_files.LocalFileSource.__init__` — accept `root: str | Path`, coerce to `Path` (so JSON strings work).
- **Delete**
  - Any import of `CONNECTORS_ROOT` from `app/core/config.py` that was only there to construct `LocalFileSource(CONNECTORS_ROOT)` — the loader does the substitution.

## Workflow

**Pre-check**
- Plan 01 shipped; `settings.CONNECTORS_ROOT` and `settings.DATA_SOURCES_FILE` resolve.
- Plan 06 shipped (unrelated but ships the "declarative-config" pattern this plan reuses).

**Do**
1. Add `app/core/data_sources.json` with the single `local_documents` row.
2. Write `app/core/data_sources.py` as above.
3. Rewire `app/core/services.py` to call `load_data_sources()`.
4. Ensure `LocalFileSource.__init__` accepts a `str` and coerces to `Path`.
5. Add two tests in `app/tests/test_data_sources.py`:
   - Loading the default JSON returns a dict with one entry whose source is a `LocalFileSource` pointing at `settings.CONNECTORS_ROOT`.
   - Loading a JSON with an unknown `kind` raises `RuntimeError` and names the valid kinds.

**Verify**
- `python -c "from app.core.data_sources import load_data_sources; print(load_data_sources())"` prints `{"local_documents": <LocalFileSource ...>}`.
- Document search tool (via chat or direct `/tools/execute`) still returns hits over `data/cadre-missions/`.
- Adding a second row with `kind: "local_files"` and a different `root` adds a second source; `document_search_tool` lists both.

**Commit**
`refactor(connectors): declarative data-source registry`

**Rollback**
`git restore -SW app/core/ connectors/`

## Verification checklist

- [ ] `app/core/services.py` builds `data_sources` from the JSON, not a literal.
- [ ] Unknown `kind` raises with the valid-kind list.
- [ ] `${CONNECTORS_ROOT}` substitution works.
- [ ] Document search still returns hits.
- [ ] Loader test covers "unknown kind" error path.

## Out of scope

- Implementing SharePoint / SAP / AI Search sources.
- Per-source RBAC (pitch staged).
- Hot-reload of the JSON.
- A validation schema for the JSON file (future, if the shape grows).

---

## Reasoning / justification extracts

**User instruction:**
- "we also only have local sql and no external data connectors for now but make sure to keep abstractions so it can be added later".

**Pitch commitments honoured:**
- "DataSource Registry ⟨I⟩ DataSource — LocalFile — filesystem (live) · SharePoint — Graph API [LocalFile mirror] · SAP — REST/OData [CSV fixtures] · STK/MATLAB — adapter [reserved] · Vector index — AI Search [LocalFile hybrid]" (§1 Containers, item 4).
- "concrete backend is swappable per-request" (§2 Internals, Panel C).
- "Same ⟨I⟩ DataSource call site; cutover is config" (§4 Design Decisions, Retrieval row).

**Why a JSON file over an env var JSON blob:**
- Readable in a PR, lintable as JSON, diffable.
- Multiple-source config is awkward in a single env var.
- `settings.DATA_SOURCES_FILE` still lets the path be overridden per deployment.

**Why not pydantic for schema validation:**
Zero pydantic rule from the overview plan. The loader's "unknown kind" error is the only validation we need today; add JSON Schema with a tiny validator later if the config shape grows.
