FROM python:3.8-alpine

ENV PYTHONBUFFERED 1
ENV SECRET_KEY ^efn8quf@f1v-^x^5cre5*pyv37j)ryx5-gib*p@xd5w4v-tic

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev nginx libressl gettext


WORKDIR /code
COPY . /code/
RUN mkdir -p /code/static/assets

RUN pip install --upgrade pip
RUN pip install -U pip setuptools
RUN pip install pipenv==2018.11.26

COPY Pipfile* ./
RUN pipenv install --dev --system

RUN adduser -D $USER docker
RUN chown -R $USER:docker /code

USER $USER

EXPOSE 8000
