# CRAFT Pitch — Design Notes

Companion to `CRAFT-pitch.md` / `CRAFT-pitch.html` / `CRAFT-pitch.pdf` in this folder. The pitch is a proposal of the end-state architecture; this document is the reasoning behind every piece of it — why each section exists, why each diagram is shaped the way it is, why specific technologies were chosen, and what the terminology actually means. Written so another agent (or a human landing cold) can inquire about the proposal and get consistent answers.

Nothing here is read by code. Not onboarding.

---

## 1. What the pitch is and isn't

**Is.** A proposal of the final CRAFT architecture — the containers, their interfaces, the data flow, the role boundaries, the dependencies CRAFT needs from IT / procurement / domain partners.

**Isn't.** A progress report. We don't say "today we use X, tomorrow we'll use Y." The team already understands that where the end-state tech isn't in place yet, we build temporary alternatives. Pitching the alternatives dilutes the proposal.

**Consequence.** Anywhere the pitch names a backend (Postgres, Managed DB behind `⟨I⟩ WorkspaceStore`, Azure AI Search, Azure Log Analytics, Microsoft Agent Framework), that is the committed end-state choice. Temporary alternatives — the local backing stores we build when the real thing isn't accessible yet — are team-known and don't belong in the pitch.

---

## 2. Section-by-section rationale

### §1 "What CRAFT Is"
Opens with one sentence that fixes the reader's model of what we're proposing: an **audited retrieval-augmented AI assistant** for CSA mission engineering and finance. Three load-bearing words:

- *Audited* — every tool call and LLM turn produces an `AgentAction` record. Not best-effort logging; a hash-chained immutable chain.
- *Retrieval-augmented* — answers come from retrieved mission documents, with citations. Not raw LLM knowledge.
- *AI assistant* — not a batch pipeline; an interactive agent that chooses tools.

