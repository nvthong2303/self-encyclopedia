## Guildline

## Reverse proxy:
### Service + Route:
- Chạy service BE tại localhost:3000 (paths: ```/, /health-check, /users```)
- Tạo Service:
    ```
    Name: test-localhost
    Tags:

    Protocol: http
    Host: 172.24.0.1 (IP current, không dùng localhost vì đang chạy Kong trong docker, không thể ping đến localhost:3000 được, dùng IP thay thế)
    Path: /health-check
    Port: 3000
    ```
- Thêm Route cho Service: 
    ```
    Name: rpite-localhost
    Tag: 
    Protocols: HTTP/HTTPS
    Paths: [/test/health-check, /test-health-check]

    ```
- ```http://localhost:8000/test-health-check``` -> ```http://localhost:3000/health-check```
- ```http://localhost:8000/test/health-check/``` -> ```http://localhost:3000/health-check```
- ```http://nvthong-Vostro-3500:8000/test/health-check/``` -> ```http://localhost:3000/health-check```
- mọi request đến port 8000 (port Kong) có endpoint /health-check hoăc /test/health-check đều được service xử lý


### Upstream + target
- Chạy service BE tại localhost:3000 (paths: ```/, /health-check, /users```)
- Tạo Upstreams: 
    ```
    Name: localhost_1
    ```
- Tạo Target:
    ```
    Target address: 172.24.0.1:3000 (không dùng localhost, vì trong docker không thể phân giải được)
    Weight: 
    ```
- Tạo Gateway Service:
    ```
    Name: service_with_upstreams
    Host: localhost_1 (tên upstreams)
    Path: /health-check
    ```
- Tạo Routes:
    ```
    Name: route_upstream
    paths: /test-upstreams
    ```
- ```http://nvthong-Vostro-3500:8000/test-upstreams``` -> ```http://localhost:3000/health-check```
- ```http://localhost:8000/test-upstreams``` -> ```http://localhost:3000/health-check```


### Consumer:
#### Consumer Authenticated:
- Cài đặt consumer authenticated cho API /users:
    - Chọn routes:
    - Install Plugin Key Authentication
    - Tạo mới Consumer
    - Tạo Credentials, tạo New Key Auth Credential
    - Set apikey.
    - Request đến route /user phải đi kèm params apikey="apikey"
    ```http://localhost:8000/users?apikey=apikey```


### Proxy cache:
- Cache for scope Route:
    - Chọn route:
    - Install Plugin for route
    - Check lại curl: 
    ```
    # call lần đầu tiên:
    curl -i -s -XGET http://localhost:8000/api/get-count | grep X-Cache
    X-Cache-Key: 4372f104bf961a6a8535
    X-Cache-Status: Miss

    # trong 30s tiếp, response trả về từ cache của Kong:
    curl -i -s -XGET http://localhost:8000/api/get-count | grep X-Cache
    X-Cache-Key: 4372f104bf961a6a8535
    X-Cache-Status: Hit

    # request tiếp theo sau khi cache hết hiệu lực:
    curl -i -s -XGET http://localhost:8000/api/get-count | grep X-Cache
    X-Cache-Key: 4372f104bf961a6a8535
    X-Cache-Status: Refresh
    ```
- response phải trả về có Content Type: json/application hoặc text/plain mới đc cache.

### Rate limit:


