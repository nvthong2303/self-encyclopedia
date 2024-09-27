# Debezium:
- Opensource triển khai các ứng dụng xử lý flow dữ liệu realtime.
- Hoạt động như một connector, kết nối với các csdl bằng cách sử dụng log và trigger khi dữ liệu có sự thay đổi (INSERT, DELETE, UPDATE, TRUNCAT)
- Thường sử dụng kèm với Kafka connect và đóng vai trò như một connector trong kafka. Những event (INSERT, UPDATE, DELETE) được Debezium connectors gửi đến kafka và được sử dụng cho nhiều service khác nhau.
- Hỗ trợ tương đối đầy đủ các loại csdl phổ biến, mỗi loại có cách kết nối khác nhau nhưng hầu như debezium đều dựa trên logs.
    - PostgreSQL: sử dụng WAL (Write-Ahead Logging) để theo dõi sự thay đổi dữ liệu. WAL là một bản ghi liên tục của tất cả các thay đổi đối với csdl. Debezium đọc WAL và chuyển các thay đổi thành các luồng dữ liệu.
    - MongoDB: Oplog (Operations Log), Debezium sử dụng Oplog để theo dõi các thay đổi trong db và chuyển các thay đổi thành luồng dữ liệu. Oplog là bản ghi liên tục của tất cả các thay đổi CRUD được thực hiện trong database.
    - MySQL: BinLog (Binary Log)
    - SQL Server: CDC (Change Data Capture)
    - Oracle: LogMiner
    - Db2: CDC
    - Cassandra: CDC
    - ...

## Debezium engine: 
- Có hỗ trợ bộ debezium-api

## Ứng dụng:
- Dùng làm CDC, Datalake, ETL, ...

## Change Data Capture:
- 

