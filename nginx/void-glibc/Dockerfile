# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
 && ln -sf /dev/stderr /var/log/nginx/error.log
CMD [ "/usr/bin/nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;" ]
EXPOSE 80
RUN basicimg-setapp "$(nginx -v 2>&1 | cut -d' ' -f3-)"