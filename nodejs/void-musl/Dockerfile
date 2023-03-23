# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:musl
RUN basicimg-install nodejs nodejs-devel
RUN corepack enable
CMD [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarn --version)"
