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

## 이 목록을 쓰는 법 — 써 보고, 내 연구에 맞게 고친다

여기 있는 도구는 대부분 영어권 자료와 특정 분야를 전제로 만들어졌다. 그대로 쓰면 반쯤 맞고 반쯤 어긋난다. 이 목록은 설치해서 끝내라는 추천표가 아니라 **고쳐 쓸 출발점**을 모아 둔 것이다.

1. **작게 써 본다** — 지금 하는 연구 단계에서 하나를 골라, 이미 결론을 아는 작은 자료(읽어 둔 논문 몇 편, 분석해 본 데이터 일부)에 돌려 본다. 답을 알아야 도구가 어디서 틀리는지 보인다.
2. **어긋나는 곳을 찾는다** — 한국어 문서를 못 읽는지, 국내 학술 DB(KCI·RISS·NKIS)를 모르는지, 프롬프트가 공학·의학 논문에 맞춰져 있는지, 정책연구에 필요한 출력(시사점·대안 비교)이 없는지 확인한다.
3. **내 쪽으로 고친다** — 포크해서 프롬프트·설정·입출력 형식을 바꾼다. 오픈소스라서 가능한 일이다. 코드를 직접 못 고쳐도 요즘은 AI 코딩 도구에 "이 레포를 한국어 정책문서에 맞게 고쳐 줘"라고 시키는 것으로 시작할 수 있다.
4. **다시 나눈다** — 고친 결과가 쓸 만하면 공개하거나 원 레포에 PR을 보낸다. 같은 불편을 겪는 연구자가 반드시 있다.

**이 목록 자체도 마찬가지다.** 포크해서 `data/repos.json`을 자기 분야에 맞게 빼고 더하면 나만의 목록이 된다(README는 스크립트가 다시 만든다).

> 고치기 전에 라이선스를 확인하자. MIT·Apache는 수정·재배포가 자유롭지만, GPL·AGPL(예: Zotero, pandoc)은 고친 것을 배포할 때 소스도 같은 라이선스로 공개해야 한다.

레포 37개 · 스타 수 갱신일 **2026-10-05** (GitHub Actions가 매주 자동 갱신)

## 목차

