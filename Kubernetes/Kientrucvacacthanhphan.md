# Kiến trúc Kunbernetes và các thành phần chính

- Kubernetes là một trong các orchestration tools nằm trong hệ sinh thái của container, do vậy K8S có cách thành phần để đảm bảo thực hiện được việc tự động hóa triển khai, mở rộng và vận hành container trên các cụm cluster (các máy chạy container).
- Chức năng chính:
    - Điều phối container, storage.
    - Load balancing và Service discovery.
    - Tự động triển khai và khôi phục.
    - Tự động đóng gói.
    - Tự động hồi phục.
    - Quản lý và bảo mật.



## Kiến trúc
![image info](./images/k8s%20structure.png)
- các thành phần chính của kunernetes: Master node và Worker node.
    - Master Node: đóng vai trò là control plane, điều khiển toàn bộ các hoạt động chung và kiểm soát các container trên các worker node. Các thành phần trên master node bao gồm: API-server, Controller-manager, Scheduler, Etcd và Docker engine. (Docker engine dùng để chạy các thành phần còn lại trên master node)
    - Worker Node: vai trò chính là để chạy các container mà người dùng yêu cầu, thành phần chính của worker node bao gồm: kubelet, kube-proxy và Docker engine.
- trong thực tế thì số lượng worker node sẽ nhiều hơn master node.


## Các thành phần chính:
### API-server (kube-apiserver):
- Là thành phần tiếp nhận và xử lý các yêu cầu của hệ thống (người dùng, services) thông qua Rest API. 
- API-server nằm trên master node và hoạt động trên port 6443(HTTPS) và 8080(HTTP).
- Các chức năng chính:
    - Giao tiếp và điều phối container.
    - Xác thực và phân quyền.
    - Quản lý trạng thái cluster.
    - Cung cấp restful api.

### Controller-manager:
- Là thành phần quản lý trong K8S, có nhiệm vụ xử lý các tác vụ trong cụm để đảm bảo hoạt động của các tài nguyên trong cụm cluster. Tự động hóa các tác vụ như scalling, rolling update, đảm bảo H/A.
- Có các thành phần sau:
    - Node Controller
    - Replication Controller
    - Endpoints Controller
    - Service Account và Token Controller.
- Hoạt động trên Nodemaster và port 10252

### Scheduler
- Theo dõi, và đưa ra các node mỗi khi có yêu cầu tạo podd

### Etcd


### Kubelet


### kube-proxt