# 허깅페이스(Hugging Face)란?

허깅페이스는 특히 **자연어 처리(NLP)** 분야에서 유명한 오픈 소스 AI 및 머신러닝 라이브러리와 플랫폼을 제공하는 커뮤니티입니다. 자연어 처리뿐만 아니라 **컴퓨터 비전** 및 다른 머신러닝 애플리케이션에 폭넓게 사용될 수 있는 **API와 툴**들을 제공합니다. Hugging Face의 주요 목표는 연구자, 개발자, 그리고 기업들이 AI 모델을 쉽게 접근하고 사용할 수 있도록 하는 것입니다. 여기서 제공되는 도구와 리소스를 잘 활용하면 실력 향상에도 큰 도움이 됩니다.

---

## 1. Hugging Face의 주요 기능과 서비스

### 1.1 Transformers 라이브러리

- **Transformer 모델**: BERT, GPT-2, RoBERTa, T5, DistilBERT 등 다양한 **사전 학습된 NLP 모델**을 쉽게 가져와서 사용할 수 있습니다.
- **모델 허브**: 수천 개의 미리 학습된 모델들이 Hugging Face의 모델 허브에 공개되어 있어서, 이를 활용해 다양한 작업을 진행할 수 있습니다. 이 모델들은 NLP, 이미지 처리, 음성 인식 등 여러 분야에 걸쳐 있으며, 커뮤니티가 지속적으로 추가하고 있습니다.
- **Fine-tuning**: 학습된 모델을 특정한 데이터셋에 맞추어 추가 훈련(fine-tuning)하여 더 높은 성능을 낼 수 있도록 할 수 있습니다.

예시)

