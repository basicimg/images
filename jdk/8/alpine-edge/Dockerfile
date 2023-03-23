# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:edge
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add openjdk8@community
ENTRYPOINT [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"