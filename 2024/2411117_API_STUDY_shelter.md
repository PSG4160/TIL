[API 활용 사이트 - 재난안전데이터공유플랫폼](https://www.safetydata.go.kr/disaster-data/view?dataSn=184#none)

해당 사이트에서 민방위 대피소 관련 데이터셋을 불러와 활용해 보도록 하자.
(방금 API 이용신청을 해서 아직 승인은 안났다. 예행연습이라 생각하자...)


우선 어떤 데이터가 있는지 확인해야 한다.

>![](https://velog.velcdn.com/images/gyu_p/post/49e860f6-aa8c-47f6-a1c7-10b6f11079aa/image.png)
![](https://velog.velcdn.com/images/gyu_p/post/7091d4ff-580b-461b-92a2-3f4c373d0b7b/image.png)

(출처-재난안전데이터공유플랫폼)

이렇게 데이터에 대한 정보들을 미리 확인하고 어떤 데이터를 어떻게 불러올 수 있을까를 먼저 생각한다.

응답타입은 `json`과 `xml`이 있다. `json`타입을 활용할 것이니 패스하고

출력결과에 사용할 항목들을 추려보자.

`시설명`,`읍면동명`,`시설주소지번`,`시설주소도로명`,`경도도,분,초`,`위도도,분,초`,`대피가능인원수`,`개방여부` 가 필요하다.



## 활용 코드 예시

```python
import requests
from dotenv import load_dotenv
import os
import math 

def dms_to_dd(degrees, minutes, seconds):
    """
    도(degrees), 분(minutes), 초(seconds)를 받아서 소수점(decimal degrees) 형태의 좌표로 변환하는 함수
    """
    return degrees + minutes / 60 + seconds / 3600
    
def get_shelters(city_code=None, facility_name=None):
    """
    민방위 대피소 정보를 API로부터 가져오는 함수
    """
    # .env 파일 로드
    load_dotenv()
    # 환경 변수에서 API 키 가져오기
    servicekey = os.getenv("SERVICE_KEY") # SERVICE_KEY=your_actual_service_key_here `.env` 파일 안의 내용
    url = "https://www.safetydata.go.kr"
    dataName = "/V2/api/DSSP-IF-00195 " # 민방위 대피소 데이터 url 입력   
    payloads = {
        "servicekey": servicekey,
        "returnType": "json",
        "pageNo": "1",
        "numOfRows": "100",
    }

    # API 요청 보내기
    response = requests.get(url + dataName, params=payloads)
    if response.status_code == 200:
        data = response.json()
        shelters = data.get('data', [])
        return shelters
    else:
        print("데이터 가져오기 오류:", response.status_code)
        return [] 

def format_shelter_info(shelter):
    """
    대피소 정보를 포맷하여 사용자에게 표시할 수 있게 변환하는 함수
    """
    facility_name = shelter.get('FCLT_NM', 'N/A') # 시설명
    address = shelter.get('FCLT_ADDR_LOTNO') or shelter.get('FCLT_ADDR_RONA', 'N/A') # 도로명 먼저 찾고, 지번 찾기
    capacity = shelter.get('SHNT_PSBLTY_NOPE', 'N/A') # 수용 능력(대피가능 인원수)
    is_open = '예' if shelter.get('OPN_YN') == 'Y' else '아니오' # 개방 여부
    phone = shelter.get('MNG_INST_TELNO', 'N/A') # 이건 빼도될듯?

    # 경도(DMS) 정보 가져오기
    lot_provin = float(shelter.get('LOT_PROVIN', 0))
    lot_min = float(shelter.get('LOT_MIN', 0))
    lot_sec = float(shelter.get('LOT_SEC', 0))
    # 위도(DMS) 정보 가져오기
    lat_provin = float(shelter.get('LAT_PROVIN', 0))
    lat_min = float(shelter.get('LAT_MIN', 0))
    lat_sec = float(shelter.get('LAT_SEC', 0))

    # DMS를 소수점 좌표로 변환
    longitude = dms_to_dd(lot_provin, lot_min, lot_sec)
    latitude = dms_to_dd(lat_provin, lat_min, lat_sec)

    # 대피소 정보 문자열 생성
    info = (
        f"시설명: {facility_name}\n"
        f"주소: {address}\n"
        f"수용 인원: {capacity}\n"
        f"개방 여부: {is_open}\n"
        f"연락처: {phone}\n"
        f"경도: {longitude}\n"
        f"위도: {latitude}"
    )
    return info, longitude, latitude	
```

이렇게 데이터를 불러와서 대피소정보를 파악하는 함수를 만들었다.

추후에 대피소 위치와 사용자가 제공해주는 위치를 기반으로 거리를 계산하는 함수도 만들었다 (chatGPT가...)

```python
def calculate_distance(user_lon, user_lat, shelter_lon, shelter_lat):
    """
    사용자 위치와 대피소 위치 간의 거리를 계산하는 함수
    Haversine 공식을 사용하여 두 좌표 사이의 거리를 계산합니다.
    """
    # 지구 반지름 (킬로미터 단위)
    R = 6371.0

    # 좌표를 라디안으로 변환
    lon1 = math.radians(user_lon)
    lat1 = math.radians(user_lat)
    lon2 = math.radians(shelter_lon)
    lat2 = math.radians(shelter_lat)

    # 차이 계산
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine 공식 적용
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 거리 계산
    distance = R * c  # 결과는 킬로미터 단위
    return distance
```

살펴보면 `Haversine`공식을 적용하여 지구 반지름을 기반으로 위도 경도기반 차이를 이용해 거리를 계산하는 함수인것 같다.


이렇게 API key가 아직 발급전이라 눈으로 데이터를 활용하면서 실습하진 못했지만 그래도 이런 흐름으로 데이터를 가져올 수 있다는 것을 알았다.
평일에 승인이 난다면 직접 실행해서 눈으로 보고 데이터를 정제해 가장 가까운 대피소 찾기?를 한번 만들어 봐야겠다.
