FROM ghcr.io/basicimg/debian:buster
RUN --mount=type=cache,target=/var/cache,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get --no-install-recommends install -y python3
RUN ln -s /usr/bin/python3 /usr/local/bin/python
ENTRYPOINT [ "/usr/local/bin/python" ]
RUN echo "Hello, $(python3 --version) on Debian Buster!"