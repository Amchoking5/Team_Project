# 📝 Intern Projects

> ***코드는 회사보안상 공개가 어려워 데모결과, 사이트, 아키텍쳐 흐름 위주로 정리하였습니다***  

<br />

# 3. 🖼️ 마음돌봄 프로젝트

> AI와 대화하며 위로를 받는 심리 치료 프로젝트입니다.  
> ***주변에 속마음을 표현하지 않는 아동의 감정을 더욱 이해할 수 있게 AI로 이끌어내보자!***라는 아이디어에서 시작했습니다.  
> 사용자의 성격과 심리 테스트 결과를 받아 본인만의 캐릭터를 생성하고, AI와 대화하며 오늘 하루를 돌아봅니다.  
> 대화 내용은 이미지 생성형 AI를 사용해 그림일기로 만들어지며, 갤러리에서 확인할 수 있습니다.  

### 1. 제작기간

> 2024.02 ~ 2025.05

### 2. 핵심 역할

> 멀티턴 LLM  
> Stable diffusion 3 API 서버 연결
> 캐릭터 일관성 향상(프롬프트 딕셔너리, 사용자별 Lora 생성 및 관리)  

### 3. 결과물
<details>
<summary>그림일기 예시</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/cc40b43a-3a71-4a80-bac5-b59f2dd4eb17" width="800px"/>
</div>
</details>

# 📚 사용 기술

### 1. Back-end

> python3  
> Fastapi   
> langchain  

### 2. Front-end

> python3  
> gradio  
> javascript  
> typescript  
> React.js  

# 📊 Structure

<details>
<summary>마음돌봄 프로젝트</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/7c24bdf9-c085-42c2-bbdc-0cd7babf2d0f" width="800px"/>
</div>
</details>

<br />

# 🔑 핵심기능

### 1. 캐릭터 생성

> 아직 사용자의 캐릭터가 없다면 사용자에게 좋아하는 것, 현재 심리상태 등의 정보를 입력받아 사용자만의 캐릭터를 생성합니다.  
> 해당 캐릭터 사진을 바탕으로 One-page lora를 사용해 캐릭터의 특징을 학습하여 프롬프트와 함께 저장합니다.  
> 이미지를 생성할 때 사용자의 lora 정보를 불러와 사용자의 캐릭터를 생성합니다.  

### 2. 멀티턴 LLM

> 아동, 청소년 상담데이터를 Naver clova studio의 Fine tuning 기능을 활용하여 학습합니다.  
> AI와 대화할 때 그때 느꼈던 감정, 어떻게 행동하고 싶었는지 등 꼬리를 무는 질문을 이어갑니다.  

### 3. 갤러리 기능

> AI가 대화내용을 요약하여 오늘 하루의 일기를 써주고, 해당 내용으로 이미지를 생성합니다.  
> 생성된 이미지와 일기는 갤러리에 시간별로 저장되며, 확인할 수 있습니다.  

<br />