FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y curl

COPY setup.sh /workspace/setup.sh
RUN chmod +x /workspace/setup.sh

WORKDIR /workspace

RUN ./setup.sh