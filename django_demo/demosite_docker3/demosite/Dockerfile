# python env
FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
# linux terminal
RUN mkdir /demosite
WORKDIR /demosite
# copy code to docker
COPY . /demosite
RUN pip install -r requirements.txt
# RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt