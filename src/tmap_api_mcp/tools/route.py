"""경로안내: 자동차·보행자. T MAP API 1:1."""

import json

from ..client import post


def _pedestrian_body(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    start_name: str | None,
    end_name: str | None,
) -> dict:
    """보행자 API는 startX/startY/endX/endY 형식을 사용합니다."""
    return {
        "startX": str(start_x),
        "startY": str(start_y),
        "endX": str(end_x),
        "endY": str(end_y),
        "startName": start_name or "출발",
        "endName": end_name or "도착",
    }


def _car_body(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    start_name: str | None,
    end_name: str | None,
) -> dict:
    """자동차 경로 API는 routesInfo.departure/destination(lon, lat) 형식을 사용합니다."""
    return {
        "routesInfo": {
            "departure": {
                "name": start_name or "출발",
                "lon": str(start_x),
                "lat": str(start_y),
            },
            "destination": {
                "name": end_name or "도착",
                "lon": str(end_x),
                "lat": str(end_y),
            },
        }
    }


async def route_car(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    start_name: str | None = None,
    end_name: str | None = None,
) -> str:
    """자동차 경로안내. 출발/도착 좌표(WGS84)로 경로를 탐색합니다.

    Args:
        start_x: 출발 경도.
        start_y: 출발 위도.
        end_x: 도착 경도.
        end_y: 도착 위도.
        start_name: 출발지 이름(선택).
        end_name: 도착지 이름(선택).
    """
    body = _car_body(start_x, start_y, end_x, end_y, start_name, end_name)
    data = await post("/tmap/routes", json=body)
    return json.dumps(data, ensure_ascii=False, indent=2)


async def route_pedestrian(
    start_x: float,
    start_y: float,
    end_x: float,
    end_y: float,
    start_name: str | None = None,
    end_name: str | None = None,
) -> str:
    """보행자 경로안내. 출발/도착 좌표(WGS84)로 도보 경로를 탐색합니다.

    Args:
        start_x: 출발 경도.
        start_y: 출발 위도.
        end_x: 도착 경도.
        end_y: 도착 위도.
        start_name: 출발지 이름(선택).
        end_name: 도착지 이름(선택).
    """
    body = _pedestrian_body(
        start_x, start_y, end_x, end_y, start_name, end_name
    )
    data = await post("/tmap/routes/pedestrian", json=body)
    return json.dumps(data, ensure_ascii=False, indent=2)
