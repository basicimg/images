# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN basicimg-install nix
COPY nix/nix.conf /etc/nix/nix.conf
RUN chown -R root:root /nix
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
CMD [ "/usr/bin/nix" ]
RUN basicimg-setapp "$(nix --version)"
