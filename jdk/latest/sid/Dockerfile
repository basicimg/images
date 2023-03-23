# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:sid
RUN basicimg-install openjdk-19-jdk
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
