#!/bin/sh

# Cria o pipe (ignora erro se já existir)
PIPE=/tmp/pipe
[ -p "$PIPE" ] || mkfifo "$PIPE"

# Loop em background que envia o conteúdo do CSV para o pipe com intervalo
(
  while true; do
    while read line; do
      echo "[LOG] Enviando: $line" >&2
      echo "$line"
      sleep 1
    done < /dados.csv
  done > "$PIPE"
) &

# Stream contínuo do pipe para a porta 9999
cat "$PIPE" | nc -lk -p 9999
