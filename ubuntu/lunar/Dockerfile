# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN ln -s /usr/share/debootstrap/scripts/gutsy /usr/share/debootstrap/scripts/lunar
RUN debootstrap --variant=minbase --components=main,universe --include=build-essential lunar /system https://mirror.fcix.net/ubuntu/
RUN chroot /system apt-get clean
RUN rm -rf /system/var/lib/apt/lists/*
COPY debian/basicimg-install.sh /system/usr/local/bin/basicimg-install
RUN basicimg-init-system 'Ubuntu 23.04 "Lunar Lobster"'

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/bash", "-ec" ]
CMD [ "/bin/bash" ]
RUN basicimg-hello
