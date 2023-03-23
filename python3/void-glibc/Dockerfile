FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S python3
ENTRYPOINT [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"