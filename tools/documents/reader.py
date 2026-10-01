"""Document reader tool — read and extract text from documents."""

import io
import json
import re
from typing import Any

from app.core.logging import log_function_call
from connectors.protocols import DataSource

MAX_CHUNK_SIZE = 4000


class TextAnalysisTool:
    """Read documents from data sources and return structured text for the agent."""

    def __init__(self, sources: dict[str, DataSource]) -> None:
        self._sources = sources

    def definition(self) -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_document",
                "description": (
                    "Read and extract text from a document. "
                    "Supports .txt, .pdf, .docx, .csv. "
                    "Returns the document text split into chunks with metadata."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "File path from the data source.",
                        },
                        "source_name": {
                            "type": "string",
                            "description": "Data source name.",
                        },
                        "chunk_index": {
                            "type": "integer",
                            "description": "Which chunk to read. Default 0 (first chunk).",
                        },
                    },
                    "required": ["path", "source_name"],
                },
            },
        }

    def execute(
        self,
        args: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any] | None]:
        path = args.get("path", "")
        source_name = args.get("source_name", "")
        chunk_index = args.get("chunk_index", 0)
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.documents.reader",
            "execute",
            path=path,
            source_name=source_name,
            chunk_index=chunk_index,
            source="agent_or_route",
        )

        source = self._sources.get(source_name)
        if source is None:
            log_function_call(
                "tools.documents.reader",
                "execute",
                step="error",
                error=f"Unknown source: {source_name}",
            )
            return self._build_error(tool_call_id, source_name), None

        try:
            file = source.read_file(path)
        except FileNotFoundError:
            log_function_call(
                "tools.documents.reader",
                "execute",
                step="error",
                error=f"File not found: {path}",
            )
            return self._build_error(tool_call_id, source_name, path), None

        text = self._extract_text(file.content, file.mime_type, file.name)
        chunks = self._chunk_text(text)

        log_function_call(
            "tools.documents.reader",
            "execute",
            step="complete",
            file=file.name,
            total_chunks=len(chunks),
        )

        return (
            _build_tool_result_msg(file.name, chunks, chunk_index, tool_call_id),
            _build_rich_content(file.name, chunks, chunk_index),
        )

    def _extract_text(self, content: bytes, mime_type: str, filename: str) -> str:
        if filename.lower().endswith(".pdf") or "pdf" in mime_type:
            return self._extract_pdf(content)
        if filename.lower().endswith(".docx") or "word" in mime_type:
            return self._extract_docx(content)
        if filename.lower().endswith(".csv") or "csv" in mime_type:
            return content.decode("utf-8", errors="replace")
        return content.decode("utf-8", errors="replace")

    def _extract_pdf(self, content: bytes) -> str:
        import pdfplumber  # type: ignore[import-untyped]

        with pdfplumber.open(io.BytesIO(content)) as pdf:
            pages = []
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    pages.append(page_text)
        return "\n\n".join(pages)

    def _extract_docx(self, content: bytes) -> str:
        from docx import Document  # type: ignore[import-untyped]

        doc = Document(io.BytesIO(content))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)

    def _chunk_text(self, text: str) -> list[str]:
        """Split text into chunks at paragraph boundaries, respecting MAX_CHUNK_SIZE.

        Each chunk is up to 4000 characters. Chunks split on blank-line paragraph
        boundaries whenever possible. Returns a list with at least one chunk.

        >>> tool = TextAnalysisTool.__new__(TextAnalysisTool)
        >>> tool._chunk_text("Short text.")
        ['Short text.']
        >>> tool._chunk_text("")
        ['']
        >>> chunks = tool._chunk_text("A\\n\\nB")
        >>> len(chunks) >= 1
        True
        """
        chunks: list[str] = []
        current = ""

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            if len(current) + len(para) + 2 <= MAX_CHUNK_SIZE:
                current += ("\n\n" if current else "") + para
            else:
                if current:
                    chunks.append(current)
                current = para

        if current:
            chunks.append(current)

        return chunks or [text]

    def _build_error(
        self,
        tool_call_id: str,
        source_name: str,
        path: str = "",
    ) -> dict[str, Any]:
        return {
            "role": "tool_result",
            "content": {
                "tool_call_id": tool_call_id,
                "result": json.dumps(
                    {
                        "error": (
                            f"Could not read '{path}' from source '{source_name}'. "
                            f"Check the path and source name are correct."
                        ),
                    }
                ),
            },
        }


def _build_tool_result_msg(
    file_name: str,
    chunks: list[str],
    chunk_index: int,
    tool_call_id: str,
) -> dict[str, Any]:
    safe_index = min(chunk_index, len(chunks) - 1) if chunks else 0
    chunk = chunks[safe_index] if chunks else ""
    return {
        "role": "tool_result",
        "content": {
            "tool_call_id": tool_call_id,
            "result": json.dumps(
                {
                    "file": file_name,
                    "total_chunks": len(chunks),
                    "current_chunk": safe_index,
                    "text": chunk,
                }
            ),
        },
    }


def _build_rich_content(
    file_name: str,
    chunks: list[str],
    chunk_index: int,
) -> dict[str, Any]:
    safe_index = min(chunk_index, len(chunks) - 1) if chunks else 0
    chunk = chunks[safe_index] if chunks else ""
    return {
        "role": "rich_content",
        "content": {
            "type": "document_text",
            "file_name": file_name,
            "chunk_index": safe_index,
            "total_chunks": len(chunks),
            "preview": chunk[:500],
        },
    }
