# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:buster
RUN basicimg-install python3 python3-dev python3-venv
RUN ln -s /usr/bin/python3 /usr/local/bin/python
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
CMD [ "/opt/venv/bin/python" ]
RUN basicimg-setapp "$(python --version)"
