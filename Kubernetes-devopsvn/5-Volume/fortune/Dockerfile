FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y fortune && \
    apt-get clean

RUN mkdir -p /var/htdocs

COPY fortune.sh /usr/local/bin/fortune.sh

RUN chmod +x /usr/local/bin/fortune.sh

WORKDIR /var/htdocs

CMD ["/usr/local/bin/fortune.sh"]
