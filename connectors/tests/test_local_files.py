"""Tests for connectors/local_files.py — LocalFileSource."""

import tempfile
from pathlib import Path

import pytest

from connectors.local_files import LocalFileSource
from connectors.protocols import FileContent, FileEntry


# Fixture: a temporary directory with known files for testing
@pytest.fixture
def temp_root() -> Path:
    """Create a temporary directory with a small file tree:

    root/
        data.csv
        notes.txt
        subdir/
            config.json
    """
    root = Path(tempfile.mkdtemp())

    # Create files with known content
    (root / "data.csv").write_text("a,b,c\n1,2,3\n")
    (root / "notes.txt").write_text("hello world\n")

    sub = root / "subdir"
    sub.mkdir()
    (sub / "config.json").write_text('{"key": "value"}')

    return Path(root)


# Fixture: LocalFileSource wired to the temp directory
@pytest.fixture
def source(temp_root: Path) -> LocalFileSource:
    return LocalFileSource(temp_root)


class TestInit:
    def test_root_is_resolved_absolute_path(self, temp_root: Path) -> None:
        source = LocalFileSource(temp_root)
        assert source._root.is_absolute()
        assert source._root == temp_root.resolve()


class TestListFiles:
    def test_list_root_returns_all_files(self, source: LocalFileSource) -> None:
        entries = source.list_files("")
        # Should list data.csv and notes.txt (files directly in root)
        names = {e.name for e in entries}

        assert "data.csv" in names
        assert "notes.txt" in names

        # subdir is a directory, not a file — should not appear
        assert "subdir" not in names

    def test_list_subdirectory_returns_file(self, source: LocalFileSource) -> None:
        entries = source.list_files("subdir")
        assert len(entries) == 1
        assert entries[0].name == "config.json"

    def test_list_nonexistent_path_returns_empty(self, source: LocalFileSource) -> None:
        entries = source.list_files("nonexistent")
        assert entries == []

    def test_file_entry_has_correct_metadata(self, source: LocalFileSource) -> None:
        entries = source.list_files("")
        csv_entry = next(e for e in entries if e.name == "data.csv")

        assert csv_entry.path == "data.csv"
        assert csv_entry.size > 0
        assert csv_entry.mime_type in ("text/csv", "application/octet-stream")
        assert csv_entry.modified  # ISO timestamp string, not empty


class TestReadFile:
    def test_read_csv_returns_content(self, source: LocalFileSource) -> None:
        content = source.read_file("data.csv")
        assert content.name == "data.csv"
        assert content.content == b"a,b,c\n1,2,3\n"
        assert "csv" in content.mime_type or content.mime_type == "text/plain"

    def test_read_txt_returns_content(self, source: LocalFileSource) -> None:
        content = source.read_file("notes.txt")
        assert content.content == b"hello world\n"

    def test_read_file_in_subdirectory(self, source: LocalFileSource) -> None:
        content = source.read_file("subdir/config.json")
        assert content.name == "config.json"
        assert content.content == b'{"key": "value"}'

    def test_read_nonexistent_file_raises(self, source: LocalFileSource) -> None:
        with pytest.raises(FileNotFoundError):
            source.read_file("does-not-exist.txt")

    def test_read_directory_raises(self, source: LocalFileSource) -> None:
        with pytest.raises(FileNotFoundError):
            source.read_file("subdir")


class TestSearch:
    def test_search_by_name_exact_match(self, source: LocalFileSource) -> None:
        results = source.search("data.csv")
        assert len(results) == 1
        assert results[0].name == "data.csv"

    def test_search_by_name_partial_match(self, source: LocalFileSource) -> None:
        results = source.search("data")
        assert len(results) == 1
        assert results[0].name == "data.csv"

    def test_search_case_insensitive(self, source: LocalFileSource) -> None:
        results = source.search("DATA.CSV")
        assert len(results) == 1
        assert results[0].name == "data.csv"

    def test_search_no_match_returns_empty(self, source: LocalFileSource) -> None:
        results = source.search("zzz_not_a_file_zzz")
        assert results == []

    def test_search_finds_files_in_subdirectories(self, source: LocalFileSource) -> None:
        results = source.search("config")
        # Should find config.json in subdir/
        assert len(results) == 1
        assert results[0].name == "config.json"
        assert results[0].path == "subdir/config.json"


class TestPathSecurity:
    def test_resolve_blocks_escape_via_dotdot(self, temp_root: Path) -> None:
        source = LocalFileSource(temp_root)
        with pytest.raises(ValueError, match="escapes"):
            source._resolve("../etc/passwd")

    def test_resolve_blocks_absolute_path_escape(self, temp_root: Path) -> None:
        source = LocalFileSource(temp_root)
        with pytest.raises(ValueError, match="escapes"):
            source._resolve("/etc/hosts")