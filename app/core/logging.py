"""Centralized structured JSON logging with daily rotation and trace IDs.

All HTTP requests hitting the Flask server are logged via global
before_request / after_request hooks. One JSON line per request,
written to storage/database/log/cheddar-YYYY-MM-DD.jsonl.

Noisy requests (Dash internals, static assets) are filtered out.
One file per day, auto-rotated at midnight, 90-day retention.

Trace IDs: every request generates a short UUID that propagates to
ALL log lines in that request's lifecycle. Internal functions can
call get_trace_id() to read it — no parameter passing needed.
Origin tags mark each line as "user_request" or "internal" so you
can filter by trigger source.

Design decisions documented in docs/route-gated-architecture.md.
"""

import contextvars
import fnmatch
import functools
import json
import logging
import time
import uuid
from datetime import datetime, timezone
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Any

from flask import Flask, g, has_request_context, request

# ---------------------------------------------------------------------------
# Paths and logger setup
# ---------------------------------------------------------------------------

# Logs live in storage/database/log/ at the project root (NOT inside app/)
PROJECT_ROOT = Path(__file__).parent.parent.parent
LOGS_DIR = PROJECT_ROOT / "storage" / "database" / "log"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Internal logger name — use get_structured_logger() to obtain
_LOGGER_NAME = "cheddar.structured"


# ---------------------------------------------------------------------------
# Trace ID — contextvar fallback for code outside Flask request context
# ---------------------------------------------------------------------------

# When code runs inside a Flask request (most HTTP handlers), g.trace_id
# stores the trace ID. When code runs outside a request (background jobs,
# tests, CLI scripts), this contextvar is the fallback.
_trace_id_var: contextvars.ContextVar[str] = contextvars.ContextVar("trace_id", default="no-trace")


def generate_trace_id() -> str:
    """Create a new short trace ID — first 8 characters of a UUID4 hex.

    Why 8 chars: readable in logs, still 4 billion combos — enough for
    one process. The full UUID is overkill for a single-request trace.
    """
    return uuid.uuid4().hex[:8]


def get_trace_id() -> str:
    """Return the current trace ID, preferring request context.

    Checks g.trace_id first (set by before_request hook for HTTP requests).
    Falls back to the contextvar (set manually for background jobs, tests).
    Returns "no-trace" if neither was ever set — means something logs
    before a trace ID was generated.
    """
    if has_request_context() and hasattr(g, "trace_id"):
        return g.trace_id
    return _trace_id_var.get()


def set_trace_id(trace_id: str) -> None:
    """Set the trace ID on both g (request context) and the contextvar.

    Why both: inside a request, all code reads g automatically. Outside a
    request, the contextvar is the only store. Setting both means any code
    path — Flask or otherwise — finds the trace ID with get_trace_id().
    """
    if has_request_context():
        g.trace_id = trace_id
    _trace_id_var.set(trace_id)


def get_origin() -> str:
    """Return "user_request" or "internal" based on whether we're in a Flask request.

    If inside a request context, this was triggered by an HTTP hit — "user_request".
    Otherwise it's a background job, test, or CLI script — "internal".
    The caller can override this by passing origin= directly in extra.
    """
    return "user_request" if has_request_context() else "internal"


# ---------------------------------------------------------------------------
# JSON formatter — one JSON object per log line
# ---------------------------------------------------------------------------


