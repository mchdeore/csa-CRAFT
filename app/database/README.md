# app/database

Filesystem location for the runtime SQLite DB (`cheddar.db`, path hardcoded in `storage/store.py`). Not a Python package in practice; the `__init__.py` is a historical artifact. Real migrations live in `storage/database/migrations/`.
