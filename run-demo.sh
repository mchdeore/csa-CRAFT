#!/bin/bash
# run-demo.sh — seed database and start demo server
set -e

echo "=== CSA Cheddar Demo Quick ==="
echo ""

# Seed the database with missions and demo users
echo "[1/2] Seeding database..."
python -m storage.database.demo_seed

# Start the demo server
echo ""
echo "[2/2] Starting demo server on http://localhost:8050"
echo ""
python -m demo.runner