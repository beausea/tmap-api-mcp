# tmap-api-mcp

T MAP Open API를 [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) 도구로 노출하는 서버입니다.

- **1:1 매핑**: T MAP API 한 개당 MCP 도구 한 개.
- **조합은 호출 측**: 장소 검색 → 경로 안내 등 플로우는 프롬프트/클라이언트에서 여러 도구를 순서대로 호출.

## 설치 및 실행

```bash
# uv
uv add tmap-api-mcp
# 또는 클론 후
cd tmap-api-mcp && uv sync
```

**환경변수**: T MAP API 키가 필요합니다. [SK open API](https://openapi.sk.com)에서 발급 후 설정하세요.

```bash
export TMAP_APP_KEY="your-app-key"
```

**MCP 서버 실행 (stdio)**:

```bash
uv run tmap-api-mcp
# 또는
PYTHONPATH=src python -m tmap_api_mcp.server
```

Cursor 등에서 MCP 서버로 추가할 때는 명령에 `uv run tmap-api-mcp` 또는 `python -m tmap_api_mcp.server`를, 인자에 `[]`를 사용하면 됩니다.

## 제공 도구

| 도구 | 설명 |
|------|------|
| `poi_search` | 장소(POI) 통합 검색 |
| `geocode` | 주소 → 좌표 (지오코딩) |
| `reverse_geocode` | 좌표 → 주소 (리버스 지오코딩) |
| `route_car` | 자동차 경로안내 |
| `route_pedestrian` | 보행자 경로안내 |

## 문서

- [MCP 설계 가이드](docs/MCP_DESIGN_GUIDE.md) — 설계 원칙, API 매핑 절차, 도구 명명 규칙 등.

## API 참조

- [T MAP API](https://tmapapi.tmapmobility.com/main.html)
- [TMAP API 약관](https://tmapapi.tmapmobility.com/terms.html)
- [SK open API](https://openapi.sk.com) (API 키 발급)

## 라이선스

MIT. 재배포 시 출처 표기. T MAP API 이용 시 해당 약관을 준수해야 합니다.
