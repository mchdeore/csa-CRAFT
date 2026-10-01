"""
CADRe Part A document ingestion — extracts numeric parameters from markdown text.

Uses regex on known patterns found in gen-2 CADRe files. Returns extracted
fields with confidence scores per field.
"""

import base64
import json
import re
from typing import Any

from app.core.logging import log_function_call


# Patterns for each field
PATTERNS = {
    "mass_kg": [
        r"Unit\s*mass\s*\D+?(\d+(?:\.\d+)?)\s*kg",
        r"Initial\s*unit\s*mass\s*\D+?(\d+(?:\.\d+)?)\s*kg",
        r"mass\s*kg.*?(\d+(?:\.\d+)?)",
    ],
    "power_w_gen": [
        r"Power\s*Generation\s*\D+?(\d+(?:\.\d+)?)\s*W",
        r"Generation\s*/\s*provision\s*\D+?(\d+(?:\.\d+)?)\s*W",
        r"power_w_gen.*?(\d+(?:\.\d+)?)",
    ],
    "power_w_nom": [
        r"Nominal\s*Power\s*\D+?(\d+(?:\.\d+)?)\s*W",
        r"Nominal\s*/\s*peak\s*demand\s*\D+?(\d+(?:\.\d+)?)\s*W",
        r"Nominal\s*power\s*\|?\s*(\d+(?:\.\d+)?)\s*W",
    ],
    "power_w_peak": [
        r"Peak\s*Power\s*\D+?(\d+(?:\.\d+)?)\s*W",
        r"Peak\s*power\s*\|?\s*(\d+(?:\.\d+)?)\s*W",
    ],
    "payload_mass_kg": [
        r"Payload.*?mass\s*\D+?(\d+(?:\.\d+)?)\s*kg",
        r"Payload\s*/\s*experiment\s*allocation\s*\D+?(\d+(?:\.\d+)?)\s*kg",
    ],
    "propellant_mass_kg": [
        r"Propellant.*?\D+?(\d+(?:\.\d+)?)\s*kg",
        r"propellant.*?(\d+(?:\.\d+)?)\s*kg\s*(?:propellant|monopropellant)",
    ],
    "delta_v_ms": [
        r"Delta.V.*?\D+?(\d+(?:\.\d+)?)\s*m/s",
        r"Δv.*?(\d+(?:\.\d+)?)\s*m/s",
        r"delta-v.*?(\d+(?:\.\d+)?)\s*m/s",
    ],
    "duration_years": [
        r"Science.*?(\d+)\s*yr",
        r"duration.*?(\d+(?:\.\d+)?)\s*y(?:ea)?r",
        r"design\s*life.*?(\d+(?:\.\d+)?)\s*y(?:ea)?r",
    ],
    "number_spacecraft": [
        r"Number\s*of\s*(?:Spacecraft|Units)\s*\D+?(\d+)",
        r"constellation\s*of\s*(\d+)",
        r"(\d+)\s*spacecraft",
    ],
    "data_gb_day": [
        r"Data.*?\D+?(\d+(?:\.\d+)?)\s*GB/day",
        r"Mission.data.*?(\d+(?:\.\d+)?)\s*GB/day",
    ],
}


def ingest_document(contents: str, filename: str) -> dict:
    """Extract CADRe parameters from a base64-encoded markdown file.

    Returns dict with fields (key → value), confidence (key → 0-1 score),
    filename, and field_count. If decoding fails, returns dict with error key.

    >>> import base64
    >>> text = "| Unit mass | 445 kg |\\\\n| Power Generation | 450 W |\\\\n| Nominal Power | 450 W |"
    >>> encoded = "data:text/markdown;base64," + base64.b64encode(text.encode()).decode()
    >>> result = ingest_document(encoded, "test.md")
    >>> result["ok"]
    True
    >>> "mass_kg" in result["fields"]
    True
    >>> result["fields"]["mass_kg"]
    445.0
    >>> "power_w_gen" in result["fields"]
    True
    """
    try:
        # Decode base64
        _, content_string = contents.split(",", 1)
        raw = base64.b64decode(content_string)
        text = raw.decode("utf-8", errors="replace")
    except Exception:
        return {"error": "Could not decode file. Expected base64 text."}

    # Strip leading page info, keep everything
    text_lower = text.lower()

    fields = {}
    confidence = {}

    for field_name, patterns in PATTERNS.items():
        best_value = None
        best_conf = 0.0

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if not match:
                # Try on lowercased version too
                match = re.search(pattern.lower(), text_lower, re.IGNORECASE)
            if match:
                try:
                    value = float(match.group(1).replace(",", ""))
                    # Higher confidence for more specific patterns (earlier in list)
                    idx = PATTERNS[field_name].index(pattern)
                    conf = 0.8 + (0.2 * (1 - idx / len(PATTERNS[field_name])))
                    if conf > best_conf:
                        best_value = value
                        best_conf = conf
                except (ValueError, IndexError):
                    pass

        if best_value is not None:
            fields[field_name] = best_value
            confidence[field_name] = best_conf

    return {
        "ok": True,
        "filename": filename,
        "fields": fields,
        "confidence": confidence,
        "field_count": len(fields),
    }


class IngestDocumentTool:
    """Tool wrapper for CADRe document ingestion — used by the PydanticAI agent."""

    def definition(self) -> dict[str, Any]:
        """OpenAI-compatible tool definition."""
        return {
            "type": "function",
            "function": {
                "name": "ingest_document",
                "description": (
                    "Extract numeric parameters from a base64-encoded CADRe Part A "
                    "markdown document. Required parameters: contents (base64 string), "
                    "filename (string)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contents": {
                            "type": "string",
                            "description": "Base64-encoded file contents",
                        },
                        "filename": {
                            "type": "string",
                            "description": "Original filename (e.g. my-mission-part-a.md)",
                        },
                    },
                    "required": ["contents", "filename"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        """Execute ingestion with given args. Returns (tool_message, None)."""
        contents = args.get("contents", "")
        filename = args.get("filename", "")
        tool_call_id = args.get("tool_call_id", "")

        log_function_call(
            "tools.documents.ingest",
            "execute",
            filename=filename,
        )

        result = ingest_document(contents, filename)

        if result.get("error"):
            return (
                {
                    "role": "tool_result",
                    "content": {
                        "tool_call_id": tool_call_id,
                        "result": json.dumps({"error": result["error"]}),
                    },
                },
                None,
            )

        fields = result.get("fields", {})
        field_list = ", ".join(f"{k}={v}" for k, v in sorted(fields.items()))

        return (
            {
                "role": "tool_result",
                "content": {
                    "tool_call_id": tool_call_id,
                    "result": json.dumps(
                        {
                            "status": "ok",
                            "filename": filename,
                            "field_count": len(fields),
                            "fields": field_list,
                        }
                    ),
                },
            },
            None,
        )