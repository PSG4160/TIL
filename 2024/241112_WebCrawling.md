
# 크롤링이란?

- 웹 사이트에서 자동화된 방법으로 데이터를 수집하는 과정이다.

## 주요 절차

1. **URL 분석**
2. **HTTP GET 요청 송신 및 응답 수신**
3. **HTML 파싱** (원하는 정보 추출)
4. **데이터 정제 후 저장**

![크롤링 절차 이미지](https://velog.velcdn.com/images/gyu_p/post/0b308fec-aaa4-421c-af1c-f3cf23813704/image.png)

---

# 웹이란?

- 월드 와이드 웹(World Wide Web)의 줄임말로, 인터넷을 통해 텍스트, 이미지, 동영상 등을 연결하여 볼 수 있게 하는 시스템이다.

## URL이란?

![URL 구조 이미지](https://velog.velcdn.com/images/gyu_p/post/2a43378a-6e40-4900-bbb9-1a9349b1047d/image.png)

- **protocol**: 규약, 데이터를 주고받는 방식 (예: 웹 자원은 주로 `http`나 `https` 사용)
- **host**: IP 주소(서버의 네트워크 주소), 주로 도메인 이름으로 표현됨
- **port**: 특정 포트 번호를 통해 서버에 접속
- **resource path**: 서버의 자원 경로로, 서버 설계자가 지정한 특정 경로
- **query**: 자원 경로에 특정 파라미터를 전달할 때 사용 (예: 페이지 번호)

---

# HTTP 요청 메소드 주요 4가지

1. **조회** - GET: 데이터를 조회할 때 사용 (주로 크롤링에 사용)
2. **추가** - POST: 데이터를 추가할 때 사용
3. **수정** - PUT: 데이터를 수정할 때 사용
4. **삭제** - DELETE: 데이터를 삭제할 때 사용

아주 중요한 메소드들입니다!

![HTTP 메소드 설명 이미지](https://velog.velcdn.com/images/gyu_p/post/85598a91-c521-470b-9989-980c5d8b7d3a/image.png)

---

## User Agent 확인 방법

- `what is my user agent`을 크롬에서 검색하여 자신의 User Agent를 확인할 수 있다.

![User Agent 예시 이미지](https://velog.velcdn.com/images/gyu_p/post/1e9fd014-ff0f-456a-a3ad-42629b10aad8/image.png)

---

# 크롤링 기본

1. `F12` 키를 누르면 개발자 도구 창이 열립니다.
   
   ![개발자 도구 이미지](https://velog.velcdn.com/images/gyu_p/post/1f0456cb-4485-4e53-aa8e-4b8f1c125e88/image.png)

2. 개발자 도구에서 화살표 아이콘을 누르고 웹에 가져다 대면 원하는 요소의 정보를 확인할 수 있습니다.

   ![화살표 도구 이미지](https://velog.velcdn.com/images/gyu_p/post/4764b7f9-11f7-4a1b-8223-fec0c5b33fc5/image.png)

3. `Network` 탭을 통해 크롤링에 유용한 다양한 정보들을 확인할 수 있습니다.
   - 예를 들어, `preview` 탭에서 원하는 정보를 확인하고 주소를 복사할 수 있습니다.

   ![Network 탭 이미지](https://velog.velcdn.com/images/gyu_p/post/4de527e1-6984-4075-9ed0-0c9fa74e74ab/image.png)

---

# 과제
다음편...
- **삼성전자 최근 3개월 일별 시세 데이터 가져오기**

네이버페이 증권에서 삼성전자 시세란에 
![](https://velog.velcdn.com/images/gyu_p/post/0cd946cb-c3a5-44a5-b0c0-c1d365a6d58e/image.png)

이렇게 일별 시세들을 크롤링 해 보는 실습을 했다.
오늘 특강에 실습답안?과 비교해보니 수정 할 부분이 산더미다.
코드를 비교해보고 어떤 부분이 부족했는지 알아보는 시간을 가져야겠다.