# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:sid
RUN basicimg-install redis
RUN mkdir -p /etc/redis
COPY redis/redis.conf /etc/redis/redis.conf
CMD [ "/usr/bin/redis-server", "/etc/redis/redis.conf" ]
EXPOSE 6379
RUN basicimg-setapp "$(redis-server --version)"
