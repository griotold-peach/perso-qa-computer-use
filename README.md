# Perso.ai QA Automation with Computer Use

Perso.ai 웹사이트 QA 자동화 프로젝트 - Claude Computer Use API 활용

## 프로젝트 개요

Claude의 Computer Use 기능을 활용하여 Perso.ai의 20개 QA 태스크를 자동화합니다.

### 기술 스택

- **Python 3.12** - 프로그래밍 언어
- **uv** - 패키지 관리자
- **Claude Computer Use API** - Sonnet 4.5
- **Docker** - 실행 환경 (Ubuntu 22.04 + X11)
- **VNC** - 브라우저 화면 확인

---

## 빠른 시작

### 1. 환경변수 설정
```bash
export ANTHROPIC_API_KEY=your_api_key_here
export PERSO_EMAIL=your_email@example.com
export PERSO_PASSWORD=your_password
```

### 2. Docker 이미지 빌드
```bash
docker build -t perso-qa-computer-use .
```

### 3. 실행
```bash
docker run \
    -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
    -e PERSO_EMAIL=$PERSO_EMAIL \
    -e PERSO_PASSWORD=$PERSO_PASSWORD \
    -e WIDTH=1920 \
    -e HEIGHT=1080 \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 6080:6080 \
    -p 8080:8080 \
    -it perso-qa-computer-use
```

### 4. 브라우저에서 확인
```
http://localhost:8080
```

VNC 화면에서 Firefox가 실행되는 모습을 실시간으로 볼 수 있습니다!

---

## 프로젝트 구조
```
perso-qa-computer-use/
├── perso_qa_automation/       # 메인 패키지
│   ├── loop.py                # Computer Use agent loop
│   ├── config.py              # 설정 파일
│   ├── main.py                # 전체 태스크 실행
│   │
│   ├── tools/                 # Computer Use 도구들
│   │   ├── computer.py        # 마우스, 키보드, 스크린샷
│   │   ├── bash.py            # 터미널 명령
│   │   └── edit.py            # 파일 편집
│   │
│   ├── tasks/                 # Perso.ai QA 태스크
│   │   ├── task_01_login.py   # 1. 로그인
│   │   ├── task_02_upload.py  # 2. 파일 업로드
│   │   └── ...                # 3-20. 나머지 태스크
│   │
│   └── utils/                 # 유틸리티
│       └── runner.py          # 태스크 실행 헬퍼
│
├── image/                     # Docker 시작 스크립트들
├── docs/                      # 문서
│   ├── PRD.md                 # 프로젝트 요구사항
│   └── SETUP.md               # 설치 가이드
│
├── screenshots/               # 스크린샷 저장
├── logs/                      # 로그 파일
├── Dockerfile                 # Docker 이미지 설정
└── README.md                  # 이 파일
```

---

## 태스크 실행

### 컨테이너 내부에서 실행
```bash
# 컨테이너 ID 확인
docker ps

# 컨테이너 내부 접속
docker exec -it <container_id> /bin/bash

# 전체 태스크 실행
python -m perso_qa_automation.main

# 개별 태스크 실행 (예: Task 01)
python -m perso_qa_automation.tasks.task_01_login
```

---

## 태스크 목록

### Phase 1 (MVP)
- 🔲 Task 01: 홈페이지 접속 및 로그인
- 🔲 Task 02: 로컬 파일 업로드
- 🔲 Task 03: 유튜브 롱폼 링크 업로드
- 🔲 Task 04: 유튜브 쇼츠 링크 업로드
- 🔲 Task 05: 틱톡 링크 업로드

### Phase 2
- 🔲 Task 06-10: 링크 업로드 및 검증
- 🔲 Task 11-15: 다운로드 및 편집 기능

### Phase 3
- 🔲 Task 16-20: 고급 기능 테스트

전체 목록은 [docs/PRD.md](docs/PRD.md) 참고

---

## 개발 가이드

### 새 태스크 추가
```python
# perso_qa_automation/tasks/task_XX_name.py

import asyncio
from ..config import config
from ..utils.runner import run_task

TASK_XX_PROMPT = """
작업 설명...
"""

async def run():
    prompt = TASK_XX_PROMPT.format(...)
    return await run_task(prompt, "Task XX: 이름")

if __name__ == "__main__":
    asyncio.run(run())
```

### Docker 재빌드
```bash
# 코드 변경 후 재빌드
docker stop <container_id>
docker rm <container_id>
docker build -t perso-qa-computer-use .
# 다시 실행
```

---

## 환경변수

### 필수 환경변수
```bash
# Anthropic API
ANTHROPIC_API_KEY=sk-ant-...

# Perso.ai 로그인
PERSO_EMAIL=your@email.com
PERSO_PASSWORD=your_password

# Computer Use 설정 (선택)
WIDTH=1920
HEIGHT=1080
DISPLAY_NUM=1
```

### .env 파일 사용 (선택)
```bash
# .env.example을 복사
cp .env.example .env

# .env 파일 편집
nano .env

# Docker 실행 시 환경변수 자동 로드
docker run --env-file .env -p 8080:8080 -it perso-qa-computer-use
```

---

## 문제 해결

### VNC 화면이 안 보여요
- Docker 컨테이너가 실행 중인지 확인: `docker ps`
- 포트 8080이 사용 가능한지 확인: `lsof -i :8080`
- 브라우저 새로고침 (Cmd+R 또는 Ctrl+R)

### API Rate Limit 에러
- Claude API 사용량 확인: https://console.anthropic.com/settings/usage
- 태스크 간 대기 시간 추가
- `only_n_most_recent_images=3` 설정으로 토큰 절약

### Firefox가 실행 안 돼요
- VNC 화면에서 Firefox 아이콘 확인
- 주소창 클릭해서 URL 직접 입력
- 시작 마법사는 무시하고 주소창 사용

### Docker 빌드 에러
```bash
# 캐시 없이 재빌드
docker build --no-cache -t perso-qa-computer-use .
```

---

## 포트 정보

- **8080** - VNC 브라우저 접속 (추천)
- **6080** - VNC 전용 (8080과 동일한 화면)
- **5900** - VNC 직접 연결 (클라이언트 필요)

---

## 참고 문서

- [PRD.md](docs/PRD.md) - 프로젝트 요구사항 문서
- [Computer Use Demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) - 공식 데모

---

## 라이선스

MIT
