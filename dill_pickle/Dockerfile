FROM alpine:latest
RUN apk update
RUN apk add py3-flask
COPY /app /app
# CMD chmod -R -w /app
USER daemon
EXPOSE 5000
WORKDIR /app
ENV FLASK_ENV=prod
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
