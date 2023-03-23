FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S redis
RUN mkdir -p /etc/redis
COPY redis/redis.conf /etc/redis/redis.conf
CMD [ "/usr/bin/redis-server", "/etc/redis/redis.conf" ]
EXPOSE 6379
RUN basicimg-setapp "$(redis-server --version)"