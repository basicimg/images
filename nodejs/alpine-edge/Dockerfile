# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:edge
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add nodejs nodejs-dev npm@community yarn@community
ENTRYPOINT [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarn --version)"