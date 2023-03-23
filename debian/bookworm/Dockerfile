# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    --mount=type=cache,target=/system/var/lib/apt,sharing=locked \
    debootstrap --variant=minbase --components=main,contrib --include=build-essential bookworm /system https://deb.debian.org/debian/
RUN basicimg-init-system "Debian Bookworm"

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/bash", "-ec" ]
CMD [ "/bin/bash" ]
RUN basicimg-hello