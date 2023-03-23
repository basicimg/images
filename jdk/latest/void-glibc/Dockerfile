# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:glibc
RUN basicimg-install openjdk17
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
