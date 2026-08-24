# 📝 Intern Projects

> ***코드는 회사보안상 공개가 어려워 데모결과, 사이트, 아키텍쳐 흐름 위주로 정리하였습니다***  

<br />

# ⚙️ 스스로 개선하는 AI : Necro Flow

> 영상생성 모델을 고도화 하기위한 프로젝트입니다.
> 구간별로 체크포인트를 만들어 이전 체크포인트 혹은 타겟 체크포인트의 영상생성 모델과 비교하여 스스로 성능을 개선합니다.  
> Unified reward model을 사용해 두 영상을 비교하여, AI로 약점을 분석한 뒤, 오픈소스 사이트에서 해당 약점을 보완하기 위한 데이터 셋을 추가 수집하여 재학습합니다.
> 로그를 통해 진행상황 및 AI분석 리포트, 데이터 수집 관계도 등을 확인할 수 있습니다.

### 1. 제작기간

> 2026.03 ~ 2025.06

### 2. 핵심 역할

> 전체 파이프라인 설계
> 기존 코드기반 작업들을 fastapi 서버를 활용하여 api통신으로 결합

### 3. 결과물
<details>
<summary>Necro Flow 메인 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/b0e007ee-f85f-4ab4-8422-f4a5ef4dfbfa" width="800px"/>
</div>
</details>

<details>
<summary>AI agent 사용예시</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/398d74e5-f450-4682-a3b0-491f5dbda381" width="800px"/>
</div>
</details>

<br />

<details>
<summary>데이터 수집 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/92388f72-dc71-4850-bff7-7c294efcee4e" width="800px"/>
</div>
</details>

<br />

<details>
<summary>영상 캡셔닝 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/ca8ae348-d738-418b-aaa9-00a6e08ff2e6" width="800px"/>
</div>
</details>

<br />

<details>
<summary>컷 분할 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/b53e4332-6250-4302-8549-59a27e81a1dd" width="800px"/>
</div>
</details>

<br />

<details>
<summary>AI 학습 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/3ae602a8-a383-4acc-8bd6-276ac8b66b07" width="800px"/>
</div>
</details>

<br />

<details>
<summary>영상 생성 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/748a2738-b746-4cb6-a387-be6fc6b5b161" width="800px"/>
</div>
</details>

<br />

<details>
<summary>영상 평가 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/0bf3c71b-591c-4363-bd1c-73e41617c0e1" width="800px"/>
</div>
</details>

<br />

<details>
<summary>영상 평가 상세 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/a4806d6f-e12d-4bcb-8d7c-5eb06f5fa82c" width="800px"/>
</div>
</details>

<br />

<details>
<summary>얼굴 인식 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/63d2b18c-47bc-4967-9504-7914289a7475" width="800px"/>
</div>
</details>

<br />

<details>
<summary>QA 평가 분석 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/c842ac55-a7c5-486f-beca-341ff8a78084" width="800px"/>
</div>
</details>

<br />

<details>
<summary>AI Agent report 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/97073db9-02c3-41a7-bbca-4e0367ae3181" width="800px"/>
</div>
</details>

<br />

<details>
<summary>API 연동 관리 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/7a40e6da-ffb9-446a-a754-0ea913353c8a" width="800px"/>
</div>
</details>

<br />

<details>
<summary>데이터 흐름 관리 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/a2444124-b613-46ff-9327-960a1e1c82dd" width="800px"/>
</div>
</details>

<br />

# 📚 사용 기술

### 1. Back-end

> Fastapi   
> Chroma DB   
> Mongo DB   
> langchain   
> Lightx2v   
> Unified   
> reward model   
> face detection   
> OCR   
> api data crawl   
> langchain  

### 2. Front-end

> javascript  
> typescript  
> React.js  
> Vite   

# 📊 Structure

<details>
<summary>Structure</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/bd43088e-ed69-4a14-a1ca-679214b20e85"width="800px"/>
</div>
</details>
<br />

# 🔑 핵심기능

### 1. AI Agent로 관리하는 영상 생성, 평가, 학습

> AI Agent를 활용해 24시간 영상 생성 모델을 고도화 하기위해 데이터를 처리합니다.   
> 영상은 자사모델 Necro와 경쟁사 모델(Runware 사이트)로 생성하였습니다.   
> 평가는 얼굴인식, QA 인간평가, AI 평가로 구성되어 있습니다.   
> AI Agent report에서 약점 분석 결과와 그에 따른 데이터 처리 흐름을 확인할 수 있습니다.   

### 2. 영상 평가를 위한 구체적인 분석

> 얼굴의 일관성을 확인하기 위해 얼굴인식 이후 벡터비교를 통해 가장 유사한 얼굴을 찾은 뒤, 코사인 유사도로 각각의 얼굴을 비교하여 점수를 측정한다.   
> Unified Reward Model을 통해 AI기반 통합 점수를 측정하여 데이터셋 영상별로 비교를 진행하고 평균을 내어 모델의 순위를 비교한다.   
> 기존 Annohub와 API연동을 진행하여 추가비교가 필요한 경우 Pairwise 비교 데이터셋을 만들어 작업자에게 자동으로 할당하여 처리한다.   

### 3. 수집된 데이터 전처리 알고리즘

> Pixabay, Pexels와 같은 라이센스가 자유로운 데이터 사이트에서 약점 키워드 기반으로 데이터를 수집한다.   
> 영상의 경우 컷편집을 통해 영상을 5~10초 정도의 짧은 영상으로 만들어 저장한다.
> 각각의 짧은 컷을 임베딩하여 Chroma DB에 저장한 뒤 중복되는 영상을 제거한다.   
> Sky caption, FIBO등 AI를 통해 영상 Captioning을 진행하여, ( 시작이미지, 영상, 캡션 프롬프트 )의 트리플렛 데이터셋을 만든다.
> 해당 데이터셋으로 AI 추가학습을 진행하고 이전 결과와 비교하여 롤백하거나 신규 체크포인트 지점을 이동시킨다.

<br />