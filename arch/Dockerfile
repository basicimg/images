# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN mkdir -m 0755 -p /system/var/lib/pacman /system/var/log /system/dev /system/run /system/etc/pacman.d
RUN mkdir -m 1777 -p /system/tmp
RUN mkdir -m 0555 -p /system/sys /system/proc
COPY arch/mirrorlist /system/etc/pacman.d/mirrorlist
COPY arch/pacman.conf .
RUN wget https://mirror.fcix.net/archlinux/core/os/x86_64/archlinux-keyring-20230320-1-any.pkg.tar.zst
RUN pacman -U --noconfirm --assume-installed pacman archlinux-keyring-20230320-1-any.pkg.tar.zst
RUN pacman-key --gpgdir /system/etc/pacman.d/gnupg --init
RUN pacman-key --gpgdir /system/etc/pacman.d/gnupg --populate
RUN pacman --config=pacman.conf -r /system -Sy --noconfirm base base-devel
RUN rm -rf /var/cache/pacman/*
COPY arch/basicimg-install.sh /system/usr/local/bin/basicimg-install
RUN basicimg-init-system "Arch Linux"

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/bash", "-ec" ]
CMD [ "/bin/bash" ]
RUN basicimg-hello
