-- 004: Stream buffer for tool output streaming
-- Stores incremental tool results for polling by UI.

CREATE TABLE IF NOT EXISTS stream_buffer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    workspace_id TEXT NOT NULL,
    tool_name TEXT NOT NULL,
    event_type TEXT NOT NULL,       -- 'start', 'progress', 'complete', 'error'
    payload TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (username) REFERENCES users(username)
);

CREATE INDEX IF NOT EXISTS idx_stream_buffer_user_ws
    ON stream_buffer(username, workspace_id, created_at);