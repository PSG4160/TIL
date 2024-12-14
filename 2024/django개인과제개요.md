# 프로젝트 개요

`spartamarket`는 다음과 같은 기능을 목표로 한다.

- 비회원 접근 불가: 모든 기능은 로그인한 사용자만 이용할 수 있다.
- 회원 기능: 회원가입, 로그인, 로그아웃
- 프로필 페이지: 사용자별 username, 가입일, 등록한 물품 목록, 찜한 물품 목록, 팔로우/팔로워 관리
- 상품 관리: 물품 목록 보기, 물품 상세 보기, 물품 등록, 수정, 삭제
- 찜하기(좋아요) 기능: 각 물건에 대해 “찜”을 할 수 있음
이 프로젝트에서 유저, 상품, 찜, 팔로우 등 여러 기능이 얽혀 있으므로, 앱을 어떻게 나누고, 모델과 뷰를 어떻게 설계할지 고민하는 과정이 필요하다.

## 구조 설계

```bash
spartamarket/
├─ manage.py
├─ spartamarket/           # 메인 폴더
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ asgi.py
├─ accounts/               # 계정
│  ├─ migrations/
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  ├─ urls.py
│  ├─ templates/accounts/
│  └─ ...
├─ products/               # 상품
│  ├─ migrations/
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  ├─ urls.py
│  ├─ templates/products/
│  └─ ...
└─ templates/              
   └─ base.html

```

이런식으로 `accounts`와 `products`는 필수 앱이으로 넣어주고 추후 앱 분리할지 말지 결정하면 될 것 같다.

---

**CustomUserModel**을 먼저 설정하고 마이그레이션 하기... `setting` 변경. 일단  필요한 구조를 짜야겠다. 특강때 배운 ERD를 먼저 구성해보고 가야할지 고민이다.
