# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:buster
RUN basicimg-install python3 python3-dev
RUN ln -s /usr/bin/python3 /usr/local/bin/python
CMD [ "/usr/local/bin/python" ]
RUN basicimg-setapp "$(python --version)"
