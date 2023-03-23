# syntax=docker/dockerfile:1
FROM ghcr.io/basicimg/debian:bookworm
RUN basicimg-install ruby
CMD [ "/usr/bin/ruby" ]
RUN basicimg-setapp "$(ruby -v 2>&1 | cut -d' ' -f-2) and gem $(gem -v)"
