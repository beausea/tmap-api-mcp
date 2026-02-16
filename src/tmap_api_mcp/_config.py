"""설정: API 키는 환경변수에서만 읽습니다."""

import os

BASE_URL = "https://apis.openapi.sk.com"
APP_KEY_ENV = "TMAP_APP_KEY"


def get_app_key() -> str | None:
    """환경변수에서 appKey를 반환합니다. 없으면 None."""
    return os.environ.get(APP_KEY_ENV)


def require_app_key() -> str:
    """appKey를 반환합니다. 없으면 예외를 발생시킵니다."""
    key = get_app_key()
    if not key:
        raise ValueError(
            f"T MAP API appKey가 필요합니다. 환경변수 {APP_KEY_ENV}를 설정하세요."
        )
    return key
