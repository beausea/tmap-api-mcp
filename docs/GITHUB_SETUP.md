# GitHub 저장소 올리기

로컬은 **원격 이름 `main`**, **브랜치 `main`** 으로 관리합니다. 원격 URL은 `https://github.com/beausea/tmap-api-mcp.git` 입니다.

- **푸시**: `git push -u main main` (최초 1회) 후에는 `git push`
- **풀**: `git pull main main`

---

## 이미 저장소를 만든 경우

GitHub에 [beausea/tmap-api-mcp](https://github.com/beausea/tmap-api-mcp) 가 이미 있으면, 로컬 커밋을 올리려면:

```bash
cd /Users/beausea/Workspace/tmap-api-mcp
git push -u main main
```

이후에는 `git push` 만 하면 됩니다.

---

## 새로 저장소를 만들 때 (다른 계정/이름)

### 방법 A: GitHub CLI

```bash
gh auth login
cd /Users/beausea/Workspace/tmap-api-mcp
gh repo create tmap-api-mcp --public --source=. --remote=main --push
```

### 방법 B: 웹에서 빈 저장소 생성 후

1. [GitHub New Repository](https://github.com/new) 에서 **Repository name**: `tmap-api-mcp`, **Public**, README 추가 안 함 → Create repository.
2. 원격 URL 설정 (사용자명이 다르면 수정):

   ```bash
   git remote set-url main https://github.com/본인사용자명/tmap-api-mcp.git
   ```

3. 푸시:

   ```bash
   git push -u main main
   ```
