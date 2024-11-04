
```
pip install requests
```
# 전체 코드
```python
import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

# 설정 가능한 변수
output_filename = "output_audio.mp3"

url = "모델 URL"
headers = {
    "xi-api-key": "API - KEY",
    "Content-Type": "application/json"
}

# 문장을 입력받습니다.
text = input("텍스트를 입력하세요: ")

# 음성 생성 요청을 보냅니다.
data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.3,
        "similarity_boost": 1,
        "style": 1,
        "use_speaker_boost": True
    }
}

response = requests.post(url, json=data, headers=headers, stream=True)

if response.status_code == 200:
    audio_content = b""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            audio_content += chunk

    segment = AudioSegment.from_mp3(io.BytesIO(audio_content))
    segment.export(output_filename, format="mp3")
    print(f"Success! Wrote audio to {output_filename}")

    # 오디오를 재생합니다.
    play(segment)
else:
    print(f"Failed to save file: {response.status_code}")
```

`url`에 `elevenlabs`홈페이지의 voice를 참고해서 
`"https://api.elevenlabs.io/v1/text-to-speech/<voice ID>"`
입력한다.


`api key` 도 홈페이지에서 로그인 후 발급받아서 실습을 진행함.

>C:\Users\1\anaconda3\envs\AI\lib\site-packages\pydub\utils.py:198: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
  warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
  FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다
  
  이런 에러가 나와서 `ffmpeg`를 설치했다.
  
  
 **설치**
 
 
ffmpeg 홈페이지에 접속

[홈페이지 사이트](https://ffmpeg.org/download.html)

![](https://velog.velcdn.com/images/gyu_p/post/d226351e-f7d7-4b3a-bd41-80f522f53b72/image.png)
여기

- `gyan.dev`로 들어간다.


![](https://velog.velcdn.com/images/gyu_p/post/fc7af53f-41f7-437a-b905-dc2ecfe1a56d/image.png)


- `releasae`에서 `ffmpeg-7.0.2-essentials_build.zip`를 받고 압축풀기


- 환경 변수 설정 -> 편집 `bin` 디렉토리 위치로 경로 추가

- ffmpeg 버전 확인 (깔렸는지 확인)
![](https://velog.velcdn.com/images/gyu_p/post/6430b079-3997-456b-bc5f-7eb0e4c9ddaf/image.png)


과정을 거쳐서 실습을 진행하고 `VScode`의 터미널에서 파이썬 호출 명령어로 실행하니 관리자 권한 구문이 나왔다.
```
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\1\\AppData\\Local\\Temp\\tmpt1kr40kj.wav'
```

만들어진 voice파일은 경로에 저장되었으나, 바로 실행은 관리자 권한이 필요함

천튜터님:

Eleven Labs 를 사용하는 실습(ChatGPT와 ElevenLabs 실습, 음성 생성과 번역을 활용한 번역 서비스 만들기)을 진행하실 때 생성된 오디오 파일에 대한 권한 문제(Permission denied)로 재생이 안되는 경우가 있습니다

`해결 방법 : pydub.playback의 play 라이브러리 사용하는 대신 playsound 라이브러리 사용`

1. 설치
`pip install playsound `
2. 코드변경
```
# 오디오 파일을 재생하는 코드 부분을 아래와 같이 변경해주세요
# 기존 코드
 # Pydub을 통해 mp3 파일을 불러와서 재생
audio = AudioSegment.from_mp3(audio_path)
play(audio)  # Pydub의 play() 함수 사용

---- 변경 후
import playsound

# 오디오를 재생합니다.
playsound.playsound(audio_path)
```