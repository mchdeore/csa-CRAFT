"""Tests for route gate, role escalation, and permission middleware."""

import pytest
from flask import Flask

from app.core.logging import (
    _ROLE_LEVEL,
    _ROUTE_RULES,
    _find_matching_rule,
    _has_permission,
    _role_number,
)


class TestRoleEscalation:
    """Higher roles inherit lower-role access."""

    def test_role_number_mapping(self) -> None:
        assert _role_number("base_user") == 1
        assert _role_number("power_user") == 2
        assert _role_number("admin") == 3
        assert _role_number("unknown") == 0

    def test_escalation_admin_passes_base_user(self) -> None:
        """admin (level 3) should pass any route requiring base_user (level 1)."""
        assert _role_number("admin") >= _role_number("base_user")

    def test_escalation_power_user_passes_base_user(self) -> None:
        """power_user (level 2) should pass routes requiring base_user (level 1)."""
        assert _role_number("power_user") >= _role_number("base_user")

    def test_base_user_fails_power_user(self) -> None:
        """base_user (level 1) fails routes requiring power_user (level 2)."""
        assert _role_number("base_user") < _role_number("power_user")

    def test_base_user_fails_admin(self) -> None:
        """base_user (level 1) fails routes requiring admin (level 3)."""
        assert _role_number("base_user") < _role_number("admin")


class TestRouteRules:
    """Route rules match correctly using fnmatch patterns."""

    def test_find_chat_send(self) -> None:
        rule = _find_matching_rule("/chat/send")
        assert rule is not None
        assert rule["min_role"] == "base_user"

    def test_find_chat_upload(self) -> None:
        rule = _find_matching_rule("/chat/upload")
        assert rule is not None
        assert rule["min_role"] == "power_user"

    def test_find_admin_wildcard(self) -> None:
        rule = _find_matching_rule("/admin/users")
        assert rule is not None
        assert rule["min_role"] == "admin"

    def test_find_admin_settings(self) -> None:
        rule = _find_matching_rule("/admin/settings")
        assert rule is not None
        assert rule["min_role"] == "admin"

    def test_no_rule_for_unknown_path(self) -> None:
        rule = _find_matching_rule("/unknown/path")
        assert rule is None

    def test_find_storage_list_wildcard(self) -> None:
        rule = _find_matching_rule("/storage/list/alice")
        assert rule is not None
        assert rule["min_role"] == "base_user"

    def test_find_storage_load_wildcard(self) -> None:
        rule = _find_matching_rule("/storage/load/bob/ws123")
        assert rule is not None
        assert rule["min_role"] == "base_user"


class TestHasPermission:
    """Backward-compatible permission check using rules."""

    def test_admin_has_admin_access(self) -> None:
        assert _has_permission("admin", "/admin/users") is True

    def test_base_user_no_admin_access(self) -> None:
        assert _has_permission("base_user", "/admin/users") is False

    def test_base_user_has_chat_access(self) -> None:
        assert _has_permission("base_user", "/chat/send") is True

    def test_power_user_has_upload_access(self) -> None:
        assert _has_permission("power_user", "/chat/upload") is True

    def test_base_user_no_upload_access(self) -> None:
        assert _has_permission("base_user", "/chat/upload") is False

    def test_unknown_path_denied(self) -> None:
        assert _has_permission("admin", "/secret/hack") is False


class TestInternalRoutes:
    """Internal route prefixes bypass the perimeter gate."""

    def test_internal_prefixes_exist(self) -> None:
        from app.core.logging import _INTERNAL_ROUTE_PREFIXES
        assert "/chat/internal/" in _INTERNAL_ROUTE_PREFIXES
        assert "/tools/execute/" in _INTERNAL_ROUTE_PREFIXES
        assert "/tools/list" in _INTERNAL_ROUTE_PREFIXES
        assert "/debug/" in _INTERNAL_ROUTE_PREFIXES

    def test_public_prefixes_exist(self) -> None:
        from app.core.logging import _PUBLIC_ROUTE_PREFIXES
        assert "/auth/" in _PUBLIC_ROUTE_PREFIXES
        assert "/static/" in _PUBLIC_ROUTE_PREFIXES


class TestJsonError:
    """Error response helper."""

    def test_json_error_format(self) -> None:
        from app.core.logging import _json_error
        result = _json_error("Forbidden")
        assert result == {"error": "Forbidden"}