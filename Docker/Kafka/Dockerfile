FROM busybox:1.36.1 as file
RUN wget https://repo.maven.apache.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/1.0.1/jmx_prometheus_javaagent-1.0.1.jar
FROM docker.io/bitnami/kafka:3.7
COPY --link --from=file /jmx_prometheus_javaagent-1.0.1.jar /jmx/jmx_prometheus_javaagent-1.0.1.jar
COPY <<EOF /jmx/config.yaml
lowercaseOutputName: true
rules:
- pattern: ".*"
EOF

# docker run -it --hostname kafka-server \
#       -p 9092:9092 -p 9093:9093 -p 2020:2020 -p 7071:7071 \
#     -e KAFKA_CFG_NODE_ID=0 \
#     -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
#     -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
#     -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
#     -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-server:9093 \
#     -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
#     -e JMX_PORT=2020 \
#     -e EXTRA_ARGS=-javaagent:/jmx/jmx_prometheus_javaagent-1.0.1.jar=7071:/jmx/config.yaml \
#     test
# jmx port: 2020
# curl http://<IP>:7071/metrics