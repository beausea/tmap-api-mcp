"""MCP 서버 도구 등록 및 설정 검증."""

import pytest
from mcp.server.fastmcp import FastMCP


@pytest.fixture
def server():
    """tmap_api_mcp 서버 모듈을 로드해 mcp 인스턴스를 반환합니다."""
    from tmap_api_mcp.server import mcp
    return mcp


def test_mcp_instance_is_fastmcp(server):
    assert isinstance(server, FastMCP)


def test_tools_registered(server):
    """설계 가이드: 1:1 매핑된 도구가 등록되어 있어야 합니다."""
    tools = getattr(server, "_tool_manager", server)
    tool_names = list(getattr(tools, "_tools", {}).keys())
    expected = {"poi_search", "geocode", "reverse_geocode", "route_car", "route_pedestrian"}
    assert set(tool_names) == expected, f"Expected {expected}, got {set(tool_names)}"
