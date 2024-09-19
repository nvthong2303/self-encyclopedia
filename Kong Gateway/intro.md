# Kong Gateway


## API Gateway ?


## Kong ?
- là một API gateway cloud-native nhẹ, nhanh và linh hoạt. API gateway là một reverse proxy giúp quản lý, config và route request tới APIs. Đứng trước mọi RestFulAPI và có thể mở rộng thông qua các modules và plugins. 
- Được thiết kế để chạy trên kiến trúc phi tập trung bao gồm hybrid-cloud và multi-cloud.


### Các thành phần chính:
#### Services
- Chỉ định path thực tế cho microservice backend API.
- Biểu thị cho một cái service hoặc version của service tiện cho việc config và sử dụng.
- Các tham số:
    - Name*: Tên service
    - Tags: tags cho service

    - Protocol*: grpc, http, tcp, udp, websocket.
    - Host*: Host của Service BE.
    - Path: đường dẫn mà Kong sẽ mặc định thêm vào (host:port/path) khi có request được chuyển đến
    - Port: Port dịch vụ
    - Retries: Số lần gọi lại BE khi request không thành công
    - Connection Timeout: thời gian tối đa chờ response từ BE.
    - Write Timeout: thời gian chờ Kong gửi dữ liệu đến BE.
    - Read Timeout: thời gian chờ nhận phản hồi từ BE.


Ví dụ:
- khi cấu hình path trong service ```/health-check```:
    - khi tạo route: ```/test-health-check``` 
        -  ```http://localhost:8000/test-health-check``` --> ```localhost:3000/health-check```
        - ```http://localhost:8000/test-health-check/users``` --> ```localhost:3000/health-check/users```
- khi cấu hình path trong service: ```/```
    - tạo route: ```/test-health-check```
        - ```http://localhost:8000/test-health-check``` --> ```localhost:3000```
        - ```http://localhost:8000/test-health-check/users``` --> ```localhost:3000/users```


#### Routes
- Xác định các path được expose ra ngoài và ánh xạ nó tới các Backend service.
- Tập hợp các quy tắc để Kong match request tới đúng service mà nó cần tới.
- Các tham số:
    - Name*: Tên route
    - Service*: ID của Service route sẽ fordward request tới.
    - Tags: tags cho route
    - Protocol*: grpc, http, tcp, udp, websocket.
    - HTTPS/HTTP Routing Rules: Danh sách routing rules 
        - Paths: danh sách các path được khai báo sẽ được route xử lý
        - SNIs: danh sách các Server Name Indication (trong TLS)
        - Hosts: danh sách các host / domain route xử lý, không có mặc định là /*
        - Methods: 
        - Headers: danh sách cặp key-value trong headers, không có không kiểm tra headers
    - Path handling:
    - HTTPS redirect status code: 
    - Regex Priority: 

#### Upstreams
- Chứa thông tin chi tiết về thiết bị của microservice backend, health check, và load balancing configuration.
- Là một virtual hostname dùng chứa các config giúp khai báo, quản lý, loadbalancing và monitoring các server chứa các service BE.
- Trên thực tế, tạo 1 upstreams tương ứng với 1 cụm server chứa các service BE khác nhau.
- Các tham số:
    - Name*: Name upstreams
    - Host Header: thay đổi host, không có sẽ dùng host gốc của request hoặc target
    - Client Certificate: 
    - Tags: label
    - Algorithm: thuật toán cân bằng tải (round robin / consisten hashing /  least connections / latency )
    - Slots:
    - Hash on
        - Hash on

    - Hash Fallback
        - Hash Fallback

    - Active Health Checks
    - Passive Health Checks / Circuit Breakers
    - Healthchecks Threshold


#### Targets
- microservice IP và port riêng lẻ được thêm vào Upstreams cho loadbalancing.
- Set targets: đích mà các upstreams / services hướng tới, tương ứng là địa chỉ của các server chứa các service BE. 

#### Consumers
- User hoặc ứng dụng sử dụng APIs

#### Plugins
- các tính năng được thêm vào workflow của Kong.


### Các tính năng chính:
#### Routing, Loadbalancing, health checking:
#### Authentication, Authorization:
#### Proxy, SSL/TLS, Connectivity:
#### Plugins cho workflow Kong:
#### Ingress Controller:
#### Hibrid deployment, Declarative Databaseless Deployment:
#### Ratelimit, Caching, Monitoring:


## How it work ?
### Routing traffic:
- Cách mà Kong route traffic:
    - Client request:
    - Kong nhận request
    - Kiểm tra config Route
    - Liên kết Route với Service
    - Proxy request đến BE
    - Nhận Response từ BE
    - Trả về Client


### Load balaning:
- Phân phối request đến các service BE (upstreams server) theo cơ chế load balancing.
- Các thuật toán: 
    - Round Robin: phân phối vòng
    - Least Connections: phân phối đến server có số lượng kết nối thấp nhất thời điểm nhận request
    - IP Hash: phân phối đến 1 server, đảm bảo các request từ một client đều đến 1 server.

### Health check and Circuit 
- Cơ chế:
    - Health Check chủ động: Kong gửi các request giả lập để kiểm tra tình trạng của chúng.
    - Health Check thụ động: Kong theo dõi response của các request từ Client để đánh giá tình trạng của chúng.

