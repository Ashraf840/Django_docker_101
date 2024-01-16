FROM ubuntu:22.04

ENV PYTHONBUFFERED=1

# Install necessary packages
RUN apt-get update \
    && apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools \
        python3.10-venv \
        uwsgi \
        uwsgi-plugin-python3 \
        wget \
    && python3 -m pip install --upgrade pip \
    && apt upgrade -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir -p /etc/uwsgi/vassals

WORKDIR /django

COPY requirements.txt requirements.txt

RUN python3 -m venv env \
    && /bin/bash -c "source env/bin/activate" \
    && pip install -r requirements.txt \
    && mkdir -p logs/ \
    && touch logs/uwsgi.log

COPY . .

COPY ./uwsgi.service /etc/systemd/system/
COPY ./emperor.ini /etc/uwsgi/
COPY ./emperor.uwsgi.service /etc/systemd/system/
COPY ./app.ini /etc/uwsgi/vassals

# Install docker-systemctl-replacement
# Download and extract docker-systemctl-replacement
RUN wget https://github.com/gdraheim/docker-systemctl-replacement/archive/master.tar.gz && \
    tar xzf master.tar.gz && \
    mv docker-systemctl-replacement-master /docker-systemctl-replacement && \
    rm master.tar.gz && \
    apt-get remove -y wget && \
    apt-get autoremove -y

# Enable docker-systemctl-replacement
RUN ln -s /docker-systemctl-replacement/docker-systemctl-replacement /usr/local/bin/systemctl

EXPOSE 8080

COPY ./script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh

CMD ["sh", "-c", "/usr/local/bin/script.sh"]

# CMD python3 manage.py runserver 0.0.0.0:8080