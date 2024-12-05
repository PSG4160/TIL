
# window에서 Docker 설치하기

## WSL2 설치를 위한 사전 준비
### WSL2란?

>WSL2란?
WSL2(Windows Subsystem for Linux 2)는 Windows에서 Linux 환경을 실행할 수 있는 서브시스템으로, Microsoft에서 개발한 도구입니다. WSL1에 비해 성능과 호환성이 대폭 개선되었으며, 실제 Linux 커널을 사용해 가상 머신(VM) 없이 네이티브 Linux 환경과 유사한 성능을 제공합니다.

### 사전 설정하기
![](https://velog.velcdn.com/images/gyu_p/post/a8d0080f-7907-4c68-a266-d0e6e61c95b9/image.png)
![](https://velog.velcdn.com/images/gyu_p/post/1e5e3fd1-710d-490c-b2fd-431ed5b0d838/image.png)

이렇게 `Hyper -V`와 `Linux`용 하위 시스템을 체크 해야한다.!
**설정하면 컴퓨터 재부팅이 된다**

>Hyper-V란?
Hyper-V는 Microsoft에서 제공하는 가상화 플랫폼입니다. Windows 운영 체제에 내장된 기능으로, 사용자가 하나의 물리적 컴퓨터에서 여러 개의 가상 컴퓨터(VM, Virtual Machine)를 실행할 수 있게 해줍니다.

### WSL 설치 명령어

```
wsl --install

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

wsl --update

```

>dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
WSL2를 실행하기 위해 필요한 Windows의 가상화 플랫폼 기능을 활성화하는 명령어
Virtual Machine Platform을 활성화하여 WSL2가 Hyper-V 기반 경량 가상화 기술을 사용할 수 있도록 설정.


## Ubuntu 설치하기

### Ubuntu란?


>Linux 기반의 운영 체제 중 하나로, 전 세계적으로 가장 널리 사용되는 배포판입니다

**Ubuntu의 사용 사례**


1. 개발 환경

    - 프로그래밍, 웹 개발, 데이터 과학, 머신러닝 환경에 적합.
    - 다양한 언어와 도구를 지원: Python, Java, Node.js 등.
2. 서버 운영

    - 웹 서버(Apache, Nginx), 데이터베이스 서버(MySQL, PostgreSQL), 클라우드 서버로 널리 사용.
3. 교육 및 학습

    - Linux 명령어 학습과 시스템 관리 공부에 이상적.
4. 일반 사용자

    - 무료 운영 체제로 데스크톱 PC나 노트북에서 사용 가능.
5. 컨테이너 및 클라우드

	- Docker, Kubernetes 같은 컨테이너 플랫폼에서 기본 운영 체제로 많이 사용.
    
### Ubuntu 설치

https://apps.microsoft.com/detail/9pn20msr04dw?gl=KR&hl=ko-kr
![](https://velog.velcdn.com/images/gyu_p/post/c52b765f-7e95-45a1-9422-f895b2a2eb65/image.png)

위 링크로 설치한 후 앱을 실행하여 ubuntu에 `docker` 설치하기

```bash
# docker engine gpg 키 등록
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# apt source 에 docker 관련 추가
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# docker engine 설치
sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
docker-buildx-plugin docker-compose-plugin docker-compose

# docker 그룹에 현재 계정을 등록하여 sudo 없이 docker 명령을 사용하게 함
sudo usermod -aG docker user
sudo service docker restart

# 새로운 터미널을 열고 확인
docker version
```


### Docker Desktop


https://docs.docker.com/desktop/setup/install/windows-install/

위 링크로 접속 후

![](https://velog.velcdn.com/images/gyu_p/post/d9d7e9a0-bc82-411a-abfe-efc6172e9be4/image.png)

`Docker Desktop for Windows - x86_64`을 눌러 `Docker Desktop`설치하기


설치 되었으면 앱에서 

![](https://velog.velcdn.com/images/gyu_p/post/33be7352-fd5b-4904-acd3-676d848b39c5/image.png)


`우측 상단 톱니바퀴 → 왼쪽 Resources → WSL Integration → Apply&restart`

이렇게 설정하면 재부팅 했던걸로 기억한다...

>이 옵션은 Docker Desktop과 WSL2(Windows Subsystem for Linux 2) 간의 통합 설정을 의미합니다. Docker Desktop은 WSL2를 통해 Docker 엔진을 실행하며, 이 설정을 통해 특정 Linux 배포판(WSL2 Distro)에서 Docker를 사용할 수 있도록 설정합니다.

