# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:3-17
RUN apk add --no-cache redis
ENTRYPOINT [ "/usr/bin/redis-server" ]
RUN basicimg-setapp "$(redis-server --version)"