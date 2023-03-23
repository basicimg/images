# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:edge
RUN basicimg-install python3 python3-dev
CMD [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"
