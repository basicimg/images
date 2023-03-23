# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:musl
RUN basicimg-install redis
RUN mkdir -p /etc/redis
COPY redis/redis.conf /etc/redis/redis.conf
CMD [ "/usr/bin/redis-server", "/etc/redis/redis.conf" ]
EXPOSE 6379
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "redis-cli", "ping" ]
RUN basicimg-setapp "$(redis-server --version)"
