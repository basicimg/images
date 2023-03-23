FROM ghcr.io/basicimg/arch
RUN basicimg-install jdk11-openjdk
CMD [ "/usr/bin/java" ]
RUN basicimg-setapp "$(java -version 2>&1 | head -n 1)"
