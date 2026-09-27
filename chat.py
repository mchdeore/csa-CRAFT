"""DeepSeek chat implementation."""

import os

from openai import OpenAI

from config import DEEPSEEK_BASE_URL, DEEPSEEK_MODEL, SYSTEM_PROMPT


class DeepSeekChat:
    def __init__(self) -> None:
        self._client: OpenAI | None = None

    def _get_client(self) -> OpenAI | None:
        if self._client is not None:
            return self._client
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            return None
        self._client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL)
        return self._client

    def get_response(self, messages: list[dict]) -> str:
        client = self._get_client()
        if client is None:
            return "DeepSeek API key not configured. Set DEEPSEEK_API_KEY in .env"
        api_messages: list = [{"role": "system", "content": SYSTEM_PROMPT}]
        api_messages.extend(messages)
        resp = client.chat.completions.create(model=DEEPSEEK_MODEL, messages=api_messages)
        return resp.choices[0].message.content or ""
