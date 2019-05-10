# docker build -t rakesh/pymodules .
FROM ubuntu:16.04

MAINTAINER RakeshD <rakesh.cloud12@gmail.com>

ENV PYTHONUNBUFFERED 2

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:deadsnakes/ppa
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
#RUN apt-get install -y --no-install-recommends python3 python3-virtualenv
RUN apt-get install -y python3.6 python3.6-dev python3-pip python3.6-venv

RUN ln -sfn /usr/bin/python3.6 /usr/bin/python3 && ln -sfn /usr/bin/python3 /usr/bin/python && ln -sfn /usr/bin/pip3 /usr/bin/pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt --upgrade
RUN pip3 install connexion[swagger-ui]
COPY . /usr/src/app

EXPOSE 8082

ENTRYPOINT [ "gunicorn" ]
CMD ["-w", "2", "-b", "0.0.0.0:8082", "basic.wsgi"]
