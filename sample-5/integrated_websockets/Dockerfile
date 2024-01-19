FROM python:3.10.13-alpine

# ENV PATH="/scripts:${PATH}"

# COPY ./requirements_ubuntu.txt /requirements_ubuntu.txt
COPY ./requirements_docker.txt /requirements_docker.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements_docker.txt
RUN apk del .tmp

RUN mkdir /app
# COPY ./app /app
COPY . .
WORKDIR /app

# # COPY script.sh script.sh
# COPY ./scripts/script.sh /scripts/script.sh
# RUN chmod +x /scripts/script.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web


EXPOSE 8080

# RUN python manage.py collectstatic --noinput
RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate

# CMD ["uwsgi", "--http", ":8080", "--module", "app.wsgi:application"]
# CMD ["uwsgi", "--http", ":8080", "--module", "app.wsgi:application", "--pythonpath", "/app"]

# CMD ["sh", "-c", "/scripts/script.sh"]
# CMD ["/myscript.sh"]

# RUN /bin/bash -c 'python manage.py collectstatic --noinput'

CMD ["uwsgi", "--socket", ":8080", "--master", "--enable-threads", "--module", "app.wsgi:application"]
# CMD ["uwsgi", "--socket", ":8080", "--master", "--enable-threads", "--module", "app.wsgi:application", "--pythonpath", "/app"]