# 00 — Refactor overview

**Status:** planned · execute plans 01–14 in order · one commit per plan

## Why

Two parallel problems to solve in one refactor pass:

1. **Demo-shaped code leaked into the webapp** during a prior "boot the demo" pass — hardcoded `demo:admin` user, `./data` default for `CONNECTORS_ROOT`, silent echo fallback in the chat provider when Azure creds are missing. All of that belongs in config or a seeder, not in `.py` files.
2. **The code has drifted from its own pitch document.** Pitch names LangGraph but code uses `pydantic-ai`; pitch promises hash-chained append-only JSONL audit but code writes plain JSONL; pitch names five protocols but only four are formalised. Several tool slots the pitch calls "reserved" don't exist as reservations — they're gaps.

Goal of this refactor: align to the pitch, delete the demo garbage, bring the project to professional-dev structure (installable package, Makefile, factory pattern, declarative config), and shrink the dependency surface. One PR against `master`.

## Agent-runtime decision (locked)

- **Azure OpenAI SDK direct.** No LangChain, no LangGraph, no `pydantic-ai`, no `environs`, no `pydantic-settings`. Zero pydantic in the install.
- A ~250-line ReAct loop in `chat/agent.py` on top of `openai.AsyncAzureOpenAI` covers one primary agent + ~10 tools (pitch scope).
- HITL via a SQLite `approvals` table + resume route (same mechanics the pitch wants from a Postgres queue at end state).
- Protocols stay (`⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ ChatProvider`, `⟨I⟩ WorkspaceStore`, `⟨I⟩ AgentActionLog`) so a different runtime can slot in later without touching routes/audit/data.

## Env naming conventions

- App-level vars use plain conventional names: `SECRET_KEY`, `PORT`, `HOST`, `DEBUG`, `DATABASE_URL`, `LOG_DIR`.
- Service-specific vars keep the service prefix: `AZURE_OPENAI_*`.
- **No product prefix** (`CHEDDAR_*`) anywhere.
- Every required var raises at startup when missing. No silent defaults for identity, secrets, or paths.

## Plan order

| # | Plan | Depends on | One-line |
|---|---|---|---|
| 01 | `01-config-stdlib-dotenv.md` | — | typed `settings` object; stdlib + `python-dotenv`; delete every other `os.environ.get` |
| 02 | `02-app-factory.md` | 01 | `create_app()` factory; thin `app.py` |
| 03 | `03-agent-azure-sdk.md` | 01, 02 | drop `pydantic-ai`; ~250-line ReAct loop on Azure OpenAI SDK |
| 04 | `04-audit-hash-chained.md` | 01, 03 | formalise `AgentActionLog`; hash-chained append-only JSONL |
| 05 | `05-users-seeder.md` | 01 | delete `DEFAULT_USERS`; `scripts/seed.py` writes SQLite |
| 06 | `06-permissions-declarative.md` | 01 | `permissions.json`; de-dupe role levels |
| 07 | `07-data-sources-registry.md` | 01, 06 | `data_sources.json`; registry for SharePoint/SAP/AI Search slots |
| 08 | `08-delete-weather-news.md` | 03, 07 | delete demo tools; reserve pitch tool slots as `NotImplementedError` stubs |
| 09 | `09-packaging-makefile.md` | 01–08 | `[project]` + hatchling + Makefile |
| 10 | `10-debug-routes-gated.md` | 01, 06 | gate `/debug/*` on `ENABLE_DEBUG_ROUTES` |
| 11 | `11-docs-cleanup.md` | 08 | root README + CONTRIBUTING + folder READMEs; delete stale docs |
| 12 | `12-test-guardrails.md` | 01–11 | config / permissions / audit / imports guardrails + route×role matrix |
| 13 | `13-hitl-skeleton.md` | 03, 04, 06 | SQLite approval queue + resume routes; UI reserved |
| 14 | `14-dead-code-sweep.md` | all above | delete symbols with zero callers |

Each plan file is standalone — a reader following it does not need to open another plan to execute. Shared decisions (env schema, dependency list, agent-runtime choice) are repeated in the plans that need them, intentionally.

## Final dependency list after this refactor

**Runtime:** `dash`, `flask`, `flask-login`, `openai`, `pandas`, `plotly`, `python-dotenv`, `requests`, `werkzeug`, `msal`, `pdfplumber`, `python-docx`

