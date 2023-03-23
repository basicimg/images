# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bookworm
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y nix-bin
COPY nix/nix.conf /etc/nix/nix.conf
RUN mkdir -p /nix && chown -R root:root /nix
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
CMD [ "/usr/bin/nix" ]
RUN basicimg-setapp "$(nix --version)"