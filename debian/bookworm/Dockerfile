# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/bootstrap:latest AS bootstrap
RUN debootstrap --variant=minbase --components=main,contrib --include=build-essential bookworm /system https://deb.debian.org/debian/
RUN chroot /system apt-get clean
RUN rm -rf /system/var/lib/apt/lists/*
COPY debian/basicimg-install.sh /system/usr/local/bin/basicimg-install
RUN basicimg-init-system 'Debian 12 "Bookworm"'

FROM scratch
COPY --from=bootstrap /system/ /
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL [ "/bin/bash", "-ec" ]
CMD [ "/bin/bash" ]
RUN basicimg-hello