**Dev:** `ruff`, `pyright`, `bandit`, `pip-audit`, `detect-secrets`, `pytest`, `pytest-cov`, `pre-commit`

**Build:** `hatchling`

**Removed:** `pydantic-ai`, `pydantic-ai[openai]`, any transitive pydantic (nothing in the install pulls it anymore).

## Verification across the whole refactor

Once plans 01–14 are shipped:

- `grep -rE "os\.environ|os\.getenv" --include='*.py'` → only `app/core/config.py`.
- `grep -rE "^import pydantic\|^from pydantic " --include='*.py'` → zero.
- `grep -rn "pydantic_ai\|pydantic-ai\|langchain\|langgraph" --include='*.py'` → zero.
- `pip list | grep -iE "pydantic|langchain|langgraph"` → zero.
- `grep -rE "DEFAULT_USERS|CHE-DSV4P|cheddar-internal-dev|cheddar-dev-secret-key"` → zero.
- `grep -rEi "weather|open.?meteo|guardian|cohere|rerank|montreal"` → zero outside `.git/`.
- `grep -rE '\\bCHEDDAR_[A-Z_]+'` → zero.
- `make help` lists every verb.
- `make check` passes on a scratch clone.

---

## Reasoning / justification extracts

**User instructions driving this refactor:**
- "I want the refactor to be true to this" (CRAFT pitch, attached).
- "ideally llanggraph is our agent harness and runtime as a mature solution but suggest something else if that's senseless when it comes to actually coding it".
- "if there's an azure solution we should try and use it to reduce dependency surface area and code simplicity".
- "we also only have local sql and no external data connectors for now but make sure to keep abstractions so it can be added later".
- "no hardcoding anything though clean that up I think that's going to cause a lot of cleanup issues later".
- "we are using good developer practices like abstract var names in the env, and proper routes".
- "don't prefix stuff with CHEDDAR, make it real dev names".
- "break plans into smaller plans, pull from head of repo and put plans in dedicated plan folders".

**Why Azure OpenAI SDK beats LangGraph for this scope:**
LangChain pulls `pydantic` as a hard transitive dep; at ~1 primary agent + 10 tools the framework is net overhead. The SDK gives us tool-calling, streaming, structured outputs, and a Content Safety hook direct. HITL interrupt and checkpointing fit in ~50 extra lines against our existing SQLite store. Deployment surface is identical.

**Pitch commitments honoured in this refactor:**
- `⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ ChatProvider`, `⟨I⟩ WorkspaceStore`, `⟨I⟩ AgentActionLog` protocols (§4 Design Decisions, Protocol contracts row).
- Hash-chained append-only JSONL audit (§5 Immutable audit row; §4 Audit sink).
- Route-gated RBAC with `base(1) < power(2) < admin(3)` escalation (§1 Containers, item 2).
- Bounded ReAct recursion (`recursion_limit=25`) (§6 Requirements Traceability, Primary agent row).
- `AgentAction` envelope with trace_id, agent_id, step, confidence, citations (§2 Internals, Panel A).
- Guardrail hook point in tool wrapper (§5 Guardrails + sandbox row).

**Reserved slots (not implemented in this refactor; abstractions ready):**
- Azure AI Search / hybrid retrieval — `⟨I⟩ DataSource` registry.
- SharePoint / SAP / STK / MATLAB — `⟨I⟩ DataSource` registry.
- Entra ID + MSAL — `⟨I⟩ AuthProvider`.
- Azure Content Safety — guardrail hook in tool wrapper.
- Azure Container Apps sandbox — `CodeExecTool` reserved stub.
- Postgres HITL queue — swap behind the SQLite `ApprovalQueue` class.
- Azure Log Analytics — forward JSONL from `HashChainedJsonlLog` at deploy time.

**Research informing the structure (not needed to execute, kept for the record):**
- Flask application factory pattern — [Flask best practices](https://tessl.io/registry/tessl-labs/flask-best-practices), [Plotly community](https://community.plotly.com/t/recommended-project-structure-mvc-pattern/27868).
- Feature-sliced layered architecture — [Pythonworld — top-tech codebase structure](https://medium.com/the-pythonworld/how-top-tech-companies-structure-their-python-codebases-a71f812e614f).
- 12-factor config — [FastAPI settings guide](https://fastapi.tiangolo.com/advanced/settings/).
