# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /fuego_de_quazar

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP=fuego_de_quazar/__init__.py
CMD [ "flask", "run"]