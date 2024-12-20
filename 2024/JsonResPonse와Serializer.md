## django-seed

`django_seed`를 통해서 프로젝트 앱에서 만든 모델의 fake쿼리셋들을 만들 수 있다.
 테스트용 데이터를 한번에 많이 만들 수 있음.
 
> - Github : **https://github.com/Brobin/django-seed**
- *Django-seed* uses the [faker](https://www.github.com/joke2k/faker/) library to generate test data for your Django models.
- Django-seed allows you to write code to generate models, and seed your database with one simple `manage.py` command!

```bash
pip install django-seed
```
**django-seed**설치 후 프로젝트 `settings`에서

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "django_seed",
    # Local
    "articles",
]
```

`APPS`에 추가해준다.

### `seeding`을 해서 가짜 데이터들을 만드는 명령어

```bash
python manage.py seed articles --number=30
```

`articles`모델의 30개 쿼리셋 객체들을 만들어줌

## Response 만들기


django-seed를 통해서 만든 데이터들을 실행시켜 보면
```django
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Article List</h2>
    <hr><br>

    {% for article in articles %}
    <h3>{{ article.title }}</h3>
    <p>{{ article.content }}</p>
    <p>{{ article.created_at }}</p>
    <p>{{ article.updated_at }}</p>
    <hr>
    {% endfor %}
</body>
</html>
```


![](https://velog.velcdn.com/images/gyu_p/post/039b0dbe-9059-4c79-9728-2a6772091e7f/image.png)

이런식으로 데이터들이 나올 수 있다. 이제 이런 형태들을 `json`형태로 나타내도록 하자.


```python
#urls
from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("html/", views.article_list_html, name="article_list_html"),
    path("json-01/", views.json_01, name="json_01"),
]

#views

def json_01(request):
    articles = Article.objects.all()
    json_res = []

    for article in articles:
        json_res.append(
            {
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
        )

    return JsonResponse(json_res, safe=False)
```

똑같이 articles 쿼리셋 객체로 나타내주고 `for`문을 이용해서 빈 리스트에 딕셔너리 형태의 데이터들을 저장해준다.

`return JsonResponse(json_res, safe=False)` 에서 `safe=False`는 딕셔너리 형태면 놔 두면 되는데, 지금 json_res라는 빈 리스트에 append하는 형식이라 이를 직렬화(Serialization)하기 위해서는 False로 설정해야 한다.

`JsonResponse`는 JSON으로 인코딩된 response를 만드는 `HttpResponse`의 서브 클래스다.


![](https://velog.velcdn.com/images/gyu_p/post/ea00f356-80af-4a91-915b-3b080a6aefd1/image.png)

이렇게 만든 view를 장고를 통해서 실행시키면 아래와 같이 나옴

![](https://velog.velcdn.com/images/gyu_p/post/14269fd5-e756-457a-a3cc-f6b14932980c/image.png)


## Response 형식만 바꿔서 송출하기

![](https://velog.velcdn.com/images/gyu_p/post/3e6b9d28-4ed9-41fd-bb79-90efae3e16a7/image.png)

위 사진과 같이 모델의 데이터를 모두 다 송출할 수 있도록 하는법

![](https://velog.velcdn.com/images/gyu_p/post/68b51c90-ad6c-463a-b06c-2e9425f1de0a/image.png)

이런 송출은 적혀있듯 유연하지 못하다는 큰 단점이 있다.
단점들을 보완하고 좀 더 유연하게 데이터를 제공해 줄 수 있는 Djang Rest Framework를 정리 해 보자. 내일..
