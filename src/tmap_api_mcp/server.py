"""MCP 서버 진입점. T MAP API를 1:1 도구로 노출합니다."""

from mcp.server.fastmcp import FastMCP

from .tools.geocoding import geocode as _geocode, reverse_geocode as _reverse_geocode
from .tools.poi import poi_search as _poi_search
from .tools.route import route_car as _route_car, route_pedestrian as _route_pedestrian

mcp = FastMCP("tmap-api-mcp")


@mcp.tool()
async def poi_search(
    search_keyword: str,
    search_type: str = "all",
    page: int = 1,
    count: int = 20,
    res_coord_type: str = "WGS84GEO",
    req_coord_type: str = "WGS84GEO",
    center_lon: str | None = None,
    center_lat: str | None = None,
    radius: str | None = None,
) -> str:
    """장소(POI) 통합 검색. 시설물명·상호·주소·전화번호로 검색합니다."""
    return await _poi_search(
        search_keyword=search_keyword,
        search_type=search_type,
        page=page,
        count=count,
        res_coord_type=res_coord_type,
        req_coord_type=req_coord_type,
        center_lon=center_lon,
        center_lat=center_lat,
        radius=radius,
    )


@mcp.tool()
async def geocode(
    address: str,
    city_do: str | None = None,
    gu_gun: str | None = None,
    res_coord_type: str = "WGS84GEO",
) -> str:
    """주소를 좌표로 변환(지오코딩)."""
    return await _geocode(
        address=address,
        city_do=city_do,
        gu_gun=gu_gun,
        res_coord_type=res_coord_type,
    )


@mcp.tool()
async def reverse_geocode(
    lat: float,
    lon: float,
    res_coord_type: str = "WGS84GEO",
    address_type: str = "A10",
) -> str:
    """좌표를 주소로 변환(리버스 지오코딩)."""
    return await _reverse_geocode(
        lat=lat,
        lon=lon,
        res_coord_type=res_coord_type,
        address_type=address_type,
    )


@mcp.tool()
async def route_car(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    start_name: str | None = None,
    end_name: str | None = None,
) -> str:
    """자동차 경로안내. 출발/도착 WGS84 좌표로 경로 탐색."""
    return await _route_car(
        start_x=start_x,
        start_y=start_y,
        end_x=end_x,
        end_y=end_y,
        start_name=start_name,
        end_name=end_name,
    )


@mcp.tool()
async def route_pedestrian(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    start_name: str | None = None,
    end_name: str | None = None,
) -> str:
    """보행자 경로안내. 출발/도착 WGS84 좌표로 도보 경로 탐색."""
    return await _route_pedestrian(
        start_x=start_x,
        start_y=start_y,
        end_x=end_x,
        end_y=end_y,
        start_name=start_name,
        end_name=end_name,
    )


def main() -> None:
    """stdio 전송으로 MCP 서버 실행."""
    mcp.run(transport="stdio")
