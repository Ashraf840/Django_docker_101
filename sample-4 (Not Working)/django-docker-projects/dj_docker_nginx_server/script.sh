#!/bin/bash

# Delete the unnecessary files & folders
uwsgi_aav='/etc/uwsgi/apps-available'
uwsgi_aen='/etc/uwsgi/apps-enabled'
if [ -d "$uwsgi_aav" ]; then
    rm -rf "$uwsgi_aav"
fi
if [ -d "$uwsgi_aen" ]; then
    rm -rf "$uwsgi_aen"
fi

# Start systemd
/lib/systemd/systemd &

systemctl daemon-reload
systemctl start uwsgi.service
systemctl enable uwsgi.service
systemctl start emperor.uwsgi.service
systemctl enable emperor.uwsgi.service

# Keep the container running
tail -f /dev/null

# service uwsgi start
# service uwsgi.service start 
# service emperor.uwsgi.service start