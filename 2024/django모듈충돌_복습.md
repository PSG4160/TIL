## 모듈 충돌 해결

![](https://velog.velcdn.com/images/gyu_p/post/ee84312c-d98f-4986-ba7b-ec0b4a4ca51c/image.png)

위와같이 프로젝트 폴더의 `urls.py`에 
```python
from articles import views
from users import views
```
모듈을 `views`로 똑같은 이름으로 지정해서 모듈 충돌이 발생했다.
![](https://velog.velcdn.com/images/gyu_p/post/11ae805f-0fd3-495d-961c-a6117a8b1ae5/image.png)

`index`는 `articles`앱의 `views.py`에 있으나, `user.views`를 참조하려고 해서 발생한 문제같다.

`from articles import views` 하나만 있을때는 `views`가 `articles`의 `views`를 잘 가르키지만, `from users import views`로 인해 `views`가 `uers.views`로 덮어 씌어진거 같음.

따라서 `path('index/', views.index)`는 `users.views.index`를 참조하려 하고, 만약 `users.views`에 `index`가 없으면 오류가 발생한다.!

```python
from articles import views as articles_views

path('index/', articles_views.index)
```
`views`의 이름을 지어주고, `index/` 참조를 정확하게 지정해서 해결했다.

혹은 사용하지 않는
```python
from users import views
```
를 삭제해도 된다.

## 데이터 주고 받기

### 세팅

`data-throw.html`와 `data-catch.html`을 만들어서 서로 데이터를 주고받는 것을 `django`로 실습해보자.

새로만든 폴더에서 가상환경과 `django` 세팅 후 실행.

혼자 하려니 머리가 새하얘짐

본 프로젝트에 `urlpattern`의 path 추가하기

```python
    path('data-catch/', views.data_catch, name='data-catch'),
    path('data-throw/', views.data_throw, name='data-throw'),
```
앱 `arcticles`의 `views`에서 정의 후 `templates`에도 `html`파일들을 만들어 주자.

![](https://velog.velcdn.com/images/gyu_p/post/a364674f-48b9-436a-8b1a-d93ab9a80a09/image.png)
![](https://velog.velcdn.com/images/gyu_p/post/67d229cf-bea1-4fbd-94eb-5f53a6a0f068/image.png)

일단 이렇게 설정하고 진행한다.

기본적으로 `path`에서 지정된 url 경로로 들어오면 `articles`앱의 `views`에서 처리 후 응답한다!


### html 설정

만들어진 `data_catch.html`, `data_throw.html`의 틀을 `templates` 문법을 이용하여 설정한다.

```python
{% extends 'base.html' %}

{% block content %}
{% endblock content %}
```

`data-throw`에서 데이터를 받으면 `data-catch`로 보내는 형식으로 만들어야 하니, `html form`을 이용해서 짜보자.

```python
data_throw.html의 내용

{% extends 'base.html' %}


{% block content %}
<h1> DATA-THROW </h1>
<form action="{% url 'data-catch' %}" method = 'GET'>

    <label for='message'>데이터 입력</label>
    <input type='text' id='message' name='message'>

    <button type='submit'>전송</button>
</form>
{% endblock content %}

```


- `<form>`태그를 사용하여 사용자 입력을 서버에 전송할 수 있도록 한다.
- `action`속성 : form 데이터를 제출할 url을 설정한다. 'data-catch'는 path에서 지정한 name으로 간편하게 url을 다 적지 않아도 templates 테그를 사용하여 지정할 수 있다.
- `method`속성 : form 데이터를 제출할 HTTP 메서드를 지정한다.
	
    - `GET` : 데이터를 URL 쿼리 문자열로 전송한다. 입력된 데이터는 서버에서 `request.Get`으로 접근가능하다.
    
- `<label>` 태그 : 사용자에게 입력 필드의 용도를 설명한다.
	
- `for="message"`:
      - `<label>`과 `<input>`을 연결
      - 클릭 시 `<input>` 필드로 포커스가 이동
      - `id="message"`인 `<input>`과 연결
      
- `type='text'`: 사용자로부터 텍스트 데이터를 입력 받는 필드
- `id="message"`: 고유한 식별자로, `<label>` 태그와 연결된다.
- `name='message'`: 서버로 전송될 데이터의 이름(Key)을 지정한다. 사용자가 입력한 값은 `name`속성을 기반으로 서버에 전송되며 `request.GET['message']`로 접근 가능하다.

---

이렇게 `data_throw.html`를 정의하고, 표현된 `views`에서 `data-catch`와 `templates`의 `data_catch.html`을 설계하도록 하자.


```python
#articles의 views

def data_catch(request):
    message = request.GET.get('message')
    context = {"message":message}
    return render(request, 'data_catch.html', context)
```

**`request.GET`**:

- GET 요청의 쿼리 문자열 데이터를 담고 있는 사전(dictionary) 형태의 객체입니다.
- URL에서 ?key=value 형식으로 전달된 데이터를 추출합니다.

- 예: 클라이언트가 `/data-catch/?message=hello`라는 요청을 보냈다면, `request.GET`은 `{'message': 'hello'}`를 포함합니다.

**`.get('message')`**:

- `message`라는 키에 해당하는 값을 가져옵니다.
- 키가 존재하지 않을 경우 기본값으로 None을 반환합니다(오류를 방지).


- URL에 ?message=hello가 포함되어 있다면, message 변수는 'hello'를 갖습니다.
- URL에 ?message가 없으면 message 변수는 None이 됩니다.

**`context`**
- "message"라는 키에 message 변수의 값을 저장합니다.
- 템플릿에서 {{ message }}를 사용하여 데이터를 출력할 수 있습니다.

```python
data_catch.html 내용

{% extends 'base.html' %}


{% block content %}
    <h1>Data catch</h1>

    <h3>Current data </h3>
    <p>Current data is: {{ message }} </p>

    <a href="{% url 'data-throw' %}">데이터 던지러 가기 ! </a>
{% endblock content %}
```

---

![](https://velog.velcdn.com/images/gyu_p/post/e5cb980f-da62-4611-adaf-f580e885d9c4/image.png)
![](https://velog.velcdn.com/images/gyu_p/post/16451c47-63e3-4087-8838-c8bf8c5880c8/image.png)


이렇게 `Data-throw`에서 입력을 하면 `data-catch`로 잘 전송되는 것을 확인 할 수 있다.


---

점점 복습도 어렵다...! 갈수록 진도가 나가지 않는다.
