FROM python:3.9-bullseye

RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev supervisor nano gettext

WORKDIR /app/

COPY requirements/common.txt /tmp/common.txt
COPY requirements/local.txt /tmp/local.txt
RUN pip install -r /tmp/local.txt

COPY . /app/

