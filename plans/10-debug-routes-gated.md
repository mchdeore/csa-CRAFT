# 10 — Gate /debug/* routes behind ENABLE_DEBUG_ROUTES

**Status:** planned · depends on `01-config-stdlib-dotenv.md`, `06-permissions-declarative.md`

## Why

`/debug/routes` and `/debug/pipeline` are useful dev / support affordances but have no place in production. Today they are always registered. The pitch's RBAC perimeter does not try to hide "map the app" endpoints; the right pattern is to not register them when the deploy says they're off.

The `/debug/pipeline` payload also still references weather, news and Cohere wiring — stale after plan 08. Rewrite it when gating.

## Scope

**In**
- `app/core/routes.py` registers `/debug/routes` and `/debug/pipeline` only when `settings.ENABLE_DEBUG_ROUTES` is true.
- Rewrite the `/debug/pipeline` payload to reflect reality after plans 03, 04, 07, 08.
- `permissions.json` can keep an admin rule for `/debug/*` so that even if someone forgets the flag, non-admins get 403 (defence in depth).

**Out**
- A whole admin UI around pipeline inspection.
- Metrics / Prometheus endpoint.

## Files touched

- **Edit**
  - `app/core/routes.py` — wrap `_register_debug_routes` registration in `if settings.ENABLE_DEBUG_ROUTES`.
  - `app/core/routes.py:_register_debug_routes` — rewrite the `/debug/pipeline` payload per below.

## Payload rewrite

```python
# /debug/pipeline response (sketch) — reflects post-refactor reality
{
    "codepaths": {
        "chat": {
            "route": "POST /chat/send",
            "flow": [
                "chat.routes:send_message",
                "chat.provider:AzureChatProvider.get_response",
                "chat.agent:run_agent (ReAct loop on openai.AsyncAzureOpenAI)",
                "chat.agent:tool.execute (⟨I⟩ Tool)",
                "app.core.audit:HashChainedJsonlLog.emit",
                "storage.store:save_messages",
            ],
        },
        "auth": {
            "routes": ["POST /auth/login", "POST /auth/logout"],
            "flow": ["auth.routes → auth.provider:try_login/do_logout → storage.store:list_users"],
        },
        "storage": {
            "routes": [
                "GET /storage/list/<username>",
                "POST /storage/create",
                "GET /storage/load/<username>/<workspace_id>",
                "POST /storage/save-messages/<username>/<workspace_id>",
            ],
            "flow": ["storage.routes → storage.store:SqliteStore"],
        },
        "tools": {
            "routes": ["GET /tools/list", "POST /tools/execute/<tool_name>"],
            "flow": [
                "tools.routes → tools.documents.search:DocumentSearchTool",
                "tools.routes → tools.documents.reader:TextAnalysisTool",
                "tools.routes → tools.documents.excel:ExcelTool",
                "tools.routes → tools.charts.*",
                "tools.routes → tools.classifier:ClassifierTool (RESERVED)",
                "tools.routes → tools.historical_mission (RESERVED)",
                "tools.routes → tools.cost_aggregator (RESERVED)",
                "tools.routes → tools.vendor_aggregator (RESERVED)",
                "tools.routes → tools.code_exec (RESERVED)",
            ],
        },
        "connectors": {
            "flow": ["app.core.data_sources:load_data_sources → connectors.local_files:LocalFileSource"],
        },
        "hitl": {
            "routes": ["GET /admin/approvals", "POST /admin/approvals/<trace_id>/<decision>"],
            "flow": ["storage.approvals:ApprovalQueue (SQLite today, Postgres end state)"],
            "enabled": settings.ENABLE_HITL,
        },
    },
    "audit": {
        "sink": "app.core.audit:HashChainedJsonlLog",
        "path": str(settings.LOG_DIR / "cheddar-YYYY-MM-DD.jsonl"),
        "forwarder": "deploy-time: Azure Log Analytics (reserved)",
    },
}
```

## Workflow

**Pre-check**
- Plans 01 (`ENABLE_DEBUG_ROUTES` in settings) and 06 (`permissions.json`) shipped.

**Do**
1. Wrap `_register_debug_routes(app)` registration in `app/core/routes.py:register_all` with `if settings.ENABLE_DEBUG_ROUTES`.
2. Rewrite the `/debug/pipeline` payload as above (reference `settings.*` where current state matters).
3. Add `/admin/debug/*` or keep `/debug/*` under an admin rule in `permissions.json` so a leftover ON flag still blocks non-admins. (Decision: keep the path at `/debug/*`, add a role rule `{"pattern":"/debug/*","min_role":"admin"}` so defence-in-depth stands even if the registration flag is on.)

**Verify**
- `ENABLE_DEBUG_ROUTES=0 python app.py` → `curl http://127.0.0.1:8050/debug/routes` returns 404.
- `ENABLE_DEBUG_ROUTES=1 python app.py` with a base_user session → 403.
- `ENABLE_DEBUG_ROUTES=1 python app.py` with an admin session → 200 and the payload lists the real codepaths (no weather, no news, no Cohere).
- `pytest -q` passes (add a quick test asserting the registration conditional).

**Commit**
`refactor(debug): gate /debug/* on ENABLE_DEBUG_ROUTES, refresh pipeline map`

**Rollback**
`git restore -SW app/core/routes.py app/core/permissions.json`

## Verification checklist

- [ ] `/debug/*` returns 404 when `ENABLE_DEBUG_ROUTES=0`.
- [ ] `/debug/*` returns 403 for non-admins when `ENABLE_DEBUG_ROUTES=1`.
- [ ] `/debug/pipeline` payload has no weather / news / Cohere references.
- [ ] Audit sink section names `HashChainedJsonlLog`.

## Out of scope

- Prometheus / OpenTelemetry metrics endpoints.
- A Dash UI around the pipeline map.

---

## Reasoning / justification extracts

**Pitch alignment:**
- Pitch §1 shows "unregistered route → 404 (before auth)" and "role < required → 403" as the two failure modes. Gating by registration lets us emit 404 when the deploy says debug is off (no information leak about what exists).
- Pitch §8 System-Health Tooling — the debug map is the human-facing version of the invariants pytest already verifies.

**User instructions:**
- "accessible to 'manual' users too" — when enabled, `/debug/pipeline` is the exact self-description a dev or an agent needs. When off, the surface shrinks for production.

**Why defence in depth (admin role rule even when enabled):**
Config-only gates fail open on a misconfig. Pairing the registration flag with a permission rule means a stray `ENABLE_DEBUG_ROUTES=1` in prod still gets stopped by the role check.
