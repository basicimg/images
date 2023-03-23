# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:sid
RUN basicimg-install openjdk-8-jdk
CMD [ "/usrva" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
