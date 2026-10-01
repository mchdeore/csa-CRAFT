# 00 — Refactor overview

**Status:** planned · execute plans 01–14 in order · one commit per plan

## Why

Two parallel problems to solve in one refactor pass:

1. **Demo-shaped code leaked into the webapp** during a prior "boot the demo" pass — hardcoded `demo:admin` user, `./data` default for `CONNECTORS_ROOT`, silent echo fallback in the chat provider when Azure creds are missing. All of that belongs in config or a seeder, not in `.py` files.
2. **The code has drifted from its own pitch document.** Pitch names LangGraph but code uses `pydantic-ai`; pitch promises hash-chained append-only JSONL audit but code writes plain JSONL; pitch names five protocols but only four are formalised. Several tool slots the pitch calls "reserved" don't exist as reservations — they're gaps.

Goal of this refactor: align to the pitch, delete the demo garbage, bring the project to professional-dev structure (installable package, Makefile, factory pattern, declarative config), and shrink the dependency surface. One PR against `master`.

## Agent-runtime decision (locked)

- **Microsoft Agent Framework (`agent-framework`)** is the primary agent runtime, chosen as the Azure-native blessed path (successor to Semantic Kernel, GA April 2026, `1.12.x` as of July 2026). First-class Azure OpenAI integration via `agent-framework-openai`; Microsoft Foundry integration via `agent-framework-foundry` if that layer is in-scope at execution time (plan 03 marks this TBD).
- No LangChain, no LangGraph, no `pydantic-ai`, no `environs`, no `pydantic-settings`. **`pydantic` is permitted as a transitive dep** pulled in by Agent Framework's function-tool decorator (which uses `typing.Annotated[..., pydantic.Field(...)]` for parameter descriptions). The rule softens from "zero pydantic in the install" to **"no direct `import pydantic` in our source"** — plan 12 enforces.
- HITL via Agent Framework's native function-approval primitive (`approval_mode="always_require"` on risky function tools; the agent run returns `user_input_requests` instead of invoking the tool). Persistence + resume stay on our side (SQLite `approvals` table + admin route — plan 13), same mechanics the pitch wants from a Postgres queue at end state.
- Protocols stay (`⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ ChatProvider`, `⟨I⟩ WorkspaceStore`, `⟨I⟩ AgentActionLog`) so a different runtime can slot in later without touching routes/audit/data.
- **Fallback.** The SDK-direct hand roll (`openai.AsyncAzureOpenAI` + ~250-line ReAct loop) is kept as a documented alternate `⟨I⟩ ChatProvider` implementation — see `docs-depo/exploration/azure-openai-sdk-usage.md`. If Agent Framework access is blocked (preview access, licensing, air-gap), one class swap in `app/core/services.py` restores the project without touching routes / audit / data.

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
| 03 | `03-agent-azure-sdk.md` | 01, 02 | drop `pydantic-ai`; adopt Microsoft Agent Framework (`agent-framework`) as the primary agent runtime |
| 04 | `04-audit-hash-chained.md` | 01, 03 | formalise `AgentActionLog`; hash-chained append-only JSONL |
| 05 | `05-users-seeder.md` | 01 | delete `DEFAULT_USERS`; `scripts/seed.py` writes SQLite |
| 06 | `06-permissions-declarative.md` | 01 | `permissions.json`; de-dupe role levels |
| 07 | `07-data-sources-registry.md` | 01, 06 | `data_sources.json`; registry for SharePoint/SAP/AI Search slots |
| 08 | `08-delete-weather-news.md` | 03, 07 | delete demo tools; reserve pitch tool slots as `NotImplementedError` stubs |
| 09 | `09-packaging-makefile.md` | 01–08 | `[project]` + hatchling + Makefile |
| 10 | `10-debug-routes-gated.md` | 01, 06 | gate `/debug/*` on `ENABLE_DEBUG_ROUTES` |
| 11 | `11-docs-cleanup.md` | 08 | delete root README + onboarding; folder-explainer READMEs only |
| 12 | `12-test-guardrails.md` | 01–11 | config / permissions / audit / imports guardrails + route×role matrix |
| 13 | `13-hitl-skeleton.md` | 03, 04, 06 | SQLite approval queue + resume routes; UI reserved |
| 14 | `14-dead-code-sweep.md` | 01–13 | delete symbols with zero callers |
| 15 | `15-dir-reorg.md` | 01–11 | rename `docs-depo` → `dev-docs-depo`; move `data/` and `plans/` under it; delete `pitch/` |
| 16 | `16-test-structure-adoption.md` | 01, 03, 07, 08, 09 | cherry-pick the three-tier test strategy from `feat/development-rules-and-test-suite`; reject what doesn't fit |

