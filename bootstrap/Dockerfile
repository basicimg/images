# syntax=docker/dockerfile:1
FROM alpine:3.17.2@sha256:ff6bdca1701f3a8a67e328815ff2346b0e4067d32ec36b7992c1fdc001dc8517 AS bootstrap
RUN apk \
    --repository https://mirror.fcix.net/alpine/edge/main/ \
    --repository https://mirror.fcix.net/alpine/edge/community/ \
    --repository https://mirror.fcix.net/alpine/edge/testing/ \
    --allow-untrusted --root /system --initdb \
    add --no-cache alpine-base wget debootstrap binutils zstd pacman arch-install-scripts
RUN mkdir -p /system/system
RUN mkdir -m 1777 -p /system/tmp
COPY scripts/* /usr/local/bin/
RUN chmod +x /usr/local/bin/basicimg-*
RUN basicimg-init-system "bootstrap"

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PAGER=less
SHELL [ "/bin/sh", "-ec" ]
CMD [ "/bin/sh" ]
WORKDIR /tmp
