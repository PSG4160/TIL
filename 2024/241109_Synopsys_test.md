# 소설 시놉시스 생성하기

## 전체 코드
```python
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
import os

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수로부터 API 키를 가져옵니다.

# model 설정
model = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4", max_tokens=500)


# 사용자 입력 받기
genre = input("소설의 장르는 무엇인가요? ")
setting = input("소설의 배경은 어디인가요? ")
characters = input("주요 캐릭터들을 소개해주세요: ")
theme = input("이야기의 주제나 테마는 무엇인가요? ")
tone = input("소설의 톤과 분위기는 어떠한가요? ")
conflict = input("주요 갈등이나 문제가 있다면 무엇인가요? ")
audience = input("타겟 독자층은 누구인가요? ")
special_requests = input("특별히 추가하고 싶은 요청사항이 있나요? 없으면 '없음'이라고 입력해주세요: ")

# 프롬프트 템플릿 작성
template = """
당신은 창의적이고 섬세한 소설가입니다. 아래의 정보를 기반으로 흥미롭고 매력적인 소설 시놉시스를 작성하세요.

- **장르**: {genre}
- **배경**: {setting}
- **주요 캐릭터**: {characters}
- **주제/테마**: {theme}
- **톤과 분위기**: {tone}
- **주요 갈등 요소**: {conflict}
- **타겟 독자층**: {audience}
- **특별 요청사항**: {special_requests}

시놉시스는 500자 이내로 작성해주세요.

시놉시스:
"""

# System 메시지 템플릿 생성
system_message = SystemMessagePromptTemplate.from_template(template)

# ChatPromptTemplate 구성
chat_prompt = ChatPromptTemplate.from_messages([system_message])

# 프롬프트 포맷팅 및 메시지 생성
messages = chat_prompt.format_messages(
    genre=genre,
    setting=setting,
    characters=characters,
    theme=theme,
    tone=tone,
    conflict=conflict,
    audience=audience,
    special_requests=special_requests
)

# 시놉시스 생성
response = model.invoke(messages)

# 결과 출력
print("\n[생성된 시놉시스]\n")
print(response.content)
```
## 코드 설명
1. 필요로 하는 라이브러리 `import`하기

	- `langchain_openai`는 LangChain 라이브러리에서 OpenAI의 언어 모델과의 통합을 위해 사용되는 모듈입니다.
    
    - `langchain.prompts.chat`모듈은 LangChain에서 대화형 프롬프트를 생성하고 관리하는 데 사용되는 클래스와 함수들을 포함하고 있습니다.
    
    - `ChatPromptTemplate` 클래스는 대화형 프롬프트를 템플릿화하여 동적으로 생성할 수 있도록 도와줍니다.
    
    - `SystemMessagePromptTemplate` 클래스는 시스템 메시지를 템플릿화하여 모델에게 지시사항이나 역할을 전달할 때 사용합니다.

2. API_KEY 설정하기
	- 환경변수(터미널)에 `OPNEAI_API_KEY`를 입력하고, `os라이브러리`를 통해 불러옵니다.
    
3. model 설정

	- `gpt-4`모델을 불러오고, 토큰 수를 `500`으로 제한합니다. 즉 대답 토큰을 500으로 제한
    
4. 사용자 입력 받기
	- 소설 시놉시스 생성을 위한 다양한 정보를 입력받는 부분입니다. 각각의 `input()` 함수를 사용하여 사용자와 상호작용하며, 사용자가 입력한 값을 변수에 저장합니다. 
    
5. 프롬프트 템플릿 작성

6. System 메시지 템플릿 생성

	- `from_template(template)`를 호출하여 앞서 작성한 프롬프트 `template` 문자열을 기반으로 `SystemMessagePromptTemplate` 객체를 생성하고, `system_message` 변수에 저장합니다.
    
