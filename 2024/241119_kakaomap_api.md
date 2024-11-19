# 카카오맵 API 활용하여 비상대피소 찾기 구현하기

최근 비상사태 발생 시 가장 가까운 대피소를 세 곳 찾는 기능을 구현하기 위해 카카오맵 API를 활용해보았다. 대피소 자료에 대한 정리는 아래에 링크로 걸어두었으니 참고하면 좋을 것 같다.

[재난안전 플랫폼 API 활용 - 비상대피소 정리](https://velog.io/@gyu_p/%EC%9E%AC%EB%82%9C%EC%95%88%EC%A0%84%ED%94%8C%EB%9E%AB%ED%8F%BC)

API 발급 과정에서 "비즈 비지니스?"와 같은 내용이 나와서 당황했는데, 다행히 꼭 해야 하는 것은 아니었다. 

![](https://velog.velcdn.com/images/gyu_p/post/ac65c3e1-910e-49ee-b0f2-3bb71d83dde9/image.png)

### 카카오맵 API 설정하기

처음에는 REST API 미지원이라는 문구 때문에 다른 플랫폼을 사용해야 하나 싶었지만, 장소 정보는 로컬 API를 통해 지원된다는 것을 알고, 전반적인 내용을 카카오 개발자 사이트에서 찾아보았다.

[kakao developers](https://developers.kakao.com/docs/latest/ko/local/dev-guide)에서 관련 자료를 확인할 수 있었다. 지도 관련 상세 기능과 부가 기능은 REST API로 지원되지 않는 부분도 있었지만, 내가 필요로 하는 정보는 다행히 불러올 수 있었다.



문서의 양식이 전에 사용하던 다른 플랫폼들과는 조금 달라서 초반에는 약간 헤맸다. 그래도 구글링과 챗지피티의 도움 덕분에 문제를 해결할 수 있었다. 

![](https://velog.velcdn.com/images/gyu_p/post/31157982-0058-43bc-aad8-ea7e17d4e265/image.png)- 출처 kakao developers

### 카카오맵 API 테스트 코드

```python
import requests
# .env 파일 로드
load_dotenv()
kakaoapikey = os.getenv("REST_API_KEY")
#print(f"'{kakaoapikey}'")
def get_coordinates(query):
    """
    카카오맵 API를 이용해 검색 질의어(query)의 경도와 위도를 반환하는 함수.
    
    Args:
        query (str): 검색할 장소 또는 주소.

    Returns:
        tuple: (longitude, latitude) - 경도(x), 위도(y)
    """
    # 카카오맵 API 엔드포인트
    url = "https://dapi.kakao.com/v2/local/search/address.json"
    
    # 요청 헤더
    headers = {
        "Authorization": f"KakaoAK {kakaoapikey}"
    }
    
    # 요청 파라미터
    params = {
        "query": query,
        "size": 1  # 결과를 하나만 가져오도록 설정
    }
    
    # API 요청
    response = requests.get(url, headers=headers, params=params)
    
    # 응답 확인
    if response.status_code == 200:
        data = response.json()  # JSON 응답 파싱
        documents = data.get("documents", [])
        if documents:
            # 첫 번째 검색 결과의 경도(x)와 위도(y) 반환
            x = documents[0].get("x")
            y = documents[0].get("y")
            return (x, y)
        else:
            print("검색 결과가 없습니다.")
            return None
    else:
        # 에러 메시지 출력
        print(f"API 요청 실패: {response.status_code}, {response.text}")
        return None


# 사용 예시
if __name__ == "__main__":    
    query = input("")  # 검색할 주소 또는 장소
    coordinates = get_coordinates(query)
    if coordinates:
        print(f"경도(x): {coordinates[0]}, 위도(y): {coordinates[1]}")

```

위 코드는 `kakaomap api`가 잘 동작하는지 확인하기 위해 작성한 코드이다. 경도와 위도를 반환하는 함수로 테스트해본 결과, 특정 주소를 입력했을 때는 잘 작동했다. 예를 들어:

- **주소명**: 00광역시 00동 000 - 000
- **결과**: 경도(x): 128.12341234, 위도(y): 35.123412341234

그러나 **장소명**으로 입력했을 때는 잘 작동하지 않았다. 예를 들어:

- **장소명**: 00동 치킨집, 00지하철역

이 부분은 더 찾아보아야 할 것 같다.

### 거리 계산을 위한 Haversine 함수 정의

장소 간 거리를 계산하기 위해 `haversine` 함수를 정의하였다. 이 함수는 두 지점의 위도와 경도를 받아 거리를 킬로미터 단위로 계산한다.

```python
from math import radians, sin, cos, sqrt, atan2
# Haversine 공식을 사용하여 거리 계산 함수 정의
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    위도와 경도를 받아 두 지점 사이의 거리를 킬로미터 단위로 계산하는 함수
    """
    # 위도와 경도를 라디안으로 변환
    lat1_rad, lon1_rad = radians(lat1), radians(lon1)
    lat2_rad, lon2_rad = radians(lat2), radians(lon2)

    # 위도와 경도의 차이 계산
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine 공식 적용
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    R = 6371  # 지구 반지름 (킬로미터 단위)
    distance = R * c
    return distance
```

### 현재 위치와 가까운 대피소 찾기

사용자에게 현재 주소를 입력받고, 가까운 세 곳의 대피소 정보를 반환하는 코드도 작성해보았다. 카카오맵의 URL 링크는 다음과 같이 완성시켰다.

```python
# 사용자로부터 주소 입력 및 좌표 얻기
query = input("현재 주소를 입력하세요: ")  # 검색할 주소 또는 장소
coordinates = get_coordinates(query)
if coordinates:
    user_lon = coordinates[0]
    user_lat = coordinates[1]
    print(f"경도(x): {user_lon}, 위도(y): {user_lat}")

    user_lon = float(user_lon)
    user_lat = float(user_lat)
    
    # 거리 계산 및 가까운 대피소 찾기
    def calculate_distance(row):
        try:
            shelter_lat = float(row['위도'])
            shelter_lon = float(row['경도'])
            return haversine_distance(user_lat, user_lon, shelter_lat, shelter_lon)
        except (ValueError, TypeError):
            return None  # 거리 계산이 불가능한 경우 None 반환
            
    # 새로운 열 추가 및 필터링 조건 적용
    df_result['거리'] = df_result.apply(calculate_distance, axis=1)
    df_result = df_result[df_result['거리'].notnull()]

    # 거리순으로 정렬하여 상위 3개의 대피소 선택
    df_sorted = df_result.sort_values(by='거리')
    df_top3 = df_sorted.head(3)

    # 결과 출력
    print("\n가장 가까운 대피소 정보 (거리순):")
    for idx, row in df_top3.iterrows():
        print(f"\n[{idx+1}]")
        print(f"시설명: {row['시설명']}")
        print(f"주소: {row['주소']}")
        print(f"현재 위치로부터의 거리: {row['거리']:.2f} km")

        # Kakao Map 링크 생성
        shelter_lat = row['위도']
        shelter_lon = row['경도']
        shelter_add = row['주소'].replace(' ', '')
        kakao_map_link = f"https://map.kakao.com/link/search/{shelter_add}"
        
        print(f"지도 링크: {kakao_map_link}")
else:
    print("좌표를 가져올 수 없습니다.")

```
카카오맵 `url` 링크를 
`kakao_map_link = f"https://map.kakao.com/link/search/{shelter_add}"`
이렇게 완성시켰다.
그 전에는 
[kakao 지도 Web Api 가이드](https://apis.map.kakao.com/web/guide/#bigmapurl) - 이 곳에서 
![](https://velog.velcdn.com/images/gyu_p/post/8f5b535e-b2d9-4bd2-8bbe-9b52f4317b00/image.png)
그림과 같은 `URL Pattern`들을 찾아보고 입력했는데 자꾸 이상한 페이지가 뜬다거나, 원하는 장소 검색이 제대로 되지 않았다.



결과 예시는 다음과 같다:

```
현재 주소를 입력하세요: 서울 종로구 사직로8길 31
경도(x): 126.971979688446, 위도(y): 37.5749462708923

가장 가까운 대피소 정보 (거리순):

[5340]
시설명: 세양빌딩 지하2층
주소: 서울특별시 종로구 사직로8길 39, 세양빌딩 지하1층 (내자동)
현재 위치로부터의 거리: 0.11 km
지도 링크: https://map.kakao.com/link/search/서울특별시종로구사직로8길39,세양빌딩지하1층(내자동)

[5321]
시설명: 적선현대빌딩 지하주차장 2~4층
주소: 서울특별시 종로구 사직로 130, 적선현대빌딩 지하1층 (적선동)
현재 위치로부터의 거리: 0.12 km
지도 링크: https://map.kakao.com/link/search/서울특별시종로구사직로130,적선현대빌딩지하1층(적선동)

[5300]
시설명: 지하철3호선 경복궁역 대합실 승강장
주소: 서울특별시 종로구 사직로 지하130, 3호선 경복궁역 지하1~3층 (적선동)
현재 위치로부터의 거리: 0.14 km
지도 링크: https://map.kakao.com/link/search/서울특별시종로구사직로지하130,3호선경복궁역지하1~3층(적선동)
```

처음에는 `장소`로 시도했다가 잘 되지 않아 주소로 바꾸고 공백을 제거하여 해결했는데, 문제를 해결하는 과정에서 많은 시행착오가 있었지만 그 덕분에 하나씩 해결해 나가는 즐거움을 느낄 수 있었다.

### 다음 목표

아직 `LLM`을 활용한 챗봇을 만드는 일은 멀었지만, 이렇게라도 조금씩 구현이 되고 있다는 게 정말 재밌다. 이제 다음으로는 이 기능을 좀 더 확장하고, 실제 사용자에게 유용하게 사용할 수 있도록 하고 싶다. 우선 `Stramlit`을 이용 해봐야겠다. (openai의 `Function calling`을 오늘 배웠는데, 이걸 써보면 어떨까 싶다.)
