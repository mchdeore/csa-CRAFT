# tools

Agent tools exposed to the chat loop. Each subpackage is a tool family (charts, documents, news, weather). `registry.py` wires them into `tools.registry.ToolRegistry`; `routes.py` exposes direct REST execution for testing without the LLM.

Every subpackage `__init__.py` must declare `__all__` — enforced by `app/tests/test_architecture.py`.
