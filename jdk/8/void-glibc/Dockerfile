# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN basicimg-install openjdk8
CMD [ "/usrva" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
