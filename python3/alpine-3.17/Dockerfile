# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/alpine:3-17
RUN basicimg-install python3 python3-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
CMD [ "/opt/venv/bin/python" ]
RUN basicimg-setapp "$(python --version)"
