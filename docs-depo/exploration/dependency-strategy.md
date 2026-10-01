# Dependency strategy — Azure-native, pitch-aligned, trade-off visible

Why CRAFT's dependency list looks the way it does after the Microsoft Agent Framework pivot, what the current set lets us ship today, and what we can grow into without rewrites.

> **This doc records the trade-off we already took, not a decision tree.** The project adopted Microsoft Agent Framework as the primary agent runtime (plan 03). The "when would a framework earn its keep" tables below are therefore retrospective — they show what we gained by taking the trigger, and what the honest cost is. The hand-rolled Azure OpenAI SDK path is kept as a documented fallback (`azure-openai-sdk-usage.md`).

Companion to `azure-openai-sdk-usage.md` (fallback reference). Informs plan `00-refactor-overview.md`.

---

## Dependency surface after the refactor

Only runtime deps. Dev tooling (ruff / pyright / pytest etc.) kept separate.

### Direct runtime deps

| Package | Role | Why we need it |
|---|---|---|
| `dash` | Web UI framework | Chat UI, workspace sidebar, chart rendering. Built on Flask. |
| `flask` | HTTP routing | Routes, before/after request hooks, session management. |
| `flask-login` | Session auth | Login / logout flow against our `⟨I⟩ AuthProvider`. |
| `openai` | OpenAI / Azure OpenAI SDK | Still a direct dep: used by Agent Framework's `agent-framework-openai` provider; also used by the fallback `AzureChatProvider` sketch if we ever drop Agent Framework. |
| `agent-framework` | Microsoft Agent Framework (umbrella) | Primary agent runtime — `ChatAgent`, function-tool decorator, HITL via `approval_mode="always_require"`, workflow `RequestPort`. Successor to Semantic Kernel, GA April 2026. Pulls `agent-framework-core` and `agent-framework-openai` automatically. |
| `agent-framework-foundry` | Microsoft Foundry integration | Added when Foundry (Azure AI Foundry agent runtime) is in-scope. Plan 03 marks this TBD — keep `agent-framework` alone if Foundry isn't exercised in the MVP. |
| `pandas` | Tabular data | Spreadsheet upload tool, chart data munging. |
| `plotly` | Interactive charts | What Dash renders for all chart tools. |
| `python-dotenv` | `.env` loading | Loads env into `os.environ` for `app/core/config.py`. |
| `requests` | HTTP client | Any outbound non-LLM calls (document fetchers, future connectors). |
| `werkzeug` | WSGI helpers + password hashing | Pulled in by Flask; we also use `generate_password_hash` / `check_password_hash`. |
| `msal` | Microsoft identity SDK | Reserved for Entra ID cutover; stays as a dep because the stub `⟨I⟩ AuthProvider` can honour MSAL-shaped tokens in tests. |
| `pdfplumber` | PDF parsing | `TextAnalysisTool` reads mission PDFs. |
| `python-docx` | DOCX parsing | `TextAnalysisTool` reads CADRe parts. |

That's **13–14 direct runtime packages** (14 with `agent-framework-foundry`).

### Transitive deps that come with Agent Framework (acknowledged)

Agent Framework pulls a chunk of the Azure Python surface and `pydantic`:

| Transitive | Why it arrives |
|---|---|
| `pydantic`, `pydantic-core` | Agent Framework's `@tool` decorator uses `typing.Annotated[..., pydantic.Field(description=...)]` for parameter descriptions. Hard dep. |
| `httpx` | Agent Framework's chat clients use `httpx` under the hood. |
| `azure-core` | Shared Azure Python base. |
| Deeper `openai` sub-tree | Agent Framework pins / exercises more of the `openai` SDK than our direct use alone. |

Roughly **5–10 extra packages** in the install footprint on top of the direct list. We tolerate the install; plan 12's `test_imports.py` still forbids direct `import pydantic` in **our** source.

### The honest trade-off

The first iteration of this doc said "**12 runtime packages**, compare to ~20 for a LangChain-based path". Agent Framework pushes us from 12 direct deps + near-zero transitives to **~14 direct + 5–10 transitives**, so the overall install is closer to the LangChain footprint than the hand-rolled SDK path was. In exchange:

