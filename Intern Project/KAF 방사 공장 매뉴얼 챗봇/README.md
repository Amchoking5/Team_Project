# 📝 Intern Projects

> ***코드는 회사보안상 공개가 어려워 데모결과, 사이트, 아키텍쳐 흐름 위주로 정리하였습니다***  

<br />

# 🏭 KAF 방사 공장 매뉴얼 챗봇

> 세종시 챗봇 AI 충녕의 후속 프로젝트입니다.  
> KAF 방사 공장의 메뉴얼 데이터를 학습하여 답변을 제공하고, 매뉴얼 생성을 도와주는 시스템입니다.  
> 다국어 기능, 음성 입출력 기능, LLM 답변 생성시 이미지 출력 기능을 구현했습니다.  
> 관리자 페이지에서 파일 업로드, 검색 삭제 가능하며, 피드백 페이지에서 잘못된 답변을 수정하여 다음 출력을 개선할 수 있습니다.   

### 1. 제작기간

> 2024.11 ~ 2025.01

### 2. 핵심 역할

> 관리자 및 피드백 페이지 개발 (Backend, Frontend)
> 참고자료 및 이미지 출력을 위한 DB 구조 변경

### 3. 결과물
<details>
<summary>서비스 소개</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/e29d4b4c-286b-48ef-a394-327ea68d5084" width="800px"/>
</div>
</details>

<br />

<details>
<summary>데모 비디오</summary>
<div markdown="1" style="padding-left: 15px;">
<video src="https://github.com/user-attachments/assets/f60694de-59a6-4e8e-b134-09abae814d72" width="800px" autoplay loop muted></video>
</div>
</details>

<br /> 

<details>
<summary>관리자 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/378a8299-0507-44a6-a687-cc86a4d888dd" width="800px"/>
</div>
</details>

<br />

<details>
<summary>피드백 페이지</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/708030fe-6b43-49e2-9089-3375ad7ee8ed" width="800px"/>
</div>
</details>

<br />

# 📚 사용 기술

### 1. Back-end

> python3  
> Fastapi  
> Pinecone DB  
> langchain  
> poetry  
> whisper  
> docker  
> MS Azure
> blob storage

### 2. Front-end

> javascript  
> typescript  
> React.js  

# 📊 Structure

<details>
<summary>기능 정리</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/da88f93a-8b80-408e-9434-0888b2b0d30e" width="800px"/>
</div>
</details>

<br />

<details>
<summary>Structure</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://github.com/user-attachments/assets/6878563f-fd2c-4cc1-b2d6-580f8a86651d" width="800px"/>
</div>
</details>
<br />

# 🔑 핵심기능

### 1. 참고자료 및 답변 이미지 제공

> 전처리 과정에서 관련 이미지 및 원본 페이지 정보를  MS Azure Blob Storage에 저장합니다.  
> Pinecone DB의 metadata에 이미지 주소, 원본 문서 이름, 페이지 정보를 저장합니다.  
> 답변 생성시 참고한 문서정보, 페이지 위치, 이미지를 함께 Front-end에 제공하여 출력합니다.  

### 2. 관리자 페이지 (파일 추가 / 검색 / 삭제 )

> 업로드 된 문서를 관리할 수 있는 관리자 페이지를 추가했습니다.  
> 문서 첫페이지가 미리보기 화면으로 볼 수 있게 만들었으며 웹 사이트 크기에 한 줄에 따라 표시되는 문서의 갯수가 달라집니다.  
> 검색창에 키워드를 입력하여 문서를 찾을 수 있고, 문서를 선택하여 삭제할 수 있으며,  
> 추가 버튼을 누르고 파일을 업로드하여 새로운 문서를 학습시킬 수 있습니다.   

### 3. 피드백 페이지

> 수정 전 답변이 출력되거나 올바르지 않은 답변이 생성되었을 때 피드백 기능을 통해 업로드 된 문서의 내용을 수정합니다.  
> 생성된 답변을 클릭하면 피드백 팝업이 뜨며, 피드백을 제출할 수 있습니다.  
> 관리자가 피드백을 확인하여 Accept를 한다면 DB 문서에 해당 내용이 포함됩니다.  

### 4. 다국적 번역기능 및 음성 입출력 기능

> 사이트에 언어설정을 추가하여 영어, 한국어, 태국어, 베트남어 등 다양한 언어를 선택할 수 있습니다.  
> 챗봇에 질문시 입력된 언어를 인식하여 자동으로 해당 언어로 답변을 생성합니다.  

<br />