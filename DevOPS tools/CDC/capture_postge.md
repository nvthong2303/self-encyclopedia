# Track every PostgreSQL data change using Debezium

- Gồm 3 thành phần: postgresql / kafka / connector:
```
version: '3.7'


networks:
   cdc-using-debezium-network:
       name: cdc-using-debezium-network
       driver: bridge
       external: false


services:
   cdc-using-debezium-postgres:
       image: debezium/postgres:11
       container_name: cdc-using-debezium-postgres
       hostname: cdc-using-debezium-postgres
       restart: always
       ports:
           - '5443:5432'
       environment:
           POSTGRES_PASSWORD: 123
           POSTGRES_USER: postgres
           POSTGRES_DB: cdc-using-debezium
       volumes:
           - 'cdc-using-debezium-postgres-data:/var/lib/postgresql/data'
       networks:
           - cdc-using-debezium-network


   cdc-using-debezium-kafka:
       image: bitnami/kafka:3.4
       container_name: cdc-using-debezium-kafka
       hostname: cdc-using-debezium-kafka
       restart: always
       ports:
           - '9092:9092'
       environment:
           KAFKA_CFG_NODE_ID: 1
           KAFKA_KRAFT_CLUSTER_ID: q0k00yjQRaqWmAAAZv955w # base64 UUID
           KAFKA_CFG_PROCESS_ROLES: controller,broker
           KAFKA_CFG_LISTENERS: INTERNAL://cdc-using-debezium-kafka:29092,CONTROLLER://cdc-using-debezium-kafka:29093,EXTERNAL://0.0.0.0:9092
           KAFKA_CFG_ADVERTISED_LISTENERS: INTERNAL://cdc-using-debezium-kafka:29092,EXTERNAL://localhost:9092
           KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
           KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: 1@cdc-using-debezium-kafka:29093
           KAFKA_CFG_INTER_BROKER_LISTENER_NAME: INTERNAL
           KAFKA_CFG_CONTROLLER_LISTENER_NAMES: CONTROLLER
       networks:
           - cdc-using-debezium-network


   cdc-using-debezium-connect:
       image: debezium/connect:2.3
       container_name: cdc-using-debezium-connect
       hostname: cdc-using-debezium-connect
       restart: always
       ports:
           - '8083:8083'
       environment:
           BOOTSTRAP_SERVERS: cdc-using-debezium-kafka:29092
           GROUP_ID: 1
           CONFIG_STORAGE_TOPIC: my_connect_configs
           OFFSET_STORAGE_TOPIC: my_connect_offsets
           STATUS_STORAGE_TOPIC: my_connect_statuses
           ENABLE_DEBEZIUM_SCRIPTING: 'true'
       links:
           - cdc-using-debezium-kafka
           - cdc-using-debezium-postgres
       networks:
           - cdc-using-debezium-network


volumes:
   cdc-using-debezium-postgres-data:
       name: cdc-using-debezium-postgres-data
       driver: local
```

- Verify PostgreSQL: ```docker exec cdc-using-debezium-postgres psql --username=postgres --dbname=cdc-using-debezium --command='SHOW wal_level'```
```
 wal_level 
-----------
 logical
(1 row)
```
- ```docker exec cdc-using-debezium-postgres psql --username=postgres --dbname=cdc-using-debezium --command='SHOW shared_preload_libraries'```
```
 shared_preload_libraries 
--------------------------
 decoderbufs,wal2json
(1 row)
```

- Verify Kafka: ```curl localhost:8083 | jq '.'```
```
{
  "version": "3.4.0",
  "commit": "2e1947d240607d53",
  "kafka_cluster_id": "q0k00yjQRaqWmAAAZv955w"
}
```

- Deploy connector cho Postgres:
```
curl --location 'http://localhost:8083/connectors' \
   --header 'Accept: application/json' \
   --header 'Content-Type: application/json' \
   --data '{
   "name": "cdc-using-debezium-connector",
   "config": {
       "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
       "database.hostname": "127.0.0.1",
       "database.port": "5443",
       "database.user": "postgres",
       "database.password": "123",
       "database.dbname": "cdc-using-debezium",
       "database.server.id": "184054",
       "table.include.list": "public.User",
       "topic.prefix": "cdc-using-debezium-topic"
   }
}'
```


- Monitor database changes
- Get capture from kafka

- following: https://dev.to/emtiajium/track-every-postgresql-data-change-using-debezium-5e19