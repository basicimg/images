FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S redis
ENTRYPOINT [ "/usr/bin/redis-server" ]
RUN basicimg-setapp "$(redis-server --version)"