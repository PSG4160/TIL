# FAQ 챗봇 만들기

어제 간단하게 `LLM`을 활용하여, 소설 시놉시스 만들기를 해 봤다.
다양한 라이브러리를 활용해 보지 못해서 아쉬웠는데 오늘 실습을 통해 간단하게나마 활용 할 수 있었다.

## 처음 코드
```python
import os
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


# 모델 및 임베딩 설정
llm = ChatOpenAI(model_name="gpt-3.5-turbo")  # 테스트 시에는 gpt-3.5-turbo 사용 권장
embeddings = OpenAIEmbeddings()

# FAQ 데이터 준비
faq_data = [
    {"question": "주문 취소는 어떻게 하나요?", "answer": "주문 취소는 마이페이지에서 가능합니다."},
    {"question": "배송 조회는 어디서 할 수 있나요?", "answer": "주문 내역에서 배송 상태를 확인할 수 있습니다."},
    {"question": "반품 신청은 어디서 할 수 있나요?", "answer": "반품 신청은 고객센터를 통해 진행하실 수 있습니다."},
    {"question": "회원 가입은 어떻게 하나요?", "answer": "홈페이지 상단의 회원가입 버튼을 클릭하여 진행하세요."},
    {"question": "비밀번호를 잊어버렸어요.", "answer": "로그인 페이지에서 비밀번호 찾기를 클릭하세요."},
    {"question": "포인트는 어떻게 사용하나요?", "answer": "결제 시 포인트 사용 옵션을 선택하실 수 있습니다."},
    {"question": "해외 배송이 가능한가요?", "answer": "죄송하지만 현재는 국내 배송만 가능합니다."},
    {"question": "상품 교환은 어떻게 하나요?", "answer": "교환은 구매 후 7일 이내에만 가능합니다. 고객센터에 문의해주세요."},
    {"question": "결제 수단은 어떤 것이 있나요?", "answer": "신용카드, 계좌이체, 간편결제 등을 지원합니다."},
    {"question": "영수증 발급은 어떻게 하나요?", "answer": "주문 완료 후 마이페이지에서 영수증을 출력하실 수 있습니다."}
]

# 질문과 답변을 결합한 문서 생성
documents = [f"질문: {item['question']}\n답변: {item['answer']}" for item in faq_data]

# 벡터 스토어 생성
vectorstore = FAISS.from_texts(documents, embeddings)

# Retriever 설정
retriever = vectorstore.as_retriever()

# 프롬프트 템플릿 작성
prompt_template = """
당신은 고객 상담사입니다. 아래의 정보를 바탕으로 고객의 질문에 대해 정확하고 친절하게 답변해 주세요.

질문: {input}
정보: {context}

답변:
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["input", "context"]
)

# 문서 결합 체인 생성
combine_docs_chain = create_stuff_documents_chain(llm, PROMPT)

# 체인 생성
qa_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=combine_docs_chain
)


# 사용자 입력 받기
user_question = input("궁금한 점을 질문해 주세요: ")

# 답변 생성
response = qa_chain.invoke({"input": user_question})

# 결과 출력
print("\n[답변]\n")
print(response)
```
### 답변
```
궁금한 점을 질문해 주세요: 비밀번호

[답변]

{'input': '비밀번호', 'context': [Document(metadata={}, page_content='질문: 비밀번호를 잊어버렸어요.\n답변: 로그인 페이지에서 비밀번호 찾기를 클릭하세요.'), Document(metadata={}, page_content='질문: 회원 가입은 어떻게  
하나요?\n답변: 홈페이지 상단의 회원가입 버튼을 클릭하여 진행하세요.'), Document(metadata={}, page_content='질문: 결제 수단은 어떤 것이 있나요?\n답변: 신용카드, 계좌이체, 간편결제 등을 지원합니다.'), Document(metadata={}, page_content='질문: 포인트는 어떻게 사용하나요?\n답변: 결제 시 포인트 사용 옵션을 선택하실 수 있습니다.')], 'answer': '고객님, 비밀번호를 잊어버리셨다면 로그인 페이지에서 비밀번호 찾기를 클릭하시면 재설정할 수 있습니 
다. 회원 가입은 홈페이지 상단의 회원가입 버튼을 클릭하여 진행하실 수 있습니다. 결제 수단으로는 신용카드, 계좌이체, 간편결제 등을 지원하고 있으며, 포인트는 결제 시 포인트 사용 옵션을 선택하여 사용하실 수 있습니다. 부가적
인 질문이 있으시면 언제든지 문의해 주세요. 감사합니다.'}
```
### 트러블 슈팅

