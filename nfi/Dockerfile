FROM alpine:latest
RUN apk update
RUN apk add py3-flask iputils py3-waitress
COPY /app /app
RUN chown daemon:daemon /app/logs
USER daemon
EXPOSE 5000
WORKDIR /app
ENV FLASK_ENV=prod
ENTRYPOINT ["python3", "/app/app.py"]
