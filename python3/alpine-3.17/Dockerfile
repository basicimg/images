# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:3-17
RUN basicimg-install python3 python3-dev
CMD [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"
