# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:sid
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y nginx
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
 && ln -sf /dev/stderr /var/log/nginx/error.log
CMD [ "/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;" ]
EXPOSE 80
RUN basicimg-setapp "$(nginx -v 2>&1 | cut -d' ' -f3-)"