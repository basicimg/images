FROM ghcr.io/basicimg/arch
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    pacman -Sy --noconfirm jdk8-openjdk
ENTRYPOINT [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version | head -n 1)"