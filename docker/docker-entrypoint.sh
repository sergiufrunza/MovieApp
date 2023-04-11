#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput

/usr/local/bin/supervisord