FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ARG GIT_SHA=unknown
ENV PORT=8080 APP_VERSION=unset GIT_SHA=${GIT_SHA}
EXPOSE 8080
CMD ["python", "app.py"]