- [① 주제설정](#topic) — 아이디어·연구질문 탐색
- [② 이론·선행연구 수집·분석](#literature) — 문헌관리·문헌 질의·체계적 문헌고찰·계량서지
- [③ 분석틀 설계](#framework) — 인과구조·가설·식별 조건
- [④ 데이터 분석](#analysis) — 정량·정성
- [⑤ 결론·시사점 도출](#conclusion) — 결과 해석·정리·집필

<a id="topic"></a>
## ① 주제설정

*아이디어·연구질문 탐색*

| 레포 | ★ | 최근 푸시 | 용도 | 강점 |
|---|---:|---|---|---|
| [stanford-oval/storm](https://github.com/stanford-oval/storm) | 31.6k | 2025-09-30 💤 | 주제를 여러 관점으로 조사해 위키식 개관을 쓴다. 낯선 주제의 지형을 빠르게 잡을 때 | 관점이 다른 가상 전문가들의 질의응답을 시뮬레이션해 조사 범위가 한쪽으로 쏠리지 않는다. 결과 문서에 인용이 달리고, Co-STORM 모드에서는 사람이 대화에 끼어들어 방향을 틀 수 있다 |
| [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 29.9k | 2026-10-01 | 딥리서치 에이전트. 웹과 로컬 문서를 섞어 조사 보고서 생성 | 계획을 세운 뒤 여러 출처를 나눠 수집해 출처가 달린 장문 보고서를 낸다. 내 PDF 등 로컬 문서를 웹 검색과 함께 쓸 수 있고, LLM·검색엔진을 바꿔 끼울 수 있으며 MCP도 지원한다 |
| [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 14.7k | 2025-12-19 | 아이디어 생성→실험→논문 자동화. 새로움 검사(novelty check) 로직이 참고할 만하다 | 생성한 아이디어를 Semantic Scholar로 기존 연구와 대조해 이미 나온 것인지 걸러 내고, 자동 리뷰어로 결과를 스스로 평가한다. 실행 가능한 ML 실험을 전제로 하므로 사회과학에서는 아이디어·새로움 검사 단계만 떼어 쓰는 편이 현실적이다 |
| [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | 12.7k | 2026-08-10 🗄️ | 딥리서치 레퍼런스 구현. 보관 처리돼 더는 갱신되지 않으니 코드 참고용 | LangGraph로 짠 구조가 작고 읽기 쉬워 딥리서치가 어떻게 돌아가는지 배우기 좋다. 모델·검색 도구를 설정으로 바꿀 수 있고 Deep Research Bench 평가 결과를 공개했다 |
| [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) | 5.8k | 2025-10-16 | NeurIPS 2025. 선행연구에서 연구 아이디어를 뽑아낸다 | 문헌 검토부터 아이디어 도출·구현·논문 작성까지 전 과정을 한 틀에서 다룬다. 연구 에이전트를 평가하는 벤치마크 세트와 데이터를 함께 공개해 성능을 비교해 볼 수 있다 |

<a id="literature"></a>
## ② 이론·선행연구 수집·분석

*문헌관리·문헌 질의·체계적 문헌고찰·계량서지*

| 레포 | ★ | 최근 푸시 | 용도 | 강점 |
|---|---:|---|---|---|
| [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | 25.8k | 2026-07-14 | 내 PDF 묶음과 대화하는 RAG. 인용 위치를 표시한다 | 웹 UI가 있어 설치하면 바로 쓴다. 답변의 근거를 브라우저 PDF 뷰어에서 하이라이트로 보여 주고, 관련도가 낮으면 경고한다. Ollama 등 로컬 LLM을 쓰면 자료를 외부로 보내지 않을 수 있고, 다중 사용자·공유 컬렉션을 지원한다 |
| [zotero/zotero](https://github.com/zotero/zotero) | 15.5k | 2026-10-04 | 문헌관리의 표준 | 브라우저 커넥터로 논문 메타데이터와 PDF를 한 번에 저장하고, Word·LibreOffice 플러그인으로 인용과 참고문헌 목록을 자동 생성한다. CSL 인용 스타일이 방대하고, 그룹 라이브러리로 공동 연구진이 문헌을 함께 관리한다. 플러그인 생태계가 넓다 |
| [windingwind/zotero-pdf-translate](https://github.com/windingwind/zotero-pdf-translate) | 12.0k | 2026-10-03 | Zotero 안에서 해외 문헌 번역 | PDF에서 문장을 선택하면 바로 번역되고, 제목·초록 같은 메타데이터와 메모도 번역한다. 구글·DeepL·GPT 계열 등 번역 엔진을 골라 쓸 수 있다 |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | 9.3k | 2026-09-25 | 논문 전용 RAG. 인용 정확도가 강점이라 선행연구 질의응답에 맞다 | 검색한 문단을 LLM이 다시 요약·채점한 뒤 답하므로 엉뚱한 근거가 섞이는 일이 적고, 답마다 인용을 붙인다. 인용 수·철회(retraction) 여부 같은 메타데이터를 자동으로 보강해 준다 |
| [MuiseDestiny/zotero-gpt](https://github.com/MuiseDestiny/zotero-gpt) | 7.5k | 2026-05-01 | Zotero에 LLM 연결(요약·질의) | Zotero를 떠나지 않고 지금 연 PDF(전문 또는 선택 문장)나 선택한 논문에 질문하고 요약을 받는다. 선택한 문장을 바탕으로 내 라이브러리에서 관련 문헌을 찾아 준다 |
| [asreview/asreview](https://github.com/asreview/asreview) | 1.0k | 2026-09-28 | 체계적 문헌고찰의 선별 작업을 능동학습으로 줄여 준다 | 연구자가 몇 편을 포함·제외로 판정하면 관련 가능성이 높은 논문부터 보여 줘서 수천 편을 끝까지 다 읽지 않고도 선별할 수 있다. 판정 과정이 기록으로 남아 선별 절차를 보고하기 쉽다 |
| [massimoaria/bibliometrix](https://github.com/massimoaria/bibliometrix) | 666 | 2026-10-03 | 계량서지 분석(R). 스타는 적지만 이 분야 표준 | Web of Science·Scopus·Dimensions·OpenAlex 등에서 내보낸 파일을 바로 읽어 공저·동시인용·키워드 네트워크와 주제 변화를 분석한다. biblioshiny 웹 화면으로 코드 없이도 쓸 수 있다 |

<a id="framework"></a>
## ③ 분석틀 설계

*인과구조·가설·식별 조건*

> 이 단계는 스타가 많은 레포가 드물다. 개념 설계 작업이 코드로 잘 옮겨지지 않기 때문이다.

| 레포 | ★ | 최근 푸시 | 용도 | 강점 |
|---|---:|---|---|---|
| [py-why/dowhy](https://github.com/py-why/dowhy) | 8.3k | 2026-10-04 | 인과 가정을 그래프로 명시하고 식별 가능성·반박 검정을 확인한다. 분석틀 검증용으로 가장 추천 | 모형화→식별→추정→반박의 4단계를 강제해 머릿속 인과 가정을 코드로 드러낸다. 가짜 처치·무작위 공통원인 같은 반박 검정이 내장되어 있어 분석틀이 얼마나 버티는지 미리 볼 수 있고, EconML과 연동된다 |
| [py-why/causal-learn](https://github.com/py-why/causal-learn) | 1.7k | 2026-09-04 | 데이터로 인과구조를 탐색한다(탐색적 틀 설정) | 제약 기반(PC 등)·점수 기반(GES 등)·함수형 인과모형 기반 탐색 알고리즘을 한 패키지에 모았다. CMU Tetrad 계열을 파이썬으로 옮긴 것이라 이론적 배경이 탄탄하고, 독립성 검정·점수 함수 같은 부품도 따로 쓸 수 있다 |
| [jtextor/dagitty](https://github.com/jtextor/dagitty) | 351 | 2026-03-04 | DAG를 그려 통제변수 조합과 식별 조건을 도출한다. 웹판 있음 | 브라우저에서 그림 그리듯 인과 그래프를 그리면 어떤 변수를 통제해야 하는지(adjustment set)와 데이터로 검정할 수 있는 함의를 바로 계산해 준다. 같은 그래프를 R 패키지로 불러 논문 부록에서 재현할 수 있다 |
| [ChicagoHAI/hypothesis-generation](https://github.com/ChicagoHAI/hypothesis-generation) | 134 | 2025-11-12 | HypoGeniC. 데이터·문헌에서 LLM으로 가설 생성(연구용 코드) | LLM이 만든 가설 후보를 데이터에 대한 설명력으로 평가하며 반복해 다듬는다. 문헌에서 뽑은 가설과 데이터에서 뽑은 가설을 합치는 방식(HypoRefine)도 제공한다 |

<a id="analysis"></a>
## ④ 데이터 분석

*정량·정성*

### 정량

| 레포 | ★ | 최근 푸시 | 용도 | 강점 |
|---|---:|---|---|---|
| [shap/shap](https://github.com/shap/shap) | 25.8k | 2026-10-04 | ML 모델 해석(변수 기여도) | 섀플리 값으로 개별 예측을 변수별 기여로 일관되게 나눈다. 트리 모델용 빠른 알고리즘과 요약·의존도 그림이 있어 블랙박스 모델 결과를 보고서 언어로 옮기기 좋다 |
| [statsmodels/statsmodels](https://github.com/statsmodels/statsmodels) | 11.7k | 2026-10-04 | 파이썬 회귀·시계열·계량경제 기본기 | R처럼 수식(`y ~ x1 + x2`)으로 모형을 쓰고, 결과표에 표준오차·검정통계량이 기본으로 나온다. OLS·GLM·시계열·혼합모형·강건 표준오차까지 사회과학 통계의 기본기를 폭넓게 갖췄다 |
| [uber/causalml](https://github.com/uber/causalml) | 6.0k | 2026-10-04 | 이질적 처치효과·업리프트 분석 | 메타러너(S·T·X·R 러너)와 업리프트 트리 등 처치효과 이질성 추정기를 한곳에 모았다. '정책·개입에 누가 더 반응하는가'를 묻는 분석에 맞다 |
| [py-why/EconML](https://github.com/py-why/EconML) | 4.8k | 2026-10-01 | DML 등 ML 기반 인과추정(Microsoft) | Double Machine Learning·인과 포레스트·도구변수 기반 추정 등 경제학계의 최신 추정기를 신뢰구간과 함께 제공한다. 정책 트리로 효과가 누구에게 크고 작은지 해석할 수 있다 |
| [bashtage/linearmodels](https://github.com/bashtage/linearmodels) | 1.1k | 2026-09-28 | 패널·도구변수 회귀 | 패널 고정효과·확률효과, 2SLS·GMM, 군집 강건 표준오차 등 statsmodels에 부족한 계량경제 모형을 채워 준다 |
| [jasp-stats/jasp-desktop](https://github.com/jasp-stats/jasp-desktop) | 1.0k | 2026-10-03 | SPSS를 대신할 GUI 통계 패키지(베이지안 포함) | SPSS 사용자에게 익숙한 클릭 방식이라 코딩 없이 분석하고, 같은 분석을 빈도주의·베이지안 양쪽으로 돌려 볼 수 있다. 무료이고 윈도·맥·리눅스를 모두 지원한다 |
| [lrberge/fixest](https://github.com/lrberge/fixest) | 455 | 2026-06-26 | 고정효과 추정(R). 정책평가 계량의 사실상 표준 | 여러 겹의 고정효과를 매우 빠르게 추정하고, 여러 모형을 한 줄로 동시에 돌린다. 이중차분·이벤트스터디 그림과 출판용 LaTeX 표 출력을 기본 제공한다 |
| [bcallaway11/did](https://github.com/bcallaway11/did) | 420 | 2026-08-28 | 다기간(staggered) 이중차분(R) | Callaway & Sant'Anna(2021) 추정량의 저자 구현이다. 지역마다 정책 도입 시점이 다른 경우 기존 이원고정효과(TWFE) 추정이 갖는 편향을 피하고, 도입 후 기간별 효과를 집계해 보여 준다 |

### 정성

| 레포 | ★ | 최근 푸시 | 용도 | 강점 |
|---|---:|---|---|---|
| [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio) | 28.4k | 2026-10-05 | 텍스트 코딩·주석 작업(협업 가능) | 텍스트·이미지·음성 등 거의 모든 형식을 다루고, 코딩 체계를 설정으로 정의한다. 여러 코더가 함께 작업하고, ML 모델을 붙여 초벌 코딩을 자동으로 채울 수 있다 |
| [doccano/doccano](https://github.com/doccano/doccano) | 10.8k | 2026-04-14 | 가벼운 텍스트 라벨링 | 설치와 사용이 가볍고 문서 분류·개체명·구간 태깅처럼 텍스트 작업에 집중한다. 여러 명이 나눠 코딩하기 쉽다 |
| [MaartenGr/BERTopic](https://github.com/MaartenGr/BERTopic) | 7.9k | 2026-10-03 | 토픽모델링. 정책문서·언론 분석 | 문맥 임베딩을 써서 LDA보다 짧은 글에서도 주제가 또렷하다. 시간에 따른 주제 변화, 주제 계층, 시각화가 내장돼 있고, 다국어 임베딩 모델로 바꿔 한국어 문서에도 쓸 수 있다 |
| [quanteda/quanteda](https://github.com/quanteda/quanteda) | 891 | 2026-10-05 | 정치학 쪽 텍스트 계량(R) | 문서-특징 행렬, 사전 기반 분석이 빠르고 문서화가 잘돼 있다. 확장 패키지로 Wordfish 같은 정치 텍스트 척도화 모형까지 이어진다 |
| [bab2min/Kiwi](https://github.com/bab2min/Kiwi) | 789 | 2026-09-15 | 한국어 형태소 분석. 국문 텍스트라면 필수 | 속도가 빠르고 오타·띄어쓰기 오류에도 비교적 잘 버틴다. 사용자 사전으로 정책 용어·기관명을 쉽게 추가할 수 있고, 파이썬(kiwipiepy)·자바·C# 등으로 쓸 수 있다 |
| [ccbogel/QualCoder](https://github.com/ccbogel/QualCoder) | 689 | 2026-10-03 | NVivo·ATLAS.ti를 대신할 오픈소스 질적 코딩 도구 | 텍스트·PDF·이미지·음성·영상에 코드를 달고 메모·사례 속성·코드 교차 보고서를 만든다. AI 보조 코딩 기능이 있고 무료다 |

<a id="conclusion"></a>
## ⑤ 결론·시사점 도출

*결과 해석·정리·집필*

> 시사점을 도출하는 판단 자체를 자동화한 오픈소스는 사실상 없다. 여기 모은 것은 결과를 해석하고 정리해 글로 옮기는 도구다.

| 레포 | ★ | 최근 푸시 | 용도 | 강점 |
|---|---:|---|---|---|
| [typst/typst](https://github.com/typst/typst) | 56.4k | 2026-10-02 | LaTeX 대안 조판 시스템 | LaTeX보다 문법이 단순하고, 증분 컴파일로 결과가 거의 즉시 나오며, 오류 메시지가 읽기 쉽다. 웹 편집기(typst.app)에서 공동 작업도 할 수 있다 |
| [jgm/pandoc](https://github.com/jgm/pandoc) | 46.6k | 2026-10-05 | md→docx·pdf 변환, 인용 자동 처리 | 마크다운 원고 하나로 docx·pdf·html·LaTeX를 모두 뽑는다. citeproc로 CSL 스타일 인용과 참고문헌을 자동으로 만들고, 참조 문서를 지정해 워드 서식을 맞출 수 있다 |
| [overleaf/overleaf](https://github.com/overleaf/overleaf) | 18.2k | 2026-09-17 | 공동 LaTeX 집필 | 설치 없이 브라우저에서 여러 명이 LaTeX 원고를 동시에 편집한다. 오픈소스판을 기관 서버에 직접 설치해 쓸 수도 있다 |
| [quarto-dev/quarto-cli](https://github.com/quarto-dev/quarto-cli) | 6.1k | 2026-10-03 | 분석 코드와 본문을 한 문서에 두는 재현 가능한 보고서 | R·파이썬(Jupyter) 코드와 본문을 한 파일에 두어, 데이터나 분석이 바뀌면 표·그림·본문 수치가 함께 갱신된다. Word·PDF·HTML·슬라이드로 출력한다 |
| [JabRef/jabref](https://github.com/JabRef/jabref) | 4.8k | 2026-10-04 | BibTeX 참고문헌 관리 | BibTeX 파일을 직접 다뤄 LaTeX·pandoc과 궁합이 좋다. DOI로 서지 정보를 자동으로 채우고 중복 항목을 찾아 준다 |
| [vincentarelbundock/modelsummary](https://github.com/vincentarelbundock/modelsummary) | 952 | 2026-08-19 | 회귀표를 출판용으로 정리(R) | 여러 회귀모형을 한 표로 묶어 Word·LaTeX·HTML 등으로 내보낸다. 표준오차 종류를 바꿔 끼우는 등 표를 세밀하게 손볼 수 있다 |
| [vincentarelbundock/marginaleffects](https://github.com/vincentarelbundock/marginaleffects) | 647 | 2026-09-16 | 한계효과·예측값 해석(R). 계수를 시사점 언어로 옮기는 단계 | 로짓이나 상호작용항처럼 계수를 그대로 읽기 어려운 모형을 '확률이 몇 %p 바뀌는가' 같은 해석 가능한 양으로 바꿔 준다. 매우 많은 모형 종류를 지원하고 파이썬판도 있다 |

## 기여하기

추가하고 싶은 레포가 있으면 `data/repos.json`의 해당 단계에 `{"repo": "owner/name", "note": "용도 한 줄", "strength": "강점 한두 문장"}`을 넣어 PR을 보내 주세요. README는 직접 고치지 않습니다 — 스크립트가 생성합니다.

```bash
GITHUB_TOKEN=$(gh auth token) python3 scripts/build_readme.py
```

## 라이선스

[CC0 1.0](LICENSE) — 목록 자체는 퍼블릭 도메인. 각 도구의 라이선스는 해당 레포를 따른다.
