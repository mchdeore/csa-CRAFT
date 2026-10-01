"""Tests for tools/documents/search.py — DocumentSearchTool with mock DataSource."""

import json
from unittest.mock import MagicMock

import pytest

from connectors.protocols import FileEntry
from tools.documents.search import DocumentSearchTool


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_source() -> MagicMock:
    """A DataSource mock that returns FileEntry lists."""
    source = MagicMock()
    return source


@pytest.fixture
def tool(mock_source: MagicMock) -> DocumentSearchTool:
    """DocumentSearchTool with one mock source named 'project_files'."""
    return DocumentSearchTool(sources={"project_files": mock_source})


@pytest.fixture
def sample_entries() -> list[FileEntry]:
    """Sample file entries that a DataSource would return."""
    return [
        FileEntry(
            name="report.pdf",
            path="/docs/report.pdf",
            size=204800,
            modified="2025-05-01",
            mime_type="application/pdf",
        ),
        FileEntry(
            name="notes.txt",
            path="/docs/notes.txt",
            size=1024,
            modified="2025-05-02",
            mime_type="text/plain",
        ),
    ]


# ---------------------------------------------------------------------------
# list_files via query="list"
# ---------------------------------------------------------------------------


class TestListFiles:
    """When query is 'list', the tool calls DataSource.list_files()."""

    def test_list_returns_all_files(
        self,
        tool: DocumentSearchTool,
        mock_source: MagicMock,
        sample_entries: list[FileEntry],
    ) -> None:
        """Calling with query='list' invokes list_files and returns all entries."""
        mock_source.list_files.return_value = sample_entries

        tool_msg, rich = tool.execute(
            {"query": "list", "source_name": "project_files", "tool_call_id": "call_l1"}
        )

        # tool_msg contains count + capped file list
        result = json.loads(tool_msg["content"]["result"])
        assert result["count"] == 2
        assert len(result["files"]) == 2

        # rich content has all files
        assert rich["role"] == "rich_content"
        assert rich["content"]["type"] == "file_listing"
        assert len(rich["content"]["files"]) == 2

        mock_source.list_files.assert_called_once()
        mock_source.search.assert_not_called()


# ---------------------------------------------------------------------------
# search via query="something"
# ---------------------------------------------------------------------------


class TestSearch:
    """When query is not 'list', the tool calls DataSource.search(query)."""

    def test_search_returns_matching_entries(
        self,
        tool: DocumentSearchTool,
        mock_source: MagicMock,
        sample_entries: list[FileEntry],
    ) -> None:
        """A specific query calls search() and returns matching results."""
        mock_source.search.return_value = sample_entries

        tool_msg, rich = tool.execute(
            {"query": "report", "source_name": "project_files", "tool_call_id": "call_s1"}
        )

        result = json.loads(tool_msg["content"]["result"])
        assert result["count"] == 2

        mock_source.search.assert_called_once_with("report")
        mock_source.list_files.assert_not_called()


# ---------------------------------------------------------------------------
# Empty results
# ---------------------------------------------------------------------------


class TestEmptyResults:
    """When no files match, the tool returns zero-count gracefully."""

    def test_empty_search_returns_zero(
        self, tool: DocumentSearchTool, mock_source: MagicMock
    ) -> None:
        """A search with no results returns count=0 and empty file list."""
        mock_source.search.return_value = []

        tool_msg, rich = tool.execute(
            {"query": "nothing", "source_name": "project_files", "tool_call_id": "call_e1"}
        )

        result = json.loads(tool_msg["content"]["result"])
        assert result["count"] == 0
        assert result["files"] == []

        assert rich["content"]["files"] == []


# ---------------------------------------------------------------------------
# Error handling — unknown source
# ---------------------------------------------------------------------------


class TestUnknownSource:
    """When source_name is not in the sources dict, an error is returned."""

    def test_unknown_source_returns_error(
        self, tool: DocumentSearchTool
    ) -> None:
        """An unknown source_name produces an error tool_msg listing available sources."""
        tool_msg, rich = tool.execute(
            {"query": "list", "source_name": "not_real", "tool_call_id": "call_u1"}
        )

        result = json.loads(tool_msg["content"]["result"])
        assert "error" in result
        assert "Unknown" in result["error"]
        assert "project_files" in result["error"]

        assert rich is None


# ---------------------------------------------------------------------------
# execute returns correct tuple shape
# ---------------------------------------------------------------------------


class TestExecuteShape:
    """execute() always returns a (tool_msg, rich) tuple."""

    def test_returns_two_element_tuple(
        self, tool: DocumentSearchTool, mock_source: MagicMock
    ) -> None:
        """The return type is always a 2-tuple."""
        mock_source.list_files.return_value = []

        result = tool.execute(
            {"query": "list", "source_name": "project_files", "tool_call_id": "call_t1"}
        )

        assert isinstance(result, tuple)
        assert len(result) == 2
        tool_msg, rich = result

        assert tool_msg["role"] == "tool_result"
        assert rich["role"] == "rich_content"


# ---------------------------------------------------------------------------
# definition tests
# ---------------------------------------------------------------------------


class TestDefinition:
    """definition() schema check."""

    def test_definition_requires_query_and_source(
        self, tool: DocumentSearchTool
    ) -> None:
        """search_documents requires query and source_name."""
        definition = tool.definition()

        func = definition["function"]
        assert func["name"] == "search_documents"
        assert "query" in func["parameters"]["properties"]
        assert "source_name" in func["parameters"]["properties"]
        assert set(func["parameters"]["required"]) == {"query", "source_name"}