# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bullseye
RUN basicimg-install nix-bin
COPY nix/nix.conf /etc/nix/nix.conf
RUN mkdir -p /nix && chown -R root:root /nix
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
CMD [ "/usr/bin/nix" ]
RUN basicimg-setapp "$(nix --version)"
