### 크롤링에서 API 호출로 대체한 트러블슈팅

---

#### **1. 문제 상황**
Steam에서 특정 사용자의 상위 2개 플레이 시간을 조회하는 기능을 구현하던 중, 기존 크롤링 방식을 사용했을 때 아래와 같은 문제에 직면했습니다.

1. **로그인이 필요한 페이지**: Steam의 특정 API는 사용자 게임 정보 조회에 로그인을 요구했습니다. Selenium을 사용한 크롤링은 이를 우회하기 어렵고 비효율적이었습니다.
2. **HTML 구조 변경 가능성**: Steam 웹 페이지의 DOM 구조가 변경될 경우, 크롤링 로직이 깨질 위험이 있었습니다.
3. **속도와 신뢰성 문제**: 크롤링 방식은 API 호출보다 느리고, 요청이 차단될 가능성이 높았습니다.

---

#### **2. 문제 해결 방향**
크롤링 대신 Steam에서 공식적으로 제공하는 **API 호출 방식**으로 전환했습니다.  
이를 통해 데이터를 보다 안정적으로, 효율적으로 가져올 수 있었습니다.

---

#### **3. 수정 전 크롤링 코드**
이전 코드에서는 Selenium을 사용하여 Steam 사용자 페이지에서 게임 정보를 크롤링했습니다.

```python
def fetch_top2_playtime(self, driver, steam_id_str):
    base_url = "https://steamcommunity.com/"
    if steam_id_str.isdigit():
        url = f"{base_url}profiles/{steam_id_str}/games/?tab=all"
    else:
        url = f"{base_url}id/{steam_id_str}/games/?tab=all"
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._2-pQFn1G7dZ7667rrakcU3"))
        )
        rows = driver.find_elements(By.CSS_SELECTOR, "div._2-pQFn1G7dZ7667rrakcU3")
    except:
        return []
    
    # 이후 코드 생략 (DOM 구조에서 데이터를 추출하는 방식)
```

이 방식은 위에서 언급한 **로그인 문제**, **HTML 구조 변경 리스크** 등으로 유지보수하기 어려웠습니다.

---

#### **4. 수정 후 API 호출 코드**
Steam의 [GetOwnedGames API](https://partner.steamgames.com/doc/webapi/IPlayerService#GetOwnedGames)를 활용하여 데이터를 가져오도록 수정했습니다.  
이 방식은 API 키와 SteamID64를 사용하며, 더 안전하고 효율적입니다.

```python
def fetch_top2_playtime_api(self, api_key, steam_id_str):
    # SteamID64 확인 및 변환
    if not steam_id_str.isdigit():
        steam_id_str = self.resolve_vanity_url(api_key, steam_id_str)
        if not steam_id_str:
            return []

    # API 호출
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": api_key,
        "steamid": steam_id_str,
    }
    try:
        resp = requests.get(url, params=params).json()
        if "response" in resp and "games" in resp["response"]:
            games = resp["response"]["games"]
            data = [
                {"app_id": game["appid"], "playtime": round(game["playtime_forever"] / 60, 2)}
                for game in games
            ]
            top2 = sorted(data, key=lambda x: x["playtime"], reverse=True)[:2]
            return top2
    except:
        return []
```

---

#### **5. 주요 변경 사항**

1. **크롤링 → API 호출**:
   - Selenium과 BeautifulSoup을 사용하는 대신, HTTP 요청을 통해 Steam의 공식 API를 호출했습니다.
   - API 호출 결과는 JSON 형식으로 제공되어, 추가 데이터 파싱 없이 쉽게 처리할 수 있습니다.

2. **SteamID64 변환 로직 추가**:
   - 사용자 입력이 커스텀 URL일 경우, `resolve_vanity_url` 메서드를 사용해 SteamID64로 변환했습니다.

3. **플레이 시간 계산 및 상위 2개 게임 정렬**:
   - `playtime_forever` 값(분 단위)을 시간 단위로 변환하고, 내림차순으로 정렬하여 상위 2개의 게임 정보를 반환했습니다.

---

#### **6. 결과 및 개선 효과**

1. **신뢰성과 유지보수성 증가**:
   - API는 Steam이 직접 제공하므로, HTML 구조 변경에 영향을 받지 않아 유지보수가 쉬워졌습니다.

2. **속도 향상**:
   - Selenium 기반 크롤링보다 API 호출 방식이 훨씬 빠릅니다.

3. **데이터 정확성 개선**:
   - Steam API는 공식 데이터 소스에서 제공되므로, 크롤링 중 발생할 수 있는 데이터 누락이나 왜곡 문제가 없습니다.

4. **로그인 문제 해결**:
   - Steam API는 인증된 API 키를 사용하므로 로그인 문제를 우회할 수 있었습니다.

---

#### **7. 배운 점**

- **API 사용의 중요성**: 크롤링은 간단한 작업에는 유용하지만, 공식 API가 제공되는 경우 이를 사용하는 것이 훨씬 효율적입니다.
- **유지보수성 고려**: 초기에 크롤링으로 구현하더라도, 유지보수성과 안정성을 고려해 장기적으로 API 호출로 전환할 수 있어야 합니다.

---

이 경험은 TIL에 기록하기 적합한 사례로, **기존 크롤링 코드의 문제점 → API 전환 과정 → 최종 개선 효과**를 잘 보여주는 사례였습니다.
