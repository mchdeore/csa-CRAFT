-- Common queries for the kanban board. Run these against cheddar.db
-- after applying schema.sql.

-- ── Board overview: all tasks grouped by column ──
SELECT
    c.name AS column_name,
    c.sort_order AS col_order,
    t.id AS task_id,
    t.title,
    t.priority,
    t.assignee,
    t.github_pr_url,
    t.github_pr_number,
    t.development_plan_file,
    t.development_description_file,
    t.created_at,
    t.updated_at
FROM kanban_columns c
LEFT JOIN kanban_tasks t ON t.column_id = c.id
ORDER BY c.sort_order, t.sort_order;

-- ── Tasks with open PRs (in review or in-progress) ──
SELECT
    c.name AS column_name,
    t.title,
    t.github_pr_url,
    t.github_pr_number,
    t.assignee,
    t.priority
FROM kanban_tasks t
JOIN kanban_columns c ON c.id = t.column_id
WHERE c.name IN ('in-progress', 'review')
  AND t.github_pr_url IS NOT NULL
ORDER BY t.priority, c.sort_order;

-- ── Tasks blocked or stalled (no movement in 7 days) ──
SELECT
    t.title,
    c.name AS column_name,
    t.updated_at,
    t.assignee,
    t.github_pr_url
FROM kanban_tasks t
JOIN kanban_columns c ON c.id = t.column_id
WHERE c.name NOT IN ('done', 'backlog')
  AND t.updated_at < datetime('now', '-7 days')
ORDER BY t.updated_at;

-- ── Work-in-progress count per column (check wip limits) ──
SELECT
    c.name,
    c.wip_limit,
    COUNT(t.id) AS task_count
FROM kanban_columns c
LEFT JOIN kanban_tasks t ON t.column_id = c.id
GROUP BY c.id
ORDER BY c.sort_order;

-- ── Recent activity: last 10 task moves ──
SELECT
    t.title,
    col_from.name AS from_column,
    col_to.name AS to_column,
    m.moved_at,
    m.moved_by,
    m.note
FROM kanban_moves m
JOIN kanban_tasks t ON t.id = m.task_id
LEFT JOIN kanban_columns col_from ON col_from.id = m.from_column_id
JOIN kanban_columns col_to ON col_to.id = m.to_column_id
ORDER BY m.moved_at DESC
LIMIT 10;