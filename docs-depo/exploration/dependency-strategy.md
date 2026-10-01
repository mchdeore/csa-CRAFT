# Dependency strategy — minimal surface, pitch-aligned, Azure-ready

Why CRAFT's dependency list is deliberately short, what the current set lets us ship today, and what we can grow into without rewrites.

Companion to `azure-openai-sdk-usage.md`. Informs plan `00-refactor-overview.md`.

---

## Dependency surface after the refactor

Only runtime deps. Dev tooling (ruff / pyright / pytest etc.) kept separate.

| Package | Role | Why we need it |
|---|---|---|
| `dash` | Web UI framework | Chat UI, workspace sidebar, chart rendering. Built on Flask. |
| `flask` | HTTP routing | Routes, before/after request hooks, session management. |
| `flask-login` | Session auth | Login / logout flow against our `⟨I⟩ AuthProvider`. |
| `openai` | Azure OpenAI SDK | Only LLM transport. Chat completions, tool calling, structured output, streaming. |
| `pandas` | Tabular data | Spreadsheet upload tool, chart data munging. |
| `plotly` | Interactive charts | What Dash renders for all chart tools. |
| `python-dotenv` | `.env` loading | Loads env into `os.environ` for `app/core/config.py`. |
| `requests` | HTTP client | Any outbound non-LLM calls (document fetchers, future connectors). |
| `werkzeug` | WSGI helpers + password hashing | Pulled in by Flask; we also use `generate_password_hash` / `check_password_hash`. |
| `msal` | Microsoft identity SDK | Reserved for Entra ID cutover; stays as a dep because the stub `⟨I⟩ AuthProvider` can honour MSAL-shaped tokens in tests. |
| `pdfplumber` | PDF parsing | `TextAnalysisTool` reads mission PDFs. |
| `python-docx` | DOCX parsing | `TextAnalysisTool` reads CADRe parts. |

That's **12 runtime packages**. Compare to a LangChain-based alternative which, at minimum, would add `langchain`, `langchain-core`, `langchain-openai`, `langgraph`, `pydantic`, `pydantic-core`, `langsmith` (transitive), and a handful of smaller helpers — ~20 extra packages for the same capability.

---

## What this surface lets us solve today

Every row in pitch §5 "Solving the Problems — Today and at End State" that is marked **live** or **today** is reachable with the deps above. No gaps.

| Problem (requirement) | How these deps solve it today |
|---|---|
| Cited retrieval (UMR-002/005/006, ARR-002/003) | `pdfplumber` + `python-docx` extract the corpus; our `LocalFileSource` serves it; `DocumentSearchTool` returns provenance (file / page / section). No LangChain needed. |
| RBAC + data scope (UMR-012/017/058) | `flask-login` sessions + our declarative `permissions.json` + SQLite `users` + `QueryTool.set_user`. |
| Immutable audit (UMR-015/027/045) | Stdlib `hashlib` + `fcntl` lock → `HashChainedJsonlLog` on disk. Nothing exotic. |
| LLM-based reasoning + tool calling (UMR-001/011/013) | `openai` SDK's native `tools=` + `tool_calls` fields. We write a ~250-line ReAct loop around them. |
| Workspace + session (UMR-014/092/095) | `storage.store.SqliteStore` + `SqliteDataStore` — all stdlib `sqlite3`. |
| Interactive charts | `plotly` figures returned from each chart tool, rendered in `dash`. |
| Bilingual Q&A (UMR-001/046/048) | The underlying LLM handles EN/FR; nothing extra on our side today. |
| Dev invariants (pitch §8) | `ruff`, `pyright`, `pytest`, `bandit`, `pip-audit`, `detect-secrets` all in dev extras. |

**What this means operationally.** On the day the refactor ships, a user can log in with a seeded admin account, upload a CADRe part, ask "what are the top risks in this document?", get a cited answer with a chart of severity counts, and have the entire turn written to a hash-chained append-only JSONL audit log. Everything else in the pitch is a swap behind an existing protocol — not a new dependency.

---

## What more development adds, without expanding the dep surface meaningfully

For each pitch end-state row, how we land it without touching the core deps.

### Capability deltas we can ship with no new deps

