"""App settings and constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

WORKSPACES_DIR = Path(__file__).parent.parent / "workspaces"
SYSTEM_PROMPT = (
    "You are a helpful assistant with access to weather and news tools. "
    "When a user asks about a city or location, proactively use BOTH the get_weather "
    "tool and the search_news tool to give a comprehensive answer. "
    "For example, if asked about Montreal, call get_weather(city='Montreal') AND "
    "search_news(query='Montreal news today'). "
    "IMPORTANT: Always provide all required arguments when calling tools. "
    "For get_weather, always include the city parameter. "
    "For search_news, always include the query parameter. "
    "Never call a tool with empty arguments."
)

# Default root for local file connectors
CONNECTORS_ROOT = Path(os.environ.get("CONNECTORS_ROOT", Path.home() / "Documents"))

# Weather (Open-Meteo) — free, no API key needed
OPEN_METEO_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
OPEN_METEO_ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"
OPEN_METEO_GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

# News (The Guardian)
GUARDIAN_API_KEY = os.environ.get("GUARDIAN_API_KEY", "")
GUARDIAN_SEARCH_URL = "https://content.guardianapis.com/search"

# Cohere Rerank on Azure
AZURE_COHERE_ENDPOINT = os.environ.get("AZURE_COHERE_ENDPOINT", "")
AZURE_COHERE_API_KEY = os.environ.get("AZURE_COHERE_API_KEY", "")
AZURE_COHERE_RERANK_MODEL = os.environ.get("AZURE_COHERE_RERANK_MODEL", "Cohere-rerank-v3-english")


def build_system_prompt(user_context: dict | None = None) -> str:
    """Build the system prompt with user-specific context and available data keys.

    Injects user profile info (division, region, role) and a list of
    queryable data keys scoped to the user's role. The model uses these
    to know what data is available without leaking what isn't.
    """
    parts = [SYSTEM_PROMPT]

    # Inject user profile for context-aware responses
    if user_context:
        division = user_context.get("division", "")
        region = user_context.get("region", "")
        role = user_context.get("role", "")
        if division or region or role:
            parts.append(
                f"The user works in {division or 'an unspecified division'} "
                f"in the {region or 'unknown'} region "
                f"as a {role or 'staff member'}."
            )

        # List available data keys the user can query
        data_keys = user_context.get("available_data_keys", [])
        if data_keys:
            parts.append(
                f"Available data keys for query_data tool: {', '.join(sorted(data_keys))}."
            )

        sources = user_context.get("available_sources", [])
        if sources:
            parts.append(
                f"Available data sources: {', '.join(sources)}. "
                f"Use search_documents to find files and read_document to view them."
            )

    # Always remind about query_data for data operations
    parts.append(
        "You have a query_data tool for reading, storing, and listing data. "
        "Use action='list' to see available data keys. "
        "Use action='query' with a key to retrieve stored data. "
        "Use action='store' with key and value to save data."
    )

    return "\n".join(parts)
