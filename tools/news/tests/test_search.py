"""Tests for tools/news/search.py — NewsTool with mock Guardian + Cohere APIs."""

import json
from unittest.mock import MagicMock, patch

import pytest

from tools.news.search import NewsTool


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

MOCK_GUARDIAN_URL = "http://fake-guardian/api"
MOCK_COHERE_ENDPOINT = "http://fake-cohere"
MOCK_COHERE_KEY = "fake-key"
MOCK_COHERE_MODEL = "rerank-v3.5"
MOCK_GUARDIAN_KEY = "fake-guardian-key"


@pytest.fixture
def tool() -> NewsTool:
    """NewsTool with fake endpoints that won't make real network calls."""
    return NewsTool(
        guardian_api_key=MOCK_GUARDIAN_KEY,
        guardian_search_url=MOCK_GUARDIAN_URL,
        cohere_endpoint=MOCK_COHERE_ENDPOINT,
        cohere_api_key=MOCK_COHERE_KEY,
        cohere_model=MOCK_COHERE_MODEL,
    )


@pytest.fixture
def guardian_response() -> dict:
    """A valid Guardian API response with 2 articles."""
    return {
        "response": {
            "status": "ok",
            "total": 2,
            "results": [
                {
                    "id": "world/2025/jun/01/article-a",
                    "webTitle": "Climate summit reaches historic deal",
                    "webUrl": "https://theguardian.com/climate-deal",
                    "fields": {
                        "trailText": "World leaders agreed on a binding framework.",
                        "bodyText": "Full article body covering the summit details...",
                    },
                },
                {
                    "id": "world/2025/jun/01/article-b",
                    "webTitle": "New renewable energy record set",
                    "webUrl": "https://theguardian.com/energy-record",
                    "fields": {
                        "trailText": "Solar and wind surpassed 50% of grid supply.",
                        "bodyText": "Detailed analysis of the energy milestone...",
                    },
                },
            ],
        }
    }


@pytest.fixture
def cohere_rerank_response() -> dict:
    """A Cohere rerank response that reorders the two documents."""
    return {
        "id": "rerank-abc",
        "results": [
            {"index": 1, "relevance_score": 0.94},
            {"index": 0, "relevance_score": 0.72},
        ],
    }


@pytest.fixture
def empty_guardian_response() -> dict:
    """Guardian response with zero results."""
    return {"response": {"status": "ok", "total": 0, "results": []}}


# ---------------------------------------------------------------------------
# _fetch tests
# ---------------------------------------------------------------------------