- **Microsoft-blessed framework** inside an Azure/PBMM end-state — the procurement and support story is Microsoft-native end-to-end.
- **HITL out of the box** — `approval_mode="always_require"` + `user_input_requests` replaces our 60-line hand roll.
- **Future-proofing** — multi-agent orchestration, `RequestPort` workflow pauses, OpenTelemetry wiring, hosted tools (Code Interpreter, Bing, Azure AI Search, OpenAPI) all available behind the same `ChatAgent` surface. We don't light them up today, but we don't have to migrate frameworks later to get them.
- **Successor-to-Semantic-Kernel** story holds for the audit trail: adopting Agent Framework now avoids an eventual migration **from** Semantic Kernel or an ad-hoc hand roll.

What we gave up: the "zero pydantic in the install" rule, and a measurably smaller lockfile. These were defensible choices against a LangChain adoption; against the Microsoft-native framework at the end state we're explicitly aiming for, they're too strict. The trade is visible so the next person reading this doc sees exactly what moved and why.

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

### Triggers that would have justified a framework (retrospective)

We already took the trigger — these are kept to record the trade, not to drive a future decision. The ones below *would have* pushed us from a hand roll to a framework; adopting Microsoft Agent Framework from day one preempts them all. If any arrives, we extend inside Agent Framework (its own `Workflow`, hosted tools, OpenTelemetry) instead of swapping frameworks:

- ≥ 3 specialist agents coordinating under a planner (multi-agent orchestration) → Agent Framework `Workflow`.
- Dynamic tool composition from user input (tools built at runtime) → Agent Framework `@tool` factory.
- A hybrid-retrieval chain with self-correction loops → Agent Framework hosted retrieval tools + custom `⟨I⟩ DataSource`.
- A requirement that needs streaming per-node graph events to the UI → Agent Framework streaming + `Workflow` events.
- Procurement line for first-party tracing → OpenTelemetry via Agent Framework.

---

## Guardrails against dep creep

Baked into the test suite (plan 12):

- `test_imports.py` fails if `langchain*`, `langgraph`, or `pydantic-ai` appear in `importlib.metadata.distributions()`. It **does not** fail on `pydantic` alone — Agent Framework pulls it transitively and that is the explicit trade (plan 03).
- `test_imports.py` also fails if any of `{pydantic, pydantic_core, pydantic_ai, langchain, langchain_core, langchain_openai, langgraph}` appear as a `from`/`import` line in **our source**. The direct-source rule is stricter than the install rule — we tolerate the transitive, we never reach past Agent Framework into pydantic directly.
- `test_rules.py` fails if `os.environ`/`os.getenv` appears outside `app/core/config.py`.
- `pre-commit` runs `pip-audit` so any new dep's CVEs surface on the commit that introduces them.
- `pyproject.toml`'s `dependencies` is the single source of truth; `app/requirements.txt` is derived.

Adding a direct dep is a code review conversation, not an accident. Agent Framework version bumps may change the transitive set; `pip-audit` + the lockfile diff on the bump PR are the review surface.

---

## Why this matters for CRAFT specifically

CRAFT lives in a PBMM / Azure-consolidated end-state. In that environment, every added package is:

- a procurement check (CVE + license),
- a line on the dependency-audit report,
- a maintenance commitment for the lifetime of the system.

Shipping ~14 direct + ~5–10 transitive runtime packages — anchored by **Microsoft-native** packages (`agent-framework`, `openai`, `msal`, future `azure-*` connectors) — is a dependency-audit shape that reads straight for a Microsoft/Azure procurement reviewer: every direct package is either Microsoft-owned or a well-known OSS staple (`dash`, `flask`, `pandas`, `plotly`, `requests`). The architecture choices (protocol seams for `⟨I⟩ Tool`, `⟨I⟩ DataSource`, `⟨I⟩ AuthProvider`, `⟨I⟩ ChatProvider`, `⟨I⟩ AgentActionLog`) still mean each Azure cutover adds one well-scoped package, not a tree of transitive deps.

The ambition at end state is still the full pitch surface — AI Search, Entra, Log Analytics, APIM, Content Safety, Container Apps. The dependency strategy says we get there one targeted swap at a time, with a known cost per step, behind contracts that already exist, inside a Microsoft-native agent runtime from day one.

---

## References

- Pitch §4 Design Decisions (component / end-state / current alternative table).
- Pitch §5 Solving the Problems — Today and at End State.
- Pitch §7 Blockages (End State / Current Alternative).
- `docs-depo/exploration/azure-openai-sdk-usage.md` — companion doc on the agent runtime choice.
- `plans/00-refactor-overview.md` — the refactor these notes justify.
