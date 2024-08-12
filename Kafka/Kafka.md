# Apache Kafka Cheat Sheet

## Giới thiệu
Kafka là một nền tảng phân phối event trực tuyến. hoạt động dựa trên mô hình publish-subsribe. Các event (message) được các Producer publish vào các Topic và được consum từ các Consumer. Có khả năng chịu tải và chịu lỗi cao.

Kafka KRaft: mode mới giới thiệu từ kafka 6.0, sử dụng thuật toán đồng thuận Raft để quản lý metadata thay vì sử dụng zookeeper. Tăng độ tin cậy, khả năng mở rộng cao hơn, độ phức tạp thấp hơn.

## Các thành phần chính:

### Broker
Kafka broker là một server kafka, một cụm kafka bao gồm nhiều broker.

### Topic
Topic, dùng để lưu trữ các message, các message được gửi vào 1 Topic được phân loại và xử lý theo các quy tắc khác nhau.
Topic, 

### Partition
Partition, trong mỗi Topic có thể được chia thành nhiều partition. Partition là đơn vị lưu trữ "MẢNG" có thứ tự các message. Và được phân bố đều trên các broker.

Trong partition, mỗi message có offset duy nhất (~index) không thay đổi được, mỗi message thêm vào partition được thêm vào commit log. 

Một message được gửi đến Topic, nó sẽ được xác định partition thông qua thuật toán mã hóa hoặc round-robin, đảm bảo phân phối đều giữa các partition trong Topic.

Khi một consumer đăng ký nhận message từ 1 Topic, nó sẽ được Kafka chỉ định cho 1 consumer cụ thể, sau đó chỉ nhận message từ partition này.

Số lượng partition trong 1 Topic ? phụ thuộc nhiều yếu tố, lượng message, tốc độ xử lý, độ trễ, ...


### Message
Message (event).

### Replication
Kafka hỗ trợ replicate giữa các broker để đảm bảo H/A và mỗi partition có thể có 1 hoặc nhiều bản replicate trên các broker khác nhau.



### Producer

### Consumer

### Consumer Group

### Zookeeper
Zookeeper, 1 dịch vụ quản lý các dịch vụ phân tán.

Vai trò:
- Lưu trữ thông tin của kafka broker, topic, partition, ...
- Thực hiện leader election cho các partition () 
- Gửi thông tin đến kafka về các event hệ thống: new topic, delete topic, broker die, ...

Kafka có thể hoạt động mà không có zookeeper không ? có

Kafka sử dụng zookeeper để theo dõi metadata của các topic, partition và các broker.

Zookeeper theo dõi tình trạng hoạt động của các broker trong cụm , broker nào hoạt động, không hoạt động
Consumer muốn đọc message cần kết nối đến 1 broker, zookeeper giúp consumer tìm ra broker


### Documentation
#### Topics and logs
Kafka cluster lưu trữ lại tất cả message được publish cho dù chúng đã được consum hay chưa trong 1 khoảng thời gian (theo cấu hình).
MetaData duy nhất được giữ lại là offset, được kiểm soát bởi consumer, thông thường consumer sẽ tăng offset bằng cách đọc message tuy nhiên trong thực tế thì offset này do consumer kiểm soát và nó có thể sử dụng message theo thứ tự mà consumer muốn (có thể reset offset về vị trí cũ để xử lý lại khi cần). 

"Consumers are very cheap", tức là consumer không ảnh hưởng nhiều đến cluster và các consumer khác.

#### Distribution


### Các trường hợp có thể xảy ra khi 1 group consumer đọc message từ 1 topic:
#### 1. 4 partion - 1 consumer
Consumer sẽ consum toàn bộ message từ các partition.

#### 1. 4 partion - 2 consumer
Consumer 1 được chỉ định nhận message từ partition 0,2
Consumer 2 được chỉ định nhận message từ partition 1,3

* Kafka luôn đảm bảo mỗi message chỉ được đọc bởi một consumer duy nhất trong 1 group.
* Vì các message được lưu trữ trên các partition trong 1 Topic là khác nhau nên 2 consumer không bgio đọc cùng 1 message.

#### 1. 4 partion - n consumer (n>4)
Sẽ có 1 consumer bị bỏ không.

#### 1. 4 partion - 2 group consumer (4 and 2 consumer)
Nếu muốn chỉ định nhiều consumer đọc từ cùng 1 partition thì các consumer này cần nằm ở các group khác nhau.

### Q/A
- Có băt buộc phải có Group Consumer không ? Có, nếu không đặt groupId sẽ bị exeption.
- Khi một consumer mới tham gia vào group, partition được phân bổ ntn ? 
    Giả sử 1 Topic với 3 partition và 1 group gồm 2 consumer. Với mỗi partition được gán cho 1 consumer và 1 partition còn lại gán cho consumer khác.
        - case1: consumer mới được thêm vào group, 

