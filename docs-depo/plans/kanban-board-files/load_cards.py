"""
Load kanban cards from cards.json into the database.
Run with: python3 docs-depo/plans/kanban-board-files/load_cards.py
"""

import json
import sqlite3
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
DB_PATH = REPO_ROOT / "app" / "database" / "cheddar.db"
CARDS_PATH = Path(__file__).resolve().parent / "cards.json"


def get_column_id(cursor: sqlite3.Cursor, column_name: str) -> int:
    cursor.execute("SELECT id FROM kanban_columns WHERE name = ?", (column_name,))
    result = cursor.fetchone()

    if result is None:
        raise ValueError(
            f"Column '{column_name}' not found in kanban_columns. "
            f"Run setup.sh first to seed the default columns."
        )

    return result[0]


def insert_cards(cards: list[dict]) -> int:
    connection = sqlite3.connect(str(DB_PATH))
    cursor = connection.cursor()

    count = 0
    for card in cards:
        column_id = get_column_id(cursor, card["column"])

        cursor.execute(
            """
            INSERT INTO kanban_tasks (
                title, description, column_id,
                github_pr_url, github_pr_number,
                development_plan_file, development_description_file,
                priority, assignee, tags, estimated_hours
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                card["title"],
                card["description"],
                column_id,
                card.get("github_pr_url"),
                card.get("github_pr_number"),
                card.get("development_plan_file"),
                card.get("development_description_file"),
                card.get("priority", "medium"),
                card.get("assignee"),
                json.dumps(card.get("tags", [])),
                card.get("estimated_hours"),
            ),
        )
        count += 1

    connection.commit()
    connection.close()
    return count


def main():
    with open(CARDS_PATH) as f:
        cards = json.load(f)

    if not cards:
        print("cards.json is empty — nothing to load.")
        return

    loaded = insert_cards(cards)
    print(f"Loaded {loaded} cards into the kanban board.")


if __name__ == "__main__":
    main()