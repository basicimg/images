FROM ghcr.io/basicimg/arch
RUN --mount=type=cache,target=/system/var/cache,sharing=locked \
    pacman -Sy --noconfirm ruby
CMD [ "/usr/bin/ruby" ]
RUN basicimg-setapp "$(ruby -v 2>&1 | cut -d' ' -f-2) and gem $(gem -v)"