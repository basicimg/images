FROM ghcr.io/basicimg/arch
RUN basicimg-install nodejs npm
RUN corepack enable
CMD [ "/usr/bin/node" ]
RUN basicimg-setapp "Node.js $(node --version) with npm $(npm --version) and yarn $(yarn --version)"