Plans 01–14 run strictly in order. Plan 15 (dir reorg) runs after plan 11 and can land before 12/14 — once it ships, every reference to `docs-depo/` in the tree becomes `dev-docs-depo/` and `plans/` moves to `dev-docs-depo/plans/` (including these plan files themselves). Plan 16 (test adoption) is independent of 15 and can run in parallel; its only hard deps are plans 01, 03, 07, 08, 09.

Each plan file is standalone — a reader following it does not need to open another plan to execute. Shared decisions (env schema, dependency list, agent-runtime choice) are repeated in the plans that need them, intentionally.

## Final dependency list after this refactor

**Runtime (direct):** `dash`, `flask`, `flask-login`, `openai`, `pandas`, `plotly`, `python-dotenv`, `requests`, `werkzeug`, `msal`, `pdfplumber`, `python-docx`, `agent-framework` (umbrella — includes `agent-framework-core` and `agent-framework-openai`; `agent-framework-foundry` added separately if Foundry is in-scope — TBD per plan 03).

**Runtime (transitive, acknowledged):** Agent Framework pulls `pydantic`, `pydantic-core`, `httpx`, `azure-core`, and may deepen the `openai` sub-tree — roughly 5–10 extra packages in the install footprint. We tolerate the install; `test_imports.py` still forbids direct `import pydantic` in our source (plan 12).

**Dev:** `ruff`, `pyright`, `bandit`, `pip-audit`, `detect-secrets`, `pytest`, `pytest-cov`, `pre-commit`

**Build:** `hatchling`

**Removed:** `pydantic-ai`, `pydantic-ai[openai]`.

## Verification across the whole refactor

Once plans 01–14 are shipped:

- `grep -rE "os\.environ|os\.getenv" --include='*.py'` → only `app/core/config.py`.
- `grep -rE "^import pydantic\|^from pydantic " --include='*.py'` → zero *in our source* (transitive install via `agent-framework` is allowed).
- `grep -rn "pydantic_ai\|pydantic-ai\|langchain\|langgraph" --include='*.py'` → zero.
- `pip list | grep -iE "langchain|langgraph|pydantic_ai"` → zero. (`pydantic` *is* expected here as a transitive of `agent-framework`.)
- `pip list | grep -iE "^agent-framework"` → non-empty.
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
- "no lets use azure explicitly ... modify plans as if we already have it or just need to install it" — the Agent Framework pivot. We now adopt Microsoft Agent Framework (`agent-framework`) as the primary runtime from day one and treat the SDK-direct hand roll as the documented fallback.
- "we also only have local sql and no external data connectors for now but make sure to keep abstractions so it can be added later".
- "no hardcoding anything though clean that up I think that's going to cause a lot of cleanup issues later".
- "we are using good developer practices like abstract var names in the env, and proper routes".
- "don't prefix stuff with CHEDDAR, make it real dev names".
- "break plans into smaller plans, pull from head of repo and put plans in dedicated plan folders".
- "remove onboarding docs" (plan 11 scope locked to folder explainers only, no README/CONTRIBUTING).
- "i feel like there is too many data folders... rename docs-depo to dev-docs-depo, delete zzz pitch docs, put all demo, research, plans and things of that nature in dev-doc-depo" (plan 15).
- "make another plan to review and implement this branches test structure feat/development-rules-and-test-suite" (plan 16).

**Why Microsoft Agent Framework for this scope:**
`agent-framework` is Microsoft's enterprise agent SDK, successor to Semantic Kernel, with first-class Azure OpenAI and Azure AI Foundry integration. In an Azure/PBMM end-state the "Microsoft-blessed framework" procurement story outweighs the dep-surface cost. We give up the "zero pydantic installed" rule (Agent Framework pulls it as a transitive dep via its `@tool` decorator), gain built-in HITL (`approval_mode="always_require"` + `user_input_requests`), workflow `RequestPort`, and future paths to multi-agent orchestration without an eventual framework migration.

**Why not LangGraph:**
Still net overhead at this scope (one primary agent + ~10 tools), and not Microsoft-native. If multi-agent orchestration ever lands we would use Agent Framework's `Workflow` layer, not LangGraph.

**Why keep the SDK-direct path documented (not deleted):**
If Agent Framework access is blocked (preview access, licensing, air-gap) the hand-rolled ReAct loop on `openai.AsyncAzureOpenAI` is a drop-in alternate `⟨I⟩ ChatProvider` — one class swap in `app/core/services.py`. The fallback reference lives in `docs-depo/exploration/azure-openai-sdk-usage.md`.

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
