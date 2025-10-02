FROM python:3.11-slim

# 컨테이너 작업 디렉토리
WORKDIR /app

# 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --no-warn-script-location

# 🔹 GitHub Actions에서 전달받을 build-args 선언
ARG HOMEWEB_USER
ARG HOMEWEB_PW
ARG HOMEWEB_KEY

# 🔹 빌드 시 전달된 ARG를 ENV로 저장 → 컨테이너 실행 환경변수로 사용 가능
ENV HOMEWEB_USER=$HOMEWEB_USER
ENV HOMEWEB_PW=$HOMEWEB_PW
ENV HOMEWEB_KEY=$HOMEWEB_KEY

# 소스 복사
COPY . .

# Flask 실행 (개발용, 테스트 시)
CMD ["python", "app.py"]