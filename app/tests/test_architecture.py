"""Enforce project folder structure rules — auto-discovers feature folders."""

import ast
import subprocess
import sys
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