class JsonFormatter(logging.Formatter):
    """Format log records as single-line JSON objects for machine parsing.

    Why JSON lines: every line is a valid JSON object. You can pipe through
    `jq` to filter, aggregate, or search. Standard text logs require regex;
    JSON lines are unambiguous.
    """

    # Fields that must always appear, in order
    _BASE_FIELDS = ["timestamp", "level", "logger", "module", "route", "event"]

    def format(self, record: logging.LogRecord) -> str:
        # Start with the fixed ordered fields
        log_entry: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "module": record.module,
            "route": getattr(record, "route", "-"),
            "event": record.getMessage(),
        }

        # Auto-inject trace_id and origin if the caller didn't set them explicitly.
        # This means even a bare logger.info("hello") gets a trace ID for free.
        # If the caller passed trace_id in extra=, that wins.
        if not hasattr(record, "trace_id"):
            record.trace_id = get_trace_id()
        if not hasattr(record, "origin"):
            record.origin = get_origin()

        # Fold in extra attributes passed via `extra=` or set on the record.
        # We use record.__dict__ instead of dir() because dir() leaks
        # internal methods and properties (getMessage, levelname, etc.).
        std_attrs = frozenset(
            {
                "args",
                "asctime",
                "created",
                "exc_info",
                "exc_text",
                "filename",
                "funcName",
                "levelname",
                "levelno",
                "lineno",
                "module",
                "msecs",
                "msg",
                "name",
                "pathname",
                "process",
                "processName",
                "relativeCreated",
                "stack_info",
                "thread",
                "threadName",
            }
        )
        for key, value in record.__dict__.items():
            if key.startswith("_") or key in self._BASE_FIELDS or key in std_attrs:
                continue
            if value is not None:
                log_entry[key] = value

        # Attach exception info if present
        if record.exc_info and record.exc_info[0]:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry, default=str, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Handler factory — one handler writes everything to rotating daily files
# ---------------------------------------------------------------------------


def _build_file_handler() -> TimedRotatingFileHandler:
    """Create a date-rotating handler that writes to storage/database/log/cheddar-YYYY-MM-DD.jsonl.

    Why TimedRotatingFileHandler: rotates at midnight, keeps one file per day.
    No manual cron job needed. No external logrotate config needed.
    The suffix is the date, so files sort naturally.
    """
    handler = TimedRotatingFileHandler(
        filename=str(LOGS_DIR / "cheddar.jsonl"),
        when="midnight",
        interval=1,
        backupCount=90,  # Keep 90 days of logs
        encoding="utf-8",
        utc=True,
    )

    # Name rotated files with the date they cover
    # e.g. cheddar.jsonl.2026-09-28
    handler.suffix = "%Y-%m-%d"

    handler.setFormatter(JsonFormatter())
    handler.setLevel(logging.DEBUG)

    return handler


# ---------------------------------------------------------------------------
# Logger getter — call this anywhere you need to emit structured logs
# ---------------------------------------------------------------------------

# Lazily built singleton
_structured_logger: logging.Logger | None = None


def get_structured_logger() -> logging.Logger:
    """Return the project-wide structured JSON logger.

    Why a function instead of a module-level variable: the handler needs
    the LOGS_DIR to exist (which may be created after import), and we want
    to avoid side effects at import time. This is safe to call as many times
    as needed — the same logger instance is reused.
    """
    global _structured_logger

    if _structured_logger is not None:
        return _structured_logger

    logger_instance = logging.getLogger(_LOGGER_NAME)
    logger_instance.setLevel(logging.DEBUG)

    # Don't propagate to the root logger (which writes app/logs/server.log)
    logger_instance.propagate = False

    # Only add handler once
    if not logger_instance.handlers:
        logger_instance.addHandler(_build_file_handler())

    _structured_logger = logger_instance

    return _structured_logger


# ---------------------------------------------------------------------------
# Global request logging — before_request + after_request hooks
# ---------------------------------------------------------------------------


def _should_skip_logging() -> bool:
    """Decide whether to skip logging for this request.

    Returns True for noisy requests we don't care about:
      - Dash internal dependency requests (/_dash-*)
      - Static asset files (.css, .js, favicon.ico, etc.)
      - Requests with no endpoint (internal routing noise)

    Why filter these: Dash fires hundreds of internal polling requests
    per minute. Logging every single one would swamp the log files and
    make real requests hard to find.
    """
    # Dash internal dependency and update requests
    if request.path.startswith("/_dash-"):
        return True

    # Static asset files served by Flask
    if request.endpoint and request.endpoint.startswith("static"):
        return True

    # No matched endpoint — internal routing or preflight noise
    # Still log POST/PUT/DELETE even without endpoint — could be malformed
    return request.endpoint is None and request.method in ("GET", "OPTIONS", "HEAD")


