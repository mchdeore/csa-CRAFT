#!/bin/bash
# Set up the kanban board in the existing cheddar.db database.
# Run from repo root: bash docs-depo/plans/kanban-board-files/setup.sh

set -euo pipefail

DB="app/database/cheddar.db"
SCHEMA="docs-depo/plans/kanban-board-files/schema.sql"
SEED="docs-depo/plans/kanban-board-files/seed.sql"

echo "=== Applying kanban schema to $DB ==="
sqlite3 "$DB" < "$SCHEMA"
echo "Schema applied."

echo "=== Seeding default columns and example task ==="
sqlite3 "$DB" < "$SEED"
echo "Seed data inserted."

echo "=== Done. Run queries with: sqlite3 $DB < docs-depo/plans/kanban-board-files/queries.sql ==="