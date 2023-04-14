FROM  public.ecr.aws/docker/library/python:3.10-buster
# Nginx
RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install nano
RUN apt-get install -y net-tools nginx
RUN apt -y install gettext
RUN rm /etc/nginx/sites-enabled/default
COPY nginx/nginx.conf /etc/nginx/sites-enabled
# Supervisord
COPY nginx/supervisord.conf /etc/supervisord.conf
ENV PYTHONUNBUFFERED 1
# Python deps
RUN mkdir /web
WORKDIR /web
COPY web/requirements.txt /web/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY web/ /web/
RUN pwd
RUN ["chmod", "+x", "/web/scripts/docker-entrypoint.sh"]
ENTRYPOINT ["/web/scripts/docker-entrypoint.sh"]