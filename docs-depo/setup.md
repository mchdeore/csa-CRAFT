# Setup & Run

Dev-facing notes. Not a public README. For new contributors: pair with an in-person walkthrough; this file is a reminder, not an onboarding.

## Install

```bash
pip install -r app/requirements.txt
cp app/.env.example app/.env   # then fill in the Azure OpenAI / Guardian / Cohere keys
```

If `app/.env` is left unconfigured, chat falls back to echoing the input word by word.

## Run

```bash
python app.py
```

Dash app serves on http://localhost:8050. First page is the login screen (see `auth/provider.py` for the in-memory user list).

## Tests

Three-tier testing system. See `app/tests/CODEBASE_RULES.md` for the full philosophy.

```bash
# Tier 1: Run doctests during development (fast, catches obvious breaks)
pytest --doctest-modules tools/

# Tier 2: Run all tests including feature tests (pre-merge check)
pytest

# Tier 3: Run only architecture/rules enforcement
pytest app/tests/test_architecture.py
pytest app/tests/test_rules.py

# Run specific feature tests
pytest storage/tests/
pytest auth/tests/
```

Rules the tests enforce: see `app/tests/CODEBASE_RULES.md`.
    30|
## Pre-commit

```bash
pre-commit install          # once
pre-commit run --all-files  # ad-hoc
```

Runs ruff, bandit, detect-secrets, file-hygiene hooks (configured in `.pre-commit-config.yaml`). This is the final quality gate — catches blind spots before code hits the repo.
