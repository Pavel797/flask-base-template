FROM python:3.7-alpine

RUN apk add --update --no-cache \
    gcc \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    musl-dev

WORKDIR /app
ENV PYTHONBUFFERED 1
ENV PYTHONPATH /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
