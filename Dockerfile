FROM ubuntu:16.04
MAINTAINER Qamber Mehdi

RUN apt-get update -y && \
apt-get install -y python-pip python-dev build-essential

VOLUME /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/bin/python", "app.py"]