## Các mô hình triển khai phổ biến
### SingleCluster (1 broker + 1 zookeeper)
Mô hình cơ bản có thể có 1 broker kafka hoặc 1 broker kafka + 1 zookeeper.

#### 1. 1 broker kafka:
```
version: "2"

services:
  kafka:
    image: docker.io/bitnami/kafka:3.7
    ports:
      - "9092:9092"
    volumes:
      - "kafka_data:/bitnami"
    environment:
      # KRaft settings
      - KAFKA_CFG_NODE_ID=0
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka:9093
      # Listeners
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
volumes:
  kafka_data:
    driver: local
```
env:
- KAFKA_CFG_NODE_ID: id node
- KAFKA_CFG_PROCESS_ROLES: vai trò của node
- KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: các controller voter, bao gồm id và địa chỉ controller
- KAFKA_CFG_LISTENERS: định nghĩa các listener cho kafka
- KAFKA_CFG_ADVERTISED_LISTENERS: định nghĩa các listeners broadcast ra ngoài
- KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: các giao thức bảo mật cho các listener
- KAFKA_CFG_CONTROLLER_LISTENER_NAMES: tên các listener cho controller
- KAFKA_CFG_INTER_BROKER_LISTENER_NAME: tên các listener dùng giao tiếp giữa các broker



#### 2. 1 broker kafka + 1 zookeeper:
```
version: "2"

services:
  zookeeper:
    image: docker.io/bitnami/zookeeper:3.9
    ports:
      - "2181:2181"
    volumes:
      - "zookeeper_data:/bitnami"
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
  kafka:
    image: docker.io/bitnami/kafka:3.4
    ports:
      - "9092:9092"
    volumes:
      - "kafka_data:/bitnami"
    environment:
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
    depends_on:
      - zookeeper

volumes:
  zookeeper_data:
    driver: local
  kafka_data:
    driver: local
```

### Cluster:

#### 1. 3 broker kafka:
```
# Copyright Broadcom, Inc. All Rights Reserved.
# SPDX-License-Identifier: APACHE-2.0

version: "2"

services:
  kafka-0:
    image: docker.io/bitnami/kafka:3.7
    ports:
      - "9092"
    environment:
      # KRaft settings
      - KAFKA_CFG_NODE_ID=0
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
      - KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
      # Listeners
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
      # Clustering
      - KAFKA_CFG_OFFSETS_TOPIC_REPLICATION_FACTOR=3
      - KAFKA_CFG_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=3
      - KAFKA_CFG_TRANSACTION_STATE_LOG_MIN_ISR=2
    volumes:
      - kafka_0_data:/bitnami/kafka
  kafka-1:
    image: docker.io/bitnami/kafka:3.7
    ports:
      - "9092"
    environment:
      # KRaft settings
      - KAFKA_CFG_NODE_ID=1
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
      - KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
      # Listeners
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
      # Clustering
      - KAFKA_CFG_OFFSETS_TOPIC_REPLICATION_FACTOR=3
      - KAFKA_CFG_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=3
      - KAFKA_CFG_TRANSACTION_STATE_LOG_MIN_ISR=2
    volumes:
      - kafka_1_data:/bitnami/kafka
  kafka-2:
    image: docker.io/bitnami/kafka:3.7
    ports:
      - "9092"
    environment:
      # KRaft settings
      - KAFKA_CFG_NODE_ID=2
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093,2@kafka-2:9093
      - KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
      # Listeners
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
      # Clustering
      - KAFKA_CFG_OFFSETS_TOPIC_REPLICATION_FACTOR=3
      - KAFKA_CFG_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=3
      - KAFKA_CFG_TRANSACTION_STATE_LOG_MIN_ISR=2
    volumes:
      - kafka_2_data:/bitnami/kafka

volumes:
  kafka_0_data:
    driver: local
  kafka_1_data:
    driver: local
  kafka_2_data:
    driver: local
```


#### 2. KRaft cluster:
```
version: '2'

services:
  kafka-combined:
    image: docker.io/bitnami/kafka:latest
    ports:
      - "9092:9092"
    environment:
      - KAFKA_CFG_NODE_ID=0
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
    volumes:
      - kafka_0_data:/bitnami/kafka
  kafka-controller:
    image: docker.io/bitnami/kafka:latest
    environment:
      - KAFKA_CFG_NODE_ID=1
      - KAFKA_CFG_PROCESS_ROLES=controller
      - KAFKA_CFG_LISTENERS=CONTROLLER://:9093
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv
    volumes:
      - kafka_1_data:/bitnami/kafka
  kafka-broker:
    image: docker.io/bitnami/kafka:latest
    environment:
      - KAFKA_CFG_NODE_ID=2
      - KAFKA_CFG_PROCESS_ROLES=broker
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-0:9093,1@kafka-1:9093
    volumes:
      - kafka_2_data:/bitnami/kafka

volumes:
  kafka_0_data:
    driver: local
  kafka_1_data:
    driver: local
  kafka_2_data:
    driver: local
```




