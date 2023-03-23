FROM ghcr.io/basicimg/arch
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    pacman -Sy --noconfirm python
CMD [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"