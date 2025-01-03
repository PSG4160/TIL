## SRS란 무엇인가?
>`Software Requirements Specification`(SRS)은 소프트웨어 개발 프로젝트에서 요구사항을 명확하고 체계적으로 문서화한 공식적인 문서입니다. SRS는 개발팀, 이해관계자, 사용자 간의 소통을 원활하게 하고, 개발 및 유지보수 단계에서 참조할 수 있는 중요한 가이드 역할을 합니다.

## SRS 작성요령

1. **기능 요구사항 (Functional Requirements)**

- 시스템이 수행해야 할 구체적인 동작과 기능을 정의합니다.
- 예: "사용자는 이메일과 비밀번호를 통해 로그인할 수 있어야 한다."

2. **비기능 요구사항 (Non-Functional Requirements)**

- 성능, 보안, 신뢰성, 확장성 등 시스템의 특성을 정의합니다.
- 예: "시스템은 하루 최대 10만 건의 거래를 처리할 수 있어야 한다."

3. **외부 인터페이스 요구사항 (External Interface Requirements)**

- 사용자 인터페이스(UI), API, 하드웨어 인터페이스 등을 정의합니다.

---

위와 같이 SRS을 작성할 수 있지만, 현재 프로젝트에서 사용하는 템플릿과 직관성에 따라서 아래와 같이 프레임을 짜서 작성했다.

![](https://velog.velcdn.com/images/gyu_p/post/7c719d35-8641-4dd4-8712-32369a64c88b/image.png)

위 사진과 같이 중요도 순으로 
- `High` : 필수기능
- `Medium` : 도전 기능  ⭐️
- `Low` : 도전 기능  ⭐️⭐️

으로 나누고, 비고에 상세하게 작성을 원칙 -> 세부사항으로 나눌 예정이다. 기능 요구사항을 작업 분배가 용이한 형태로 작성해서 추후 분업할때 직관적으로 볼 수 있는 장점이 있다. 좀더 자세한 기능 요구사항을 기술하는게 필요하다면, RQ넘버마다 혹은 요구사항 내용 제목별로 페이지화 해서 자세하게 기술하면 된다.! 이를 바탕으로 API명세서를 작성해야 하기에 팀원들과 충분한 의사소통이 필요했다. 시간이 좀 걸리고 아직 미완성이지만 팀원들과 좀 더 신경써야 한다.! 

