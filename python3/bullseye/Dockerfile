# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bullseye
RUN basicimg-install python3-full python3-dev python-is-python3
CMD [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"
