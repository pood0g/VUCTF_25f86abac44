FROM alpine:latest
RUN apk update
RUN apk add py3-flask
COPY /app /app
WORKDIR /app
USER daemon
ENV FLASK_ENV=prod
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
