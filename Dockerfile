FROM python:3.11-slim

# 컨테이너 작업 디렉토리
WORKDIR /app

# 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --no-warn-script-location

# 소스 복사
COPY . .

# Flask 실행 (개발용, 테스트 시)
CMD ["python", "app.py"]