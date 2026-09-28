"""Guardian news search + Cohere rerank tool."""

import json
import logging
from typing import Any

import requests as req_mod

from app.core.logging import log_function_call

logger = logging.getLogger(__name__)


class NewsTool:
    """Search Guardian news and rerank with Cohere on Azure."""

    def __init__(
        self,
        guardian_api_key: str,
        guardian_search_url: str,
        cohere_endpoint: str,
        cohere_api_key: str,
        cohere_model: str,
    ) -> None:
        self._guardian_api_key = guardian_api_key
        self._guardian_search_url = guardian_search_url
        self._cohere_endpoint = cohere_endpoint
        self._cohere_api_key = cohere_api_key
        self._cohere_model = cohere_model

    def definition(self) -> dict[str, Any]:
        desc = "Search for news articles about a person or topic."
        return {
            "type": "function",
            "function": {
                "name": "search_news",
                "description": desc,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query, e.g. 'Kamala Harris'",
                        },
                    },
                    "required": ["query"],
                },
            },
        }

    def execute(self, args: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
        query = args.get("query", "")
        log_function_call(
            "tools.news.search",
            "execute",
            query=query,
            source="agent_or_route",
        )
        articles = self._fetch(query)
        tool_msg = {
            "role": "tool_result",
            "content": {
                "tool_call_id": args.get("tool_call_id", ""),
                "result": json.dumps(
                    {
                        "status": "ok",
                        "count": len(articles),
                        "query": query,
                    }
                ),
            },
        }
        rich = {
            "role": "rich_content",
            "content": {"type": "news_cards", "query": query, "articles": articles},
        }
        log_function_call(
            "tools.news.search",
            "execute",
            step="complete",
            article_count=len(articles),
        )
        return tool_msg, rich

    def _fetch(self, query: str) -> list[dict[str, Any]]:
        articles = self._fetch_guardian(query)
        if not articles:
            return []
        docs = self._build_docs(articles)
        return self._rerank_or_fallback(docs, query)

    def _fetch_guardian(self, query: str) -> list[dict[str, Any]]:
        log_function_call("tools.news.search", "_fetch_guardian", query=query)
        params = {
            "q": query,
            "api-key": self._guardian_api_key,
            "page-size": 20,
            "order-by": "relevance",
            "show-fields": "trailText,bodyText",
        }
        try:
            resp = req_mod.get(self._guardian_search_url, params=params, timeout=15)
            resp.raise_for_status()
            return resp.json().get("response", {}).get("results", [])
        except req_mod.RequestException as e:
            logger.error("Guardian API error: %s", e)
            return []
        except Exception as e:
            logger.error("Guardian parse error: %s", e)
            return []

    def _build_docs(self, articles: list[dict[str, Any]]) -> list[dict[str, Any]]:
        docs = []
        for article in articles:
            fields = article.get("fields", {})
            title = article.get("webTitle", "")
            snippet = fields.get("trailText", "")
            docs.append(
                {
                    "title": title,
                    "url": article.get("webUrl", ""),
                    "snippet": snippet,
                    "body_preview": fields.get("bodyText", "")[:500],
                    "text_for_rerank": f"{title}. {snippet}",
                }
            )
        return docs

    def _rerank_or_fallback(
        self,
        docs: list[dict[str, Any]],
        query: str,
    ) -> list[dict[str, Any]]:
        if not self._cohere_endpoint or not self._cohere_api_key:
            for doc in docs:
                doc["relevance_score"] = 0.0
            return docs[:8]
        try:
            return self._cohere_rerank(docs, query)
        except req_mod.RequestException as e:
            logger.error("Cohere rerank error: %s", e)
        except Exception as e:
            logger.error("Cohere rerank parse error: %s", e)
        for doc in docs:
            doc["relevance_score"] = 0.0
        return docs[:8]

    def _cohere_rerank(
        self,
        docs: list[dict[str, Any]],
        query: str,
    ) -> list[dict[str, Any]]:
        cohere_url = f"{self._cohere_endpoint.rstrip('/')}/v1/rerank"
        headers = {
            "Authorization": f"Bearer {self._cohere_api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self._cohere_model,
            "query": query,
            "documents": [d["text_for_rerank"] for d in docs],
            "top_n": min(8, len(docs)),
        }
        resp = req_mod.post(cohere_url, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        reranked = []
        for result in data.get("results", []):
            idx = result.get("index", 0)
            score = result.get("relevance_score", 0)
            doc = docs[idx].copy()
            doc["relevance_score"] = round(score, 4)
            reranked.append(doc)
        return reranked
