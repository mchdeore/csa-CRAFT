"""
Sync PR description fields from a template into the kanban board.
Parses a pull_request_template.md filled with values and updates the
corresponding kanban_tasks row.

Usage:
  python3 docs-depo/plans/kanban-board-files/sync_pr.py <task_id> <pr_description_file.md>

The PR description file must follow the structure in .github/pull_request_template.md.
"""

import hashlib
import re
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
DB_PATH = REPO_ROOT / "app" / "database" / "cheddar.db"


def extract_section(text: str, heading: str) -> str:
    """Extract the content under a markdown heading until the next heading or end."""

    # Match the heading, capture everything until next ## heading or end of file
    pattern = rf"## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)"

    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return ""

    content = match.group(1).strip()

    # Strip checkbox markers for cleaner storage
    content = re.sub(r"^\s*-\s*\[ \]\s*", "- ", content, flags=re.MULTILINE)
    content = re.sub(r"^\s*-\s*\[x\]\s*", "- ", content, flags=re.MULTILINE)

    return content


def compute_hash(fields: dict[str, str]) -> str:
    """SHA256 of all PR description fields combined, for staleness detection."""

    combined = "|".join(
        fields.get(key, "") for key in sorted(fields.keys())
    )

    return hashlib.sha256(combined.encode()).hexdigest()[:16]


def sync_pr_description(task_id: int, pr_file_path: str) -> None:
    """Parse PR description file and update kanban_tasks row."""

    pr_path = Path(pr_file_path)
    if not pr_path.exists():
        print(f"Error: PR description file not found: {pr_file_path}")
        sys.exit(1)

    text = pr_path.read_text()

    # Map markdown headings to kanban_tasks columns
    field_map = {
        "Summary": "pr_change_summary",
        "Scope Affected": "pr_scope_affected",
        "Behavior Changes": "pr_behavior_changes",
        "Test Suite": "pr_test_suite",
        "Validation Criteria": "pr_validation_criteria",
        "Unfinished Items / Known Gaps": "pr_unfinished_items",
        "Related Issues / PRs": "pr_related_issues",
    }

    fields: dict[str, str] = {}

    for heading, column in field_map.items():
        content = extract_section(text, heading)
        fields[column] = content

    # Compute hash for all fields
    fields["pr_description_hash"] = compute_hash(fields)

    connection = sqlite3.connect(str(DB_PATH))
    cursor = connection.cursor()

    # Verify task exists
    cursor.execute("SELECT id, title FROM kanban_tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()

    if task is None:
        print(f"Error: No kanban task found with id={task_id}")
        connection.close()
        sys.exit(1)

    print(f"Updating task #{task_id}: {task[1]}")

    # Build SET clause dynamically
    set_clauses = []
    values: list[str] = []

    for column, value in fields.items():
        set_clauses.append(f"{column} = ?")
        values.append(value)

    values.append(task_id)

    sql = f"UPDATE kanban_tasks SET {', '.join(set_clauses)}, updated_at = datetime('now') WHERE id = ?"
    cursor.execute(sql, values)

    connection.commit()
    connection.close()

    print(f"Updated {len(fields)} fields for task #{task_id}.")
    print(f"Description hash: {fields['pr_description_hash']}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 docs-depo/plans/kanban-board-files/sync_pr.py <task_id> <pr_description_file.md>")
        print("Example: python3 docs-depo/plans/kanban-board-files/sync_pr.py 2 pr-descriptions/aggregation-pipeline-pr.md")
        sys.exit(1)

    task_id = int(sys.argv[1])
    pr_file = sys.argv[2]
    sync_pr_description(task_id, pr_file)


if __name__ == "__main__":
    main()