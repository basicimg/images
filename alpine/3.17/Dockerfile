# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    apk \
    --repository https://dl-cdn.alpinelinux.org/alpine/v3.17/main/ \
    --allow-untrusted --root /system --initdb \
    add alpine-base
RUN touch /system/basicimg
COPY alpine/repositories /system/etc/apk/repositories
COPY alpine/3.17/repositories .
RUN cat repositories >> /system/etc/apk/repositories

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PAGER=less
SHELL [ "/bin/sh", "-c" ]
CMD [ "/bin/sh" ]
RUN echo "Hello, Alpine 3.17!"