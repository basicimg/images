# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/ubuntu:kinetic
RUN basicimg-install openjdk-8-jdk
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
