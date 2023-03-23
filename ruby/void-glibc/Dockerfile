# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S ruby
CMD [ "/usr/bin/ruby" ]
RUN basicimg-setapp "$(ruby -v 2>&1 | cut -d' ' -f-2) and gem $(gem -v)"