FROM alpine:latest

RUN apk add --no-cache netcat-openbsd

COPY dados.csv /dados.csv
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]