-- 003: Audit log for HITL approve/reject
-- Records every human-in-the-loop decision with timestamp, user, and context.

CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    action TEXT NOT NULL,           -- 'approve' or 'reject'
    target_type TEXT NOT NULL,      -- 'comparison', 'compliance', 'risk'
    target_id TEXT NOT NULL,        -- identifier of what was acted on
    context_json TEXT,              -- snapshot of data at decision time
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (username) REFERENCES users(username)
);

CREATE INDEX IF NOT EXISTS idx_audit_log_user ON audit_log(username);
CREATE INDEX IF NOT EXISTS idx_audit_log_target ON audit_log(target_type, target_id);