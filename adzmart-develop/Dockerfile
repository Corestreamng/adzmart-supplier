# syntax=docker/dockerfile:1
FROM python:3.11
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ADD requirements/prod.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

ADD . /app

CMD hypercorn adzmart.asgi:application --bind '0.0.0.0:8080' --bind '[::]:8080' --access-log - --error-log - -k uvloop -w 4
