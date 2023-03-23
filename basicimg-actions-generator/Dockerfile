# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/python3
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y python3-yaml
RUN mkdir /app
WORKDIR /app
COPY basicimg-actions-generator/ .
RUN chmod +x generate.py
RUN basicimg-setapp "basicimg-actions-generator"
VOLUME [ "/repo" ]
WORKDIR /repo
CMD [ "/app/generate.py" ]