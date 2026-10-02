-- Extended queries that include the structured PR description fields.
-- Run after applying schema_v2_additions.sql.

-- ── Board overview with PR description hash for staleness check ──
SELECT
    c.name AS column_name,
    t.id AS task_id,
    t.title,
    t.priority,
    t.assignee,
    t.github_pr_number,
    t.pr_change_summary,
    t.pr_scope_affected,
    t.pr_description_hash,
    t.updated_at
FROM kanban_columns c
LEFT JOIN kanban_tasks t ON t.column_id = c.id
ORDER BY c.sort_order, t.sort_order;

-- ── Tasks with PR that need description sync (hash empty or stale) ──
SELECT
    t.id,
    t.title,
    t.github_pr_url,
    t.github_pr_number,
    t.pr_description_hash,
    CASE
        WHEN t.pr_description_hash = '' THEN 'never-synced'
        WHEN t.pr_change_summary = '' THEN 'empty-summary'
        ELSE 'ok'
    END AS sync_status
FROM kanban_tasks t
WHERE t.github_pr_url IS NOT NULL
ORDER BY t.pr_change_summary = '' DESC, t.id;

-- ── Scope summary: what areas does each PR touch? ──
SELECT
    t.title,
    t.github_pr_number,
    t.pr_scope_affected
FROM kanban_tasks t
WHERE t.github_pr_url IS NOT NULL
  AND t.pr_scope_affected != ''
ORDER BY t.github_pr_number;

-- ── Unfinished items across all active tasks ──
SELECT
    t.title,
    c.name AS column_name,
    t.assignee,
    t.pr_unfinished_items
FROM kanban_tasks t
JOIN kanban_columns c ON c.id = t.column_id
WHERE c.name NOT IN ('done')
  AND t.pr_unfinished_items != ''
ORDER BY c.sort_order, t.priority;

-- ── Validation criteria for tasks in review ──
SELECT
    t.title,
    t.github_pr_number,
    t.pr_validation_criteria,
    t.pr_test_suite
FROM kanban_tasks t
JOIN kanban_columns c ON c.id = t.column_id
WHERE c.name = 'review'
  AND t.github_pr_url IS NOT NULL
ORDER BY t.id;