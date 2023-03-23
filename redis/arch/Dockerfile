FROM ghcr.io/basicimg/arch
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    pacman -Sy --noconfirm redis
ENTRYPOINT [ "/usr/bin/redis-server" ]
RUN basicimg-setapp "$(redis-server --version)"