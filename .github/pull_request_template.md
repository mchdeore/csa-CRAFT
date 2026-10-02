## Summary

<!-- One paragraph: what this PR does and why. Keep it under 5 sentences. -->

## Scope Affected

<!-- Check all that apply. Delete those that don't. -->
- [ ] `database/` — schema changes, migrations, queries
- [ ] `api/` — routes, middleware, request/response contracts
- [ ] `ui/` — templates, static assets, frontend components
- [ ] `auth/` — authentication, authorization, session management
- [ ] `connectors/` — external service integrations
- [ ] `tools/` — CLI utilities, helper scripts
- [ ] `tests/` — test infrastructure, new test suites
- [ ] `docs-depo/` — documentation, plans, exploration notes
- [ ] `plans/` — development plans
- [ ] Other: ________________

## Behavior Changes

<!-- For each user-facing or internal behavior that changed, describe:
     - BEFORE: what happened previously
     - AFTER: what happens now
     - MIGRATION: steps required to adapt (if any)
     
     If no behavior changes, write "None." -->

## Test Suite

<!-- How to validate this PR. Include exact commands. -->

```
# Run these tests:
pytest app/tests/

# Or specific test file:
pytest app/tests/test_example.py -v
```

- [ ] All existing tests pass
- [ ] New tests added for changed behavior
- [ ] Manual verification steps documented below (if applicable)

### Manual Verification

<!-- Steps a reviewer can follow to manually confirm the change works. -->

1. 
2. 
3. 

## Validation Criteria

<!-- What must be true for this PR to be considered done and mergeable.
     Write each criterion as a checkbox. -->

- [ ] 
- [ ] 
- [ ] 

## Unfinished Items / Known Gaps

<!-- Anything intentionally left out of this PR. Future work, edge cases
     not yet handled, or decisions deferred. If nothing, write "None." -->

## Related Issues / PRs

<!-- Link related GitHub issues, PRs, or kanban task IDs. -->

- Task: `docs-depo/plans/kanban-board-files/cards.json` entry #
- Issues: #
- Depends on: #
- Blocks: #

## Kanban Board Update

<!-- Confirm the kanban board reflects this PR's state. -->

- [ ] Kanban task `github_pr_url` and `github_pr_number` populated
- [ ] Structured PR fields (`pr_change_summary`, `pr_scope_affected`, etc.) filled in `kanban_tasks`
- [ ] Task moved to `review` column