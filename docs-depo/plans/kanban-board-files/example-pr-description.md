## Summary

Adds SQL aggregation pipeline that rolls up cadre_params data by mission type, power band, and payload mass range. Output stored in global_datasets for downstream charting and comparison views.

## Scope Affected

- [x] `database/` — schema changes, migrations, queries
- [ ] `api/` — routes, middleware, request/response contracts
- [ ] `ui/` — templates, static assets, frontend components
- [ ] `auth/` — authentication, authorization, session management
- [ ] `connectors/` — external service integrations
- [ ] `tools/` — CLI utilities, helper scripts
- [x] `tests/` — test infrastructure, new test suites
- [ ] `docs-depo/` — documentation, plans, exploration notes
- [ ] `plans/` — development plans

## Behavior Changes

- BEFORE: No aggregation queries existed. Global datasets only held manually inserted rows.
- AFTER: Three aggregation queries are available via SQL views. Queries group missions by type, power band (0-100W, 100-500W, 500W+), and payload mass range (0-50kg, 50-200kg, 200kg+). Results are materialized into global_datasets on demand.
- MIGRATION: Run `app/database/migrations/002_aggregation_views.sql` to create the views. No data migration needed — reads from existing cadre_params table.

## Test Suite

```
# Run all tests:
pytest app/tests/

# Run aggregation-specific tests:
pytest app/tests/test_aggregation.py -v
```

- [x] All existing tests pass
- [x] New tests added for each aggregation view (3 test classes, 15 test cases)
- [x] Manual verification: ran aggregation views against 50-mission test dataset, results verified against spreadsheet calculation

### Manual Verification

1. Run migration: `sqlite3 app/database/cheddar.db < app/database/migrations/002_aggregation_views.sql`
2. Query aggregation view: `sqlite3 app/database/cheddar.db "SELECT * FROM v_mission_power_bands;"`
3. Confirm row counts match expected values from test fixture
4. Confirm no NULL values in aggregation columns

## Validation Criteria

- [x] All three aggregation views produce correct row counts for test dataset
- [x] Views handle NULL cadre_params fields gracefully (skip, don't crash)
- [x] Empty dataset case returns zero rows, not errors
- [x] Migration is idempotent (can run twice without errors)
- [x] Code reviewed by at least one other developer

## Unfinished Items / Known Gaps

- Real-time aggregation refresh not implemented — data is materialized on migration only. Will add scheduled refresh in follow-up PR.
- Only three grouping dimensions supported. Additional dimensions (delta-v band, duration band) deferred to v2.
- No database indexes optimized for aggregation queries yet. Benchmarked acceptable for current dataset size (<10k rows), will re-evaluate at 100k rows.

## Related Issues / PRs

- Task: `docs-depo/plans/kanban-board-files/cards.json` entry #2
- Issues: None
- Depends on: None
- Blocks: PR for mission comparison UI (#3 on kanban board)

## Kanban Board Update

- [x] Kanban task `github_pr_url` and `github_pr_number` populated
- [x] Structured PR fields synced via `sync_pr.py`
- [x] Task moved to `review` column