"""지오코딩: 주소↔좌표 변환. T MAP API 1:1."""

import json

from ..client import get, post


async def geocode(
    address: str,
    city_do: str | None = None,
    gu_gun: str | None = None,
    res_coord_type: str = "WGS84GEO",
) -> str:
    """주소를 좌표로 변환(지오코딩).

    Args:
        address: 주소 또는 지번.
        city_do: 시/도 (선택).
        gu_gun: 구/군 (선택).
        res_coord_type: 응답 좌표 타입. WGS84GEO 등.
    """
    params = {
        "version": 1,
        "address": address,
        "resCoordType": res_coord_type,
    }
    if city_do:
        params["city_do"] = city_do
    if gu_gun:
        params["gu_gun"] = gu_gun
    data = await get("/tmap/geocoding", params=params)
    return json.dumps(data, ensure_ascii=False, indent=2)


async def reverse_geocode(
    lat: float,
    lon: float,
    res_coord_type: str = "WGS84GEO",
    address_type: str = "A10",
) -> str:
    """좌표를 주소로 변환(리버스 지오코딩).

    Args:
        lat: 위도.
        lon: 경도.
        res_coord_type: 요청/응답 좌표 타입.
        address_type: 주소 유형. A10(도로명), A20(지번) 등.
    """
    params = {
        "version": 1,
        "lat": str(lat),
        "lon": str(lon),
        "resCoordType": res_coord_type,
        "addressType": address_type,
    }
    data = await get("/tmap/geo/reverseGeocoding", params=params)
    return json.dumps(data, ensure_ascii=False, indent=2)
