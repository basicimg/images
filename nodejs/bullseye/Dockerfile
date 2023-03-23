# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bullseye
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y nodejs npm yarnpkg
CMD [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarnpkg --version)"