# T MAP API MCP 설계 가이드

이 문서는 **T MAP API 공식 문서**를 기준으로 tmap-api-mcp의 MCP(Model Context Protocol) 서버를 설계·구현할 때 따를 가이드입니다.

---

## 1. API 참조 자료 (필수)

모든 API 스펙·샘플·설명은 아래 공식 사이트에서 확인합니다.

| 용도 | URL |
|------|-----|
| **API 전체 구조·가이드·샘플·Docs** | [T MAP API – Guide](https://tmapapi.tmapmobility.com/main.html) |
| **웹서비스 가이드** | [웹서비스 가이드](https://tmapapi.tmapmobility.com/main.html#webservice/guide/webserviceGuide.guide1) |
| **REST API 레퍼런스 (엔드포인트·파라미터)** | [tmap-skopenapi.readme.io](https://tmap-skopenapi.readme.io/reference) |
| **약관·한도** | [TMAP API 약관](https://tmapapi.tmapmobility.com/terms.html) |
| **API 키 발급** | [SK open API](https://openapi.sk.com) |

- **설계·구현 시**: T MAP API 사이트의 **API > Guide / Sample / Docs** 및 **웹서비스 가이드**에서 기능별 설명·요청/응답 형식을 확인한 뒤, readme.io에서 REST URL·메서드·파라미터를 맞춥니다.
- **Base URL**: `https://apis.openapi.sk.com` (SK Open API). 모든 요청에 `appKey` 헤더 필요.

---

## 2. MCP 설계 원칙

### 2.1 1:1 매핑

- **T MAP API 한 개 = MCP 도구(tool) 한 개**로 대응합니다.
- 한 도구가 여러 API를 묶어 호출하거나, 내부에서 “검색 후 경로 요청” 같은 플로우를 구현하지 않습니다.
- 공식 문서에 나온 **기능(엔드포인트/메서드) 단위**로 도구를 나눕니다.

### 2.2 조합은 호출 측

- “장소 검색 → 좌표 확인 → 경로 안내”, “주소 → 지오코딩 → 경로” 같은 **조합·플로우**는 MCP 서버에 두지 않습니다.
- **프롬프트, LLM, MCP 클라이언트**가 필요한 도구를 여러 번 호출해 순서대로 조합합니다.
- MCP는 **API를 그대로 노출**하고, 인자를 받아 해당 API만 호출한 뒤 응답을 반환하는 역할만 합니다.

### 2.3 데이터·캐시

- TMAP API 약관: **API로 얻은 데이터는 24시간 초과 저장·이용 불가**.
- MCP에서는 API 응답을 24시간 넘게 보관·캐시하지 않습니다. 실시간 요청/응답 또는 TTL ≤ 24시간 캐시만 사용합니다.

---

## 3. API → MCP 도구 매핑 절차

새 API를 MCP 도구로 추가할 때 아래 순서를 따릅니다.

### Step 1: 공식 문서에서 API 확인

1. [T MAP API – main](https://tmapapi.tmapmobility.com/main.html) 접속.
2. 왼쪽 메뉴에서 **API** > **Guide / Sample / Docs** 이동.
3. 대상 기능이 속한 그룹 확인:
   - **POI 검색** (장소 통합 검색, 상세, 주변 카테고리, 경로 반경, 읍면동/도로명 등)
   - **지오코딩** (Geocoding, Reverse, Full Text, 좌표변환, 주소변환 등)
   - **경로안내** (자동차, 보행자, 타임머신, 직선거리, 다중 경유지, 경유지 최적화 등)
   - **교통정보**, **Static Map**, **Road API**, **유가정보**, **경로 매트릭스**, **what3words**, **Puzzle** 등
4. [웹서비스 가이드](https://tmapapi.tmapmobility.com/main.html#webservice/guide/webserviceGuide.guide1)에서 해당 기능의 요청/응답 설명이 있으면 함께 참고.

### Step 2: REST 스펙 확인 (readme.io)

1. [tmap-skopenapi.readme.io – Reference](https://tmap-skopenapi.readme.io/reference)에서 동일 기능의 REST API 페이지 탐색.
2. 다음을 정리:
   - **HTTP 메서드** (GET / POST)
   - **URL 경로** (예: `/tmap/pois`, `/tmap/routes/pedestrian`)
   - **필수/선택 파라미터** (쿼리, 헤더, body)
   - **응답 형식** (JSON 필드 등)

### Step 3: 도구 이름·파라미터 정의

- **도구 이름**: API 기능을 직관적으로 나타내는 snake_case. 예: `poi_search`, `route_car`, `reverse_geocode`, `puzzle_restaurant_ranking_districts`.
- **도구 파라미터**: REST API의 요청 파라미터와 1:1로 대응시키고, 타입·필수 여부·설명을 명시해 LLM이 호출하기 쉽게 합니다.

### Step 4: 구현

- 공통 HTTP 클라이언트로 `appKey`를 붙여 해당 URL을 호출.
- 응답을 그대로 반환하거나, MCP 응답 형식에 맞게 감싸서 반환.
- **한 도구 = 한 API 호출**만 수행.

---

## 4. 도구 목록 참조 (공식 문서 기준)

T MAP API 사이트 **API > Sample / Docs** 구조를 기준으로, 아래와 같이 그룹별로 도구를 나눌 수 있습니다. 실제 URL·파라미터는 readme.io와 웹서비스 가이드에서 최종 확인합니다.

- **POI 검색**: 장소(POI) 통합 검색, 명칭(POI) 상세 정보 검색, 명칭(POI) 주변 카테고리 검색, 읍면동/도로명 조회, 지역분류코드 검색, 명칭(POI) 경로 반경 검색 → 각 1개 도구.
- **지오코딩**: Geocoding, Reverse Geocoding, Full Text Geocoding, 좌표변환, 주소변환, 가까운 도로 찾기, 우편번호 검색, Reverse Label → 각 1개 도구.
- **경로안내**: 자동차 경로안내, 보행자 경로안내, 타임머신 자동차, 직선 거리 계산, 경로 이미지 안내, 화물차 경로안내, 다중 경유지 안내(30/100/200), 경유지 순서 최적화(10/20/30/100) → 각 1개 도구.
- **기타**: 교통정보, 지오펜싱(공간검색·영역조회), Road API, Static Map, 유가정보, 경로 매트릭스, what3words 관련, **Puzzle**(장소 혼잡도, 음식점 목록/순위/분석 등) → 문서에 나온 기능당 1개 도구.

상세한 **API ↔ 도구 이름** 표는 프로젝트 계획서(예: `.cursor/plans/` 또는 `README.md`)의 1:1 목록을 따릅니다.

---

## 5. 도구 명명·설명 규칙

- **이름**: `동사_대상` 또는 `역할_대상` 형태의 snake_case. 예: `poi_search`, `route_car`, `geocode`, `reverse_geocode`, `puzzle_restaurant_ranking_districts`.
- **설명**: T MAP API 공식 문서의 해당 기능 설명을 요약해, “무엇을 하는 API인지”, “주요 인자(검색어, 좌표, 반경 등)”를 한두 문장으로 적습니다.
- **파라미터 설명**: readme.io/가이드의 파라미터 설명을 옮겨와 LLM이 올바른 값을 넣을 수 있게 합니다.

---

## 6. 에러 처리·약관 준수

- **appKey**: 코드에 포함하지 않고, 환경변수(예: `TMAP_APP_KEY`) 또는 설정에서만 읽습니다.
- **API 오류**: HTTP 상태 코드·에러 메시지를 그대로 또는 요약해 도구 응답에 포함해, 호출 측에서 재시도·대체 플로우를 결정할 수 있게 합니다.
- **약관**: 무료 한도 초과 시 종량/정액 가입 필요, 동일 서비스 다중 프로젝트 금지, **데이터 24시간 보관 금지**를 README 등에 안내합니다.

---

## 7. 참고 문서 링크 정리

| 문서 | URL |
|------|-----|
| T MAP API (API 전체) | https://tmapapi.tmapmobility.com/main.html |
| 웹서비스 가이드 | https://tmapapi.tmapmobility.com/main.html#webservice/guide/webserviceGuide.guide1 |
| REST API 레퍼런스 | https://tmap-skopenapi.readme.io/reference |
| TMAP API 약관 | https://tmapapi.tmapmobility.com/terms.html |
| SK open API | https://openapi.sk.com |

이 가이드는 위 자료를 기준으로 MCP를 설계·구현할 때 사용합니다. API 스펙이 변경되면 공식 문서를 다시 확인해 도구 목록과 파라미터를 갱신합니다.
