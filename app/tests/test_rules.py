"""Code quality tests for things pyright and ruff don't catch."""

import ast
import os
import re
import sys
from collections.abc import Generator
from pathlib import Path

MAX_FUNCTION_LINES = 250
MAX_CYCLOMATIC_COMPLEXITY = 15
PROJECT_ROOT = Path(__file__).parent.parent.parent
REQUIREMENTS_FILE = PROJECT_ROOT / "app" / "requirements.txt"

IMPORT_TO_PACKAGE: dict[str, str] = {
    "dotenv": "python_dotenv",
    "PIL": "pillow",
    "cv2": "opencv_python",
    "bs4": "beautifulsoup4",
    "yaml": "pyyaml",
    "sklearn": "scikit_learn",
    "gi": "pygobject",
    "attr": "attrs",
    "docx": "python_docx",
}

_REQUIREMENT_NAME_RE = re.compile(r"^([A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?)")

# Files exempt from the "must call log_function_call" rule.
# These are either pure re-exports, type definitions, config, templates,
# shared constants/helpers, or infrastructure that runs at import time.
_LOGGING_EXEMPT_PATTERNS = {
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
}

# Files where public functions are Dash callbacks or stubs — logging happens
# in the routes they call, not in the callback wiring itself.
_LOGGING_EXEMPT_PATHS = {
    "auth/callbacks.py",
    "app/routes.py",
}


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
        if not line or line.startswith(("#", "-")):
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


def _count_complexity(node: ast.AST) -> int:
    """Calculate McCabe cyclomatic complexity for a function node."""
    complexity = 1
    for child in ast.walk(node):
        if isinstance(child, _BRANCH_TYPES):
            complexity += 1
        elif isinstance(child, ast.BoolOp):
            complexity += len(child.values) - 1
    return complexity


