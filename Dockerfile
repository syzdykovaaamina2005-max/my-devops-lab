# Simple Dockerfile for Flask App
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app
CMD ["python", "app/app.py"]
