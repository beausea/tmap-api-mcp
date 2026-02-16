# GitHub 저장소 올리기

로컬에는 이미 Git이 초기화되어 있고 `origin`이 `https://github.com/beausea/tmap-api-mcp.git` 로 설정되어 있습니다.

## 1. GitHub에서 저장소 만들기

1. [GitHub New Repository](https://github.com/new) 접속.
2. **Repository name**: `tmap-api-mcp`
3. **Public** 선택.
4. **"Add a README" 등 추가 파일 생성하지 않기** (로컬에 이미 있음).
5. **Create repository** 클릭.

## 2. 푸시

GitHub 사용자명이 **beausea**가 아니면 먼저 원격 URL을 수정하세요.

```bash
git remote set-url origin https://github.com/본인사용자명/tmap-api-mcp.git
```

그 다음 푸시:

```bash
git push -u origin main
```

이후부터는 `git push` 만 하면 됩니다.