검색된 문서들(`Document` 객체들)이 반환되어, 출력 결과에 Document(metadata={}, page_content='...')와 같은 내용이 포함되었다. 상당히 지저분해서 이런식의 답변을 원하지 않았다.

## 수정코드

```python
import os
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA  # 수정
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")

# 모델 및 임베딩 설정
llm = ChatOpenAI(model_name="gpt-3.5-turbo")  # 테스트 시에는 gpt-3.5-turbo 사용 권장
embeddings = OpenAIEmbeddings()

# FAQ 데이터 준비
faq_data = [
    {"question": "주문 취소는 어떻게 하나요?", "answer": "주문 취소는 마이페이지에서 가능합니다."},
    {"question": "배송 조회는 어디서 할 수 있나요?", "answer": "주문 내역에서 배송 상태를 확인할 수 있습니다."},
    {"question": "반품 신청은 어디서 할 수 있나요?", "answer": "반품 신청은 고객센터를 통해 진행하실 수 있습니다."},
    {"question": "회원 가입은 어떻게 하나요?", "answer": "홈페이지 상단의 회원가입 버튼을 클릭하여 진행하세요."},
    {"question": "비밀번호를 잊어버렸어요.", "answer": "로그인 페이지에서 비밀번호 찾기를 클릭하세요."},
    {"question": "포인트는 어떻게 사용하나요?", "answer": "결제 시 포인트 사용 옵션을 선택하실 수 있습니다."},
    {"question": "해외 배송이 가능한가요?", "answer": "죄송하지만 현재는 국내 배송만 가능합니다."},
    {"question": "상품 교환은 어떻게 하나요?", "answer": "교환은 구매 후 7일 이내에만 가능합니다. 고객센터에 문의해주세요."},
    {"question": "결제 수단은 어떤 것이 있나요?", "answer": "신용카드, 계좌이체, 간편결제 등을 지원합니다."},
    {"question": "영수증 발급은 어떻게 하나요?", "answer": "주문 완료 후 마이페이지에서 영수증을 출력하실 수 있습니다."}
]

# 질문과 답변을 결합한 문서 생성
documents = [f"질문: {item['question']}\n답변: {item['answer']}" for item in faq_data]

# 벡터 스토어 생성
vectorstore = FAISS.from_texts(documents, embeddings)

# Retriever 설정
retriever = vectorstore.as_retriever()

# 프롬프트 템플릿 작성
prompt_template = """
당신은 고객 상담사입니다. 아래의 정보를 바탕으로 고객의 질문에 대해 정확하고 친절하게 답변해 주세요.

질문: {question}
정보:
{context}

답변:
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["question", "context"]
)

# RetrievalQA 체인 생성
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=False,
    chain_type_kwargs={"prompt": PROMPT}
)

# 사용자 입력 받기
user_question = input("궁금한 점을 질문해 주세요: ")

# 답변 생성
response = qa_chain.invoke({"query": user_question})

# 결과 출력
print("\n[답변]\n")
print(response['result'])
```
```
궁금한 점을 질문해 주세요: 비밀번호
[답변]

고객님, 비밀번호를 잊어버리셨다면 로그인 페이지에서 비밀번호 찾기를 클릭하시면 새로운 비밀번호를 설정하실 수 있습니다. 
회원 가입은 홈페이지 상단의 회원가입 버튼을 클릭하여 진행하실 수 있습니다. 
결제 수단으로는 신용카드, 계좌이체, 간편결제 등이 지원되며, 포인트는 결제 시 포인트 사용 옵션을 선택하여 사용하실 수 있습니다. 
추가 질문이 있으시면 언제든지 문의해 주세요. 감사합니다.
```

