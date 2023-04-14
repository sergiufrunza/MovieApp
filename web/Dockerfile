FROM  public.ecr.aws/docker/library/python:3.10-buster as web


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Python deps
RUN mkdir /web
WORKDIR /web
COPY docker/requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY .. /web/