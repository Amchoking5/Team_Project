# 📝 Intern Projects

> ***코드는 회사보안상 공개가 어려워 데모결과, 사이트, 아키텍쳐 흐름 위주로 정리하였습니다***  

<br />

# 💬 세종시 챗봇 AI 충녕

> 세종시 관련 데이터를 스스로 학습하여 답변을 제공해주는 시스템입니다.  
> Langchain과 RAG를 활용해 질문 query와 관련된 문장을 찾고, LLM을 활용해 답변을 생성합니다.  

### 1. 제작기간

> 2024.06 ~ 2024.10

### 2. 핵심 역할

> 답변 정확도 향상 및 할루시네이션 억제  
> (전처리 구조 개선, 코사인 유사도 Top k 적용, Threshold 적용)  

### 3. 결과물
<details>
<summary>웹 사이트</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/89890bbb-a37a-4ec0-af9a-f834f7040362" width="800px"/>
</div>
</details>

> [사이트 주소](https://aichat.sejong.go.kr/)  

# 📚 사용 기술

### 1. Back-end

> python3  
> Fastapi  
> Pinecone DB  
> langchain  
> poetry  

### 2. Front-end

> javascript  
> typescript  
> React.js  

# 📊 Structure

<details>
<summary>문서 전처리 학습과정</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/e81e720f-146f-4520-bfe3-9b7c786ad8ff" width="800px"/>
</div>
</details>

<br />

<summary>답변 생성 과정</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/bd355e67-02a5-40d4-b646-4768f546ab2c" width="800px"/>
</div>
</details>

<br />

# 🔑 핵심기능

### 1. 문서 전처리

> 사용자가 업로드 한 자료을 Naver clova studio의 Chunking기능을 활용해 분리하여 임베딩합니다.  
> 마찬가지로 세종시 사이트에 있는 자료를 크롤링하여 전처리를 진행합니다.  
> 키워드, 예상질문과 답변, 본문으로 나눈 뒤 Pinecone DB에 저장합니다.  

### 2. 답변 생성

> 질문 Query가 들어왔을 때, Query를 임베딩하여 Pinecone DB에 저장되어 있는 값들과 코사인 유사도를 비교합니다.  
> 만약 어떤 문서도 Threshold값을 넘기지 못하면 정보를 찾지 못했다는 답변을 제공하여 할루시네이션을 예방합니다.  
> Top K개의 문서를 확인하여 프롬프트에 함께 제공한 뒤 답변을 생성합니다.  

<br />