## 수정

**`create_retrieval_chain` -> `RetrievalQA`체인 사용**

### RetrievalQA
- 역할: RetrievalQA 클래스는 LangChain에서 가장 유연하고 강력한 검색 기반 질의 응답 체인을 생성하는 데 사용됩니다.


- 사용 방식: `from_chain_type` 메서드를 사용하여 다양한 설정과 함께 체인을 생성할 수 있습니다.


- 확장성: 프롬프트 템플릿, 모델, 리트리버 등 다양한 요소를 세부적으로 설정할 수 있어 커스터마이징에 유리합니다.


- 매개변수 지원: `return_source_documents`와 같은 매개변수를 지원하여 검색된 문서 반환 여부를 제어할 수 있습니다.

- 체인을 실행하면 언어 모델이 생성한 답변만 반환됩니다. 따라서, 출력 결과가 깔끔하고 가독성이 높아집니다.


## 전체 코드 흐름

1. `OpenAI API` 키 설정

	- 환경 변수에서 API 키를 가져옵니다.
	- 키가 없으면 예외를 발생시킵니다.
2. 모델 및 임베딩 설정

	- `ChatOpenAI`를 사용하여 언어 모델을 설정합니다.
	- `OpenAIEmbeddings`를 사용하여 임베딩 모델을 설정합니다.
3. FAQ 데이터 준비

	- FAQ 데이터를 질문과 답변의 딕셔너리 리스트로 준비합니다.
4. 문서 생성

	- 각 FAQ 항목을 "질문: ...`\`n답변: ..." 형식의 문자열로 변환하여 문서 리스트를 만듭니다.
5. 벡터 스토어 생성

	- 문서 리스트를 임베딩하여 `FAISS` 벡터 스토어를 생성합니다.
6. Retriever 설정

	- 벡터 스토어에서 리트리버를 생성합니다.
7. 프롬프트 템플릿 작성

	- 고객 상담사로서의 역할을 부여하는 프롬프트 템플릿을 작성합니다.
	- `{question}`과 `{context}` 변수를 사용하여 입력 질문과 검색된 정보를 전달합니다.
8. `RetrievalQA` 체인 생성

	- `RetrievalQA.from_chain_type` 메서드를 사용하여 체인을 생성합니다.
	- `chain_type`을 `"stuff"`로 설정하여 검색된 문서를 프롬프트에 그대로 삽입합니다.
	- `return_source_documents=False`로 설정하여 검색된 문서를 반환하지 않습니다.
	- `chain_type_kwargs`를 통해 프롬프트 템플릿을 전달합니다.
    
9. 사용자 입력 받기

	- 사용자로부터 질문을 입력받습니다.
10. 답변 생성

	- 체인을 실행하여 답변을 생성합니다.
	- 입력으로 `{"query": user_question}`을 전달합니다.
11. 결과 출력

	- 응답에서 'result' 키를 사용하여 답변을 출력합니다.
    
    
## 결론

- `RetrievalQA` 클래스를 사용하면 검색 기반 질의 응답 체인을 더욱 유연하고 세부적으로 설정할 수 있습니다.
-	`create_retrieval_chain` 함수는 간단한 사용에는 적합하지만, 확장성과 커스터마이징 측면에서 제한적입니다.
-	따라서, 프로덕션 수준의 FAQ 챗봇이나 복잡한 설정이 필요한 경우에는 `RetrievalQA`를 사용하는 것이 좋습니다.