#!/bin/bash

python manage.py collectstatic --noinput
uwsgi --socket :8080 --master --enable-threads --module app.wsgi