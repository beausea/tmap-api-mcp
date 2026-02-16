"""설정: appKey는 환경변수에서만 읽습니다."""

import os

import pytest


def test_require_app_key_raises_when_unset(monkeypatch):
    monkeypatch.delenv("TMAP_APP_KEY", raising=False)
    from tmap_api_mcp._config import require_app_key
    with pytest.raises(ValueError, match="appKey"):
        require_app_key()


def test_require_app_key_returns_value_when_set(monkeypatch):
    monkeypatch.setenv("TMAP_APP_KEY", "test-key")
    from tmap_api_mcp._config import require_app_key
    assert require_app_key() == "test-key"


def test_get_app_key_none_when_unset(monkeypatch):
    monkeypatch.delenv("TMAP_APP_KEY", raising=False)
    from tmap_api_mcp._config import get_app_key
    assert get_app_key() is None


def test_get_app_key_returns_value_when_set(monkeypatch):
    monkeypatch.setenv("TMAP_APP_KEY", "test-key")
    from tmap_api_mcp._config import get_app_key
    assert get_app_key() == "test-key"
