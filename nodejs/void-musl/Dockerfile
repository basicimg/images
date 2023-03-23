FROM ghcr.io/basicimg/void:musl
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S nodejs nodejs-devel
RUN corepack enable
ENTRYPOINT [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarn --version)"