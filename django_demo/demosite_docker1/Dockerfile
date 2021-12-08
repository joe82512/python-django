# python env
FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
# linux terminal
RUN mkdir /website
WORKDIR /website
# copy code to docker
COPY . /website
RUN pip install -r requirements.txt
# RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt