# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bookworm
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y redis
ENTRYPOINT [ "/usr/bin/redis-server" ]
RUN basicimg-setapp "$(redis-server --version)"