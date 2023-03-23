# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/void:musl
RUN basicimg-install python3 python3-devel
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
CMD [ "/opt/venv/bin/python" ]
RUN basicimg-setapp "$(python --version)"