class TestCodeQuality:
    def test_function_length_limit(self) -> None:
        violations: list[str] = []
        for fp in python_files():
            tree = ast.parse(fp.read_text())
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, ast.ClassDef):
                    for method in ast.iter_child_nodes(node):
                        if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            self._check_length(fp, method, violations)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    self._check_length(fp, node, violations)
        assert not violations, "Functions too long:\n" + "\n".join(violations)

    @staticmethod
    def _check_length(fp: Path, node: ast.AST, violations: list[str]) -> None:
        # pyright doesn't understand that ast.FunctionDef inherits end_lineno/lineno
        func_node = node  # type: ignore[assignment]
        if not hasattr(func_node, "end_lineno") or func_node.end_lineno is None:
            return
        length = func_node.end_lineno - func_node.lineno + 1
        if length > MAX_FUNCTION_LINES:
            violations.append(
                f"{fp.name}:{func_node.lineno} {func_node.name} "
                f"is {length} lines (max {MAX_FUNCTION_LINES})"
            )

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
                            top,
                            fp.name,
                            node.lineno,
                            required,
                            stdlib,
                            local,
                            violations,
                        )
                elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                    top = node.module.split(".")[0]
                    self._check_import(
                        top,
                        fp.name,
                        node.lineno,
                        required,
                        stdlib,
                        local,
                        violations,
                    )

        assert not violations, "Imports not listed in requirements.txt:\n" + "\n".join(violations)

    @staticmethod
    def _check_import(
        module: str,
        filename: str,
        line: int,
        required: set[str],
        stdlib: frozenset[str],
        local: set[str],
        violations: list[str],
    ) -> None:
        if module in stdlib:
            return
        if module in local:
            return
        pkg_name = IMPORT_TO_PACKAGE.get(module, module).lower().replace("-", "_")
        if pkg_name not in required:
            violations.append(f"{filename}:{line} imports '{module}' — add it to requirements.txt")

    def test_logging_coverage(self) -> None:
        """Non-trivial modules with public functions must use log_function_call."""
        violations: list[str] = []
        for fp in python_files():
            if fp.name in _LOGGING_EXEMPT_PATTERNS:
                continue
            if fp.name.startswith("_"):
                continue
            rel = fp.relative_to(PROJECT_ROOT)
            if str(rel) in _LOGGING_EXEMPT_PATHS:
                continue
            source = fp.read_text()
            tree = ast.parse(source)
            if not _has_public_functions(tree):
                continue
            if "log_function_call" not in source:
                violations.append(f"{rel} has public functions but no log_function_call")
        assert not violations, "Missing logging:\n" + "\n".join(violations)

    def test_cyclomatic_complexity(self) -> None:
        """No top-level function or method exceeds the complexity limit."""
        violations: list[str] = []
        for fp in python_files():
            tree = ast.parse(fp.read_text())
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, ast.ClassDef):
                    for method in ast.iter_child_nodes(node):
                        if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            self._check_complexity(fp, method, violations)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    self._check_complexity(fp, node, violations)
        assert not violations, "Functions too complex:\n" + "\n".join(violations)

    @staticmethod
    def _check_complexity(fp: Path, node: ast.AST, violations: list[str]) -> None:
        # pyright doesn't know ast.FunctionDef has lineno/name on AST base type
        func_node = node  # type: ignore[assignment]
        cc = _count_complexity(node)
        if cc > MAX_CYCLOMATIC_COMPLEXITY:
            rel = fp.relative_to(PROJECT_ROOT)
            violations.append(
                f"{rel}:{func_node.lineno} {func_node.name} "  # type: ignore[operator, union-attr]
                f"has complexity {cc} (max {MAX_CYCLOMATIC_COMPLEXITY})"
            )

    def test_no_print_statements(self) -> None:
        """Production code must use logging, not print()."""
        violations: list[str] = []
        for fp in python_files():
            tree = ast.parse(fp.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func = node.func
                    if isinstance(func, ast.Name) and func.id == "print":
                        rel = fp.relative_to(PROJECT_ROOT)
                        violations.append(f"{rel}:{node.lineno} uses print()")
        assert not violations, "Use logging instead of print():\n" + "\n".join(violations)

    def test_no_bare_except(self) -> None:
        """Bare except: clauses hide bugs — always catch a specific exception."""
        violations: list[str] = []
        for fp in python_files():
            tree = ast.parse(fp.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.ExceptHandler) and node.type is None:
                    rel = fp.relative_to(PROJECT_ROOT)
                    violations.append(f"{rel}:{node.lineno} bare except: — catch a specific type")
        assert not violations, "Bare except clauses found:\n" + "\n".join(violations)

    def test_no_hardcoded_secrets(self) -> None:
        """Flag variables that look like hardcoded secrets."""
        secret_patterns = re.compile(
            r"(api_key|secret|password|token|auth_key)\s*=\s*['\"][^'\"]{8,}['\"]",
            re.IGNORECASE,
        )
        violations: list[str] = []
        for fp in python_files():
            for lineno, line in enumerate(fp.read_text().splitlines(), 1):
                if line.strip().startswith("#"):
                    continue
                if secret_patterns.search(line):
                    if "os.environ" in line or "os.getenv" in line or "environ.get" in line:
                        continue
                    rel = fp.relative_to(PROJECT_ROOT)
                    violations.append(f"{rel}:{lineno} possible hardcoded secret")
        assert not violations, "Hardcoded secrets detected:\n" + "\n".join(violations)

    def test_no_todo_without_issue(self) -> None:
        """TODOs in code should reference who owns them or a tracking issue."""
        todo_re = re.compile(r"#\s*TODO(?!\s*\()", re.IGNORECASE)
        violations: list[str] = []
        for fp in python_files():
            for lineno, line in enumerate(fp.read_text().splitlines(), 1):
                if todo_re.search(line):
                    rel = fp.relative_to(PROJECT_ROOT)
                    violations.append(
                        f"{rel}:{lineno} TODO without owner — use TODO(name) or TODO(#issue)"
                    )
        assert not violations, "Unattributed TODOs:\n" + "\n".join(violations)

    def test_type_annotations_on_public_functions(self) -> None:
        """Public functions and methods must have a return type annotation."""
        violations: list[str] = []
        for fp in python_files():
            tree = ast.parse(fp.read_text())
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, ast.ClassDef):
                    for method in ast.iter_child_nodes(node):
                        if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            self._check_return_annotation(fp, method, violations)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    self._check_return_annotation(fp, node, violations)
        assert not violations, "Missing return type annotations:\n" + "\n".join(violations)

    @staticmethod
    def _check_return_annotation(
        fp: Path,
        node: ast.FunctionDef | ast.AsyncFunctionDef,
        violations: list[str],
    ) -> None:
        if node.name.startswith("_"):
            return
        if node.returns is None:
            rel = fp.relative_to(PROJECT_ROOT)
            violations.append(f"{rel}:{node.lineno} {node.name}() missing return annotation")
