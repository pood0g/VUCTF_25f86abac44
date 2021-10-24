FROM debian:latest
RUN mkdir /app
COPY funk32-serv /app
COPY funk64-serv /app
COPY docker-entrypoint.sh /
RUN chmod 777 /docker-entrypoint.sh
WORKDIR /app
RUN apt update
RUN apt install -y libc6-i386 socat
EXPOSE 1337
USER daemon
ENTRYPOINT [ "/docker-entrypoint.sh" ]