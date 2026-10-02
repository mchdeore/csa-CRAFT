"""
Standalone Flask server that serves the kanban board in a browser.
Reads directly from app/database/cheddar.db. No dependency on the Dash app.

Run: python3 docs-depo/plans/kanban-board-files/kanban_server.py
Open: http://localhost:8051
"""

import json
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
DB_PATH = REPO_ROOT / "app" / "database" / "cheddar.db"

APP = Flask(__name__)


def get_db() -> sqlite3.Connection:
    connection = sqlite3.connect(str(DB_PATH))
    connection.row_factory = sqlite3.Row
    return connection


@APP.route("/")
def serve_board() -> str:
    return _BOARD_HTML


@APP.route("/api/columns")
def api_columns() -> tuple:
    connection = get_db()
    rows = connection.execute(
        "SELECT id, name, sort_order, wip_limit FROM kanban_columns ORDER BY sort_order"
    ).fetchall()
    connection.close()

    columns = [dict(row) for row in rows]
    return jsonify(columns), 200


@APP.route("/api/tasks")
def api_tasks() -> tuple:
    connection = get_db()
    rows = connection.execute(
        """
        SELECT id, title, description, column_id, sort_order,
               priority, assignee, tags,
               github_pr_url, github_pr_number,
               development_plan_file, development_description_file,
               estimated_hours, logged_hours,
               pr_change_summary, pr_scope_affected,
               pr_behavior_changes, pr_test_suite,
               pr_validation_criteria, pr_unfinished_items,
               pr_related_issues, pr_description_hash,
               created_at, updated_at, completed_at
        FROM kanban_tasks
        ORDER BY sort_order
        """
    ).fetchall()
    connection.close()

    tasks = []
    for row in rows:
        task = dict(row)

        # Parse tags from JSON string
        try:
            task["tags"] = json.loads(task["tags"])
        except (json.JSONDecodeError, TypeError):
            task["tags"] = []

        tasks.append(task)

    return jsonify(tasks), 200


@APP.route("/api/tasks/<int:task_id>/move", methods=["POST"])
def api_move_task(task_id: int) -> tuple:
    data = request.get_json()

    if not data or "column_id" not in data:
        return jsonify({"error": "Missing column_id"}), 400

    new_column_id = data["column_id"]

    connection = get_db()
    cursor = connection.cursor()

    # Get current column for move log
    old = cursor.execute(
        "SELECT column_id FROM kanban_tasks WHERE id = ?", (task_id,)
    ).fetchone()

    if old is None:
        connection.close()
        return jsonify({"error": "Task not found"}), 404

    old_column_id = old["column_id"]

    # Update task
    cursor.execute(
        "UPDATE kanban_tasks SET column_id = ?, updated_at = datetime('now') WHERE id = ?",
        (new_column_id, task_id),
    )

    # Log the move
    cursor.execute(
        "INSERT INTO kanban_moves (task_id, from_column_id, to_column_id, moved_by) VALUES (?, ?, ?, ?)",
        (task_id, old_column_id, new_column_id, "kanban_server"),
    )

    connection.commit()

    # Return updated task
    task = cursor.execute(
        "SELECT * FROM kanban_tasks WHERE id = ?", (task_id,)
    ).fetchone()

    connection.close()

    task_dict = dict(task)

    try:
        task_dict["tags"] = json.loads(task_dict["tags"])
    except (json.JSONDecodeError, TypeError):
        task_dict["tags"] = []

    return jsonify(task_dict), 200


# --- Inline HTML/CSS/JS for a drag-and-drop kanban board ---

_BOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>csa-CRAFT · Kanban Board</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #0d1117;
    color: #c9d1d9;
    min-height: 100vh;
  }
  header {
    background: #161b22;
    border-bottom: 1px solid #30363d;
    padding: 12px 24px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  header h1 { font-size: 18px; font-weight: 600; color: #f0f6fc; }
  header span.badge {
    background: #238636;
    color: #fff;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 12px;
  }
  .board {
    display: flex;
    gap: 16px;
    padding: 20px;
    overflow-x: auto;
    min-height: calc(100vh - 60px);
  }
  .column {
    flex: 1;
    min-width: 280px;
    max-width: 360px;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
  }
  .column-header {
    padding: 12px 16px;
    border-bottom: 1px solid #30363d;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .column-header h2 { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
  .column-header .count {
    background: #30363d;
    color: #8b949e;
    font-size: 12px;
    padding: 1px 8px;
    border-radius: 10px;
  }
  .column-body {
    flex: 1;
    padding: 8px;
    overflow-y: auto;
    min-height: 100px;
  }
  .column-body.drag-over { background: #1a2332; }
  .card {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 12px;
    margin-bottom: 8px;
    cursor: grab;
    transition: border-color 0.15s;
  }
  .card:hover { border-color: #58a6ff; }
  .card.dragging { opacity: 0.5; border-color: #58a6ff; }
  .card-title { font-size: 13px; font-weight: 600; color: #f0f6fc; margin-bottom: 6px; }
  .card-body { font-size: 12px; color: #8b949e; line-height: 1.4; margin-bottom: 8px; }
  .card-priority {
    font-size: 11px;
    padding: 1px 6px;
    border-radius: 4px;
    display: inline-block;
  }
  .priority-urgent { background: #da3633; color: #fff; }
  .priority-high { background: #d29922; color: #fff; }
  .priority-medium { background: #30363d; color: #8b949e; }
  .priority-low { background: #21262d; color: #484f58; }
  .card-tags { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px; }
  .card-tag {
    font-size: 10px;
    background: #1a2332;
    color: #58a6ff;
    padding: 1px 6px;
    border-radius: 4px;
  }
  .card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 8px;
    font-size: 11px;
    color: #484f58;
  }
  .card-pr-link { color: #58a6ff; text-decoration: none; font-size: 11px; }
  .card-pr-link:hover { text-decoration: underline; }
  .wip-warning { color: #d29922; font-size: 11px; }
  .modal-overlay {
    display: none;
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.7); z-index: 1000;
    justify-content: center; align-items: center;
  }
  .modal-overlay.active { display: flex; }
  .modal {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    max-width: 700px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
    padding: 24px;
  }
  .modal h2 { font-size: 18px; margin-bottom: 16px; color: #f0f6fc; }
  .modal-section { margin-bottom: 16px; }
  .modal-section h3 {
    font-size: 13px;
    font-weight: 600;
    color: #8b949e;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
    border-bottom: 1px solid #30363d;
    padding-bottom: 4px;
  }
  .modal-section p, .modal-section pre {
    font-size: 13px;
    color: #c9d1d9;
    line-height: 1.5;
  }
  .modal-section pre {
    background: #0d1117;
    padding: 8px;
    border-radius: 4px;
    overflow-x: auto;
    white-space: pre-wrap;
    font-family: monospace;
    font-size: 12px;
  }
  .modal-close {
    float: right;
    background: none;
    border: none;
    color: #8b949e;
    font-size: 20px;
    cursor: pointer;
  }
  .modal-close:hover { color: #f0f6fc; }
</style>
</head>
<body>

<header>
  <h1>csa-CRAFT · Kanban Board</h1>
  <span class="badge" id="task-count"></span>
</header>

<div class="board" id="board"></div>

<div class="modal-overlay" id="modal-overlay">
  <div class="modal" id="modal">
    <button class="modal-close" onclick="closeModal()">&times;</button>
    <div id="modal-content"></div>
  </div>
</div>

<script>
let tasks = [];
let columns = [];

async function loadBoard() {
  const [colsRes, tasksRes] = await Promise.all([
    fetch('/api/columns'),
    fetch('/api/tasks')
  ]);
  columns = await colsRes.json();
  tasks = await tasksRes.json();
  renderBoard();
}

function renderBoard() {
  const board = document.getElementById('board');
  board.innerHTML = '';

  columns.forEach(col => {
    const colTasks = tasks.filter(t => t.column_id === col.id);

    const colEl = document.createElement('div');
    colEl.className = 'column';
    colEl.dataset.columnId = col.id;

    // WIP warning
    let countHtml = `<span class="count">${colTasks.length}</span>`;
    if (col.wip_limit && colTasks.length > col.wip_limit) {
      countHtml += ` <span class="wip-warning">WIP ${col.wip_limit}</span>`;
    }

    colEl.innerHTML = `
      <div class="column-header">
        <h2>${col.name}</h2>
        ${countHtml}
      </div>
      <div class="column-body" data-column-id="${col.id}"></div>
    `;

    // Drag-and-drop event listeners on the column
    const body = colEl.querySelector('.column-body');
    body.addEventListener('dragover', e => {
      e.preventDefault();
      body.classList.add('drag-over');
    });
    body.addEventListener('dragleave', () => {
      body.classList.remove('drag-over');
    });
    body.addEventListener('drop', e => {
      e.preventDefault();
      body.classList.remove('drag-over');
      const taskId = parseInt(e.dataTransfer.getData('text/plain'));
      const newColumnId = parseInt(body.dataset.columnId);
      moveTask(taskId, newColumnId);
    });

    // Render cards
    colTasks.forEach(task => {
      const card = document.createElement('div');
      card.className = 'card';
      card.draggable = true;
      card.dataset.taskId = task.id;

      card.addEventListener('dragstart', e => {
        e.dataTransfer.setData('text/plain', task.id.toString());
        card.classList.add('dragging');
      });
      card.addEventListener('dragend', () => {
        card.classList.remove('dragging');
      });

      card.addEventListener('click', () => showTaskDetail(task));

      // Truncate description for card view
      let desc = task.description || '';
      if (desc.length > 120) desc = desc.substring(0, 120) + '...';

      // PR badge
      let prHtml = '';
      if (task.github_pr_url) {
        prHtml = `<a class="card-pr-link" href="${task.github_pr_url}" target="_blank" onclick="event.stopPropagation()">PR #${task.github_pr_number || '?'}</a>`;
      }

      // Priority
      const priorityClass = `priority-${task.priority}`;

      // Tags
      let tagsHtml = '';
      if (task.tags && task.tags.length > 0) {
        tagsHtml = '<div class="card-tags">' +
          task.tags.map(t => `<span class="card-tag">${t}</span>`).join('') +
          '</div>';
      }

      card.innerHTML = `
        <div class="card-title">${task.title}</div>
        <div class="card-body">${desc}</div>
        <span class="card-priority ${priorityClass}">${task.priority}</span>
        ${tagsHtml}
        <div class="card-footer">
          <span>${task.assignee || 'Unassigned'}</span>
          ${prHtml}
        </div>
      `;

      body.appendChild(card);
    });

    board.appendChild(colEl);
  });

  document.getElementById('task-count').textContent = `${tasks.length} tasks`;
}

async function moveTask(taskId, newColumnId) {
  const res = await fetch(`/api/tasks/${taskId}/move`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ column_id: newColumnId })
  });
  if (res.ok) {
    await loadBoard();
  } else {
    console.error('Failed to move task');
  }
}

function showTaskDetail(task) {
  const overlay = document.getElementById('modal-overlay');
  const content = document.getElementById('modal-content');

  // Determine column name
  const col = columns.find(c => c.id === task.column_id);
  const columnName = col ? col.name : 'unknown';

  // Format tags
  let tagsStr = (task.tags || []).join(', ') || 'none';

  // Format scope
  let scopeHtml = task.pr_scope_affected
    ? task.pr_scope_affected.replace(/^[\\-\\s]+/, '').split('\\n').filter(l => l.trim()).map(l => `<li>${l.trim()}</li>`).join('')
    : '<li>Not populated</li>';

  content.innerHTML = `
    <h2>${task.title}</h2>

    <div class="modal-section">
      <h3>Status</h3>
      <p>Column: <strong>${columnName}</strong> &middot; Priority: <strong>${task.priority}</strong> &middot; Assignee: <strong>${task.assignee || 'Unassigned'}</strong></p>
      <p>Tags: ${tagsStr} &middot; Est. hours: ${task.estimated_hours || 'N/A'}</p>
    </div>

    <div class="modal-section">
      <h3>Description</h3>
      <p>${task.description || 'No description.'}</p>
    </div>

    ${task.github_pr_url ? `
    <div class="modal-section">
      <h3>GitHub PR</h3>
      <p><a href="${task.github_pr_url}" target="_blank">${task.github_pr_url}</a> (PR #${task.github_pr_number})</p>
    </div>` : '
    <div class="modal-section">
      <h3>GitHub PR</h3>
      <p>No PR linked yet.</p>
    </div>'}

    <div class="modal-section">
      <h3>Scope Affected</h3>
      <ul>${scopeHtml}</ul>
    </div>

    ${task.pr_change_summary ? `
    <div class="modal-section">
      <h3>Change Summary</h3>
      <p>${task.pr_change_summary}</p>
    </div>` : ''}

    ${task.pr_behavior_changes ? `
    <div class="modal-section">
      <h3>Behavior Changes</h3>
      <pre>${task.pr_behavior_changes}</pre>
    </div>` : ''}

    ${task.pr_test_suite ? `
    <div class="modal-section">
      <h3>Test Suite</h3>
      <pre>${task.pr_test_suite}</pre>
    </div>` : ''}

    ${task.pr_validation_criteria ? `
    <div class="modal-section">
      <h3>Validation Criteria</h3>
      <pre>${task.pr_validation_criteria}</pre>
    </div>` : ''}

    ${task.pr_unfinished_items ? `
    <div class="modal-section">
      <h3>Unfinished Items</h3>
      <pre>${task.pr_unfinished_items}</pre>
    </div>` : ''}

    <div class="modal-section">
      <h3>Links</h3>
      <p>
        Plan: ${task.development_plan_file || 'N/A'}<br>
        Design doc: ${task.development_description_file || 'N/A'}
      </p>
    </div>

    ${task.pr_description_hash ? `
    <div class="modal-section">
      <h3>Sync Info</h3>
      <p>PR description hash: <code>${task.pr_description_hash}</code></p>
      <p>Created: ${task.created_at} &middot; Updated: ${task.updated_at}</p>
    </div>` : ''}
  `;

  overlay.classList.add('active');
}

function closeModal() {
  document.getElementById('modal-overlay').classList.remove('active');
}

// Close modal on overlay click
document.getElementById('modal-overlay').addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});

// Load on start
loadBoard();
</script>

</body>
</html>
"""

if __name__ == "__main__":
    print(f"Starting kanban server at http://localhost:8051")
    print(f"Reading from: {DB_PATH}")
    APP.run(host="127.0.0.1", port=8051, debug=False)