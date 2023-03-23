FROM ghcr.io/basicimg/alpine:edge
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    apk add python3
ENTRYPOINT [ "/usr/bin/python" ]
RUN echo "Hello, $(python --version) on Alpine Edge!"