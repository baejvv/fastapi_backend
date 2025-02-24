# Python 공식 이미지 기반
FROM python:3.13-slim

# 최상위 디렉토리
WORKDIR /fastapi_backend

# Poetry 설치
RUN pip install --no-cache-dir poetry

# 의존성 복사
COPY pyproject.toml poetry.lock ./

# Poetry의 가상 환경을 비활성화하고 패키지 설치
RUN poetry config virtualenvs.create false && poetry install --only main --no-root

# 루트 코드 디렉토리
COPY . /fastapi_backend/
WORKDIR /fastapi_backend/backend/app

# 서버 Generate
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
