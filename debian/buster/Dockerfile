# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    --mount=type=cache,target=/system/var/lib/apt,sharing=locked \
    debootstrap --variant=minbase buster /system https://deb.debian.org/debian/
RUN touch /system/basicimg

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/bash", "-c" ]
CMD [ "/bin/bash" ]
RUN echo "Hello, Debian Buster!"