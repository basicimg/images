# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:3-17
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add openjdk8-jdk@community
ENTRYPOINT [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version | head -n 1)"