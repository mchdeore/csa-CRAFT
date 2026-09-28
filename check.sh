#!/usr/bin/env bash
set -euo pipefail

# Local dev check suite — run before every push.
# Usage: ./check.sh           (run all checks)
#        ./check.sh --quick   (skip slow checks: pyright, circular imports)

QUICK=false
if [[ "${1:-}" == "--quick" ]]; then
    QUICK=true
fi

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BOLD='\033[1m'
NC='\033[0m'

FAILED=0

run_check() {
    local name="$1"
    shift
    printf "${BOLD}%-40s${NC}" "$name"
    if output=$("$@" 2>&1); then
        printf "${GREEN}PASS${NC}\n"
    else
        printf "${RED}FAIL${NC}\n"
        echo "$output" | head -30
        echo ""
        FAILED=$((FAILED + 1))
    fi
}

echo ""
echo "========================================="
echo "  csa-cheddar local check suite"
echo "========================================="
echo ""

# 1. Ruff lint
run_check "ruff lint" \
    venv/bin/ruff check .

# 2. Ruff format check
run_check "ruff format" \
    venv/bin/ruff format --check .

# 3. Bandit security scan
run_check "bandit (SAST)" \
    venv/bin/bandit -c pyproject.toml -r . -q 2>/dev/null

# 4. Architecture tests (structure, imports, canonical paths)
run_check "architecture tests" \
    venv/bin/python -m pytest app/tests/test_architecture.py -x -q

# 5. Code quality tests (length, complexity, logging, secrets, TODOs)
run_check "code quality tests" \
    venv/bin/python -m pytest app/tests/test_rules.py -x -q

# 6. Unit tests across all features
run_check "unit tests" \
    venv/bin/python -m pytest -x -q --ignore=app/tests/test_architecture.py --ignore=app/tests/test_rules.py

# 7. Pyright type checking (slow — skip in quick mode)
if [[ "$QUICK" == false ]]; then
    run_check "pyright type check" \
        venv/bin/pyright
else
    printf "${BOLD}%-40s${YELLOW}SKIP (--quick)${NC}\n" "pyright type check"
fi

echo ""
echo "========================================="
if [[ $FAILED -eq 0 ]]; then
    printf "  ${GREEN}${BOLD}All checks passed${NC}\n"
else
    printf "  ${RED}${BOLD}$FAILED check(s) failed${NC}\n"
fi
echo "========================================="
echo ""

exit $FAILED
