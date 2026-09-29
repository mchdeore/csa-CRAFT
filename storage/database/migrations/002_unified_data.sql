-- 002: Unified data store + user profile extensions
-- Adds role/division/region/flags to users table.
-- Adds global_datasets, global_data_rows for shared queryable data.
-- Adds user_data for workspace-scoped key-value storage.
-- Adds user_profiles for extended user metadata.

-- Extend existing users table with role and profile columns
ALTER TABLE users ADD COLUMN role TEXT NOT NULL DEFAULT 'base_user';
ALTER TABLE users ADD COLUMN division TEXT NOT NULL DEFAULT '';
ALTER TABLE users ADD COLUMN region TEXT NOT NULL DEFAULT '';
ALTER TABLE users ADD COLUMN flags TEXT NOT NULL DEFAULT '[]';

-- Global datasets: shared data with minimum role requirement
CREATE TABLE IF NOT EXISTS global_datasets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT '',
    min_role TEXT NOT NULL DEFAULT 'base_user',
    schema_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Rows within a global dataset — flexible JSON per row
CREATE TABLE IF NOT EXISTS global_data_rows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset_id INTEGER NOT NULL,
    data_json TEXT NOT NULL,
    FOREIGN KEY (dataset_id) REFERENCES global_datasets(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_global_data_rows ON global_data_rows(dataset_id);

-- Key-value store per user, scoped to workspace
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    workspace_id TEXT NOT NULL,
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE(username, workspace_id, key)
);

CREATE INDEX IF NOT EXISTS idx_user_data_lookup ON user_data(username, workspace_id, key);

-- Extended user profile fields
CREATE TABLE IF NOT EXISTS user_profiles (
    username TEXT PRIMARY KEY,
    full_name TEXT NOT NULL DEFAULT '',
    preferences_json TEXT NOT NULL DEFAULT '{}',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (username) REFERENCES users(username)
);