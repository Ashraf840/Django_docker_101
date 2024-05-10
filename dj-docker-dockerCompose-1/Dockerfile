FROM python:3.11-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install -r /requirements.txt

RUN apk del .tmp

RUN mkdir /src

COPY ./src /src

WORKDIR /src

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/statc

EXPOSE 8000

RUN adduser --disabled-password user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["uwsgi", "--http", ":8080", "--enable-threads", "--module", "src.wsgi:application"]

# CMD ["entrypoint.sh"]