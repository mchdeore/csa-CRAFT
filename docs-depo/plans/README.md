# docs-depo/plans

Development process runbooks. Step-by-step workflows for common dev tasks.

Each file is a self-contained runbook — a person or agent following it should not need to re-derive context. Written for execution, not explanation.

## Structure

```
docs-depo/plans/
├── README.md                          ← This file
├── markdown-plans/
│   ├── incomplete/                    ← Plans still being worked on
│   └── complete/                      ← Plans whose work has shipped
└── kanban-board-files/                ← Kanban board system. See README inside.
```

## Kanban board

All board files live in `kanban-board-files/`. Setup, schema, queries, scripts, server — see `kanban-board-files/README.md` for the full file map.

## Active plans

- `markdown-plans/incomplete/finalize-pr-workflow.md` — End-to-end PR finalization: run tests, fix failures, lint, type-check, build PR description, sync kanban board, move to review.