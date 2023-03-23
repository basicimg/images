# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bullseye
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y openjdk-17-jdk
ENTRYPOINT [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version | head -n 1)"