[Transformers-BERT 허깅페이스 사이트](https://huggingface.co/docs/transformers/model_doc/bert)

Transformers 라이브러리의 모델 중 하나인 BERT를 자세히 알아 볼 수 있다.
![](https://velog.velcdn.com/images/gyu_p/post/32994a83-56e7-42dc-bb47-287cf0285bd5/image.png)
이렇게 다양한 모델과 `API`의 정보들을 확인하고 공부 할 수 있다.

![](https://velog.velcdn.com/images/gyu_p/post/d6091860-0add-450c-895b-7edac93c4de4/image.png)
![](https://velog.velcdn.com/images/gyu_p/post/82f20125-8b2e-42e4-97a0-729c5481f3a3/image.png)

(출처 - Hugging Face)


`BERT`의 오버뷰와 사용팁들 등등이 자세하게 나열되어 있고 오픈소스와 다양한 AI 모델들을 사용할 수 있다는 큰 장점이 있다.


### 1.2 Datasets 라이브러리

- **Dataset 관리**: 다양한 공개 데이터셋을 손쉽게 가져와 사용할 수 있는 기능을 제공하며, 데이터셋을 관리하고 전처리하는 작업을 돕는 여러 함수가 포함되어 있습니다.
- **대규모 데이터셋**: Hugging Face에는 언어, 번역, 감정 분석, 요약 등 다양한 작업에 맞는 **대규모 데이터셋**이 포함되어 있습니다.
- **커스텀 데이터셋 추가**: 자신의 데이터셋을 업로드하여 다른 사람들과 공유하거나, 모델 학습에 사용할 수 있습니다.

### 1.3 Tokenizers 라이브러리

- **토크나이징 최적화**: 매우 빠르고 효율적인 토크나이저(tokenizer)를 제공하여, 텍스트 데이터를 NLP 모델에 넣기 전에 단어를 나누는 작업을 효율적으로 수행합니다.
- **언어별 특화 지원**: 다양한 언어와 텍스트 처리 요구사항에 맞추어 최적화된 토크나이저를 제공해, 모델 학습 속도와 성능을 높일 수 있습니다.

### 1.4 Hugging Face Hub

- **모델 및 데이터셋 공유**: 자신이 학습시킨 모델을 Hugging Face Hub에 올려서 다른 사람들과 공유할 수 있습니다. **협업 도구**로서의 기능을 제공하여 모델의 버전 관리와 편리한 사용을 돕습니다.
- **Spaces**: **Gradio**나 **Streamlit** 같은 인터페이스를 사용해 자신이 만든 모델을 쉽게 배포할 수 있도록 도와주는 기능입니다. 이를 통해 자신만의 모델을 웹 애플리케이션으로 쉽게 만들어 공유할 수 있습니다.

---

## 2. Hugging Face로 할 수 있는 것

Hugging Face를 활용하면 다양한 작업과 연구를 쉽게 수행할 수 있습니다. 구체적으로 다음과 같은 작업에 유용합니다.

### 2.1 텍스트 생성, 번역, 요약

- **텍스트 생성**: GPT-2나 T5 모델을 통해 창의적인 텍스트를 자동 생성하거나, 특정 주제에 맞는 텍스트를 작성할 수 있습니다.
- **번역**: 언어 번역 모델을 사용해 다양한 언어 간 번역을 수행할 수 있습니다. Hugging Face는 미리 학습된 번역 모델을 지원하여, 자연스러운 번역을 손쉽게 시도할 수 있습니다.
- **요약**: 긴 문서나 기사의 핵심 내용을 요약하는 작업에 사용할 수 있습니다. 특히 T5, BART 모델이 요약 작업에 강점을 보입니다.

### 2.2 감정 분석, 스팸 필터링

- **감정 분석**: 특정 텍스트가 긍정적인지, 부정적인지, 또는 중립적인지 판단하는 감정 분석 모델을 구축할 수 있습니다.
- **스팸 필터링**: 스팸 메일이나 부적절한 텍스트를 필터링하는 모델을 손쉽게 구축할 수 있습니다. 이는 텍스트 분류 모델을 학습시키는 방식으로 구현할 수 있습니다.

### 2.3 이미지 분류, 객체 탐지

- **이미지 분류**: 컴퓨터 비전 분야에서도 Hugging Face의 사전 학습된 이미지 분류 모델을 사용할 수 있습니다.
- **객체 탐지 및 세분화**: 이미지에서 객체를 탐지하거나 특정 객체를 세분화하는 모델을 사용할 수 있으며, 특히 사전 학습된 비전 트랜스포머 모델이 이에 적합합니다.

### 2.4 커스텀 AI 모델 배포

- **모델 배포**: Hugging Face는 쉽게 배포할 수 있는 인프라를 제공합니다. **Gradio**나 **Streamlit**을 사용하여 모델을 웹 애플리케이션으로 바로 전환할 수 있습니다.
- **API 서비스**: Hugging Face에서 제공하는 API를 활용해 모델을 서버에 올리고 실시간으로 예측을 제공하는 서비스를 구축할 수 있습니다.

---

## 3. Hugging Face의 사용 사례

- **스타트업이나 연구 기관**에서 신속하게 모델 프로토타입을 만들고 배포할 때 유용합니다.
- **개인 프로젝트**로 AI 애플리케이션을 개발할 때, 이미 학습된 모델을 이용해 빠르게 모델 성능을 체험하고 실험할 수 있습니다.
- **학습 리소스 부족 문제 해결**: Hugging Face가 제공하는 모델을 활용해 자신의 리소스를 아끼면서 고성능 AI 모델을 사용할 수 있습니다.

---
## 4. Hugging Face의 단점

### 4.1 고성능 하드웨어 필요

Hugging Face의 많은 사전 학습된 모델들은 대규모 파라미터를 가지고 있어, 고성능 GPU가 필요합니다. 이러한 하드웨어 요구사항은 개인 개발자나 작은 기업이 접근하기 어려울 수 있습니다.

### 4.2 학습 시간 및 비용

모델을 **Fine-tuning**하거나 새로운 작업에 맞춰 학습하려면 많은 시간과 비용이 소모될 수 있습니다. 특히 클라우드 기반의 GPU 인프라를 사용하면 비용이 급격히 증가할 수 있습니다.

### 4.3 데이터 프라이버시 문제

모델 학습에 사용할 데이터가 개인 정보를 포함할 경우, 이를 **Hugging Face Hub**에 업로드하고 공유하는 것이 데이터 프라이버시 문제를 일으킬 수 있습니다. 이러한 이유로 민감한 데이터는 별도의 조치가 필요합니다.

### 4.4 한계가 있는 지원 언어 및 작업

대부분의 모델이 영어와 같은 주요 언어에 최적화되어 있으며, 일부 언어에서는 성능이 떨어질 수 있습니다. 또한 특수한 도메인이나 구체적인 작업에서는 **Hugging Face**의 사전 학습된 모델이 충분한 성능을 내지 못할 수 있습니다.


---

AI활용을 공부하면서, Hugging Face라는 커뮤니티를 알아봤다, 앞으로 진행될 많은 프로젝트들에 다양하게 활용될 것 같아서 깊은 공부가 필요할 것 같다. 😐
