# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    --mount=type=cache,target=/system/var/lib/apt,sharing=locked \
    debootstrap --variant=minbase --components=main,universe jammy /system http://archive.ubuntu.com/ubuntu/
RUN basicimg-init-system "Ubuntu Jammy"

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/bash", "-c" ]
CMD [ "/bin/bash" ]
RUN basicimg-hello