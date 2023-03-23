# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bookworm
RUN basicimg-install openjdk-17-jdk
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
