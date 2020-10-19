FROM python:3.7-alpine
LABEL maintainer="Armin Eslami"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
# add needed dependencies for installing postgres package temporarely (remove after installing)
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# delete dependencies added for installing postgres
RUN apk del .tmp-build-deps 

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
