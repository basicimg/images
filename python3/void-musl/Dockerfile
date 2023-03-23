# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:musl
RUN basicimg-install python3 python3-devel
CMD [ "/usr/bin/python" ]
RUN basicimg-setapp "$(python --version)"
