# 📝 Intern Projects

> ***코드는 회사보안상 공개가 어려워 데모결과, 사이트, 아키텍쳐 흐름 위주로 정리하였습니다***  

<br />

# 📊 QA 데이터 수집 웹 페이지 : Annohub

> 경쟁사 영상 생성 모델과 비교하여 성능을 파악하기 위한 벤치마크 QA 페이지입니다.
> Java Script와 Node JS를 사용해 프론트엔드와 벡엔드를 구성했습니다.
> PairWise, PointWise 방식으로 각각 QA의 점수를 측정하고, 결과를 Chroma DB에 저장합니다.

### 1. 제작기간

> 2026.02 ~ 2026.03

### 2. 핵심 역할

> QA 평가 데이터 수집 파이프라인 구축 및 웹 페이지 제작
> QA 작업자 근태 관리 시스템 제작

### 3. 결과물
<details>
<summary>Pointwise 기반 영상 점수 측정 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/06eab15e-43b7-4380-82c9-56bc162f57ff" width="800px"/>
</div>
</details>

<details>
<summary>Pointwise 기반 영상 점수 분석 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/ecc0e054-7dc8-4b4f-a920-ceeede8075a1" width="800px"/>
</div>
</details>

<details>
<summary>Pairwise 기반 영상 점수 측정 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/a39dfd40-9c67-4ae6-b8f7-6c4db38e42fa" width="800px"/>
</div>
</details>

<details>
<summary>Pairwise 기반 영상 점수 분석 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/7e8a04ae-bd59-42d2-b0ac-b304114f2bc5" width="800px"/>
</div>
</details>

<details>
<summary>근태 확인 달력 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/dc6053f1-1e04-4ebb-be09-6e69d9855f45" width="800px"/>
</div>
</details>

<details>
<summary>근태 분석 및 통계 확인</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/380fc1e0-4046-4147-a93e-eb5f34413c12" width="800px"/>
</div>
</details>

<br />

# 📚 사용 기술

### 1. Back-end

> javascript
> Node.js
> Chroma DB
> 공공 데이터 포탈 API

### 2. Front-end

> javascript  
> typescript  
> React.js  

# 📊 Structure

<details>
<summary>Structure</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/dc07141b-c8ef-4008-ba1c-0f1b13ac9b4f"width="800px"/>
</div>
</details>
<br />

# 🔑 핵심기능

### 1. 관리자, 작업자에 따른 페이지 분리

> 작업자는 블라인드 영상에 대해 평가항목 평가를 진행합니다.
> 관리자는 모든 평가자의 진행상황 및 결과를 확인 가능합니다.
> 통계 페이지에서 작업자, 카테고리, 평가항목에 따른 각각의 점수 분포를 확인 및 분석 가능합니다.

### 2. PointWise 평가 페이지

> 영상미, 모션, 프롬프트 적합성, 물체보존 등의 요소에 대해 각각 1~5점으로 점수 측정합니다.
> 간단한 문장으로 코멘트를 달아 구체적인 이유를 표시 가능합니다.
> Mean Opinion Score로 평균 3, 표준편차 1의 값을 가지도록 조정한 평가점수를 확인 가능합니다.
> 숫자 단축키와 좌우 방향키로 빠르게 평가를 진행할 수 있도록 했습니다.

### 3. PairWise 평가 페이지

> 영상미, 모션, 프롬프트 적합성, 물체보존 등의 요소에 대해 두 영상중 더 나은 영상을 선택합니다.
> n개의 영상에 대해 총 nC2번의 평가를 진행합니다. 
> 편향을 방지하기 위해 사용자별로 랜덤한 순서와 랜덤한 좌우 위치에 영상이 배치되도록 합니다.
> 관리자는 정렬된 순서로 각각의 영상별 평가정보를 확인할 수 있습니다.
> 숫자 단축키와 좌우 방향키로 빠르게 평가를 진행할 수 있도록 했습니다.

### 4. 근태 관리 시스템

> Annohub 메인페이지의 출근, 퇴근 버튼을 눌러 출퇴근 기록을 기록할 수 있습니다.
> 공공데이터 포탈의 공휴일정보를 이용해 총 근무시간을 계산하고, 식사 및 휴계시간을 자동으로 처리해줍니다.
> 메모기능을 추가하여 특이 출퇴근 시간이나 휴가요일을 빠르게 파악해 작업자의 교육일정을 빠르게 조정할 수 있습니다.
> 통계페이지에서 설정한 구간별 총 근무시간을 확인할 수 있습니다. 

<br />
