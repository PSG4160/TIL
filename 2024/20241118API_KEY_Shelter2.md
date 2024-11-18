

# 재난안전 플랫폼 API 활용
재난안전플랫폼에서 API Key를 발급받고 실습을 해봤다.

## 처음 코드
```python
import requests
from dotenv import load_dotenv
import os
import math 

# .env 파일 로드
load_dotenv()
# 환경 변수에서 API 키 가져오기
serviceKey = os.getenv("SERVICE_KEY") # SERVICE_KEY=your_actual_service_key_here `.env` 파일 안의 내용
#print(f"'{servicekey}'") api-key 잘 나오는지 확인.


url = "https://www.safetydata.go.kr"
dataName = "/V2/api/DSSP-IF-00195" # 민방위 대피소 데이터 url 입력   
payloads = {
    "serviceKey": serviceKey, # "servicekey : K 대문자로 써야된다고 함...ㅡㅡ
    "returnType": "json",
    "pageNo": "23", # 2만 3000개?
    "numOfRows": "1000",
    }

# API 요청 보내기
response = requests.get(url + dataName, params=payloads)
if response.status_code == 200:
    data = response.json()
else:
    print("데이터 가져오기 오류:", response.status_code)
print("최종 요청 URL:", response.url)
```
처음에 response.status_code 오류 400이 떠서 무슨 일인가 했는데, 다른 분이 홈페이지에 문의글을 작성한 것을 참고하고 `servicekey`의 k를 대문자로 입력해야 한다는 것을 알았다...

첫 오류를 지나고 무식하게 `"pageNo"`에 하나하나 요청하며 데이터가 얼마나 있는지 확인했다. 10이 지나고 뭔가 쌔하더니, 20까지 갔을때 오기가 생겨 23이 1000개의 데이터를 불러왔을 때 마지막 페이지인것을 확인했다.

마지막 페이지...
/// (글을 다 써가는데 실수로 나가기를 눌러서 여기까지 임시저장이 되어 있다. 한줄한줄쓰면서임시저장누르자한줄한줄쓰면서임시저장누르자한줄한줄쓰면서임시저장누르자)


## 모든 대피소 데이터 가져오기(수정코드)

```python
# 모든 대피소 데이터를 저장할 리스트 초기화
url = "https://www.safetydata.go.kr"
dataName = "/V2/api/DSSP-IF-00195" # 민방위 대피소 데이터 url 입력   
shelters = []
pageNo = 1
numOfRows = 1000  # 한 페이지당 최대 행 수
while True:
    # API 요청에 필요한 파라미터 설정
    payloads = {
        "serviceKey": serviceKey,  # 'K'를 대문자로 작성해야 합니다
        "returnType": "json",
        "pageNo": pageNo,
        "numOfRows": numOfRows,
    }

    # API 요청 보내기
    response = requests.get(url + dataName, params=payloads)
    if response.status_code == 200:
        data = response.json()
        # 최종 요청 URL 출력 (디버깅용)
        print(f"최종 요청 URL: {response.url}")

        # 'body' 부분에서 대피소 데이터 가져오기
        page_shelters = data.get("body", [])
        if not page_shelters:
            # 더 이상 가져올 데이터가 없으면 루프 종료
            break
        shelters.extend(page_shelters)
        pageNo += 1  # 다음 페이지로 이동
    else:
        print("데이터 가져오기 오류:", response.status_code)
        break

# 가져온 대피소 데이터의 개수 출력
print(f"총 {len(shelters)}개의 대피소 데이터를 가져왔습니다.")

```
### 수정 내용

1. 필요한 데이터 `data.get("body", [])`를 활용해 `body`에서 데이터를 get하도록 함.

2. `pageNo` 를 하나하나 바꿔가며 바보같이 호출하지말고 `shelters`리스트를 만들고 `page_shelters`를 하나하나 `extend`하기로 함
3. 디버깅용 URL을 출력하는 코드를 넣어 각 `page`마다 출력 결과물을 `pretty print`로 깔금하게 확인 할 수 있다.
4. 총 데이터 수를 확인하는 프린트 구문 추가해서 총 데이터 양 확인.





