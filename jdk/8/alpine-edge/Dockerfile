# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:edge
RUN basicimg-install openjdk8@community
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
