# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:sid
RUN basicimg-install python3-full python3-dev python-is-python3
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
CMD [ "/opt/venv/bin/python" ]
RUN basicimg-setapp "$(python --version)"
