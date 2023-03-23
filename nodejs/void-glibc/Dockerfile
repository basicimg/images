# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S nodejs nodejs-devel
RUN corepack enable
CMD [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarn --version)"