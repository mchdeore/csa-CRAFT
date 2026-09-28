"""Data source abstraction for file access — SharePoint, SMB, local."""

from typing import Protocol


class FileEntry:
    """Metadata about a single file in a data source."""

    def __init__(
        self,
        name: str,
        path: str,
        size: int,
        modified: str,
        mime_type: str = "",
    ) -> None:
        self.name = name
        self.path = path
        self.size = size
        self.modified = modified
        self.mime_type = mime_type


class FileContent:
    """Raw file content and metadata from a data source."""

    def __init__(
        self,
        name: str,
        path: str,
        content: bytes,
        mime_type: str = "",
    ) -> None:
        self.name = name
        self.path = path
        self.content = content
        self.mime_type = mime_type


class DataSource(Protocol):
    """A source that provides files for tools to consume.

    Implementations: LocalFileSource, SharePointSource, SambaSource.
    """

    def list_files(self, path: str = "") -> list[FileEntry]:
        """Return metadata for all files at the given path."""
        ...

    def read_file(self, path: str) -> FileContent:
        """Read a file and return its raw bytes with metadata."""
        ...

    def search(self, query: str) -> list[FileEntry]:
        """Search for files matching a query string. Returns matching entries."""
        ...
