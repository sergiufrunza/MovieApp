FROM  public.ecr.aws/docker/library/python:3.10-buster
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Python deps

RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /web/
EXPOSE 80
CMD ["gunicorn", "--chdir", "MovieApp", "--bind", ":80", "MovieApp.wsgi:application"]
RUN ["chmod", "+x", "/web/scripts/docker-entrypoint.sh"]
ENTRYPOINT ["/web/scripts/docker-entrypoint.sh"]