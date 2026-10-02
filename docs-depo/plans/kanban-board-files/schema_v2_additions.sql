-- Schema additions for structured PR descriptions on kanban tasks.
-- Run against cheddar.db to upgrade an existing kanban board:
--   sqlite3 app/database/cheddar.db < plans/plans-n-board/schema_v2_additions.sql

-- Structured PR description: every task that has an open PR must populate
-- these fields so other developers can extract information efficiently.
ALTER TABLE kanban_tasks ADD COLUMN pr_change_summary TEXT NOT NULL DEFAULT '';
ALTER TABLE kanban_tasks ADD COLUMN pr_scope_affected TEXT NOT NULL DEFAULT '';
-- Comma-separated list of areas: 'database', 'api', 'ui', 'auth', 'aggregation', etc.
ALTER TABLE kanban_tasks ADD COLUMN pr_behavior_changes TEXT NOT NULL DEFAULT '';
ALTER TABLE kanban_tasks ADD COLUMN pr_test_suite TEXT NOT NULL DEFAULT '';
-- Test commands to run, or 'none' / 'manual-only'
ALTER TABLE kanban_tasks ADD COLUMN pr_validation_criteria TEXT NOT NULL DEFAULT '';
-- How to verify the change is correct before merging
ALTER TABLE kanban_tasks ADD COLUMN pr_unfinished_items TEXT NOT NULL DEFAULT '';
-- What remains to be done, known gaps, follow-up tasks
ALTER TABLE kanban_tasks ADD COLUMN pr_related_issues TEXT NOT NULL DEFAULT '';
-- Comma-separated GitHub issue/PR numbers this depends on or relates to
ALTER TABLE kanban_tasks ADD COLUMN pr_description_hash TEXT NOT NULL DEFAULT '';
-- SHA256 of the combined PR description fields, for detecting staleness