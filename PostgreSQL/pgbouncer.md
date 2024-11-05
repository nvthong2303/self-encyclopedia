# PGBouncer


## Connection Pooling:
- PostgreSQL có kiến trúc xử lý khá nặng, đối với mỗi kết nối đến postmaster (daemon Postgre) đưa ra một process mới để xử lý. --> ổn định và cô lập tốt hơn nhưng khong hiệu quả trong việc xử lý các kết nối có tuổi thọ ngắn. (Mỗi kết nối đến bao gồm thiết lập TCP, tạo process và khởi tạo BE, tốn nhiều tài nguyên và thời gian hệ thống)
- Sử dụng connection pooling giải quyết vấn đề các kết nối khởi tạo quá thường xuyên, bị loại bỏ mà không sử dụng lại.

## PgBouncer:
- Là opensource, nhẹ, dùng quản lý kết nối đến postgresql, quản lý một nhóm kết nối giữa client và db tăng hiệu suất và khả năng scale, giảm sử dụng tài nguyên.
    - Nó có thể gộp các kết nối, duy trì chúng để tái sử dụng cho các request sau. (việc tạo - hủy kết nối là tốn tài nguyên nhất)
    - Cân bằng tải: Cân bằng kết nối đến với những kết nối sẵn có.
    - Query catching:
    - Monitor and Statitics:


## Setup PbBouncer:
### install PostgreSQL
following: https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart

### setup PgBouncer: 
(followling https://medium.com/@sozcandba/setup-postgresql-connection-pooling-with-pgbouncer-eb160bb0ca0a)
- ```apt-get install pgbouncer```
- Khởi tạo 3 cluster postgres để test:
    ```
    # sudo pg_createcluster 14 testdb1
    # sudo pg_createcluster 14 testdb2
    # sudo pg_createcluster 14 testdb3
    ```
- config postgres cluster 
    ```
    sudo nano etc/postgresql/14/testdb1/postgresql.conf
        # - Connection Settings -
        listen_addresses = '*'      
        # what IP address(es) to listen on;
        
        # - Authentication -
        password_encryption = md5     
        # scram-sha-256 or md5

    systemctl resstart postgresql@14-testdb1.service
    ```
- update pgbouncer config
    ```
    vi /etc/pgbouncer/pgbouncer.ini
    vi /etc/pgbouncer/userlist.txt

    systemctl restart pgbouncer.service
    ```

## Bench test bằng pgbench

### Cover số lượng lớn Client:
#### Not pgbouncer:
```
postgres@kafka-01:~$ pgbench -c 1000 -T 60 postgres -U postgres
starting vacuum...end.
connection to database "postgres" failed:
FATAL:  sorry, too many clients already
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 1
query mode: simple
number of clients: 1000
number of threads: 1
duration: 60 s
number of transactions actually processed: 0
Run was aborted; the above results are incomplete.
```
- Không thể kết nối số lượng lớn client đến postgresql

#### Using pgbouncer:
```
postgres@kafka-01:~$ pgbench -c 1000 -T 60 postgres -U postgres
starting vacuum...end.
connection to database "postgres" failed:
FATAL:  sorry, too many clients already
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 1
query mode: simple
number of clients: 1000
number of threads: 1
duration: 60 s
number of transactions actually processed: 0
Run was aborted; the above results are incomplete.
postgres@kafka-01:~$ pgbench -c 1000 -T 60 postgres -h 127.0.0.1 -p 6432 -U postgres
starting vacuum...end.
transaction type: <builtin: TPC-B (sort of)>
scaling factor: 1
query mode: simple
number of clients: 1000
number of threads: 1
duration: 60 s
number of transactions actually processed: 51663
latency average = 1181.629 ms
tps = 846.289310 (including connections establishing)
tps = 846.291933 (excluding connections establishing)
```
- Kết nối được số lượng lớn client thông qua pgbouncer.

### Performance:
#### Not pgbouncer:
```
postgres@kafka-01:~$ cat mysql.sql 
select 1;
postgres@kafka-01:~$ 
postgres@kafka-01:~$ pgbench -c 20 -t 100 -S postgres -h 127.0.0.1 -p 5432 -U postgres -C -f mysql.sql
Password: 
starting vacuum...end.
transaction type: multiple scripts
scaling factor: 1
query mode: simple
number of clients: 20
number of threads: 1
number of transactions per client: 100
number of transactions actually processed: 2000/2000
latency average = 65.500 ms
tps = 305.345263 (including connections establishing)
tps = 321.164275 (excluding connections establishing)
SQL script 1: <builtin: select only>
 - weight: 1 (targets 50.0% of total)
 - 982 transactions (49.1% of total, tps = 149.924524)
 - latency average = 29.375 ms
 - latency stddev = 17.322 ms
SQL script 2: mysql.sql
 - weight: 1 (targets 50.0% of total)
 - 1018 transactions (50.9% of total, tps = 155.420739)
 - latency average = 29.338 ms
 - latency stddev = 17.671 ms
```


#### Using pgbouncer:
```
postgres@kafka-01:~$ pgbench -c 20 -t 100 -S postgres -h 127.0.0.1 -p 6432 -U postgres -C -f mysql.sql
starting vacuum...end.
transaction type: multiple scripts
scaling factor: 1
query mode: simple
number of clients: 20
number of threads: 1
number of transactions per client: 100
number of transactions actually processed: 2000/2000
latency average = 2.903 ms
tps = 6889.349503 (including connections establishing)
tps = 7179.664552 (excluding connections establishing)
SQL script 1: <builtin: select only>
 - weight: 1 (targets 50.0% of total)
 - 982 transactions (49.1% of total, tps = 3382.670606)
 - latency average = 1.135 ms
 - latency stddev = 0.784 ms
SQL script 2: mysql.sql
 - weight: 1 (targets 50.0% of total)
 - 1018 transactions (50.9% of total, tps = 3506.678897)
 - latency average = 1.149 ms
 - latency stddev = 0.785 ms
```
- latency average giảm từ 29.338 ms --> 1.149 ms
- latency stddev giảm từ 17.671 ms --> 0.785 ms

## So sánh với PgPool-II:
- PgPool-II hỗ trợ tính năng H/A, cache query và Load Balancing tốt hơn.
- PgBouncer hỗ trợ connection pool, hạn chế tài nguyên và quản lý số lượng kết nối tốt hơn.
- 

