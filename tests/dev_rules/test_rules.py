"""Code quality tests for things pyright and ruff don't catch."""

import ast
import os
import re
import sys
from collections.abc import Generator
from pathlib import Path

MAX_FUNCTION_LINES = 30
PROJECT_ROOT = Path(__file__).parent.parent.parent
REQUIREMENTS_FILE = PROJECT_ROOT / "requirements.txt"

IMPORT_TO_PACKAGE: dict[str, str] = {
    "dotenv": "python_dotenv",
    "PIL": "pillow",
    "cv2": "opencv_python",
    "bs4": "beautifulsoup4",
    "yaml": "pyyaml",
    "sklearn": "scikit_learn",
    "gi": "pygobject",
    "attr": "attrs",
}

_REQUIREMENT_NAME_RE = re.compile(r"^([A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?)")


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


def read_requirements() -> set[str]:
    """Return normalized package names from requirements.txt."""
    if not REQUIREMENTS_FILE.exists():
        return set()
    names: set[str] = set()
    for line in REQUIREMENTS_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        match = _REQUIREMENT_NAME_RE.match(line)
        if match:
            names.add(match.group(1).lower().replace("-", "_").replace(".", "_"))
    return names


def local_module_names() -> set[str]:
    """Return top-level .py file stems in the project root (local importable modules)."""
    names: set[str] = set()
    for f in PROJECT_ROOT.iterdir():
        if f.suffix == ".py" and f.stem != "__init__":
            names.add(f.stem)
    for f in PROJECT_ROOT.iterdir():
        if f.is_dir() and (f / "__init__.py").exists() and f.name != "venv":
            names.add(f.name)
    return names


class TestCodeQuality:
    def test_function_length_limit(self) -> None:
        violations: list[str] = []
        for fp in python_files():
            tree = ast.parse(fp.read_text())
            for node in ast.walk(tree):
                if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if node.end_lineno is None:
                    continue
                length = node.end_lineno - node.lineno + 1
                if length > MAX_FUNCTION_LINES:
                    violations.append(
                        f"{fp.name}:{node.lineno} {node.name} "
                        f"is {length} lines (max {MAX_FUNCTION_LINES})"
                    )
        assert not violations, "Functions too long:\n" + "\n".join(violations)

    def test_imports_in_requirements(self) -> None:
        """Every third-party import must be listed in requirements.txt."""
        required = read_requirements()
        stdlib = sys.stdlib_module_names
        local = local_module_names()
        violations: list[str] = []

        for fp in python_files(include_tests=True):
            tree = ast.parse(fp.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        top = alias.name.split(".")[0]
                        self._check_import(
                            top, fp.name, node.lineno, required, stdlib, local, violations,
                        )
                elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                    top = node.module.split(".")[0]
                    self._check_import(
                        top, fp.name, node.lineno, required, stdlib, local, violations,
                    )

        assert not violations, (
            "Imports not listed in requirements.txt:\n" + "\n".join(violations)
        )

    @staticmethod
    def _check_import(
        module: str, filename: str, line: int,
        required: set[str], stdlib: frozenset[str],
        local: set[str], violations: list[str],
    ) -> None:
        if module in stdlib:
            return
        if module in local:
            return
        pkg_name = IMPORT_TO_PACKAGE.get(module, module).lower().replace("-", "_")
        if pkg_name not in required:
            violations.append(
                f"{filename}:{line} imports '{module}' — add it to requirements.txt"
            )
