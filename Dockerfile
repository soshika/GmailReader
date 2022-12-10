FROM ubuntu:latest

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app/cron

WORKDIR /$APP_HOME

COPY . $APP_HOME/

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    rm -rf /var/lib/apt/lists/*
RUN add-apt-repository universe
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get -y update
RUN pip3 install -r requirements.txt
CMD python3 ./main.py
