# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:stable AS bootstrap
WORKDIR /tmp
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apt-get update && apt-get download base-files netbase tzdata ca-certificates
RUN dpkg --force-all --root=/system -i *.deb
COPY distroless/passwd /system/etc/passwd

FROM scratch
COPY --from=bootstrap /system/ /