class TestFetch:
    """Test the full _fetch pipeline: Guardian → build docs → Cohere rerank."""

    def test_returns_articles_with_expected_fields(
        self,
        tool: NewsTool,
        guardian_response: dict,
        cohere_rerank_response: dict,
    ) -> None:
        """_fetch returns a list of article dicts with title, url, snippet, relevance."""
        with (
            patch("tools.news.search.req_mod.get") as mock_get,
            patch("tools.news.search.req_mod.post") as mock_post,
        ):
            mock_get.return_value = _fake_response(guardian_response)
            mock_post.return_value = _fake_response(cohere_rerank_response)

            articles = tool._fetch("climate")

        assert len(articles) == 2

        for article in articles:
            assert "title" in article
            assert "url" in article
            assert "snippet" in article
            assert "relevance_score" in article

        # Cohere rerank should reorder — highest relevance first
        assert articles[0]["relevance_score"] == 0.94

    def test_empty_results_returns_empty_list(
        self, tool: NewsTool, empty_guardian_response: dict
    ) -> None:
        """When Guardian returns 0 results, _fetch returns []."""
        with patch("tools.news.search.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response(empty_guardian_response)

            articles = tool._fetch("nothing matches this")

        assert articles == []

    def test_falls_back_on_cohere_failure(
        self,
        tool: NewsTool,
        guardian_response: dict,
    ) -> None:
        """When Cohere rerank fails, the tool falls back to unscored top-8 articles."""
        with (
            patch("tools.news.search.req_mod.get") as mock_get,
            patch("tools.news.search.req_mod.post") as mock_post,
        ):
            mock_get.return_value = _fake_response(guardian_response)
            mock_post.side_effect = __import__("requests").exceptions.ConnectionError(
                "cohere down"
            )

            articles = tool._fetch("climate")

        assert len(articles) <= 2  # only 2 docs, all returned
        # Fallback sets relevance_score to 0.0
        for article in articles:
            assert article["relevance_score"] == 0.0

    def test_guardian_request_error_returns_empty_list(self, tool: NewsTool) -> None:
        """A network error reaching Guardian results in an empty list, not an exception."""
        with patch("tools.news.search.req_mod.get") as mock_get:
            mock_get.side_effect = __import__("requests").exceptions.Timeout("slow")

            articles = tool._fetch("climate")

        assert articles == []


# ---------------------------------------------------------------------------
# execute tests
# ---------------------------------------------------------------------------


class TestExecute:
    """execute() returns (tool_msg, rich_content)."""

    def test_returns_tuple_with_news_cards(
        self,
        tool: NewsTool,
        guardian_response: dict,
        cohere_rerank_response: dict,
    ) -> None:
        """A successful search produces a tool_msg summary and news_cards rich content."""
        with (
            patch("tools.news.search.req_mod.get") as mock_get,
            patch("tools.news.search.req_mod.post") as mock_post,
        ):
            mock_get.return_value = _fake_response(guardian_response)
            mock_post.return_value = _fake_response(cohere_rerank_response)

            tool_msg, rich = tool.execute(
                {"query": "climate", "tool_call_id": "call_n1"}
            )

        # tool_msg
        assert tool_msg["role"] == "tool_result"
        result = json.loads(tool_msg["content"]["result"])
        assert result["status"] == "ok"
        assert result["count"] == 2

        # rich_content
        assert rich is not None
        assert rich["role"] == "rich_content"
        assert rich["content"]["type"] == "news_cards"
        assert rich["content"]["query"] == "climate"
        assert len(rich["content"]["articles"]) == 2

    def test_empty_query_works(
        self, tool: NewsTool, empty_guardian_response: dict
    ) -> None:
        """An empty query still produces a valid tuple, just with zero articles."""
        with patch("tools.news.search.req_mod.get") as mock_get:
            mock_get.return_value = _fake_response(empty_guardian_response)

            tool_msg, rich = tool.execute({"query": "", "tool_call_id": "call_n2"})

        result = json.loads(tool_msg["content"]["result"])
        assert result["count"] == 0
        assert rich["content"]["articles"] == []


# ---------------------------------------------------------------------------
# _build_docs tests
# ---------------------------------------------------------------------------


class TestBuildDocs:
    """Test _build_docs converts raw Guardian results to the internal doc format."""

    def test_extracts_title_url_snippet_and_text_for_rerank(
        self, tool: NewsTool, guardian_response: dict
    ) -> None:
        """Each doc gets the expected keys and text_for_rerank concatenation."""
        docs = tool._build_docs(guardian_response["response"]["results"])

        assert len(docs) == 2
        first = docs[0]
        assert first["title"] == "Climate summit reaches historic deal"
        assert first["url"] == "https://theguardian.com/climate-deal"
        assert first["snippet"] == "World leaders agreed on a binding framework."
        assert "text_for_rerank" in first
        assert "Climate summit" in first["text_for_rerank"]


# ---------------------------------------------------------------------------
# definition tests
# ---------------------------------------------------------------------------


class TestDefinition:
    """definition() schema check."""

    def test_definition_requires_query(self, tool: NewsTool) -> None:
        """The news search definition requires a query parameter."""
        definition = tool.definition()

        func = definition["function"]
        assert func["name"] == "search_news"
        assert "query" in func["parameters"]["properties"]
        assert func["parameters"]["required"] == ["query"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fake_response(json_body: dict) -> MagicMock:
    mock_resp = MagicMock()
    mock_resp.json.return_value = json_body
    mock_resp.raise_for_status.return_value = None
    return mock_resp