#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser_if_none_exists --user=${SUPER_USER_NAME} --password=${SUPER_USER_PASS}

/usr/local/bin/supervisord