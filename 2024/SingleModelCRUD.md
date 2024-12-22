
해당 강의 수강 후 처음부터 다시 공백에서 시도해봄.
# Function Based View(FBV)

## articles/urls.py
```python
from django.urls import path
from . import views
app_name = "articles"
urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
]
```

## articles/views.py

```python
from django.shortcuts import get_object_or_404
from .models import Article
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleSerializer


@api_view(["GET","POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data, partial=True) # 덮어쓰기 방식?
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 어려웠던 점


**article 생성(create)**할때, article 정의할 필요가 없는데 아무 생각없이 article을 정의하고 시작했었음. is_valid 로직을 빼먹고 작성함. serializer.data 쪽 부분 이해가 어려워서 다시 수강했음.

"PUT" 수정부분은 덮어쓰기 방식인거 같은데 --> 프론트엔드와 협업에서 기존 데이터를 불러와 로컬에 저장하고 이후 수정해서 다시 서버로 보내는 식으로 협업한다고 함 PUT 보다는 부분 데이터를 보내는 방식인 `PATCH`를 사용 할 수도 있다.

---

# Class Based View(CBV)

### Class Based View 특징

- 클래스형 뷰에서는 특정 Http Method에 대한 처리를 함수로 분리할 수 있습니다.
    
    → GET요청에 대한 처리는 `get()`에서, POST 요청에 대한 처리는 `post()`에서 정의가 가능해요!
    
- 클래스를 사용하기 때문에 코드의 재사용성과 유지보수성이 향상됩니다.
- 기본 `APIView`외에도 여러 편의를 제공하는 다양한 내장 CBV가 존재합니다.

### Class Based View 종류

- `APIView` - DRF CBV의 베이스 클래스
- `GenericAPIView`
    - 일반적인 API 작성을 위한 기능이 포함된 클래스
    - 보통 CRUD 기능이 대부분인 상황을 위해 여러가지 기능이 미리 내장되어 있습니다.
- `Mixin`
    - 재사용 가능한 여러가지 기능을 담고있느 클래스
    - 말그대로 여러 클래스를 섞어서 사용하기 위한 클래스
        - `ListModelMixin` - 리스트 반환 API를 만들기 위해 상속 받는 클래스
        - `CreateModelMixin` - 새로운 객체를 생성하는 API를 만들기위해 상속 받는 클래스
- `ViewSets`
    - 여러 엔드포인트(endpoint)를 한 번에 관리할 수 있는 클래스
    - RESTful API에서 반복되는 구조를 더 편리하게 작성할 수 있는 방법을 제공합니다.
    
    
이런 특징을 살펴보았으니, 앞서 작성했던 FBV를 CBV로 바꿔보자!

## urls.py

CBV로 바꿔주기 위해서 url을 수정해야 한다.

`as_view()` 메서드를 사용해서 패턴에 연결해야 한다

```python
from django.urls import path
from . import views
app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
]
```

## views.py
`from rest_framework.views import APIView`

`APIView`를 상속받아서 실습했다.

```python
from django.shortcuts import get_object_or_404
from .models import Article
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ArticleSerializer


class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleDetailAPIView(APIView):


    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        data = {"pk": f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)
```

안쪽의 로직은 바뀐게 없고 클래스화 시켜서 안쪽의 메서드를 활용한 API 호출을 사용한다.

이렇게 싱글모델의 CRUD를 실습해 봤다 
