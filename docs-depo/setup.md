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

```bash
pytest                              # all 5 testpaths from pyproject.toml
pytest app/tests/test_architecture.py   # structural rules only
```

Rules the tests enforce: see `app/tests/CODEBASE_RULES.md`.

## Pre-commit

```bash
pre-commit install          # once
pre-commit run --all-files  # ad-hoc
```

Runs ruff, bandit, detect-secrets, file-hygiene hooks (configured in `.pre-commit-config.yaml`).