## Backup - Restore:

## Xác thực trong Kafka:
Sử dụng SASL 

## Common Commands

### Kafka Topics

- **List topics**
    ```sh
    kafka-topics.sh --list --bootstrap-server localhost:9092
    ```

- **Create a topic**
    ```sh
    kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
    ```

- **Describe a topic**
    ```sh
    kafka-topics.sh --describe --topic my-topic --bootstrap-server localhost:9092
    ```

- **Delete a topic**
    ```sh
    kafka-topics.sh --delete --topic my-topic --bootstrap-server localhost:9092
    ```

### Kafka Producers

- **Send messages to a topic from the console**
    ```sh
    kafka-console-producer.sh --topic my-topic --bootstrap-server localhost:9092
    ```

    Type messages and hit Enter to send them.

### Kafka Consumers

- **Consume messages from a topic from the console**
    ```sh
    kafka-console-consumer.sh --topic my-topic --from-beginning --bootstrap-server localhost:9092
    ```
  
- **Get list consumer groups**
  ```sh
  kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
  ```

- **Create consumer groups**
  ```sh
  kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my_topic --group my_consumer_group
  ```

Không thể tạo trực tiếp 1 consumer group, mà trong Kafka consumer group được tạo ra khi một Client bắt đầu đăng kí nhận event từ 1 topic.


### Kafka Broker

- **Start a Kafka broker**
    ```sh
    kafka-server-start.sh config/server.properties
    ```

- **Stop a Kafka broker**
    ```sh
    kafka-server-stop.sh
    ```

### kafka Config

- **Config set retention time**
  ```
  kafka-configs.sh --bootstrap-server localhost:9092 --alter --entity-type topics --entity-name my-topic --add-config retention.ms=86400000
  ```

## GUIDELINE:
### publish message key - without key:
- khi publish message với key, key sẽ xác định partition message được gửi đến --> các message cùng key được phân phối đến cùng một partition, giữ thứ tự của chúng trong đó.
- khi publish message không có key, Kafka sẽ tự động chọn partition theo round-robin, hoặc random. 

--> Có key: khi cần đảm bảo thứ tự các message liên quan đến cùng một Topic, hoặc khi muốn message được route đến 1 partition cụ thể
Không có key: Đơn giản hóa quá trình publish message lên kafka, thứ tự của các message không quan trọng.




docker run -d --name kafka \
  --network app-tier \
  -e KAFKA_ENABLE_KRAFT=yes \
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
  -e KAFKA_CFG_BROKER_ID=0 \
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@10.60.65.90:9093,1@10.60.65.91:9093,2@10.60.65.92:9093 \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://10.60.65.90:9092 \
  -e ALLOW_PLAINTEXT_LISTENER=yes \
  -e KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv \
  -e KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -e KAFKA_CFG_NODE_ID=0 \
  -p 9092:9092 \
  -p 9093:9093 \
  bitnami/kafka:latest

docker run -d --name kafka \
  --network app-tier \
  -e KAFKA_ENABLE_KRAFT=yes \
  -e KAFKA_CFG_BROKER_ID=1 \
  -e KAFKA_CFG_NODE_ID=1 \
  -e KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv \
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@10.60.65.90:9093,1@10.60.65.91:9093,2@10.60.65.92:9093 \
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
  -e ALLOW_PLAINTEXT_LISTENER=yes \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://10.60.65.91:9092 \
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -p 9092:9092 \
  -p 9093:9093 \
  bitnami/kafka:latest

docker run -d --name kafka \
  --network app-tier \
  -e KAFKA_ENABLE_KRAFT=yes \
  -e KAFKA_CFG_BROKER_ID=2 \
  -e KAFKA_CFG_NODE_ID=2 \
  -e KAFKA_KRAFT_CLUSTER_ID=abcdefghijklmnopqrstuv \
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@10.60.65.90:9093,1@10.60.65.91:9093,2@10.60.65.92:9093 \
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
  -e ALLOW_PLAINTEXT_LISTENER=yes \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://10.60.65.92:9092 \
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
  -e KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -p 9092:9092 \
  -p 9093:9093 \
  bitnami/kafka:latest


| master | 172.29.68.182 |
| slave | 172.29.66.105 |
| slave | 172.29.67.25 |
10.60.65.90, 10.60.65.91, 10.60.65.92


// single node
docker run -d \
  --network app-tier \
  --name kafka \
  -e KAFKA_CFG_NODE_ID=0 \
  -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
  -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka:9093 \
  -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
  -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://:9092 \
  -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
  -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
  -e KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
  -p 9092:9092 \
  -p 9093:9093 \
  bitnami/kafka:latest