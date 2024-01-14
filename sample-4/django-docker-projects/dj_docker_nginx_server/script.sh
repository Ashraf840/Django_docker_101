#!/bin/bash

# Delete unnecessary files & folders
uwsgi_aav='/etc/uwsgi/apps-available'
uwsgi_aen='/etc/uwsgi/apps-enabled'
if [ -d "$uwsgi_aav" ]; then
    rm -rf "$uwsgi_aav"
fi
if [ -d "$uwsgi_aen" ]; then
    rm -rf "$uwsgi_aen"
fi

systemctl start uwsgi.service
python3 manage.py runserver 0.0.0.0:8080