# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/arch
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    pacman -Sy --noconfirm nix
COPY nix/nix.conf /etc/nix/nix.conf
RUN chown -R root:root /nix
ENV PATH="${PATH}:/nix/var/nix/profiles/default/bin"
CMD [ "/usr/bin/nix" ]
RUN basicimg-setapp "$(nix --version)"