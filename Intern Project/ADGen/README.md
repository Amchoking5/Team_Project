# 📝 Intern Projects

> ***코드는 회사보안상 공개가 어려워 데모결과, 사이트, 아키텍쳐 흐름 위주로 정리하였습니다***  

<br />

# 🎨 광고 영상 생성 프로젝트 : ADGen

> 네이버 영상생성 AI를 활용한 광고 생성 프로젝트입니다.    
> 광고 URL을 입력하면 데이터를 수집해 핵심 정보들을 수집하여, 선택한 광고전략과 목표시간에 맞는 스토리보드를 구성합니다.   
> 이후 광고 레퍼런스를 분석하여 시작이미지를 생성한 뒤 I2V로 광고영상을 생성합니다.  

### 1. 제작기간

> 2026.07 ~ 2026.08

### 2. 핵심 역할

> 영상생성 일관성 유지   
> AI 스토리보드, 광고 생성 파이프라인 설계   

### 3. 결과물
<details>
<summary>ADGen 메인 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/c154b73d-385c-4a92-ac5f-065571b4986d" width="800px"/>
</div>
</details>

<details>
<summary>스토리보드 전략 설정</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/f4c9df4a-a602-4a0f-9652-792d640a852e" width="800px"/>
</div>
</details>

<details>
<summary>스토리보드 구성 트리</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/d0c5df4b-bede-4dcc-b3a8-c327192b4b74" width="800px"/>
</div>
</details>

<details>
<summary>등장인물, 배경 레퍼런스 고정</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/8f1aa6fb-33b0-43a4-a41c-03a231efb82f" width="800px"/>
</div>
</details>

<details>
<summary>스토리보드 상세 결과 확인</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/593f9dd9-0815-4686-92e6-40e1931257d5" width="800px"/>
</div>
</details>

<details>
<summary>스토리보드 이미지, 컷 영상 생성</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/9ece71d2-2a01-4916-aeb4-c5cec5f2a4b5" width="800px"/>
</div>
</details>

<details>
<summary>영상 세부 편집</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/85fccb60-493d-46e0-ab64-4ad0261e6335" width="800px"/>
</div>
</details>

<details>
<summary>AI 광고 영상 합성</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/3cc01e12-66aa-45bc-b2cf-214d7b2c2713" width="800px"/>
</div>
</details>

<br />

# 📚 사용 기술

### 1. Back-end

> Fastapi   
> Chat GPT   
> langchain   
> lightx2v   

### 2. Front-end

> javascript  
> typescript  
> React.js  
> Vite   

# 📊 Structure

<details>
<summary>Structure</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/96ed3b97-143d-404c-a8c1-bdc33f9c2301"width="800px"/>
</div>
</details>
<br />

# 🔑 핵심기능

### 1. AI 스토리보드 생성

> 데이터 크롤링으로 분석한 상품정보를 활용해 AI가 스토리보드를 구성하고 제안합니다.   
> 목표전략과 목표설정을 설정하면 해당 조건에 맞게 컷을 구성하고, 트리구조로 만들어줍니다.   
> 각각의 컷별로 배경과 등장인물을 구체적으로 설정합니다.     

### 2. 레퍼런스 고정

> I2V 영상생성 모델을 사용하였기 때문에 영상생성 모델 자체적으로 레퍼런스를 유지하는 기능이 없습니다.   
> 따라서 최대한 레퍼런스의 특징과 동일한 컷별 시작이미지를 GPT Image2를 활용해 만들고 이를 I2V 자사 모델로 생성했습니다.   
> 등장하는 배경, 인물, 사물을 고정시켜 저장해 두고 컷 이미지를 만들 때 관련 레퍼런스 이미지를 첨부하여 R2I 생성을 하는 방법으로 일관성을 유지했습니다.   

### 3. 광고 영상 생성 

> 스토리보드별 시작이미지를 바탕으로 I2V 영상을 생성하고, 마음에 들지 않는 부분이 있다면 프롬프트를 수정하여 재생성 할 수 있습니다.   
> 영상의 시작과 끝부분에서 마음에 들지 않는 부분이 있다면 잘라낼 수 있고, 영상의 배속을 변경할 수 있습니다.   
> 만들어진 영상들 중 마음에 드는 영상들을 골라 합성하여 최종 광고 영상을 만듭니다.   

<br />