def _capture_request_context() -> dict[str, Any]:
    """Build a dict of request metadata for the structured log.

    Captures: client IP, HTTP method, route path, request body (for
    POST/PUT/PATCH, truncated to 500 chars), and user identity if
    the request is authenticated.
    """
    # Resolve client IP, handling reverse proxies
    client_ip = (
        request.headers.get("X-Forwarded-For", "").split(",")[0].strip()
        or request.remote_addr
        or "-"
    )

    log_context: dict[str, Any] = {
        "trace_id": get_trace_id(),
        "origin": "user_request",
        "client_ip": client_ip,
        "http_method": request.method,
        "route_path": request.path,
    }

    # Try to read the request body (only for methods that carry one)
    if request.method in ("POST", "PUT", "PATCH"):
        try:
            body = request.get_json(silent=True)
            if body is not None:
                body_str = json.dumps(body, default=str, ensure_ascii=False)
                if len(body_str) > 500:
                    log_context["request_body"] = body_str[:500] + "...[truncated]"
                else:
                    log_context["request_body"] = body_str
        except Exception:
            log_context["request_body"] = "[unreadable]"

    # Identify the user if authenticated
    try:
        from flask_login import current_user

        if (
            current_user
            and hasattr(current_user, "is_authenticated")
            and current_user.is_authenticated
        ):
            log_context["user_id"] = getattr(current_user, "id", "unknown")
    except Exception:  # noqa: BLE001
        pass

    return log_context


def _capture_response_summary(response: Any) -> dict[str, Any]:
    """Extract status code and a brief body preview from a Flask response.

    Returns a dict with 'status_code' and optionally 'response_body'.
    The body preview shows dict keys, list length, or first 200 chars
    of string — never the full response — to keep logs compact.
    """
    result: dict[str, Any] = {}

    # Flask responses may be tuples: (body, status) or (body, status, headers)
    if isinstance(response, tuple):
        status_code = response[1] if len(response) > 1 else 200
        raw_body = response[0]
    else:
        status_code = getattr(response, "status_code", 200)
        raw_body = response

    result["status_code"] = status_code

    # Extract a preview of the response body
    if raw_body is None:
        return result

    try:
        if hasattr(raw_body, "get_json"):
            body_data = raw_body.get_json(silent=True)
        elif hasattr(raw_body, "get_data"):
            body_data = raw_body.get_data(as_text=True)
        else:
            body_data = raw_body

        if isinstance(body_data, dict):
            keys = list(body_data.keys())
            size = len(json.dumps(body_data, default=str))
            result["response_body"] = f"dict keys={keys} len={size}"
        elif isinstance(body_data, list):
            result["response_body"] = f"list len={len(body_data)}"
        elif isinstance(body_data, str):
            preview = body_data[:200]
            if len(body_data) > 200:
                preview += "...[truncated]"
            result["response_body"] = preview
        else:
            result["response_body"] = str(type(body_data).__name__)
    except Exception:
        result["response_body"] = "[unreadable]"

    return result


def register_global_request_logging(app: Flask) -> None:
    """Wire global before_request and after_request hooks for structured logging.

    This is the single entry point for request logging. Once called during
    app startup, EVERY HTTP request (minus filtered noise) is logged as a
    JSON line. No decorators needed on individual route handlers.

    Why hooks instead of decorators: Dash callbacks, static files, and any
    route added later by third-party code all pass through Flask's hook
    system. Decorators only cover routes you explicitly annotate.
    """

    @app.before_request
    def _log_request_start() -> None:
        """Generate trace ID, capture request metadata, store start time on g."""
        if _should_skip_logging():
            return

        # Generate a fresh trace ID for this request and store it on g.
        # All log lines in this request's lifecycle will share this ID.
        set_trace_id(generate_trace_id())

        # Store start time for elapsed-time calculation in after_request
        g._log_start_time = time.monotonic()

        # Store request context to enrich the after_request log entry
        g._log_context = _capture_request_context()

    @app.after_request
    def _log_request_end(response: Any) -> Any:
        """Log the completed request with response details and elapsed time."""
        # Skip if before_request decided to skip this one
        if not hasattr(g, "_log_start_time"):
            return response

        logger_instance = get_structured_logger()
        log_context = g.pop("_log_context", {})
        start_time = g.pop("_log_start_time")
        g.pop("trace_id", None)

        elapsed_ms = round((time.monotonic() - start_time) * 1000, 2)
        log_context["elapsed_ms"] = elapsed_ms

        # Attach response summary
        response_info = _capture_response_summary(response)
        log_context.update(response_info)

        status_code = log_context.get("status_code", 0)

        # Choose log level based on status code
        if 200 <= status_code < 400:
            logger_instance.info("REQUEST_COMPLETE", extra=log_context)
        elif 400 <= status_code < 500:
            logger_instance.warning("REQUEST_CLIENT_ERROR", extra=log_context)
        else:
            logger_instance.error("REQUEST_SERVER_ERROR", extra=log_context)

        return response


