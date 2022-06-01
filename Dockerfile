FROM python:3.10-alpine3.13
LABEL maintainer="kibraks"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY Pipfile /code/

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps\
      build-base postgresql-dev musl-dev && \
    pip install pipenv && pipenv install --system --skip-lock --dev && \
    rm -rf /tmp && \
    apk del .tmp-build-deps &&\
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
