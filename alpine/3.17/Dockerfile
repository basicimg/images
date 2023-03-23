# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN apk \
    --repository https://mirror.fcix.net/alpine/v3.17/main/ \
    --allow-untrusted --root /system --initdb \
    add --no-cache alpine-base alpine-sdk
COPY arch/basicimg-install.sh /system/usr/local/bin/basicimg-install
RUN basicimg-init-system "Alpine 3.17"
COPY alpine/repositories /system/etc/apk/repositories
COPY alpine/3.17/repositories .
RUN cat repositories >> /system/etc/apk/repositories

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PAGER=less
SHELL [ "/bin/sh", "-ec" ]
CMD [ "/bin/sh" ]
RUN basicimg-hello
