FROM debian:buster

RUN apt update -y
RUN apt install virtualenv -y

WORKDIR /root
RUN virtualenv -p python3 env
RUN . env/bin/activate
RUN /root/env/bin/pip install nbformat ds100nbconvert