# ---------------------------------------------------------------------------
# Route logging decorator — kept for backward compatibility, no-op in global mode
# ---------------------------------------------------------------------------

# Flag to prevent double-logging when both global hooks and the decorator
# are active. Set by register_global_request_logging.
_GLOBAL_LOGGING_ACTIVE = False


def log_route(func: Any) -> Any:
    """Decorator that logs a single route hit (legacy, kept for backward compat).

    When global request logging is active (the default), this decorator
    does nothing — the before_request/after_request hooks already capture
    every request. When global logging is somehow disabled, this falls
    back to the old per-route behavior.

    Why keep this: existing route code may still reference it. Removing
    the decorator import is harmless, but keeping the decorator itself
    around prevents import errors if any code still uses it.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # If global hooks are active, skip — they already log this request
        if _GLOBAL_LOGGING_ACTIVE:
            return func(*args, **kwargs)

        # Fallback: old per-route logging (used only when global is off)
        logger_instance = get_structured_logger()
        start_time = time.monotonic()

        log_context = _capture_request_context()

        logger_instance.info("REQUEST_START", extra=log_context)

        try:
            response = func(*args, **kwargs)
        except Exception as exc:
            elapsed_ms = round((time.monotonic() - start_time) * 1000, 2)
            log_context["elapsed_ms"] = elapsed_ms
            log_context["error_type"] = type(exc).__name__
            log_context["error_message"] = str(exc)
            logger_instance.error("REQUEST_ERROR", extra=log_context)
            raise

        elapsed_ms = round((time.monotonic() - start_time) * 1000, 2)
        log_context["elapsed_ms"] = elapsed_ms

        response_info = _capture_response_summary(response)
        log_context.update(response_info)

        status_code = log_context.get("status_code", 0)
        if 200 <= status_code < 400:
            logger_instance.info("REQUEST_COMPLETE", extra=log_context)
        elif 400 <= status_code < 500:
            logger_instance.warning("REQUEST_CLIENT_ERROR", extra=log_context)
        else:
            logger_instance.error("REQUEST_SERVER_ERROR", extra=log_context)

        return response

    return wrapper


# ---------------------------------------------------------------------------
# Legacy compatibility — audit logging and permission checks
# ---------------------------------------------------------------------------

logger = logging.getLogger("cheddar.audit")

_ROLE_ROUTES: dict[str, list[str]] = {
    "viewer": ["/chat/send"],
    "analyst": [
        "/chat/*",
        "/tools/read_document",
        "/tools/search_documents",
        "/storage/*",
    ],
    "admin": ["*"],
}

# Track whether register_middleware has been called so we don't double-register
_MIDDLEWARE_REGISTERED = False


def register_middleware(app: Flask) -> None:
    """Wire global request logging, permission checks, and audit logging.

    This is the main entry point called from app/entry.py during startup.
    It activates:

    1. Global structured request logging (before_request + after_request)
    2. Permission checks on protected routes
    3. Legacy audit logging via the standard Python logger

    Why one function: single call site, no risk of forgetting one piece.
    """
    global _GLOBAL_LOGGING_ACTIVE, _MIDDLEWARE_REGISTERED

    # Prevent double-registration if called multiple times
    if _MIDDLEWARE_REGISTERED:
        return
    _MIDDLEWARE_REGISTERED = True

    # Activate global structured JSON logging
    _GLOBAL_LOGGING_ACTIVE = True
    register_global_request_logging(app)

    # Wire up permission checks and legacy audit logging
    _register_timer(app)
    _register_permission_check(app)
    _register_audit_log(app)


def _register_timer(app: Flask) -> None:
    """Store request start time on g for the legacy audit logger."""

    @app.before_request
    def _start_timer() -> None:
        g.request_start = time.monotonic()


def _register_permission_check(app: Flask) -> None:
    """Block requests that the current user's role doesn't allow."""

    @app.before_request
    def _check_permission() -> tuple[dict[str, str], int] | None:
        if _is_public_route():
            return None

        user = _get_current_user()
        if user is None:
            return _json_error("Unauthorized"), 401

        role = getattr(user, "role", "viewer") or "viewer"
        if not _has_permission(role, request.path):
            return _json_error("Forbidden"), 403

        return None


def _register_audit_log(app: Flask) -> None:
    """Write a one-line audit trail entry after every request (legacy format)."""

    @app.after_request
    def _audit_log(response: Any) -> Any:
        elapsed = time.monotonic() - g.pop("request_start", time.monotonic())
        user = _get_current_user()
        user_id = user.id if user else "-"
        logger.info(
            "AUDIT method=%s path=%s user=%s status=%s elapsed=%.3fs",
            request.method,
            request.path,
            user_id,
            response.status_code,
            elapsed,
        )
        return response


def _is_public_route() -> bool:
    """Check if a route is accessible without authentication."""
    if request.endpoint is None:
        return True
    if request.endpoint.startswith("static"):
        return True
    public_prefixes = ("/auth/", "/_", "/storage/", "/chat/", "/tools/", "/debug/")
    if any(request.path.startswith(p) for p in public_prefixes):
        return True
    return request.path == "/"


def _get_current_user() -> Any | None:
    """Return the currently authenticated user, or None if not logged in."""
    from flask_login import current_user

    if current_user and hasattr(current_user, "is_authenticated") and current_user.is_authenticated:
        return current_user
    return None


def _has_permission(role: str, path: str) -> bool:
    """Check if a role is allowed to access a path based on _ROLE_ROUTES."""
    patterns = _ROLE_ROUTES.get(role, [])
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def _json_error(message: str) -> dict[str, str]:
    """Build a standard JSON error response body."""
    return {"error": message}


def get_user_context() -> dict[str, str]:
    """Build a dict of user profile fields for the system prompt."""
    user = _get_current_user()
    if user is None:
        return {}
    return {
        "division": getattr(user, "division", "") or "",
        "region": getattr(user, "region", "") or "",
        "role": getattr(user, "role", "") or "",
    }


# ---------------------------------------------------------------------------
# Convenience logging functions for trace-aware internal code
# ---------------------------------------------------------------------------


def log_internal(event: str, trace_id: str | None = None, **extra: Any) -> None:
    """Log an internal/background event with origin="internal".

    Use this for code paths that run outside HTTP request handling —
    scheduled tasks, background jobs, CLI scripts, test harnesses.
    If trace_id is given, it overrides whatever the contextvar says.
    The event string is short and descriptive: "DB_MIGRATE", "CACHE_REBUILD", etc.

    Why a convenience function: callers don't need to remember to pass
    origin="internal" or trace_id in extra= every time.
    """
    logger_instance = get_structured_logger()

    log_extra: dict[str, Any] = {"origin": "internal"}
    if trace_id is not None:
        log_extra["trace_id"] = trace_id
    log_extra.update(extra)

    logger_instance.info(event, extra=log_extra)


def log_function_call(module: str, function: str, **extra: Any) -> None:
    """Log entry into a significant internal function for route-trail auditing.

    Emits a "FUNCTION_CALL" event with the module and function name.
    The log line picks up trace_id and origin automatically via the
    JsonFormatter — no need to pass them.

    Why explicit logging: with trace IDs, you can grep for one trace ID
    and see every major function call along that request's path. This
    makes debugging multi-step workflows trivial.

    Note: uses 'caller_module' and 'caller_function' as field names
    because 'module' and 'function' collide with LogRecord built-ins.
    """
    logger_instance = get_structured_logger()
    logger_instance.info(
        "FUNCTION_CALL",
        extra={"caller_module": module, "caller_function": function, **extra},
    )
