# Kong

## mode:
### DB mode:
- triển khai kèm 1 database (cassandra hoặc postgresql) để lưu trữ cấu hình và các thông tin liên quan
- dễ dàng mở rộng, vận hành.

### DB less:
- không cần database, mọi cấu hình và các thông tin đi kèm lưu trữ trong 1 file cấu hình tĩnh.
- đơn giản, hiệu suất cao, phù hợp cho các pipeline (CI/CD).
- vài tính năng có thể không hoạt động đầy đủ.


## mô hình triển khai:
### SingleNode:
### Cluster:
### Hybrid mode:


## Ports:
- 8000: Kong nhận request HTTP từ client
- 8443: Kong nhận request HTTPS từ client
- 8001: Port Kong admin (nhận API HTTP quản lý cấu hình Kong)
- 8444: Port Kong admin (nhận API HTTPS quản lý cấu hình Kong)
- 8002: HTTP - Internal Service: monitor Kong
- 8003: stream proxy - TCP/UDP: sử dụng cho các proxy stream
- 8004: stream proxy - TLS: sử dụng cho các proxy stream có TLS

## Start with docker:
- ```docker network create kong-net```

- start postgresql: ```docker run -d --name kong-database --network=kong-net -p 5432:5432 -e "POSTGRES_USER=kong" -e "POSTGRES_DB=kong" -e "POSTGRES_PASSWORD=kongpass" postgres:13```
    - POSTGRES_USER / POSTGRES_DB: username / db_name
    - POSTGRES_PASSWORD: password

- prepare Kong database: ```docker run --rm --network=kong-net -e "KONG_DATABASE=postgres" -e "KONG_PG_HOST=kong-database" -e "KONG_PG_PASSWORD=kongpass" -e "KONG_PASSWORD=test" kong/kong-gateway:3.8.0.0 kong migrations bootstrap```
    - KONG_DATABASE: db_name
    - KONG_PG_HOST: host postgresql
    - KONG_PG_PASSWORD: password user postgres
    - KONG_PASSWORD: default admin password

- license Enterprise: ``` export KONG_LICENSE_DATA='{"license":{"payload":{"admin_seats":"1","customer":"Example Company, Inc","dataplanes":"1","license_creation_date":"2017-07-20","license_expiration_date":"2017-07-20","license_key":"00141000017ODj3AAG_a1V41000004wT0OEAU","product_subscription":"Konnect Enterprise","support_plan":"None"},"signature":"6985968131533a967fcc721244a979948b1066967f1e9cd65dbd8eeabe060fc32d894a2945f5e4a03c1cd2198c74e058ac63d28b045c2f1fcec95877bd790e1b","version":"1"}}'```
    ```
    {
        "license": {
            "payload": {
                "admin_seats": "1",
                "customer": "Example Company, Inc",
                "dataplanes": "1",
                "license_creation_date": "2017-07-20",
                "license_expiration_date": "2017-07-20",
                "license_key": "00141000017ODj3AAG_a1V41000004wT0OEAU",
                "product_subscription": "Konnect Enterprise",
                "support_plan": "None"
            },
            "signature":"6985968131533a967fcc721244a979948b1066967f1e9cd65dbd8eeabe060fc32d894a2945f5e4a03c1cd2198c74e058ac63d28b045c2f1fcec95877bd790e1b",
            "version":"1"
        }
    }
    ```
- start Kong: 
    ```
    docker run -d --name kong-gateway \
    --network=kong-net \
    -e "KONG_DATABASE=postgres" \
    -e "KONG_PG_HOST=kong-database" \
    -e "KONG_PG_USER=kong" \
    -e "KONG_PG_PASSWORD=kongpass" \
    -e "KONG_PROXY_ACCESS_LOG=/dev/stdout" \
    -e "KONG_ADMIN_ACCESS_LOG=/dev/stdout" \
    -e "KONG_PROXY_ERROR_LOG=/dev/stderr" \
    -e "KONG_ADMIN_ERROR_LOG=/dev/stderr" \
    -e "KONG_ADMIN_LISTEN=0.0.0.0:8001" \
    -e "KONG_ADMIN_GUI_URL=http://localhost:8002" \
    -e KONG_LICENSE_DATA \
    -p 8000:8000 \
    -p 8443:8443 \
    -p 8001:8001 \
    -p 8444:8444 \
    -p 8002:8002 \
    -p 8445:8445 \
    -p 8003:8003 \
    -p 8004:8004 \
    kong/kong-gateway:3.8.0.0
    ```

- env:
    - KONG_DATABASE: db_name
    - KONG_PG_HOST: host_postgres
    - KONG_PG_USER: user_postgres
    - KONG_PG_PASSWORD: password_postgres
    - *_LOG: path logs
    - KONG_ADMIN_LISTEN: address Kong admin listen request
    - KONG_LICENSE_DATA: if you have enterprise license
