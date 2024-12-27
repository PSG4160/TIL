<aside>
💡 **N+1 Problem**

위와 같이 관계형 데이터베이스에서 지연로딩을 사용할 경우 관련된 객체를 조회하기 위해 N개의 추가 쿼리가 발생하고 실행 되는 문제입니다. 당연히 데이터베이스에 많은 부하가 걸리고 응답시간이 느려지는 등의 성능 문제를 야기합니다.

</aside>




- **Django에서의 Eager Loading**
    - `select_related`
        - one-to-many 또는 one-to-one 관계에서 사용
        - SQL의 JOIN을 이용해서 관련된 객체들을 한 번에 로드하는 방식
    - `prefetch_related`
        - many-to-many 또는 역참조 관계에서 주로 사용
            
            (select_related를 사용하는 관계에서도 동작)
            
        - 내부적으로 두번의 쿼리를 사용해서 동작
        첫번째 쿼리는 원래 객체를 조회하며 두번째 쿼리는 연관된 객체를 가져오는 방식
        
        
       
지연 로딩(Lazy Loading)은 필요한 시점에 관련 객체를 조회하기 때문에, 여러 개의 객체를 순차적으로 확인하는 과정에서 매번 추가 쿼리가 발생하기 쉽습니다. 예를 들어, 게시글과 작가 정보가 1대다(one-to-many) 관계로 연결되어 있고, 게시글을 반복문으로 순회하면서 작가 정보에 접근한다면, 모든 게시글에 대해 작가 정보를 가져오는 쿼리가 매번 실행됩니다. 이를 N+1 문제라고 부릅니다.

### N+1 문제 해결 방법
N+1 문제를 최소화하려면, 필요한 데이터를 한 번에 미리 불러오는 전략이 좋습니다. Django에서는 `select_related`와 `prefetch_related`가 이를 지원합니다.

1. **select_related**
    - **적용 대상**: ForeignKey나 OneToOneField와 같은 1대1 혹은 1대다 관계
    - **작동 방식**: 내부적으로 SQL JOIN을 사용해 한 번의 쿼리로 관련 객체를 같이 조회
    - **특징**: 직선적 관계(외래 키)나 일대일 관계는 `select_related`로 대부분 처리 가능

2. **prefetch_related**
    - **적용 대상**: ManyToManyField 또는 역참조 관계, 그리고 `select_related`로 처리할 수 없는 경우
    - **작동 방식**: 내부적으로 두 번의 쿼리를 실행  
      - 첫 번째 쿼리: 원본 객체들을 조회  
      - 두 번째 쿼리: 연관된 객체들을 한꺼번에 가져와 메모리에 연결
    - **특징**: `select_related`가 안 되는 관계에서 사용하기 좋으며, 연관된 객체를 한 번에 캐싱해두어 조회 성능을 높임

### 언제 어느 방법을 선택할까?
- **1대다 또는 1대1 관계**: `select_related`가 훨씬 간편하고 쿼리 수도 줄일 수 있음  
- **다대다 또는 역참조 관계**: `prefetch_related`를 사용하는 편이 유용

### 주의사항
- **불필요한 Eager Loading 지양**  
  실제로 데이터가 필요하지 않은데도 무조건 Eager Loading을 적용하면 오히려 불필요한 데이터까지 조회하게 되어 비효율적일 수 있습니다.
- **데이터 양이 매우 많을 때**  
  `prefetch_related`는 한 번에 관련 데이터를 로드하기 때문에, 연관 객체 수가 많으면 메모리에 부담이 될 수도 있습니다.

### 참고 자료
- [Django 공식 문서: select_related](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#select-related)  
- [Django 공식 문서: prefetch_related](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#prefetch-related)
