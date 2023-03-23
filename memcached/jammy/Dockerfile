# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/ubuntu:jammy
RUN basicimg-install memcached
CMD [ "/usr/bin/memcached" ]
EXPOSE 11211
RUN basicimg-setapp "$(memcached --version)"
