
내가 설정한 `Sertializer`클래스에서 오버라이딩을 통해 특정 필드를 수정하거나, 전체 필드를 수정해서 return 하는 법을 배웠다.


현재 `articles/serializers.py`에서 정의된 `CommentSerializer`를 살펴보자.

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",) # POST요청 들어오면 읽기 전용 필드는 수정 X
```

이렇게 정의되어있는 `CommentSerializer`에서 Api를 송출할때 `article` 필드를 제외해보자.

```python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"  # Comment 모델의 모든 필드를 직렬화
        read_only_fields = ("article",)  # "article" 필드는 읽기 전용

    def to_representation(self, instance):
        # 부모 클래스의 to_representation 호출 -> 기본 직렬화 실행
        ret = super().to_representation(instance)
        # 직렬화 결과에서 "article" 필드 제거
        ret.pop("article")
        return ret
```

### **코드 설명**

 `CommentSerializer` 클래스가 `serializers.ModelSerializer` 부모 클래스를 상속받고, `to_representation` 메서드를 오버라이딩하여 `Comment` 모델의 전체 직렬화 결과에서 특정 필드(`article`)을 제외(pop)한거다!

[공식문서 링크](https://www.django-rest-framework.org/api-guide/fields/#custom-fields)

위 공식문서를 확인하면, 
특정 값을 다룰때는 전체 클래스를 오버라이딩 할때 사용하는 `instance` 대신 `value`(필드 수준의 커스터마이징)를 사용한다.

**`to_representation`**의 정의
to_representation는 DRF의 직렬화 과정에서 호출되며, 모델 인스턴스를 직렬화 가능한 Python 데이터로 변환하는 메서드이다.




