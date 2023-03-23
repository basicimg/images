FROM ghcr.io/basicimg/arch
RUN basicimg-install memcached
CMD [ "/usr/bin/memcached" ]
EXPOSE 11211
RUN basicimg-setapp "$(memcached --version)"
