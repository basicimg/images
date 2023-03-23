# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:edge
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add ruby 
CMD [ "/usr/bin/ruby" ]
RUN basicimg-setapp "$(ruby -v 2>&1 | cut -d' ' -f-2) and gem $(gem -v)"