| Capability | How we add it with current deps |
|---|---|
| HITL approval queue + routes | Plan 13: SQLite `approvals` table + `AgentPaused` + resume route. Nothing new. |
| Content Safety hook wiring | Azure OpenAI already includes `content_filter_results` on responses when Content Safety is enabled on the deployment. Our `GUARDRAIL_HOOK` call site reads it. No new SDK. |
| Confidence scoring + grounding loop | Prompt engineering + a second LLM call via the same `openai` client. A new `GroundingTool` class on `⟨I⟩ Tool`. |
| Bilingual report templating | Pure Python strings + Jinja (optional add). Report content is already LLM-generated. |
| REST interoperability (UMR-055) | Already live — our Flask routes are the contract. Add OpenAPI docs via `flask-smorest` (optional add) only when consumers show up. |

### Capabilities that need **one new, targeted dep** each

| Capability | Dep | Why it earns a slot |
|---|---|---|
| Azure AI Search cutover | `azure-search-documents` | Pitch §4 Retrieval row. One new class in `connectors/azure_ai_search.py` satisfying `⟨I⟩ DataSource`; one line in `data_sources.json`. |
| SharePoint connector | `msgraph-sdk` or `office365-rest-python-client` | Pitch §4 External data. One new `⟨I⟩ DataSource` class; MSAL already present for auth. |
| SAP OData connector | `pyrfc` or plain `requests` + XML parser | Pitch §4 External data. If `requests` is enough, no new dep at all. |
| Entra ID identity | `msal` already here | Replace the `InMemoryAuth` body; same `⟨I⟩ AuthProvider` contract. |
| Content Safety as a separate wrapper (not inline on the deployment) | `azure-ai-contentsafety` | Only if we want standalone content-safety SDKs beyond what Azure OpenAI returns inline. Usually not necessary. |
| STK adapter | STK's Python API | Only if that use case lands. Local wrapper in `connectors/stk.py`. |
| Code-exec sandbox | Azure Container Apps SDK or `docker` | Pitch §4 Guardrails + sandbox. One class satisfying `⟨I⟩ Tool`. |
| Log Analytics forwarding | `azure-monitor-opentelemetry` or `azure-monitor-ingestion` | Pitch §4 Audit sink. A sidecar forwarder reads the same JSONL — not even code in this repo. |
| Postgres HITL cutover | `psycopg[binary]` | Pitch §4 HITL queue. Swap the SQLite `ApprovalQueue` class; same shape. |

### Capabilities that would justify a framework (and when)

Reproduced from `azure-openai-sdk-usage.md` for completeness. These are the only triggers that would make LangChain / LangGraph worth adding back:

- ≥ 3 specialist agents coordinating under a planner (multi-agent orchestration).
- Dynamic tool composition from user input (tools built at runtime).
- A hybrid-retrieval chain with self-correction loops that grows past ~400 lines.
- A requirement that needs streaming per-node graph events to the UI.
- LangSmith tracing becomes a procurement line.

Until then: Azure SDK direct keeps the dep tree small, the code visible, and the pitch's protocol seams honest.

---

## Guardrails against dep creep

Baked into the test suite (plan 12):

- `test_imports.py` fails if `pydantic`, `pydantic_ai`, `langchain`, or `langgraph` ever appear in `importlib.metadata.distributions()` or in our source `import` lines.
- `test_rules.py` fails if `os.environ`/`os.getenv` appears outside `app/core/config.py`.
- `pre-commit` runs `pip-audit` so any new dep's CVEs surface on the commit that introduces them.
- `pyproject.toml`'s `dependencies` is the single source of truth; `app/requirements.txt` is derived.

Adding a dep is a code review conversation, not an accident.

---

## Why this matters for CRAFT specifically

CRAFT lives in a PBMM / Azure-consolidated end-state. In that environment, every added package is:

- a procurement check (CVE + license),
- a line on the dependency-audit report,
- a maintenance commitment for the lifetime of the system.

Shipping with 12 runtime packages instead of 30 is not an aesthetic choice — it is the difference between a dependency-audit PR that passes in a week and one that stalls for a quarter. The architecture choices (protocol seams for `⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ AuthProvider`, `⟨I⟩ ChatProvider`, `⟨I⟩ AgentActionLog`) mean each Azure cutover above adds one well-scoped package, not a tree of transitive deps.

The ambition at end state is still the full pitch surface — AI Search, Entra, Log Analytics, APIM, Content Safety, Container Apps. The dependency strategy says we get there one targeted swap at a time, with a known cost per step, behind contracts that already exist.

---

## References

- Pitch §4 Design Decisions (component / end-state / current alternative table).
- Pitch §5 Solving the Problems — Today and at End State.
- Pitch §7 Blockages (End State / Current Alternative).
- `docs-depo/exploration/azure-openai-sdk-usage.md` — companion doc on the agent runtime choice.
- `plans/00-refactor-overview.md` — the refactor these notes justify.
