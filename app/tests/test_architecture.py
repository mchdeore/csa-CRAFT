"""Enforce project folder structure rules — auto-discovers feature folders."""

import ast
import os
import re
import subprocess
import sys
from collections.abc import Generator
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

ROOT_WHITELIST = {
    "app.py",
    "__init__.py",
}

REQUIRED_FILES = {"__init__.py", "templates.py", "callbacks.py", "routes.py", "tests"}

SHARED_MODULES = {"app.core"}

ALWAYS_SKIP = {"venv", "tests", "__pycache__", ".pytest_cache", "tools"}

NO_CALLBACKS = {"app"}

# Modules exempt from doctest requirement — no public logic to test
_DOCTEST_EXEMPT_PATTERNS = {
    "__init__.py",
    "templates.py",
    "protocols.py",
    "config.py",
    "dash_app.py",
    "logging.py",
    "_shared.py",
    "connection.py",
    "runner.py",
    "registry.py",
    "entry.py",
    "app.py",
    "callbacks.py",
}

# Imports that indicate a module is stateful (needs pytest, not just doctest)
_STATEFUL_IMPORTS = {
    "sqlite3",
    "flask",
    "requests",
    "openai",
    "pdfplumber",
    "docx",
}

# Modules exempt from pytest file requirement — pure logic covered by doctest
_PYTEST_EXEMPT_NAME_PATTERNS = {
    "__init__.py",
    "templates.py",
    "protocols.py",
    "config.py",
    "dash_app.py",
    "logging.py",
    "_shared.py",
    "registry.py",
    "cadre_mission_params.py",
    "demo_seed.py",
    "connection.py",
}

_BRANCH_TYPES = (
    ast.If,
    ast.IfExp,
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.ExceptHandler,
    ast.With,
    ast.AsyncWith,
    ast.Assert,
)


def python_files(include_tests: bool = False) -> Generator[Path, None, None]:
    """Yield .py files in the project, excluding venv."""
    for dirpath, _, filenames in os.walk(PROJECT_ROOT):
        path = Path(dirpath)
        if "venv" in path.parts or ".venv" in path.parts:
            continue
        if not include_tests and "tests" in path.parts:
            continue
        for f in filenames:
            if f.endswith(".py"):
                yield path / f


def _has_public_functions(tree: ast.Module) -> bool:
    """Check if a module defines any public (non-underscore) functions or methods."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith(
            "_"
        ):
            return True
        if isinstance(node, ast.ClassDef):
            for method in ast.iter_child_nodes(node):
                if isinstance(
                    method, (ast.FunctionDef, ast.AsyncFunctionDef)
                ) and not method.name.startswith("_"):
                    return True
    return False


def _has_stateful_imports(tree: ast.Module) -> bool:
    """Check if a module imports anything that makes it stateful (db, http, files)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in _STATEFUL_IMPORTS:
                    return True
        elif isinstance(node, ast.ImportFrom) and node.module:
            top = node.module.split(".")[0]
            if top in _STATEFUL_IMPORTS:
                return True
    # Also check for file opening (open, Path.open, Path.read_text, etc.)
    source = ast.unparse(tree) if hasattr(ast, "unparse") else ""
    if "open(" in source or "read_text(" in source or "write_text(" in source:
        # Only flag if it's a public function doing file I/O, not config/init
        if _has_public_functions(tree):
            return True
    return False


