# Kiến trúc Kunbernetes và các thành phần chính

- Kubernetes là một trong các orchestration tools nằm trong hệ sinh thái của container, do vậy K8S có cách thành phần để đảm bảo thực hiện được việc tự động hóa triển khai, mở rộng và vận hành container trên các cụm cluster (các máy chạy container).



## Kiến trúc
- các thành phần chính của kunernetes: Master node và Worker node.
    - Master Node: đóng vai trò là control plane, điều khiển toàn bộ các hoạt động chung và kiểm soát các container trên các worker node. Các thành phần trên master node bao gồm: API-server, Controller-manager, Scheduler, Etcd và Docker engine. (Docker engine dùng để chạy các thành phần còn lại trên master node)
    - Worker Node: vai trò chính là để chạy các container mà người dùng yêu cầu, thành phần chính của worker node bao gồm: kubelet, kube-proxy và Docker engine.
- trong thực tế thì số lượng worker node 