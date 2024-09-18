# Kong Gateway


## API Gateway ?


## kong ?
### Các thành phần chính:
#### Routes
- Xác định các path được expose ra ngoài và ánh xạ nó tới các Backend service 

#### Services
- Chỉ định path thực tế cho microservice backend API

#### Upstreams
- Chứa thông tin chi tiết về thiết bị của microservice backend, health check, và load balancing configuration.
- Là một virtual hostname dùng chứa các config giúp khai báo, quản lý, loadbalancing và monitoring các server chứa các service BE.

#### Targets
- microservice IP và port riêng lẻ được thêm vào Upstreams cho loadbalancing.

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

#### Ratelimit, Caching, Monitoring, 

