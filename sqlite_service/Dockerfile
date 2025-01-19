FROM alpine:latest
RUN apk update && apk add sqlite
COPY init.sql .
WORKDIR /db