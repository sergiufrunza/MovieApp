#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --username admin --password admin --noinput --email ''

/usr/local/bin/supervisord