# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN wget -O /tmp/void.tar.xz https://repo-fastly.voidlinux.org/live/current/void-x86_64-musl-ROOTFS-20221001.tar.xz
WORKDIR /system
RUN tar -xf /tmp/void.tar.xz
RUN basicimg-init-system "Void Linux (bootstrap musl)"

FROM scratch AS rootfs
COPY --from=bootstrap /system/ /
RUN mkdir -p /system/var/db/xbps/keys
RUN cp /var/db/xbps/keys/* /system/var/db/xbps/keys/
RUN xbps-install --reproducible --yes -S -r /system -R "https://repo-fastly.voidlinux.org/current/musl" base-minimal base-devel
RUN rm -rf /system/var/cache/xbps/*
COPY void/basicimg-install.sh /system/usr/local/bin/basicimg-install
RUN basicimg-init-system "Void Linux (musl)"

FROM scratch
COPY --from=rootfs /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/sh", "-ec" ]
CMD [ "/bin/sh" ]
RUN basicimg-hello
