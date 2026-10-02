-- Kanban job board for csa-CRAFT project development tracking.
-- Resides alongside the main cheddar.db. Each task links to a
-- GitHub PR, a development plan file, and a development description.

-- Column definitions for the kanban board
CREATE TABLE IF NOT EXISTS kanban_columns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,            -- 'backlog', 'todo', 'in-progress', 'review', 'done'
    sort_order INTEGER NOT NULL DEFAULT 0,
    wip_limit INTEGER,                    -- max tasks allowed in this column, NULL = no limit
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Task cards on the board
CREATE TABLE IF NOT EXISTS kanban_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',            -- development description
    column_id INTEGER NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0,
    -- Links to external artifacts
    github_pr_url TEXT,                              -- link to GitHub pull request
    github_pr_number INTEGER,                        -- PR number for quick reference
    development_plan_file TEXT,                      -- path to plan file in docs-depo/plans/
    development_description_file TEXT,               -- path to detailed design doc
    -- Metadata
    priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('urgent','high','medium','low')),
    assignee TEXT,                                   -- username or team name
    tags TEXT NOT NULL DEFAULT '[]',                 -- JSON array of tag strings
    estimated_hours REAL,
    logged_hours REAL NOT NULL DEFAULT 0,
    -- State
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    completed_at TEXT,
    FOREIGN KEY (column_id) REFERENCES kanban_columns(id)
);

-- Comments and activity log on each task
CREATE TABLE IF NOT EXISTS kanban_comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    author TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (task_id) REFERENCES kanban_tasks(id) ON DELETE CASCADE
);

-- Track when a task moves between columns
CREATE TABLE IF NOT EXISTS kanban_moves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    from_column_id INTEGER,
    to_column_id INTEGER NOT NULL,
    moved_at TEXT NOT NULL DEFAULT (datetime('now')),
    moved_by TEXT NOT NULL DEFAULT 'system',
    note TEXT,
    FOREIGN KEY (task_id) REFERENCES kanban_tasks(id) ON DELETE CASCADE,
    FOREIGN KEY (from_column_id) REFERENCES kanban_columns(id),
    FOREIGN KEY (to_column_id) REFERENCES kanban_columns(id)
);

-- Index for common queries
CREATE INDEX IF NOT EXISTS idx_kanban_tasks_column ON kanban_tasks(column_id, sort_order);
CREATE INDEX IF NOT EXISTS idx_kanban_tasks_assignee ON kanban_tasks(assignee);
CREATE INDEX IF NOT EXISTS idx_kanban_comments_task ON kanban_comments(task_id);
CREATE INDEX IF NOT EXISTS idx_kanban_moves_task ON kanban_moves(task_id);