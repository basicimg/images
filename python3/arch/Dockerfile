FROM ghcr.io/basicimg/arch
RUN basicimg-install python
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
CMD [ "/opt/venv/bin/python" ]
RUN basicimg-setapp "$(python --version)"
