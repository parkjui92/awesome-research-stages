## 기여하기

추가하고 싶은 레포가 있으면 `data/repos.json`의 해당 단계에 `{"repo": "owner/name", "note": "용도 한 줄"}`을 넣어 PR을 보내 주세요. README는 직접 고치지 않습니다 — 스크립트가 생성합니다.

```bash
GITHUB_TOKEN=$(gh auth token) python3 scripts/build_readme.py
```

## 라이선스

[CC0 1.0](LICENSE) — 목록 자체는 퍼블릭 도메인. 각 도구의 라이선스는 해당 레포를 따른다.
