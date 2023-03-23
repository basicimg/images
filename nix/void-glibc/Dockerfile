# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    xbps-install --reproducible --yes -S nix
COPY nix/nix.conf /etc/nix/nix.conf
RUN chown -R root:root /nix
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
CMD [ "/usr/bin/nix" ]
RUN basicimg-setapp "$(nix --version)"