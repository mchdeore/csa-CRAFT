-- Seed data: default columns and one example task.

-- Default kanban columns
INSERT OR IGNORE INTO kanban_columns (name, sort_order, wip_limit) VALUES
    ('backlog',      1, NULL),
    ('todo',         2, NULL),
    ('in-progress',  3, 3),
    ('review',       4, 2),
    ('done',         5, NULL);

-- Example task (remove or edit as needed)
INSERT INTO kanban_tasks (
    title,
    description,
    column_id,
    github_pr_url,
    github_pr_number,
    development_plan_file,
    development_description_file,
    priority,
    assignee,
    tags
) VALUES (
    'Set up kanban board in database',
    'Create schema, seed data, and query helpers for the plans-n-board kanban system. Link to the main cheddar.db and verify tables.',
    (SELECT id FROM kanban_columns WHERE name = 'done'),
    NULL,
    NULL,
    'plans/plans-n-board/schema.sql',
    'plans/plans-n-board/README.md',
    'medium',
    'cheddar',
    '["infrastructure", "planning"]'
);