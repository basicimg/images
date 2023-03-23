FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S openjdk8
ENTRYPOINT [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version | head -n 1)"