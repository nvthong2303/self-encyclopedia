FROM bitnami/redis-cluster:7.2

WORKDIR /app

USER root

RUN apt-get update \
 && apt-get install --assume-yes --no-install-recommends --quiet \
        python3 \
        python3-pip \
 && apt-get clean all

RUN pip install --no-cache --upgrade pip setuptools

RUN pip --version  # just for test