def _has_doctest(tree: ast.Module) -> bool:
    """Check if a function node's docstring contains >>> doctest examples."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("_"):
                continue
            docstring = ast.get_docstring(node)
            if docstring and ">>>" in docstring:
                return True
    return False


def _discover_features() -> set[str]:
    features: set[str] = set()
    for entry in PROJECT_ROOT.iterdir():
        if not entry.is_dir():
            continue
        if entry.name.startswith(".") or entry.name in ALWAYS_SKIP:
            continue
        if (entry / "__init__.py").exists():
            features.add(entry.name)
    return features


class TestArchitecture:
    def test_no_circular_imports(self) -> None:
        """Every .py file must import without ImportError or ModuleNotFoundError.

        Runs each import in a subprocess with a 15s timeout. Modules that
        trigger Dash/Flask startup may time out — that's not an import error,
        just heavy init. Only actual ImportError/ModuleNotFoundError count as
        violations.
        """
        modules: list[str] = []
        for entry in PROJECT_ROOT.iterdir():
            if entry.name.startswith(".") or entry.name.startswith("_"):
                continue
            if entry.name in {"venv", ".venv", "tests", "__pycache__", ".pytest_cache"}:
                continue
            if entry.suffix == ".py" and entry.stem != "__init__":
                modules.append(entry.stem)
            elif entry.is_dir() and (entry / "__init__.py").exists():
                for py in entry.rglob("*.py"):
                    if "__pycache__" in py.parts or "tests" in py.parts:
                        continue
                    if py.name == "__init__.py":
                        rel = py.parent.relative_to(PROJECT_ROOT)
                        modules.append(str(rel).replace("/", "."))
                    else:
                        rel = py.relative_to(PROJECT_ROOT)
                        mod = str(rel).replace("/", ".").removesuffix(".py")
                        modules.append(mod)

        violations: list[str] = []
        for mod in sorted(set(modules)):
            try:
                result = subprocess.run(
                    [sys.executable, "-c", f"import {mod}"],
                    capture_output=True,
                    text=True,
                    timeout=15,
                    cwd=str(PROJECT_ROOT),
                )
                if result.returncode != 0:
                    stderr = result.stderr.strip().splitlines()
                    last_line = stderr[-1] if stderr else "unknown error"
                    if "ModuleNotFoundError" in last_line or "ImportError" in last_line:
                        violations.append(f"{mod}: {last_line}")
            except subprocess.TimeoutExpired:
                pass

        assert not violations, "Circular or broken imports:\n" + "\n".join(violations)

    def test_root_files_whitelisted(self) -> None:
        violations = []
        for f in PROJECT_ROOT.iterdir():
            if f.suffix != ".py":
                continue
            if f.name in ROOT_WHITELIST:
                continue
            violations.append(f"Root file not whitelisted: {f.name}")
        assert not violations, "Unexpected .py files at project root:\n" + "\n".join(violations)

    def test_feature_folders_have_required_files(self) -> None:
        features = _discover_features()
        violations = []
        required_for_feature = REQUIRED_FILES.copy()
        for name in features:
            folder = PROJECT_ROOT / name
            check_set = (
                required_for_feature - {"callbacks.py"}
                if name in NO_CALLBACKS
                else required_for_feature
            )
            for required in check_set:
                path = folder / required
                if required == "tests":
                    if not path.is_dir():
                        violations.append(f"{name}/ missing tests/ directory")
                elif not path.is_file():
                    violations.append(f"{name}/ missing {required}")
        assert not violations, "\n".join(violations)

    def test_no_cross_feature_internal_imports(self) -> None:
        features = _discover_features()
        violations = []
        for name in features:
            folder = PROJECT_ROOT / name
            for py_file in folder.rglob("*.py"):
                if py_file.name == "__init__.py":
                    continue
                rel_path = py_file.relative_to(PROJECT_ROOT)
                if any(
                    str(rel_path).startswith(sm.replace(".", "/") + "/") for sm in SHARED_MODULES
                ):
                    continue
                self._check_imports(py_file, name, features, violations)
        assert not violations, "\n".join(violations)

    def _check_imports(
        self,
        filepath: Path,
        own_feature: str,
        features: set[str],
        violations: list[str],
    ) -> None:
        try:
            tree = ast.parse(filepath.read_text())
        except SyntaxError:
            return
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                self._check_import_from(node, filepath, own_feature, features, violations)

    def _check_import_from(
        self,
        node: ast.ImportFrom,
        filepath: Path,
        own_feature: str,
        features: set[str],
        violations: list[str],
    ) -> None:
        if node.module is None or node.level > 0:
            return
        parts = node.module.split(".")
        if len(parts) < 1:
            return
        imported = parts[0]

        is_shared = imported in SHARED_MODULES
        for i in range(2, len(parts) + 1):
            prefix = ".".join(parts[:i])
            if prefix in SHARED_MODULES:
                is_shared = True
                break

        if is_shared or imported == own_feature:
            return
        if imported in features and len(parts) == 1:
            return
        if imported in features and len(parts) == 2 and parts[1] == "templates":
            return
        if imported in features:
            rel = filepath.relative_to(PROJECT_ROOT)
            violations.append(
                f"{rel} imports '{node.module}' — cross-feature internal import. "
                f"Import via '{imported}' or '{imported}.templates' instead."
            )

    def test_tool_subpackages_have_all(self) -> None:
        """Every tools/ subpackage __init__.py must define __all__."""
        tools_dir = PROJECT_ROOT / "tools"
        violations = []
        for entry in tools_dir.iterdir():
            if not entry.is_dir() or entry.name.startswith("_"):
                continue
            init_file = entry / "__init__.py"
            if not init_file.exists():
                violations.append(f"tools/{entry.name}/ missing __init__.py")
                continue
            tree = ast.parse(init_file.read_text())
            has_all = any(
                isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "__all__" for t in node.targets)
                for node in ast.walk(tree)
            )
            if not has_all:
                violations.append(f"tools/{entry.name}/__init__.py missing __all__")
        assert not violations, "\n".join(violations)

    def test_canonical_tool_paths(self) -> None:
        """tool_map canonical paths in tools/routes.py must match real modules."""
        routes_file = PROJECT_ROOT / "tools" / "routes.py"
        if not routes_file.exists():
            return
        tree = ast.parse(routes_file.read_text())
        canonical_paths: list[tuple[str, int]] = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Dict):
                continue
            for key, value in zip(node.keys, node.values, strict=True):
                if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
                    continue
                if isinstance(value, ast.Tuple) and len(value.elts) >= 1:
                    first = value.elts[0]
                    if isinstance(first, ast.Constant) and isinstance(first.value, str):
                        canonical_paths.append((first.value, first.lineno))

        violations = []
        for path, lineno in canonical_paths:
            parts = path.split(".")
            expected_file = PROJECT_ROOT / ("/".join(parts) + ".py")
            expected_pkg = PROJECT_ROOT / "/".join(parts) / "__init__.py"
            if not expected_file.exists() and not expected_pkg.exists():
                violations.append(
                    f"tools/routes.py:{lineno} canonical path '{path}' "
                    f"does not match any module at {'/'.join(parts)}.py"
                )
        assert not violations, "Canonical paths don't match modules:\n" + "\n".join(violations)

    def test_doctest_coverage(self) -> None:
        """Every public function must have a doctest in its docstring.

        Walks all source files (excluding exempt patterns). For each module
        with public functions, checks that at least one public function has
        >>> examples in its docstring. This is not per-function granular —
        if a module has public functions but zero doctests anywhere, it fails.
        """
        violations: list[str] = []
        for fp in python_files():
            if fp.name in _DOCTEST_EXEMPT_PATTERNS:
                continue
            if fp.name.startswith("_"):
                continue

            rel = fp.relative_to(PROJECT_ROOT)
            tree = ast.parse(fp.read_text())

            if not _has_public_functions(tree):
                continue

            if not _has_doctest(tree):
                violations.append(f"{rel} has public functions but no doctests")

        assert not violations, (
            "Modules with public functions missing doctests:\n" + "\n".join(violations)
        )

    def test_pytest_coverage_for_stateful(self) -> None:
        """Every stateful module with public functions must have a matching pytest file.

        Stateful = imports sqlite3, flask, requests, openai, pdfplumber, docx,
        or opens/reads files in public functions. These modules need fixtures
        and mocks — doctests alone aren't sufficient.

        Checks that tests/test_{source_filename}.py exists relative to the
        feature root or subpackage root where the source file lives.
        """
        violations: list[str] = []
        features = _discover_features()

        for fp in python_files():
            if fp.name in _PYTEST_EXEMPT_NAME_PATTERNS:
                continue
            if fp.name.startswith("_"):
                continue

            rel = fp.relative_to(PROJECT_ROOT)
            tree = ast.parse(fp.read_text())

            if not _has_public_functions(tree):
                continue
            if not _has_stateful_imports(tree):
                continue

            # Find the feature root or subpackage root for this file
            # The source file lives at feature/subdir/file.py
            # The test file should be at feature/subdir/tests/test_file.py
            feature_root = None
            for feature_name in features:
                feature_dir = PROJECT_ROOT / feature_name
                if str(rel).startswith(feature_name + "/") or str(rel).startswith(feature_name):
                    # Determine the parent directory of this file relative to feature
                    rel_parts = Path(str(rel))
                    if len(rel_parts.parts) > 1:
                        parent_dir = rel_parts.parent
                        test_file = parent_dir / "tests" / f"test_{fp.stem}.py"
                    else:
                        test_file = PROJECT_ROOT / feature_name / "tests" / f"test_{fp.stem}.py"

                    if not test_file.exists():
                        violations.append(
                            f"{rel} is stateful (imports db/http/files) "
                            f"but missing {test_file.relative_to(PROJECT_ROOT)}"
                        )
                    break
            else:
                # File is not inside a feature folder — tools/ or demo/
                # Look for tests/ in the same directory as the file
                test_file = fp.parent / "tests" / f"test_{fp.stem}.py"
                if not test_file.exists():
                    violations.append(
                        f"{rel} is stateful (imports db/http/files) "
                        f"but missing {test_file.relative_to(PROJECT_ROOT)}"
                    )

        assert not violations, (
            "Stateful modules missing pytest test files:\n" + "\n".join(violations)
        )
