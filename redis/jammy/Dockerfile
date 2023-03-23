# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/ubuntu:jammy
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y redis
RUN basicimg-setapp "$(redis-server --version)"