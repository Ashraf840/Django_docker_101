FROM ubuntu:22.04

ENV PYTHONBUFFERED=1

RUN apt-get update \
    && apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools \
        python3.10-venv \
    && python3 -m pip install --upgrade pip \
    && apt upgrade -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /django

COPY requirements.txt requirements.txt

RUN python3 -m venv env \
    && /bin/bash -c "source env/bin/activate" \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8080

COPY ./script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh

CMD ["sh", "-c", "/usr/local/bin/script.sh"]

# CMD python3 manage.py runserver 0.0.0.0:8080