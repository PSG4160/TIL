`container`에서 `image`로 **`commit`** 하는 것과, `Dockerfile`에서 `image`로 `build`하는 것의 차이는 뭘까!?


커밋은 이미 사용하고있는 컨테이너가 있을때 그 컨테이너를 이미지로 만드는 백업과 같은 느낌이라면
빌드는 도커 파일을 통해서 만들고 싶은 이미지를 구체적으로 시간의 순서에 따라서 기록해서 만드는 이미지를 생성하는 느낌!

즉 커밋은 백업, 빌드는 생성 결과는 이미지 생성이라는 점은 똑같다!

이제 빌드를 자세히 알아보고 커밋을 간략히 알아보자

>![](https://velog.velcdn.com/images/gyu_p/post/4694c6a7-d2a0-4bec-b834-3cde967ade4d/image.png)
(출처 - 생활코딩 유튜브)



**웹서버 이미지를 만들고 싶다**

먼저 커밋으로 해보고 빌드로 완성해 보자!

![](https://velog.velcdn.com/images/gyu_p/post/92a0abd7-5d62-4fb2-a2d6-70111c3976d1/image.png)

`VS code` 터미널에서도 정상적으로 작동이 된다.!

`Docker Extension Pack`을 설치하면 시각적으로 잘 보여줄 수 있다. <그림 왼쪽 화면 참고>

```
docker run --name web-server -it ubuntu:20.04
```
위 명령어로 `ubuntu 20.04`버전을 실행하고 이름은 `web-server` , `-it`로 실행과 동시해 작업을 할 수 있는 상태로 만들었다.

터미널을 분할하고 `docker commit`을 입력하면 친절하게 아래와 같이 설명해준다.

![](https://velog.velcdn.com/images/gyu_p/post/4088afa9-408d-4d42-8a6c-7086f48dcb61/image.png)

`Usage`를 잘 살펴보고 해당하는 명령어를 입력한 다음 `commit`한 이미지들을 살펴보자.
![](https://velog.velcdn.com/images/gyu_p/post/130e6822-5f41-4cc6-915d-220079860202/image.png)


![](https://velog.velcdn.com/images/gyu_p/post/0b97aa12-096a-4f45-89a2-2e92989f908f/image.png)
확장자에도 `web-server-commit`이 잘 들어간 것을 확인 할 수 있고
![](https://velog.velcdn.com/images/gyu_p/post/91da965b-b8ff-43e5-a757-890bb4bd59da/image.png)

`docker images`명령어를 통해서도 `image`추가된 것을 볼 수 있다.


---

앞에서 commit을 통해 `image`를 백업? 한 것을 실습해봤다. 이번엔 `Dockerfile`을 이용해서 `img`를 생성해보자.

![](https://velog.velcdn.com/images/gyu_p/post/9d48f4dd-9e41-4d6d-a16e-432360c9ef59/image.png)

경로 폴더에 `Dockerfile`이라는 파일명을 만드니 고래모양이 뜨면서 뭔가 되는거 같다?

`ubuntu`를 깔고 연결을 시켰기 때문에 터미널에서 `docker`명령어를 사용하면 바로 `bash-Docker`로 지정이 된다.!

![](https://velog.velcdn.com/images/gyu_p/post/e42d110a-a463-482e-b900-95cdcf9a179d/image.png)


해당 폴더에 `app.py`를 하나 만들고 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

`Dockerfile`에는


```python

# 기본 이미지 설정
# Python 3.8을 쓸건데, 가장 가벼운 이미지로 골라줘
FROM python:3.8-slim

# 애플리케이션 파일 복사
COPY app.py /app.py

# Flask 설치
RUN pip install Flask

# 애플리케이션 실행
# RUN과 CMD의 차이 RUN은 그냥 돌리는거, CMD는 형식이 정해져있을때
CMD ["python", "/app.py"]
```

위와같은 코드를 넣어준다.!

터미널에서 

```
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
```
명령어들을 입력해주면

![](https://velog.velcdn.com/images/gyu_p/post/41698f5e-bf11-4dd6-8e11-d2a3639cad40/image.png)

이렇게 빌드가 잘 되고 `container`를 실행한 것도 확인 할 수 있다.

![](https://velog.velcdn.com/images/gyu_p/post/be200227-8140-4a55-b7eb-5c896ae1a9da/image.png)


---

이렇게 `docker`의 `commit`과 `build`에 대해서 차이점을 알아보고 실습을 진행하며 이해를 해봤다.!!



---

추가로 어제 특강시간에 `ubuntu`를 사용하여

nano app 으로 접속해서

위와 같은 과정을 통해 `build`시키고 `run`하는것도 봤다.

