# tmap-api-mcp

T MAP Open API를 [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) 도구로 노출하는 서버입니다.

- **1:1 매핑**: T MAP API 한 개당 MCP 도구 한 개.
- **조합은 호출 측**: 장소 검색 → 경로 안내 등 플로우는 프롬프트/클라이언트에서 여러 도구를 순서대로 호출.

## 문서

- [MCP 설계 가이드](docs/MCP_DESIGN_GUIDE.md) — 설계 원칙, API 매핑 절차, 도구 명명 규칙 등.

## API 참조

- [T MAP API](https://tmapapi.tmapmobility.com/main.html)
- [TMAP API 약관](https://tmapapi.tmapmobility.com/terms.html)
- [SK open API](https://openapi.sk.com) (API 키 발급)

## 라이선스

MIT. 재배포 시 출처 표기. T MAP API 이용 시 해당 약관을 준수해야 합니다.
