FROM public.ecr.aws/sam/build-python3.9:1.79.0-20230407185812
EXPOSE 8000
# Nginx
RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install nano
RUN apt-get install -y net-tools nginx
RUN apt -y install gettext
RUN rm /etc/nginx/sites-enabled/default
COPY docker/nginx.conf /etc/nginx/sites-enabled
# Supervisord
COPY docker/supervisord.conf /etc/supervisord.conf
ENV PYTHONUNBUFFERED 1
# Python deps
RUN mkdir /code
WORKDIR /code
COPY docker/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/
RUN pwd
RUN ["chmod", "+x", "/code/docker/docker-entrypoint.sh"]
ENTRYPOINT ["/code/docker/docker-entrypoint.sh"]