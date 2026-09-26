# Awesome Research Stages

**연구 단계별 오픈소스 도구 모음** — 주제설정부터 결론·시사점 도출까지, 사회과학·정책연구에서 쓸 만한 GitHub 레포를 단계별로 골랐다.

*A curated list of open-source tools for each stage of social science and policy research: topic setting, literature review, analytical framework, data analysis, and conclusions.*

```
① 주제설정 → ② 이론·선행연구 → ③ 분석틀 설계 → ④ 데이터 분석 → ⑤ 결론·시사점
```

## 고른 기준

- **스타 수가 많은 레포를 우선**하되, 스타가 적어도 해당 분야 표준인 도구는 넣었다. 스타가 많은 레포는 AI·ML 개발자층에 몰려 있고, `fixest`·`did`·`bibliometrix`·`quanteda`처럼 스타가 수백 개인 R 패키지가 실제 학계에서는 사실상 표준이다.
- 각 단계 안에서는 스타 수 순으로 정렬한다.
- 💤 = 최근 1년간 푸시 없음 · 🗄️ = 보관(archived) 처리됨

레포 37개 · 스타 수 갱신일 **2026-09-26** (GitHub Actions가 매주 자동 갱신)

## 목차

- [① 주제설정](#topic) — 아이디어·연구질문 탐색
- [② 이론·선행연구 수집·분석](#literature) — 문헌관리·문헌 질의·체계적 문헌고찰·계량서지
- [③ 분석틀 설계](#framework) — 인과구조·가설·식별 조건
- [④ 데이터 분석](#analysis) — 정량·정성
- [⑤ 결론·시사점 도출](#conclusion) — 결과 해석·정리·집필

<a id="topic"></a>
## ① 주제설정

*아이디어·연구질문 탐색*

| 레포 | ★ | 최근 푸시 | 용도 |
|---|---:|---|---|
| [stanford-oval/storm](https://github.com/stanford-oval/storm) | 31.5k | 2025-09-30 | 주제를 여러 관점으로 조사해 위키식 개관을 쓴다. 낯선 주제의 지형을 빠르게 잡을 때 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 29.6k | 2026-08-27 | 딥리서치 에이전트. 웹과 로컬 문서를 섞어 조사 보고서 생성 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 14.6k | 2025-12-19 | 아이디어 생성→실험→논문 자동화. 새로움 검사(novelty check) 로직이 참고할 만하다 |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 12.7k | 2026-08-10 🗄️ | 딥리서치 레퍼런스 구현. 보관 처리돼 더는 갱신되지 않으니 코드 참고용 |
| [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | 5.8k | 2025-10-16 | NeurIPS 2025. 선행연구에서 연구 아이디어를 뽑아낸다 |

<a id="literature"></a>
## ② 이론·선행연구 수집·분석

*문헌관리·문헌 질의·체계적 문헌고찰·계량서지*

| 레포 | ★ | 최근 푸시 | 용도 |
|---|---:|---|---|
| [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | 25.8k | 2026-07-14 | 내 PDF 묶음과 대화하는 RAG. 인용 위치를 표시한다 |
| [zotero/zotero](https://github.com/zotero/zotero) | 15.4k | 2026-09-25 | 문헌관리의 표준 |
| [windingwind/zotero-pdf-translate](https://github.com/windingwind/zotero-pdf-translate) | 11.9k | 2026-09-21 | Zotero 안에서 해외 문헌 번역 |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 9.2k | 2026-09-25 | 논문 전용 RAG. 인용 정확도가 강점이라 선행연구 질의응답에 맞다 |
| [MuiseDestiny/zotero-gpt](https://github.com/MuiseDestiny/zotero-gpt) | 7.4k | 2026-05-01 | Zotero에 LLM 연결(요약·질의) |
| [asreview/asreview](https://github.com/asreview/asreview) | 1.0k | 2026-09-21 | 체계적 문헌고찰의 선별 작업을 능동학습으로 줄여 준다 |
| [massimoaria/bibliometrix](https://github.com/massimoaria/bibliometrix) | 664 | 2026-09-24 | 계량서지 분석(R). 스타는 적지만 이 분야 표준 |

<a id="framework"></a>
## ③ 분석틀 설계

*인과구조·가설·식별 조건*

> 이 단계는 스타가 많은 레포가 드물다. 개념 설계 작업이 코드로 잘 옮겨지지 않기 때문이다.

| 레포 | ★ | 최근 푸시 | 용도 |
|---|---:|---|---|
| [py-why/dowhy](https://github.com/py-why/dowhy) | 8.3k | 2026-09-25 | 인과 가정을 그래프로 명시하고 식별 가능성·반박 검정을 확인한다. 분석틀 검증용으로 가장 추천 |
| [py-why/causal-learn](https://github.com/py-why/causal-learn) | 1.7k | 2026-09-04 | 데이터로 인과구조를 탐색한다(탐색적 틀 설정) |
| [jtextor/dagitty](https://github.com/jtextor/dagitty) | 351 | 2026-03-04 | DAG를 그려 통제변수 조합과 식별 조건을 도출한다. 웹판 있음 |
| [ChicagoHAI/hypothesis-generation](https://github.com/ChicagoHAI/hypothesis-generation) | 131 | 2025-11-12 | HypoGeniC. 데이터·문헌에서 LLM으로 가설 생성(연구용 코드) |

<a id="analysis"></a>
## ④ 데이터 분석

*정량·정성*

### 정량

| 레포 | ★ | 최근 푸시 | 용도 |
|---|---:|---|---|
| [shap/shap](https://github.com/shap/shap) | 25.8k | 2026-09-25 | ML 모델 해석(변수 기여도) |
| [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) | 11.7k | 2026-09-25 | 파이썬 회귀·시계열·계량경제 기본기 |
| [uber/causalml](https://github.com/uber/causalml) | 6.0k | 2026-08-20 | 이질적 처치효과·업리프트 분석 |
| [py-why/EconML](https://github.com/py-why/EconML) | 4.8k | 2026-09-25 | DML 등 ML 기반 인과추정(Microsoft) |
| [bashtage/linearmodels](https://github.com/bashtage/linearmodels) | 1.1k | 2026-09-21 | 패널·도구변수 회귀 |
| [jasp-stats/jasp-desktop](https://github.com/jasp-stats/jasp-desktop) | 1.0k | 2026-09-26 | SPSS를 대신할 GUI 통계 패키지(베이지안 포함) |
| [lrberge/fixest](https://github.com/lrberge/fixest) | 456 | 2026-06-26 | 고정효과 추정(R). 정책평가 계량의 사실상 표준 |
| [bcallaway11/did](https://github.com/bcallaway11/did) | 420 | 2026-08-28 | 다기간(staggered) 이중차분(R) |

### 정성

| 레포 | ★ | 최근 푸시 | 용도 |
|---|---:|---|---|
| [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio) | 28.3k | 2026-09-25 | 텍스트 코딩·주석 작업(협업 가능) |
| [doccano/doccano](https://github.com/doccano/doccano) | 10.8k | 2026-04-14 | 가벼운 텍스트 라벨링 |
| [MaartenGr/BERTopic](https://github.com/MaartenGr/BERTopic) | 7.9k | 2026-09-24 | 토픽모델링. 정책문서·언론 분석 |
| [quanteda/quanteda](https://github.com/quanteda/quanteda) | 888 | 2026-09-15 | 정치학 쪽 텍스트 계량(R) |
| [bab2min/Kiwi](https://github.com/bab2min/Kiwi) | 782 | 2026-09-15 | 한국어 형태소 분석. 국문 텍스트라면 필수 |
| [ccbogel/QualCoder](https://github.com/ccbogel/QualCoder) | 680 | 2026-09-23 | NVivo·ATLAS.ti를 대신할 오픈소스 질적 코딩 도구 |

<a id="conclusion"></a>
## ⑤ 결론·시사점 도출

*결과 해석·정리·집필*

> 시사점을 도출하는 판단 자체를 자동화한 오픈소스는 사실상 없다. 여기 모은 것은 결과를 해석하고 정리해 글로 옮기는 도구다.

| 레포 | ★ | 최근 푸시 | 용도 |
|---|---:|---|---|
| [typst/typst](https://github.com/typst/typst) | 56.3k | 2026-09-24 | LaTeX 대안 조판 시스템 |
| [jgm/pandoc](https://github.com/jgm/pandoc) | 46.4k | 2026-09-25 | md→docx·pdf 변환, 인용 자동 처리 |
| [overleaf/overleaf](https://github.com/overleaf/overleaf) | 18.2k | 2026-09-17 | 공동 LaTeX 집필 |
| [quarto-dev/quarto-cli](https://github.com/quarto-dev/quarto-cli) | 6.0k | 2026-09-25 | 분석 코드와 본문을 한 문서에 두는 재현 가능한 보고서 |
| [JabRef/jabref](https://github.com/JabRef/jabref) | 4.8k | 2026-09-25 | BibTeX 참고문헌 관리 |
| [vincentarelbundock/modelsummary](https://github.com/vincentarelbundock/modelsummary) | 952 | 2026-08-19 | 회귀표를 출판용으로 정리(R) |
| [vincentarelbundock/marginaleffects](https://github.com/vincentarelbundock/marginaleffects) | 647 | 2026-09-16 | 한계효과·예측값 해석(R). 계수를 시사점 언어로 옮기는 단계 |

## 기여하기

추가하고 싶은 레포가 있으면 `data/repos.json`의 해당 단계에 `{"repo": "owner/name", "note": "용도 한 줄"}`을 넣어 PR을 보내 주세요. README는 직접 고치지 않습니다 — 스크립트가 생성합니다.

```bash
GITHUB_TOKEN=$(gh auth token) python3 scripts/build_readme.py
```

## 라이선스

[CC0 1.0](LICENSE) — 목록 자체는 퍼블릭 도메인. 각 도구의 라이선스는 해당 레포를 따른다.
