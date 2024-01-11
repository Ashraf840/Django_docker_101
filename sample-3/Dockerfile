FROM 826546/ubuntu-22.04:redis-server-1.2

RUN apt update \
  && apt install -y \
    nginx \
  && apt upgrade -y \
  && apt clean \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 80

COPY ./shell-scripts/script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh

CMD ["sh", "-c", "/usr/local/bin/script.sh"]
