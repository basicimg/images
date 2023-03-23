# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:musl
RUN basicimg-install memcached
CMD [ "/usr/bin/memcached" ]
EXPOSE 11211
RUN basicimg-setapp "$(memcached --version)"
