FROM ghcr.io/basicimg/void:musl
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S python3 python3-devel
ENTRYPOINT [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"