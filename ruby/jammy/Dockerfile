# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/ubuntu:jammy
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y ruby
CMD [ "/usr/bin/ruby" ]
RUN basicimg-setapp "$(ruby -v 2>&1 | cut -d' ' -f-2) and gem $(gem -v)"