결과는 아래와 같다. api-key가 나오므로 주의하도록 하자
![](https://velog.velcdn.com/images/gyu_p/post/98434c9f-4478-443c-a110-dcafdcf00cb1/image.png)

```python
print(shelters[0])
print(shelters[22823])
```
리스트 `shelters`의 처음과 끝 인덱스내용을 프린트해서 출력확인

결과
```
{'GRND_UDGD_SE': '1', 'ORTM_UTLZ_TYPE': '주차장', 'SGG_CD': '3910000', 'FCLT_CD': 'S202400002', 'FCLT_SE_CD': '3           ', 'ROAD_NM_CD': '3352297     ', 'LOT_MIN': 6, 'SHNT_PSBLTY_NOPE': '34761', 'FCLT_SCL': 28678, 'LOT_SEC': 24, 'EMD_NM': '송탄동', 'FCLT_ADDR_RONA': '경기도 평택시 신촌5로 56 (칠원동, 평택지제역동문굿모닝힐맘시티4단지)', 'SE_CD': '2', 'OPN_YN': 'Y', 'LAT_SEC': 31, 'LAT_PROVIN': 37, 'LAT_MIN': 1, 'MNG_INST_TELNO': '031-8024-4900', 'FCLT_NM': '평택지제역동문굿모닝힐맘시티4단지 지하주차장 1층', 'FCLT_DSGN_DAY': '20240126', 'MNG_INST_NM': '경기도 평택시청', 'FCLT_ADDR_LOTNO': '경기도 평택시 칠원동 595 평택지제역동문굿모닝힐맘시티4단지', 'SCL_UNIT': '㎡', 'LOT_PROVIN': 127, 'EMD_CD': '3910077     '}
{'GRND_UDGD_SE': '0', 'ORTM_UTLZ_TYPE': '생활용수', 'SGG_CD': '4100100', 'FCLT_CD': 'E200500013', 'FCLT_SE_CD': '3           ', 'ROAD_NM_CD': '3194010     ', 'LOT_MIN': 43, 'SHNT_PSBLTY_NOPE': '0', 'FCLT_SCL': 80, 'LOT_SEC': 51, 'EMD_NM': '일산서구 송포동', 'FCLT_ADDR_RONA': '경기도 고양시 일산서구 대화로 97 (대화동)', 'SE_CD': '1', 'OPN_YN': 'Y', 'LAT_SEC': 8, 'LAT_PROVIN': 37, 'LAT_MIN': 40, 'MNG_INST_TELNO': '031-8075-3570', 'FCLT_NM': '명성운수(송포동)', 'FCLT_DSGN_DAY': '20050516', 'MNG_INST_NM': '경기도 고양시 일산서구청', 'FCLT_ADDR_LOTNO': '경기도 고양시 일산서구 대화동 1475번지 2호', 'SCL_UNIT': 't(톤)', 'LOT_PROVIN': 126, 'EMD_CD': '4100115     '}
```

`body`부분이 잘 나오는 것을 확인할 수 있다.

## 데이터 관리

매번 API를 호출해서 데이터를 사용하기엔 할당된 API 호출량이 100/일(일) 이라 많지 않다. 저장해서 필요할때 로컬에서 불러와 사용하는게 맞다고 판단해서 저장, 출력 코드를 추가했다.

### 데이터 저장하기

```python

import json

# 파일로 저장
with open("shelters.json", "w", encoding="utf-8") as f:
    json.dump(shelters, f, ensure_ascii=False, indent=4)  # ensure_ascii=False: 한글 깨짐 방지
```

### 데이터 불러오기

```python
# shelters.json 불러오기 API 호출 안해도 된다 이제.
# 파일에서 불러오기
with open("shelters.json", "r", encoding="utf-8") as f:
    shelters = json.load(f)

print(shelters[0:11) # 데이터 확인

```

## 판다스로 데이터 프레임 만들기

계속 `json`형태의 출력하며 데이터를 확인하니 눈이 침침하다. 이럴때 사용하라고 판다스를 배운게 분명하다.

### 데이터프레임 형성
```python
import pandas as pd

# shelters 리스트를 데이터프레임으로 변환
df = pd.DataFrame(shelters)

# 데이터프레임 확인
print(df.head())
```

결과
```
  GRND_UDGD_SE ORTM_UTLZ_TYPE   SGG_CD     FCLT_CD    FCLT_SE_CD  \
0            1            주차장  3910000  S202400002  3              
1            1            주차장  3910000  S202400001  3              
2            1            주차장  4020000  S202400001  3              
3            1          지하주차장  3650000  S201700010  3              
4            1          지하주차장  3650000  S201700011  3              

     ROAD_NM_CD  LOT_MIN SHNT_PSBLTY_NOPE  FCLT_SCL  LOT_SEC  ... LAT_PROVIN  \
0  3352297             6            34761     28678       24  ...         37   
1  3352295             6            37152     30651       27  ...         37   
2  3182030            56            39997     32998       42  ...         37   
3  3165028            23             6577      5426       55  ...         36   
4  3165028            23             5126      4229       56  ...         36   

  LAT_MIN MNG_INST_TELNO                     FCLT_NM  FCLT_DSGN_DAY  \
0       1  031-8024-4900  평택지제역동문굿모닝힐맘시티4단지 지하주차장 1층       20240126   
1       1  031-8024-4900  평택지제역동문굿모닝힐맘시티2단지 지하주차장 1층       20240126   
2      22           None             힐스테이트 금정역 지하주차장       20240131   
3      19   042-606-6036                유등마을아파트 104동       20170628   
4      19   042-606-6036                유등마을아파트 106동       20170628   

   MNG_INST_NM                    FCLT_ADDR_LOTNO SCL_UNIT LOT_PROVIN  \
0     경기도 평택시청  경기도 평택시 칠원동 595 평택지제역동문굿모닝힐맘시티4단지        ㎡        127   
1     경기도 평택시청  경기도 평택시 칠원동 559 평택지제역동문굿모닝힐맘시티2단지        ㎡        127   
2     경기도 군포시청          경기도 군포시 금정동 916 힐스테이트 금정역        ㎡        126   
3    대전광역시 중구청              대전광역시 중구 태평동 253번지 1호        ㎡        127   
4    대전광역시 중구청              대전광역시 중구 태평동 253번지 1호        ㎡        127   

         EMD_CD  
0  3910077       
1  3910077       
2  4020038       
3  3650041       
4  3650041       

[5 rows x 25 columns]
```

각 컬럼들도 눈에 보기 훨신 편해지고 관리,추적에 용이하다.
내가 생각하기에 앞으로 필요한 컬럼들을 확인하고 일단 `주소` `경도` `위도`만 사용해 보도록 하자.

### 컬럼 추출하기

```python
# DMS를 소수점 좌표로 변환하는 함수
def dms_to_dd(degrees, minutes, seconds):
    return degrees + minutes / 60 + seconds / 3600

# 위도 변환 (LAT_PROVIN, LAT_MIN, LAT_SEC를 사용)
df['위도'] = df.apply(lambda row: dms_to_dd(
    float(row['LAT_PROVIN']), 
    float(row['LAT_MIN']), 
    float(row['LAT_SEC'])
), axis=1)

# 경도 변환 (LOT_PROVIN, LOT_MIN, LOT_SEC를 사용)
df['경도'] = df.apply(lambda row: dms_to_dd(
    float(row['LOT_PROVIN']), 
    float(row['LOT_MIN']), 
    float(row['LOT_SEC'])
), axis=1)

# 주소 컬럼 설정 (도로명 주소 사용)
df['주소'] = df['FCLT_ADDR_RONA']

# 필요한 컬럼만 선택
df_result = df[['주소', '위도', '경도']]

print(df_result.head())
```

결과
```
                                         주소         위도          경도
0  경기도 평택시 신촌5로 56 (칠원동, 평택지제역동문굿모닝힐맘시티4단지)  37.025278  127.106667
1  경기도 평택시 신촌3로 12 (칠원동, 평택지제역동문굿모닝힐맘시티2단지)  37.026389  127.107500
2         경기도 군포시 엘에스로 143 (금정동, 힐스테이트 금정역)  37.373333  126.945000
3           대전광역시 중구 수침로 138 (태평동, 유등마을아파트)  36.332222  127.398611
4           대전광역시 중구 수침로 138 (태평동, 유등마을아파트)  36.331667  127.398889
```
일단 도로명 주소와 추후 거리계산을 위한 위도 경도 데이터만 남기는 데이터 프레임을 만들었다.

카카오맵 API를 활용해서 현재 위치에서 거리를 계산하고 싶었다.
문서가 처음 읽기 너무 불편하고 불친절해서 좀 헤매며 뚝딱거렸다. 내일 마저 카카오맵 API를 활용해 봐야겠다.
