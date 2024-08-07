FROM bitnami/redis-cluster:7.0

WORKDIR /

USER root

RUN apt-get update \
    &&  apt-get install -y python3.11 python3-pip python3-dev build-essential --no-install-recommends

RUN apt-get install -y vim

RUN pip3 install rdbtools python-lzf --break-system-packages

RUN sed -i 's/if version < 1 or version > 9:/if version < 1 or version > 12:/' /usr/local/lib/python3.11/dist-packages/rdbtools/parser.py

COPY restore.sh /home/restore.sh

RUN chmod +x /home/restore.sh

COPY restore_txt.sh /home/restore_txt.sh

RUN chmod +x /home/restore_txt.sh

