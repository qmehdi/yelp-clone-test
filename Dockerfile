FROM python:3.8
MAINTAINER Qamber Mehdi

# RUN apt-get clean

# RUN apt-get update -y && \
# apt-get install -y python-dev build-essential

RUN curl https://bootstrap.pypa.io/get-pip.py | python3

VOLUME /app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/bin/python", "app.py"]

