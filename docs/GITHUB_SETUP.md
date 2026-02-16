# GitHub 저장소 올리기

로컬에는 이미 Git이 초기화되어 있고, 커밋 2개가 있으며, `origin`이 `https://github.com/beausea/tmap-api-mcp.git` 로 설정되어 있습니다. **GitHub에는 아직 `tmap-api-mcp` 저장소가 없으므로** 아래 중 한 가지 방법으로 저장소를 만든 뒤 푸시하면 됩니다.

---

## 방법 A: GitHub CLI로 한 번에 (권장)

`gh`가 이미 설치되어 있습니다. **한 번만** 로그인하면 이후 저장소 생성·푸시를 한 번에 할 수 있습니다.

1. **로그인** (브라우저 또는 토큰 입력):

   ```bash
   gh auth login
   ```

   - GitHub.com 선택 → HTTPS → Login with browser 또는 Paste an authentication token 중 선택 후 진행.

2. **저장소 생성 + 푸시**:

   ```bash
   cd /Users/beausea/Workspace/tmap-api-mcp
   gh repo create tmap-api-mcp --public --source=. --remote=origin --push
   ```

   - GitHub에 `tmap-api-mcp` 저장소가 생성되고, 현재 브랜치가 자동으로 푸시됩니다.
   - 사용자명이 **beausea**가 아니면 `gh repo create` 시 자동으로 본인 계정에 만들어집니다.

---

## 방법 B: 웹에서 저장소 만든 뒤 푸시

1. **GitHub에서 빈 저장소 만들기**
   - [GitHub New Repository](https://github.com/new) 접속.
   - **Repository name**: `tmap-api-mcp`
   - **Public** 선택.
   - **"Add a README" 등 추가 파일 생성하지 않기** (로컬에 이미 있음).
   - **Create repository** 클릭.

2. **원격 URL** (사용자명이 beausea가 아니면 수정):

   ```bash
   git remote set-url origin https://github.com/본인사용자명/tmap-api-mcp.git
   ```

3. **푸시**:

   ```bash
   cd /Users/beausea/Workspace/tmap-api-mcp
   git push -u origin main
   ```

이후부터는 `git push` 만 하면 됩니다.
