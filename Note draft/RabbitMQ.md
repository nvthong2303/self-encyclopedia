# RabbitMQ Cheat Sheet

## Giới thiệu

RabbitMQ là một phần mềm phần mềm trung gian (message broker) mã nguồn mở. Nó được sử dụng để xử lý, gửi và nhận các tin nhắn từ ứng dụng, giúp các ứng dụng khác nhau có thể giao tiếp với nhau theo kiểu phân tán.

## Các thành phần chính:

- **Message Broker**: Là một dịch vụ phần mềm hoặc server trung gian nhận và chuyển tiếp các tin nhắn giữa các ứng dụng và hệ thống.
- **Exchange**: Nơi nhận mesage từ các producer và đẩy chúng vào queue dựa trên các quy tắc của từng loại Exchange. Để nhận được message, queue phải nằm trong ít nhất 1 exchange.
- **Queue**: Là nơi mà các tin nhắn được lưu trữ trước khi được consum.
- **Binding**: Liên kết giữa Exchange và Queue.
- **Producer**: 
- **Consumer**: 
- **Channel**: Một kết nối ảo trong một connection, việc publish hoặc consum từ 1 queue đều được thực hiện trên channel.
- **Routing key**: Key mà Exchange dựa vào đó để quyết định cách để định tuyến cho message đến queue (~địa chỉ dành cho message).
- **AMQP**: Giao thức truyền message bên trong RabbitMQ.

## Các mô hình triển khai phổ biến
## Backup - Restore:
## Xác thực trong Kafka:

## Common Commands

### RabbitMQ Command Line Tools

#### 1. rabbitmqctl

- **Start RabbitMQ Server**:
```bash
  rabbitmq-server start
```

- **Stop RabbitMQ Server:**:
```bash
  rabbitmq-server stop
```

- **List All Queues:**:
```bash
  rabbitmq-server list_queue
```

- **List Exchanges**:
```bash
  rabbitmq-server list_exchanges
```

- **List Bindings**:
```bash
  rabbitmq-server list_bindings
```

#### 2. rabbitmq-pluggin:

- **Enable a Plugin**:
```bash
  rabbitmq-plugins enable <plugin-name>
```

- **Disable a Plugin**:
```bash
  rabbitmq-plugins disable <plugin-name>
```




## GUILD:
### Luồng message:

### Các loại Exchanges:

direct, topic, fanout, and header exchanges


### So sánh RabbitMQ - Kafka (https://www.cloudamqp.com/blog/when-to-use-rabbitmq-or-apache-kafka.html)
- RabbitMQ là message broker , Kafka là message bus (tối ưu hóa cho các luồng dữ liệu có tốc độ truy cập cao, được phát lại)
- RabbitMQ dùng kết nối các ứng dụng, cho các tác vụ dài hạn và đáng tin cậy, Kafka dùng cho các tác vụ có lưu trữ lại dữ liệu, phân tích dữ liệu và đọc (phát) lại.
- RabbitMQ message được lưu cho đến khi được consum (ACK), Kafka mesage được lưu trữ sau 1 khoảng thời gian được config 
- RabbitMQ có hỗ trợ độ ưu tiên message còn Kafka thì không
- RabbitMQ hỗ trợ định tuyến message dễ dàng còn Kafka thì không.

