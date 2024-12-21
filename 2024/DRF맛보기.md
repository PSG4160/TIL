

# **Django REST Framework (DRF)**

- `Django`를 이용해서 `API`를 구축하는 기능을 제공하는 라이브러리입니다.
- `Django`의 `Form`, `ModelForm`과 굉장히 비슷하게 구성 및 작동합니다.

그럼 어떻게 DRF를 사용 할 수 있을까?


## 설치 및 사용

```
pip install djangorestframework
```

```python
#settings.py

INSTALLED_APPS = [
		...
		'rest_framework',
		...
]
```
명령어를 사용하여 DRF 설치하고 `INSTALLED_APPS`에 추가한다.

이제 작업을 할때 각 앱마다 `serializers.py`파일을 추가하고 작업하기!

```python
# serializers.py

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
```

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view(["GET"])
def json_drf(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

DRF를 이용한 view 작성에는 항상 `@api_view`데코레이터를 사용한다.
장고를 실행해서 확인해보면,
![](https://velog.velcdn.com/images/gyu_p/post/cdc68e02-b55e-4c14-a551-8755f68c4872/image.png)

이렇게 나오는 것을 확인 할 수 있다.


## 통신하기

`API`는 소프트웨어끼리 소통하는 방법이라고 계속해서 들었다. 그럼 파이썬 프로그램을 만들어서 콜하며 소통해보자.

`my_program.py`라는 파이썬 파일을 만들고,

```python
import requests

url = "http://127.0.0.1:8000/api/v1/articles/json-drf"
response = requests.get(url)

print(response)
print(response.json())
```
실행시켜 보면

![](https://velog.velcdn.com/images/gyu_p/post/2f1e7db8-742f-4d51-b3bc-f31c9034de5f/image.png)

터미널에서 해당 `json`값들을 불러오는 것을 확인 할 수 있다.(장고가 실행중이어야 한다)



`POSTMAN`으로 확인하면 훨씬 편리하다. 앞으로 포스트맨을 통해서 계속 테스트 하면서 진행한다고 함!
