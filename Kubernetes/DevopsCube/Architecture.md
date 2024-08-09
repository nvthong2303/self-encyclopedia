# Kiến trúc của Kubernetes:
![image info](./k8s-architecture.drawio-1.png)

- Đầu tiền, phải nhớ K8s là một hệ thống phân tán (nó có nhiều thành phần chạy trên các máy chủ khác nhau thông qua mạng, đó có thể là máy ảo hoặc máy vật lý). Bao gồm các node Control plane và các Worker node.

## 1. Control plane:
### kube-apiserver:
- Là thành phần trung tâm của cụm K8s, expose các API ra ngoài, có khả năng mở rộng cao và có thể xử lý số lượng lớn request.
- Người dùng cuối và các thành phần khác giao tiếp với cụm thông qua apiserver.
- Khi sử dụng kubectl, ở phía Backend thực chất là đang giao tiếp với apiserver thông qua rest api http. Trừ các thành phần trong cụm như scheduler, controller, ... sẽ giao tiếp với cụm qua gRPC.
- Cho phép người dùng lấy thông tin về trạng thái của các Object: Pod, Namespace, Service, ...
- Các vai trò chính của apiserver:
    - API management: expose endpoint api và xử lý toàn bộ api request. 
    - Authentication / Authorization:
    - Validate các API Object (pod, service, ...)
    - Thành phần duy nhất giao tiếp với ectd.
    - Điều phối các quy trình giữa control plane và các worker node.
    - Chủ yếu được sử dụng để truy cập từ bên ngoài cụm.
    - Hỗ trợ theo dõi sự thay đổi của tài nguyên (sửa, tạo, xóa)

### etcd:
- k8s là một hệ phân tán và nó cần 1 hệ csdl phân tán hiệu quả như etcd để hỗ trợ tính phân tán của nó. ETCD là một opensource kho lưu trữ key-value phân tán, nhất quán. Có thể koi nó là não bộ của cụm k8s.
- Các tính chất của etcd:
    - tính nhất quán cao: sử dụng thuật toán đồng thuật kraft
    - phân tán
    - lưu trữ data dưới dạng key-value: ~ BoltDB
- ETCD lưu trữ gì ? config, trạng thái, metadata của các Object (pod, secret, daemonset, ...)
- Hỗ trợ Watch api để theo dõi sự thay đổi data.

### kube-scheduler: 
- Service mặc đinh của k8s làm nhiệm vụ phân phối pod sẽ được chạy trên node nào.
- Tìm kiếm các node thỏa mãn điều kiện và lựa chọn node tối ưu nhất để chạy (CPU, disk, RAM, PV, ...).
- Trong trường hợp không có node nào thỏa mãn, pod sẽ ở trạng thái chưa được lên lịch cho tới khi Scheduler tìm được node phù hợp.


### kube-controller:
- Service có nhiệm vụ điều tiết trạng thái của k8s.
- Là một vòng lặp điều khiển giám sát trạng thái của cluster được chia sẻ qua các api và thực hiện các thay đổi cần thiết để chuyển trạng thái của cluster tới trạng thái mong muốn.

### cloud-controller-manager:
- cloud-controller-manager cung cấp các bộ controller riêng cho cloud để đảm bảo trạng thái mong muốn:
    - node controller: cung cấp thông tin đến node tới cloud-provider thông qua api
    - route controller: chịu trách nhiệm định tuyến mạng trên cloud platform, nhờ vậy mà các node có thể giao tiếp với nhau.
    - Service controller: đảm bảo việc triển khai các bộ load-balancer, gán địa chỉ IP, ...


## 2. Worker node:
### kubelet:
- Đóng via trò như 1 agent trên các worker node, nhiệm vụ chính để worker node đăng ký và quản lý bởi cụm k8s cũng như nhận nhiệm vụ triển khai các pod, đảm bảo chúng chạy ổn định. 
- Nó không quản lý các container không đc tạo bởi kubernetes:
- Các nhiệm vụ chính:
    - Tạo, sửa đổi, xóa các container cho pod
    - Chịu trách nhiệm cho các xử lý liveliness, readliness và các startup probes (các cơ chế kiểm tra trạng thái của một container trong pod).
    - Chịu trách nhiệm mount disk
    - Thu thập và báo cáo trạng thái Node và Pod thông qua api.


### kube-proxy:
- Kube-proxy là một network proxy chạy trên mỗi node trong K8S cluster, thực hiện một phần Kubernetes Service. 
- Kube-proxy duy trình network rules trên các node. Những network rules này cho phép kết nối mạng đến các pods từ trong hoặc ngoài cluster.

### Container Runtime:
- Giống như JRE là cần thiết để chạy ứng dụng java thì COntainer Runtime là thành phần cần thiết để chạy container. Nó chịu trách nhiệm pull image, run container, phân bố và cô lập tài nguyên giữa các container, quản lý vòng đời của container.
- Các khái niệm:
    - Container runtime interface (CRI)
    - Open container initiative (OCI)
    

## 3. Các thành phần bổ sung:
### Plugin CNI (Container network interface):
- CNI (Container Network Interface) là một tiêu chuẩn được sử dụng để quản lý mạng cho các container trong Kubernetes. CNI plugin là các thành phần phần mềm thực hiện giao thức CNI, cung cấp chức năng mạng cho các container bằng cách gán địa chỉ IP và thiết lập các quy tắc mạng cho container khi chúng được khởi tạo.
- CNI là một chuẩn giao diện cho phép tích hợp các plugin mạng khác nhau vào các hệ thống container như Kubernetes. CNI định nghĩa một tập hợp các thông số và giao diện API mà các plugin phải tuân theo để cung cấp mạng cho container. Kubernetes sử dụng CNI để kết nối các pod với mạng và thiết lập các quy tắc mạng.
- Cách CNI Plugin hoạt động
- Các CNI Plugin phổ biến:
    - Calico
    - Flannel
    - Weave net
    - Cilium
    - 

### CoreDNS:
### Metrics Server:
### User Interface: