FROM python:3.7.9-alpine3.13
MAINTAINER winhtaikaung(winhtaikaung28@hotmail.com)

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app
COPY run.sh /usr/src/app/
EXPOSE 80



