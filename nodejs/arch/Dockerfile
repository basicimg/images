FROM ghcr.io/basicimg/arch
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    pacman -Sy --noconfirm nodejs
RUN corepack enable
CMD [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarn --version)"