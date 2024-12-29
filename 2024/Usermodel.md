## CustomUserManager

```python
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
```

- `BaseUserManager`를 상속받아 `create_user`와 `create_superuser` 메서드를 커스터마이징했다.
- `create_user `메서드에서 이메일 유효성을 검사했고, `set_password`로 비밀번호를 해시 처리했다.
- 관리자 계정 생성을 위해 `create_superuser` 메서드에서 `is_staff`, `is_superuser` 값을 `True`로 지정했다.


## Custom User 모델

```python

class User(AbstractUser):
    email = models.EmailField('이메일', unique=True)
    username = models.CharField('닉네임', max_length=150)  # unique=True 제거
    profile_image = models.ImageField('프로필 이미지', upload_to='profile_images/', blank=True, null=True)
    followings = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='followers',
        through='Follow'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
```
- `AbstractUser`를 상속받아 이메일을 주요 필드로 설정했다.
- `USERNAME_FIELD`를 `email`로 지정해 이메일 기반 로그인을 구현했다.
- `followings`라는 `ManyToManyField`를 두어 사용자 간 팔로우 관계를 관리했다.
- 필요한 경우 `profile_image` 같은 필드를 추가해 프로필 확장이 가능했다.


## 중간 테이블

```python
class Follow(models.Model):
    follower = models.ForeignKey(
        User, related_name='followed_users', on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, related_name='following_users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
```

- `ManyToManyField`에 through 인자를 줘 직접 중간 테이블을 정의했다.
- `unique_together` 옵션을 활용해 같은 사용자 간 중복 팔로우를 방지했다.
- 이로써 원하는 시점에 팔로우 관계를 추가하거나 조회할 수 있다.

참고자료 
[공식문서](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/)

[Auth문서](https://docs.djangoproject.com/en/4.2/ref/contrib/auth/)
