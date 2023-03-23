# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:buster
RUN basicimg-install nodejs npm yarnpkg
CMD [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarnpkg --version)"
