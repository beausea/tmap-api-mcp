"""POI 검색: 장소(POI) 통합 검색. T MAP API 1:1."""

import json

from ..client import get


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
    """장소(POI) 통합 검색. 시설물명·상호·주소·전화번호 등으로 검색합니다.

    Args:
        search_keyword: 검색 키워드.
        search_type: 검색 타입 (all, name, address, tel 등). 기본 all.
        page: 페이지 번호. 기본 1.
        count: 페이지당 개수. 기본 20.
        res_coord_type: 응답 좌표 타입. WGS84GEO 등.
        req_coord_type: 요청 좌표 타입.
        center_lon: 중심 경도 (주변 검색 시).
        center_lat: 중심 위도 (주변 검색 시).
        radius: 반경(m). 주변 검색 시 사용.
    """
    params = {
        "version": 1,
        "searchKeyword": search_keyword,
        "searchType": search_type,
        "page": page,
        "count": count,
        "resCoordType": res_coord_type,
        "reqCoordType": req_coord_type,
    }
    if center_lon is not None:
        params["centerLon"] = center_lon
    if center_lat is not None:
        params["centerLat"] = center_lat
    if radius is not None:
        params["radius"] = radius
    data = await get("/tmap/pois", params=params)
    return json.dumps(data, ensure_ascii=False, indent=2)
