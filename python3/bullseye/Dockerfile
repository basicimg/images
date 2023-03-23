# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bullseye
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y python3-full python-is-python3
ENTRYPOINT [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"