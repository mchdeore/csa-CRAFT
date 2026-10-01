"""Tests for tools/documents/reader.py — TextAnalysisTool with mock DataSource."""

import json
from unittest.mock import MagicMock

import pytest

from connectors.protocols import FileContent
from tools.documents.reader import TextAnalysisTool


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_source() -> MagicMock:
    """A mock DataSource that returns a FileContent for a known path."""
    source = MagicMock()
    return source


@pytest.fixture
def tool(mock_source: MagicMock) -> TextAnalysisTool:
    """TextAnalysisTool with one mock source named 'test_source'."""
    return TextAnalysisTool(sources={"test_source": mock_source})


@pytest.fixture
def plain_text_file() -> FileContent:
    """A simple .txt file with two paragraphs."""
    return FileContent(
        name="notes.txt",
        path="/docs/notes.txt",
        content=b"Hello world.\n\nThis is the second paragraph with more text in it.",
        mime_type="text/plain",
    )


@pytest.fixture
def csv_file() -> FileContent:
    """A small CSV file."""
    return FileContent(
        name="data.csv",
        path="/docs/data.csv",
        content=b"name,score\nAlice,10\nBob,20",
        mime_type="text/csv",
    )


@pytest.fixture
def long_text_file() -> FileContent:
    """A text file with multiple paragraphs, some long enough to trigger chunking."""
    paragraphs = []
    for i in range(10):
        # Each paragraph is ~600 chars — 3 paragraphs exceed 4000
        paragraphs.append(f"Paragraph {i}: " + "x" * 590)
    content = "\n\n".join(paragraphs)
    return FileContent(
        name="long.txt",
        path="/docs/long.txt",
        content=content.encode("utf-8"),
        mime_type="text/plain",
    )


# ---------------------------------------------------------------------------
# _extract_text tests
# ---------------------------------------------------------------------------


class TestExtractText:
    """Test TextAnalysisTool._extract_text for plain text and CSV."""

    def test_extracts_plain_text(self, tool: TextAnalysisTool, plain_text_file: FileContent) -> None:
        """Plain text files are decoded from bytes to str as-is."""
        text = tool._extract_text(
            plain_text_file.content,
            plain_text_file.mime_type,
            plain_text_file.name,
        )

        assert "Hello world" in text
        assert "second paragraph" in text

    def test_extracts_csv_as_text(self, tool: TextAnalysisTool, csv_file: FileContent) -> None:
        """CSV files are decoded to UTF-8 text (no special parsing)."""
        text = tool._extract_text(
            csv_file.content,
            csv_file.mime_type,
            csv_file.name,
        )

        assert "name,score" in text
        assert "Alice,10" in text


# ---------------------------------------------------------------------------
# _chunk_text tests
# ---------------------------------------------------------------------------


class TestChunkText:
    """Test _chunk_text paragraph-boundary chunking logic."""

    def test_single_paragraph_returns_one_chunk(self, tool: TextAnalysisTool) -> None:
        """A short text stays as a single chunk."""
        chunks = tool._chunk_text("Just one paragraph here.")
        assert len(chunks) == 1
        assert chunks[0] == "Just one paragraph here."

    def test_empty_string_returns_one_empty_chunk(self, tool: TextAnalysisTool) -> None:
        """An empty string produces one chunk (the empty string)."""
        chunks = tool._chunk_text("")
        assert len(chunks) == 1
        assert chunks[0] == ""

    def test_paragraphs_split_double_newlines(self, tool: TextAnalysisTool) -> None:
        """Paragraphs separated by blank lines are kept together if they fit."""
        chunks = tool._chunk_text("First.\n\nSecond.\n\nThird.")
        assert len(chunks) == 1
        assert "First." in chunks[0]
        assert "Third." in chunks[0]

    def test_long_text_splits_at_boundaries(self, tool: TextAnalysisTool, long_text_file: FileContent) -> None:
        """When paragraphs exceed MAX_CHUNK_SIZE (4000), the text is split."""
        text = tool._extract_text(
            long_text_file.content,
            long_text_file.mime_type,
            long_text_file.name,
        )

        chunks = tool._chunk_text(text)

        # With 10 paragraphs of ~600 chars each, we expect multiple chunks
        assert len(chunks) > 1

        # Each chunk must not exceed 4000 characters
        for chunk in chunks:
            assert len(chunk) <= 4000

    def test_all_paragraphs_covered(self, tool: TextAnalysisTool, long_text_file: FileContent) -> None:
        """After chunking, every paragraph appears in at least one chunk."""
        text = tool._extract_text(
            long_text_file.content,
            long_text_file.mime_type,
            long_text_file.name,
        )

        chunks = tool._chunk_text(text)
        combined = "\n\n".join(chunks)

        for i in range(10):
            assert f"Paragraph {i}" in combined


# ---------------------------------------------------------------------------
# execute tests
# ---------------------------------------------------------------------------


class TestExecute:
    """Execute the full tool pipeline with a mock DataSource."""

    def test_returns_tool_msg_and_rich_content(
        self,
        tool: TextAnalysisTool,
        mock_source: MagicMock,
        plain_text_file: FileContent,
    ) -> None:
        """execute reads a file, chunks it, and returns both outputs."""
        mock_source.read_file.return_value = plain_text_file

        tool_msg, rich = tool.execute(
            {
                "path": "/docs/notes.txt",
                "source_name": "test_source",
                "tool_call_id": "call_d1",
            }
        )

        # tool_msg
        assert tool_msg["role"] == "tool_result"
        result = json.loads(tool_msg["content"]["result"])
        assert result["file"] == "notes.txt"
        assert "text" in result
        assert "Hello world" in result["text"]

        # rich_content
        assert rich is not None
        assert rich["role"] == "rich_content"
        assert rich["content"]["type"] == "document_text"
        assert rich["content"]["file_name"] == "notes.txt"

    def test_missing_source_returns_error(
        self, tool: TextAnalysisTool
    ) -> None:
        """An unknown source_name produces an error tool_msg."""
        tool_msg, rich = tool.execute(
            {
                "path": "/docs/notes.txt",
                "source_name": "unknown_source",
                "tool_call_id": "call_d2",
            }
        )

        result = json.loads(tool_msg["content"]["result"])
        assert "error" in result
        assert "Could not read" in result["error"]
        assert rich is None

    def test_file_not_found_returns_error(
        self,
        tool: TextAnalysisTool,
        mock_source: MagicMock,
    ) -> None:
        """When the DataSource raises FileNotFoundError, execute returns an error."""
        mock_source.read_file.side_effect = FileNotFoundError("nope")

        tool_msg, rich = tool.execute(
            {
                "path": "/docs/missing.txt",
                "source_name": "test_source",
                "tool_call_id": "call_d3",
            }
        )

        result = json.loads(tool_msg["content"]["result"])
        assert "error" in result
        assert "missing" in result["error"]
        assert rich is None


# ---------------------------------------------------------------------------
# definition tests
# ---------------------------------------------------------------------------


class TestDefinition:
    """definition() schema check."""

    def test_definition_requires_path_and_source(self, tool: TextAnalysisTool) -> None:
        """The read_document definition requires path and source_name."""
        definition = tool.definition()

        func = definition["function"]
        assert func["name"] == "read_document"
        assert "path" in func["parameters"]["properties"]
        assert "source_name" in func["parameters"]["properties"]
        assert set(func["parameters"]["required"]) == {"path", "source_name"}