7. ChatPromptTemplate 구성

	- `from_messages`는 클래스 메서드로, 메시지들의 리스트를 받아서 하나의 `ChatPromptTemplate` 객체를 생성합니다.
    
    - 여기서 `[system_message]`는 이전에 생성한 `system_message` 템플릿 객체를 리스트 형태로 전달한 것입니다.
    
    - 이 코드는 시스템 메시지를 기반으로 하는 채팅 프롬프트 템플릿을 생성합니다.
    
	- 생성된 `chat_prompt` 객체는 이후에 사용자 입력 값을 대입하여 완성된 메시지를 만들 때 사용됩니다.
    
    
8. 프롬프트 포맷팅 및 메시지 생성

	- `chat_prompt.format_messages()` 메서드를 호출하여 프롬프트 템플릿의 플레이스홀더(예: `{genre}, {setting}`)를 실제 값으로 채웁니다.
    
    - 입력된 변수들은 이전에 input() 함수를 통해 사용자로부터 받은 값들입니다.
    
    - `model.invoke(messages)`를 호출하여 `messages` 리스트를 모델에 입력합니다.
    
    
    
### 파이썬에서 실행
```
$ python novel.py
소설의 장르는 무엇인가요? 현대 판타지물
소설의 배경은 어디인가요? 대한민국
주요 캐릭터들을 소개해주세요: 주인공 이름은 하츄핑
이야기의 주제나 테마는 무엇인가요? 엄청난 적으로부터 세게를 지켜야함
소설의 톤과 분위기는 어떠한가요? 밝고 명랑함
주요 갈등이나 문제가 있다면 무엇인가요? 주인공 친구와 주인공의 갈등
타겟 독자층은 누구인가요? 5~10살 어린이
특별히 추가하고 싶은 요청사항이 있나요? 없으면 '없음'이라고 입력해주세요: 없음

[생성된 시놉시스]

"하츄핑과 비밀의 마법 세계"는 대한민국을 배경으로 한 현대 판타지물입니다. 
주인공 하츄핑은 일반적인 초등학생이지만, 어느 날 돌연 특별한 능력을 갖게 됩니다. 
그의 능력은 과거와 미래를 보는 것! 
이 능력을 통해 하츄핑은 세상 
이 곧 엄청난 적에게 위협받게 될 것을 알게 됩니다.

그 적은 바로 '그림자 왕'으로, 어둠으로 세상을 덮으려는 악당입니다. 
하츄핑은 친구들과 함께 이를 막기 위해 모험을 떠나게 되는데요. 
하지만 길가다 친구와 의견차이로 인한 갈등이 생기게 됩니다. 
친구들은 하츄핑의 능력을 믿지않고, 그를 배신하게 됩니다.

명랑하고 밝은 분위기 속에서 펼쳐지는 이야기는, 
궁극적으로 하츄핑이 친구들과의 갈등을 어떻게 극복하고, 세상을 구하는지에 대한 흥미진진한 모험을 그립니다. 
이 소설은 5~10세 어린이들에게 우정, 용기, 사랑에 대한 교훈을 전하 
며, 독자들에게 희망과 즐거움을 선사할 것입니다.
```
하츄핑 내용 모릅니다.


## 참고자료

참고 자료
- LangChain 공식 문서: https://python.langchain.com
- LangChain GitHub 저장소: https://github.com/hwchase17/langchain
- OpenAI 공식 문서: https://platform.openai.com/docs

---

Langchain에 대해서 학습하고, 간단하게 생각해본 소설 시놉시스 작성 챗봇?을 구현해 봤다.
RAG와 Faiss 등등 학습한 것을 다 녹여보고 싶었는데, 창의적인 대답을 필요로 하는 챗봇이라 쉽사리 사용하지 못했다. 다음엔 더 적절한 챗봇에 실습을 해 보도록 해야겠다.

트러블 슈팅에 관해서도 작성하고 싶었는데 적당한 오류가 나지 않았다.

라이브러리 호환성이나 모듈에 관한 오류정도 겪었는데 업데이트나 설치를 통해 간단히 해결되어 따로 기술하지 않았다.