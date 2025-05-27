FROM rust:slim

RUN apt update && apt install -y curl build-essential pkg-config libssl-dev && \
    cargo install websocat

CMD ["websocat"]