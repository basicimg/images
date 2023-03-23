# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:3-17
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add python3
ENTRYPOINT [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"