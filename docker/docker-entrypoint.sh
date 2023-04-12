#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser_if_none_exists --user=admin --password=admin

/usr/local/bin/supervisord