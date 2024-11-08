# backup - restore in kafka

## 1. backup 
### 1.1. by tmp container (failed)
- stop container kafka: ```docker stop database```
- backup thông qua 1 container khác từ image busybox: ```docker run --rm -v /path/to/kafka-backups:/backups --volumes-from kafka busybox cp -a /bitnami/kafka /backups/latest```

- -> chạy con temporary container (busybox), mount các volumes của container **database** , cho phép truy cập vào dữ liệu của **kafka**. Đồng thời mount 1 folder từ máy host (```/path/to/kafka-backups```) vào thư mục trong container temporary (```/backups```). Sao chép toàn bộ dữ liệu **kafka** từ: ```/bitnami/kafka``` sang :```/backups/lates```. sau khi backup dữ liệu, xóa container temporary ( --rm )

- -> sau quá trình backup, ở thư mục: ```/path/to/kafka-backups``` ngoài máy host, sẽ có dữ liệu backup từ kafka.

### 1.2. by kafka-backup:
```
docker run -d -v /Data/Data/kafka-backup/:/kafka-backup/ --rm \
    itadventurer/kafka-backup:v0.1.1 \
    backup-standalone.sh --bootstrap-server 172.26.0.2:9092 \
    --target-dir /kafka-backup/ --topics 'my-topic,my-topic-1'
```

## 2. restore



