# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/python3
RUN basicimg-install python3-yaml
RUN mkdir /app
WORKDIR /app
COPY basicimg-actions-generator/ .
RUN chmod +x generate.py
RUN basicimg-setapp "basicimg-actions-generator"
VOLUME [ "/repo" ]
WORKDIR /repo
CMD [ "/app/generate.py" ]