### §2a — L1 System Context (diagram)
One diagram, actors on the left, four service columns on the right. The columns are the four external concern areas: **LLM & AI** (Azure OpenAI, Agent Framework, Foundry, Content Safety), **Internal Data** (CRAFT's process + the mission corpus on disk), **External Data** (SharePoint, SAP, STK, Azure AI Search), **Ops & Audit** (Log Analytics, App Service, LaunchPad, Container Apps, Entra, APIM).

Internal vs External Data is split visually because they have *different trust and auth characteristics* — internal is in-process, external crosses the perimeter via MSAL/OAuth.

### §2b — L2 Container (diagram)
The core architectural claim. Three horizontal bands:

1. **Two caller shapes** — Primary Agent (internal) and external token-bearing clients (service / cron / pipeline). Both hit the same gate; both get the same audit; both are shaped by role.
2. **Route-Gated RBAC Layer** — the only entry point. `before_request` stamps auth + role + trace_id; `after_request` emits the audit envelope.
3. **Four domain surfaces** — Tool Registry, Storage, Data Sources, Audit Sink. Each sits behind an `⟨I⟩` protocol.

Why two caller shapes get first-class treatment: it's the pitch's answer to "how can CRAFT be used deterministically?" — a cron job with a `base` token can hit `/tools/execute/documents` directly, no agent in the loop, same audit, same RBAC. The agent is the probabilistic path; external services are the deterministic path.

### §2c — L3 Internals (three panels)
L2 shows containers; L3 opens up the ones with internal state machines.

- **Panel A · Agent** — the ReAct loop inside `ChatAgent`. LLM turn → tool-call or respond → HITL check → audit → loop (capped). Shows exactly where `user_input_requests` fires (the framework's HITL primitive).
- **Panel B · Tool & Data-Source Registries** — enumerates the actual tools and data sources behind their respective protocols. Each line reads: `<kind>  <(what it does)>`. INTERNAL vs EXTERNAL data sources repeated here from L1 for completeness.
- **Panel C · Auth** — the `before_request / handler / after_request` sandwich. The RBAC math is a single line: `base(1) < power(2) < admin(3)`.

### §2d — UC State Models
Swim-lane view of the three use cases named in §3. Compressed enough to fit on half a page; the shape of each lane is the same, which is the point — the architecture doesn't change per use case, only the Tool and DataSource behind each step do.

### §3 — Use Cases
Four flows (UC-E2 Risk, UC-F1 Cost, UC-F4 Vendor, UC Bilingual). Each is a short paragraph that names: who the actor is, what retrieval runs, which Tool classes operate on it, which `DataSource` writes land, and the UMR requirements the flow covers.

### §4 — Design Decisions (table)
Columns: **Component / Choice / Why**. Dropped the "Current alternative" column that was in an earlier draft — the pitch is proposal-only (see §1 of this doc). Each row is a bet: *for this component we are choosing X; here is why*. The last two rows (Protocol contracts, Invariants) are the integrity surface — the parts that aren't negotiable.

### §5 — Solving the Problems (table)
Columns: **Problem (requirement) / How the architecture solves it**. One row per architectural concern. Reads top-to-bottom as the full set of things CRAFT has to do.

### §6 — Requirements Traceability (table)
Columns: **Capability / Requirements / Design**. Required by the UMR tabulation ask — every capability lists which UMR / AAR / ASG / HITL / ARR requirement numbers it satisfies, and the design seam that implements it.

### §7 — Dependencies & Blockages (table)
Columns: **Dependency / Owner / Satisfies**. Everything CRAFT depends on that IT, procurement, or a domain partner has to deliver. The owner column makes clear who the ask is directed at; "satisfies" ties each ask back to a capability.

### §8 — System-Health Tooling (table)
Columns: **Tool / Role**. The invariant layer — ruff / pyright / pytest / doctest / architecture tests / bandit / pip-audit / detect-secrets. Industry-standard; runs on every commit; new invariant = new test, not new infra.

---

## 3. Terminology — the words the pitch uses, and what they mean

### Storage vs Data Sources (the question that prompted this doc)

| Concept | What it is | Protocol | End-state backing |
|---|---|---|---|
| **Storage** | CRAFT's own operational state. Where CRAFT puts things *it owns*. | `⟨I⟩ WorkspaceStore`, `⟨I⟩ ApprovalQueue` | Managed DB (Postgres for the HITL queue + 3-tier memory; same shape or compatible for workspace store) |
| **Data Sources** | Where business / mission / corpus data *lives*. CRAFT reads from and (eventually) writes to these. | `⟨I⟩ DataSource` | LocalFileSource (internal); SharePoint, SAP, STK/MATLAB, Azure AI Search (external) |

Three concrete things sit under **Storage**:
1. **Workspace sessions + scratch** — per-user chat workspaces, uploaded files, intermediate scratch state. Accessed through `⟨I⟩ WorkspaceStore`.
2. **Per-user operational data** — RBAC-scoped data CRAFT persists for the user (preferences, cached intermediates, user-visible named rows). Accessed through the same `⟨I⟩ WorkspaceStore` surface via `QueryTool.set_user` for scoping.
3. **HITL approval queue** — pending approvals written by the agent when a risky tool wants to execute; read + decided by admins through `/admin/approvals/*`. Accessed through `⟨I⟩ ApprovalQueue`. Backed by **Postgres** at end state.

Separate from Storage is **Audit**: the `AgentActionLog` writes a hash-chained JSONL stream of every tool call, LLM turn, and HITL decision. Hash chain = tamper detection. End state forwards the same lines into Azure Log Analytics for immutable retention. The audit sink is drawn as its own column in 2b because it has different durability requirements from the other storage (append-only, forwardable, verifiable).

**Why not merge Storage and Data Sources?** Because they have different trust, lifecycle, and semantics. Storage is private operational state CRAFT owns end-to-end. Data Sources are read-mostly, often live outside CRAFT's trust boundary, and need per-request RBAC scoping and token-based auth. Collapsing them would make the perimeter unclear.

### Why Postgres for the approval queue specifically
HITL approval queues need to survive restarts (an approval request may sit pending for hours or days), need multi-reader semantics (reviewer UI + agent resume logic), and need durable transactional state. Postgres is the pitch's committed answer. (If/when Postgres isn't yet available, a temporary alternative gets built — that's a team-known contingency, not pitch content.)

### Why hash-chained JSONL and not just structured logs
Pitch invariant: audit must be tamper-detectable. Plain structured JSON lets anyone with disk access edit a line unobserved. Each `AgentAction` carries `previous_hash` and `hash = sha256(previous_hash + canonical_json(payload))`, so tampering any line breaks every subsequent `hash`. `python -m app.core.audit verify` walks the chain and names the first bad trace_id. Same envelope ships into Azure Log Analytics when the forwarder is in place.

### Protocols — the six `⟨I⟩`s
- `⟨I⟩ Tool` — a thing the agent can call. `definition()` returns JSON Schema; `execute(args)` runs the operation.
- `⟨I⟩ DataSource` — a read interface over a data backend (filesystem, SharePoint, SAP, AI Search).
- `⟨I⟩ ChatProvider` — the agent runtime seam. `MsAgentFrameworkChatProvider` is the current satisfier.
- `⟨I⟩ WorkspaceStore` — CRAFT's own operational storage (workspaces, scratch, per-user data).
- `⟨I⟩ ApprovalQueue` — HITL queue (Postgres end state).
- `⟨I⟩ AgentActionLog` — audit sink.

Rule: new capability or backend = one class satisfying the right protocol. The rest of the system doesn't change.

### "Internal caller" vs "External caller"
- **Internal caller** = the primary agent, running inside the CRAFT process. Calls routes via an in-process test client, same code path as an external HTTP hit.
- **External caller** = anything outside the process presenting an Entra token: a cron, a pipeline, an upstream workflow, a human service account.

Both go through the same route gate. Role on the token determines what they can call. This is the pitch's "deterministic access" story — you don't have to go through the agent to use CRAFT's capabilities.

### "Deterministic" vs "probabilistic" use
- **Probabilistic** = the agent decides what to call based on the user's natural-language prompt. Non-deterministic by design — the LLM may pick different tools on different runs.
- **Deterministic** = an external caller hits a specific route with explicit arguments. Reproducible, scriptable, scheduled.

### `permissions.json`
Declarative role mapping. Role levels (`base(1) < power(2) < admin(3)`), public exact paths (`/`, `/favicon.ico`), public prefixes (`/auth/`, `/_`, `/static/`), internal prefixes (`/chat/internal/`, `/tools/execute/`), and route rules (`/admin/* → admin`, `/uploads → power`, etc.). Loaded at startup; `before_request` walks the list.

### `AgentAction` envelope
Per-step audit record: `trace_id`, `agent_id`, `step`, `kind` (`llm_turn` | `tool_call` | `hitl_decision`), `role`, `username`, `tool_name` (optional), `args_summary`, `result_summary`, `confidence`, `citations`, `timestamp`, `previous_hash`, `hash`. Written by `⟨I⟩ AgentActionLog`.

---

## 4. Why these technology choices

### Microsoft Agent Framework (not LangGraph, not hand-rolled)
- **Microsoft-blessed.** GA April 2026, successor to Semantic Kernel. Long-term support commitment.
- **Azure-native.** First-class Azure OpenAI + Azure AI Foundry integration. `AzureOpenAIChatClient` is the official chat client.
- **HITL built in.** Function-level `@tool(approval_mode="always_require")` → `user_input_requests`. Workflow-level `RequestPort`.
- **Bounded iteration + telemetry.** Framework handles the ReAct loop with iteration cap and OpenTelemetry hooks.
- **Not LangGraph** because LangGraph is third-party, pulls `langchain-*` + `pydantic` as hard deps, and doesn't give us anything Agent Framework doesn't.

### Azure AI Foundry (over Azure OpenAI direct, long-term)
Foundry collapses model routing, rate limiting, and Content Safety into one line while keeping Canadian PBMM data residency. The SDK call site doesn't change — only the endpoint.

### Azure AI Search for retrieval
Hybrid (vector + BM25) retrieval is what CRAFT needs to satisfy UMR-004/005/006 (ranked retrieval with threshold). Behind `⟨I⟩ DataSource`, so retrieval shape doesn't leak to the agent.

### Flask + Dash
HTTP routes are the integration contract. Any token-bearing caller can hit CRAFT. Dash shares the same Flask server, which means the reviewer UI inherits the exact same auth + audit perimeter as the public API.

### Entra ID + MSAL
Same token flow for humans and external agents. CSA-standard.

### Container Apps for code-exec
The `CodeExecTool` is reserved as a protocol slot. End-state wires it into an Azure Container Apps sandbox: ephemeral containers, no network, runtime caps, destroyed after each call. Guardrail hook sits in the tool wrapper so adding the sandbox is a config change.

---

## 5. Why the diagrams are ASCII (and when they shouldn't be)

ASCII is a deliberate choice for the proposal phase:
- **Fast to iterate.** Edit markdown, re-render HTML, see the new shape in seconds.
- **Grep-friendly.** Reviewers can quote lines, search for component names, diff versions.
- **Monospace fits the content.** Protocols, routes, and store names are all short identifiers that line up cleanly.
- **No tool dependency** beyond `python-markdown` + a browser for the PDF render.

The SVGs under `docs-depo/pitch/diagrams/` (final-L1.png, final-L2.png, etc.) were drafted earlier and still *mostly* match. They need updates to reflect: Microsoft Agent Framework replacing the "LangGraph ReAct" box, the Internal/External Data split in the L1 columns, the dual-caller shape at the top of L2, and the Storage vs DataSource clarification. Treat them as deferred art; the ASCII diagrams in the markdown are the source of truth for now.

---

## 6. Rendering pipeline

Three artefacts in this folder, all from one source:

```
CRAFT-pitch.md          ← source (markdown)
├── pdf-style.html      ← CSS (type scale, table style, code block styling)
├── CRAFT-pitch.html    ← rendered via python-markdown with extensions=['tables','fenced_code']
└── CRAFT-pitch.pdf     ← rendered from .html via headless Chromium
```

Regenerate HTML:
```python
import markdown, pathlib
md = pathlib.Path('CRAFT-pitch.md').read_text()
if md.startswith('---'):
    md = md[md.find('---', 3)+3:].lstrip()
style = pathlib.Path('pdf-style.html').read_text()
body = markdown.markdown(md, extensions=['tables', 'fenced_code'])
pathlib.Path('CRAFT-pitch.html').write_text(
    f'<!doctype html><html><head><meta charset="utf-8"><title>CRAFT</title>{style}</head><body>{body}</body></html>'
)
```

Regenerate PDF:
```bash
/opt/pw-browsers/chromium-1194/chrome-linux/chrome \
  --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=CRAFT-pitch.pdf \
  "file://$PWD/CRAFT-pitch.html"
```

**Fit check.** All six ASCII diagram blocks are ≤ 83 chars wide. Letter at 0.6in margins = 7.3in content, 10pt mono = ~95 chars fit. No block overflows. PDF is 7 pages.

---

## 7. What's deliberately NOT in the pitch

- **Temporary alternatives** (whatever local backing stores we build before the end-state tech is accessible — including CSV fixtures, in-memory auth, and any hand-rolled runtime that stands in for the framework). Team-understood, not pitch content.
- **"Today vs end-state" split.** The pitch describes the target.
- **Framework alternatives** (LangChain / LangGraph, Semantic Kernel). We chose Agent Framework; no alternatives discussion.
- **Onboarding.** No "how to install", "how to run", setup guide. Keep that out of a proposal.
- **A "we built this" tone.** Nothing is built yet. Every claim is phrased as a design, not a status report.

---

## 8. How to inquire about this doc with another agent

Point the agent at `docs-depo/pitch/CRAFT-pitch.md` and `docs-depo/pitch/CRAFT-pitch-design-notes.md` (this file). Then any of:

- *"Explain the Storage vs Data Sources split in CRAFT."* → §3 above.
- *"Why Microsoft Agent Framework over LangGraph?"* → §4 above.
- *"What's the role of the hash-chained audit log?"* → §3 ("Why hash-chained…") above.
- *"What does deterministic access mean in 2b?"* → §3 above.
- *"Why doesn't the pitch name any temporary backing stores?"* → §1 above.
- *"What are the six protocols?"* → §3 above.
- *"Who owns each dependency in §7 of the pitch?"* → it's a column in the pitch table itself.

Keep this doc and the pitch in sync when the pitch changes. The pitch is the artefact; this is the explanation. If a reader has to open this to understand the pitch, that's a signal the pitch is unclear and should be edited.
