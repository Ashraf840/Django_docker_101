FROM ubuntu:22.04

RUN apt update \
  && apt install -y \
    redis
  && apt upgrade -y \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

CMD [ "redis-server" ]

