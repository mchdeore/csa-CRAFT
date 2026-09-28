"""Local filesystem data source — reads files from a root directory."""

import mimetypes
from datetime import datetime, timezone
from pathlib import Path

from app.core.logging import log_function_call
from connectors.protocols import DataSource, FileContent, FileEntry

# Known extensions for files that mimetypes might not cover
_EXTENSION_TYPES: dict[str, str] = {
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".xls": "application/vnd.ms-excel",
    ".csv": "text/csv",
    ".txt": "text/plain",
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


class LocalFileSource(DataSource):
    """Read files from a local directory. Mounted network shares work transparently."""

    def __init__(self, root: Path) -> None:
        self._root = root.resolve()

    # Reject paths that escape the root directory
    def _resolve(self, relative_path: str) -> Path:
        resolved = (self._root / relative_path).resolve()
        if not str(resolved).startswith(str(self._root)):
            raise ValueError(
                f"Path '{relative_path}' escapes root directory. "
                f"Only paths under {self._root} are allowed."
            )
        return resolved

    # Guess MIME type from file extension
    def _guess_mime(self, path: Path) -> str:
        suffix = path.suffix.lower()
        return _EXTENSION_TYPES.get(suffix) or mimetypes.guess_type(str(path))[0] or ""

    def list_files(self, path: str = "") -> list[FileEntry]:
        log_function_call("connectors.local_files", "list_files", path=path)
        target = self._resolve(path)
        if not target.exists():
            return []

        entries: list[FileEntry] = []
        for child in sorted(target.iterdir()):
            if child.is_file():
                stat = child.stat()
                entries.append(
                    FileEntry(
                        name=child.name,
                        path=str(child.relative_to(self._root)),
                        size=stat.st_size,
                        modified=datetime.fromtimestamp(
                            stat.st_mtime,
                            tz=timezone.utc,
                        ).isoformat(),
                        mime_type=self._guess_mime(child),
                    )
                )
        return entries

    def read_file(self, path: str) -> FileContent:
        log_function_call("connectors.local_files", "read_file", path=path)
        target = self._resolve(path)
        if not target.is_file():
            raise FileNotFoundError(f"File not found: {path}")
        return FileContent(
            name=target.name,
            path=path,
            content=target.read_bytes(),
            mime_type=self._guess_mime(target),
        )

    def search(self, query: str) -> list[FileEntry]:
        """Case-insensitive filename search within root directory."""
        log_function_call("connectors.local_files", "search", query=query)
        query_lower = query.lower()
        results: list[FileEntry] = []
        for child in self._root.rglob("*"):
            if child.is_file() and query_lower in child.name.lower():
                stat = child.stat()
                results.append(
                    FileEntry(
                        name=child.name,
                        path=str(child.relative_to(self._root)),
                        size=stat.st_size,
                        modified=datetime.fromtimestamp(
                            stat.st_mtime,
                            tz=timezone.utc,
                        ).isoformat(),
                        mime_type=self._guess_mime(child),
                    )
                )
        return results
