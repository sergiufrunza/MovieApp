FROM  public.ecr.aws/docker/library/python:3.10-buster as web
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Python deps
COPY scripts/supervisord.conf /etc/supervisord.conf
RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY .. /web/
RUN ["chmod", "+x", "/web/scripts/docker-entrypoint.sh"]
ENTRYPOINT ["/web/scripts/docker-entrypoint.sh"]