# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/arch
RUN basicimg-install jdk-openjdk
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
