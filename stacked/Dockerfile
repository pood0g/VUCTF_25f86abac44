FROM debian:latest
RUN mkdir /app
COPY stacked /app
COPY stacked /app
COPY docker-entrypoint.sh /
RUN chmod 777 /docker-entrypoint.sh
WORKDIR /app
RUN apt update
RUN apt install -y socat
EXPOSE 1337
USER daemon
ENTRYPOINT [ "/docker-entrypoint.sh" ]