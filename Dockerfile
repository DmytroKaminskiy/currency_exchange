FROM python:3.7.6

RUN apt-get update && apt-get install -y \
    python-dev \
    python-setuptools \
    && apt-get clean

WORKDIR /srv/project

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
