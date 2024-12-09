장고 실습 도중 강사님이 가상환경을 만들고 `pip list`를 사용하면, 기존 전역에 설치된 환경들은 나오지 않은채로 깔끔한 list들을 보여줬다.

내 로컬 환경에서는 `venv`와 더불어 옆에 `base`이렇게 두개가 표시되고 `conda` 가상환경에 깔렸던 것들이 줄줄줄 나왔다.
![](https://velog.velcdn.com/images/gyu_p/post/24a8a5ef-f16a-455a-aee4-dbca1709bece/image.png)


`conda`의 기본 활성화를 끄는 명령어 


```
conda config --set auto_activate_base false
```
사용해서 `conda`와 충돌을 막고 깔끔한 가상환경을 만들 수 있었다.!

---

이것저것 해보기

처음부터 새로운 폴더 만들고 다 해보기

장고 프로젝트 앱 등록 urls 연결 템플릿츠 경로 만들기 상속 view template로 context 넘기기 

오전부터 장고 강의를 여기까지 들었다.
![](https://velog.velcdn.com/images/gyu_p/post/543e2b54-31c3-4818-9aec-4caa7b4f6a7a/image.png)

강사님께서 너무 친절하게 하나하나씩 좋은 정보?들을 넣어서 설명해 주셨다. 부트캠프 생활중 가장 행복하게 교육을 들은 시간이었다. 너무 만족스러우니까 지금까지 커리큘럼을 이 강사님이 해 주셨으면? 하는 마음도 좀 들었다,,,

9강까지 학습 후 배운 내용을 '처음부터 끝까지 스스로 한번 해보는 시간을 가져라' 강사님 말씀

네


## 가상환경 만들어 django 설치

### 가상환경 만들고 django 설정

`VScode`를 이용해서 가상환경을 만들면 위에 적어놨듯 `venv`와 `base`가 같이 떠서 골머리를 싸맸다.

이젠 기본 환경이 안떠서 가상환경 만드는 명령어

```
python -m venv 이름
```
이게 안먹혔다...

`conda activate base`로 기본 환경을 실행하고 위 명령어로 가상환경을 만들었다.

또다시 `venv`와 `base`가 같이뜬다 ^^...

나만 이런건가 진짜 터미널을 종료하고, 다시 실행시키고 

```
source venv/Scripts/activate
```
로 가상환경 실행해서 `venv`환경만 남기고 장고 설치,,, 

아 그전에 마냥 윈도우 맥 OS 환경 차이로 저 명령어가 다르구나 마냥 이렇게 이해 했는데, 가상환경 만들면 윈도우는 `venv`파일안의 /Scripts/activate 파일이 생기고 맥은 bin폴더 안에 activate를 생겨서 명령어가 다르더라!

```
pip install django==4.2
```

장고까지 무사 설치했다. freez > requirements.txt

```
django-admin startproject my_2_pjt
```

두번째 프로젝트 생성하고,

### 앱 생성 및 등록

앱을 만들자. `cd my_2_pjt`폴더에 들어가서,

```
python manage.py startapp articles
```
![](https://velog.velcdn.com/images/gyu_p/post/2d78ed3b-f808-4fc3-a969-45b67d27af23/image.png)


이렇게 `articles`앱이 생성됐다. 앱을 생성하면 `settings.py`에 들어가서 앱을 등록시켜야 한다.! 불과 몇시간만에 까먹었다.

![](https://velog.velcdn.com/images/gyu_p/post/54868fc8-206c-4eb4-8670-c5aedc883906/image.png)

여튼 배운대로 앱 등록하고, 트레인 콤마 `,`까지 찍고 뿌듯한걸 보니 참 속상하다.

![](https://velog.velcdn.com/images/gyu_p/post/01c1e1b6-13d2-46b4-9140-e7b38d7dfcb0/image.png)

`articles`폴더의 `views`파일안을 쳐다보면서 뭘 했던거 같은데 멍하게 쳐다보다 생각났다. `templates` 태그들과 변수들을 사용하여 `index.html`을 만드는 실습을 하려 한거같다...

![](https://velog.velcdn.com/images/gyu_p/post/e398f95f-c2b9-4c63-8fba-3a67fb058cc1/image.png)

`my_2_pjt` 폴더에 `templates`폴더를 만들고 `base.html`파일 만들기!

![](https://velog.velcdn.com/images/gyu_p/post/1236c7bb-57d3-47ed-80e5-e7fce3cb4940/image.png)

`articles` 폴더에 `templates`폴더 만들고 `index.html`만들어서 `base.html`의 내용을  `templates` 태그를 이용해서 상속받자.!

![](https://velog.velcdn.com/images/gyu_p/post/8b9f20ac-13f8-4788-bb86-6580bef92db0/image.png)



`Vscode` 하단의 언어모드를 `html`로 변경 후 `!` 탭으로 `html`양식을 끌어온다.! 

언어모드 `django templates`로 변경하고 컨트롤 + 스페이스를 누르고 block을 선택하면 쉽게 템플릿의 태그들을 사용할 수 있다. 이렇게 공부하면 편할거 같다.

![](https://velog.velcdn.com/images/gyu_p/post/aa164287-5e70-49e5-9838-4b03de24723e/image.png)

![](https://velog.velcdn.com/images/gyu_p/post/f0de110f-d10f-4fbe-bc8c-18629a475edf/image.png)

이렇게 간단하게만 작성하고, 

아

---
![](https://velog.velcdn.com/images/gyu_p/post/69d15db2-01d9-448b-b6ad-e862d54c7fda/image.png)

`from articles import views` 를 작성해야 연결이 된다... 

---

![](https://velog.velcdn.com/images/gyu_p/post/5036d551-1612-40f4-b206-9c3d22727932/image.png)

`settings`에서 TEMPLATES의 `DIRS`를 정의해서 다른 폴더의 `templates`폴더의 내용을 가져와서 상속할 수 있도록 설정한다.!


ㅎ 여기서 `python manage.py runserver`를 통해 실행하니 온갖 오류메세지가 반긴다.

![](https://velog.velcdn.com/images/gyu_p/post/00044193-b87d-4a6e-9dc4-8ba4481136c7/image.png)



주로 `views`파일에서 `index.html`을 `'`따옴표로 감싸주지 않고, context를 정의하지 않아서 뜬 오류들.

처음 배울때 작성했던 것들을 복붙했다.!!

![](https://velog.velcdn.com/images/gyu_p/post/f281a4a3-bb04-417f-8640-7c6b6b7c2da7/image.png)

![](https://velog.velcdn.com/images/gyu_p/post/33cde47b-c86c-40c8-b93a-f1bce282ff54/image.png)

강의 따라하면서 실습하면 아 그렇구나 타닥타닥 잘 따라가는데, 혼자 해보니 코드 실수도 많고 중간중간 잊어버린게 너무 많다는 것을 다시 깨달았다 ^^...
