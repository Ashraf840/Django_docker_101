FROM ubuntu:22.04

LABEL maintainer="Kh Tanjim Ashraf <shift2unleashed2011@gmail.com>"

RUN apt update \
  && apt install -y \
    redis \
  && apt upgrade -y \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 6379

COPY ./shell-scripts/script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh

CMD ["sh", "-c", "/usr/local/bin/script.sh"]
