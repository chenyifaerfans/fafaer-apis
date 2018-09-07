#!/usr/bin/env bash

#/usr/local/bin/python manage.py makemigrations
#/usr/local/bin/python manage.py migrate
#/usr/local/bin/python manage.py createsuperuser --username admin --email admin@admin.com
uwsgi -s :9001 -w fafaerapis.wsgi -p 3