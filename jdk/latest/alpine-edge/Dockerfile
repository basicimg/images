# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:edge
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add openjdk19-jdk@testing
ENTRYPOINT [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version | head -n 1)"