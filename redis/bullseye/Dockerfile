# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bullseye
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y redis
RUN mkdir -p /etc/redis
COPY redis/redis.conf /etc/redis/redis.conf
CMD [ "/usr/bin/redis-server", "/etc/redis/redis.conf" ]
EXPOSE 6379
RUN basicimg-setapp "$(redis-server --version)"