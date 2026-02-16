"""T MAP API HTTP 클라이언트. appKey를 헤더에 붙여 요청합니다."""

import httpx

from ._config import BASE_URL, require_app_key


def _headers() -> dict[str, str]:
    return {
        "appKey": require_app_key(),
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


async def get(path: str, params: dict | None = None) -> dict:
    """GET 요청 후 JSON을 반환합니다. 오류 시 예외 또는 응답 본문을 반환합니다."""
    url = f"{BASE_URL}{path}"
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(url, headers=_headers(), params=params or {})
        resp.raise_for_status()
        return resp.json() if resp.content else {}


async def post(path: str, json: dict | None = None) -> dict:
    """POST 요청 후 JSON을 반환합니다."""
    url = f"{BASE_URL}{path}"
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(url, headers=_headers(), json=json or {})
        resp.raise_for_status()
        return resp.json() if resp.content else {}
