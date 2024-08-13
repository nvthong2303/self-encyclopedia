# Service

## 1. Services
- Là 1 resource trong k8s, tạo ra single - constant point của một nhóm Pod, mỗi service sẽ có 1 IP không đổi cho đến khi xóa. Client sẽ mở connection đến service và service sẽ forward đến một trong các pod.
- Tại sao phải có service ? 
    - Pods are ephemeral: Pod mang tính chất phù du, có thể tạo, xóa, thay thế bất cứ lúc nào, nên IP của nó cũng thay đổi theo, IP không cố định
    - Multiple Pod run same application: trong RS, để tăng performance ta thường chạy nhiều pod cho 1 ứng dụng, không có IP đại diện cho các pod đó.

    -> Service sẽ tạo ra 1 endpoint cho tất cả các Pod phía sau.

#### Service quản lý connection ?
- Cũng giống RC, RS, Service cũng chọn Pod để quản lý bằng label selector.
 
example.yaml
```
apiVersion: v1
kind: Service
metadata:
  name: hello
spec:
  selector:
    app: hello-kube # label selectors Pod
  ports:
    - port: 80 # port of the serivce
      targetPort: 3000 # port of the container that service will forward to 
```

#### Có 4 loại service chính: ClusterIP, NodePort, ExternalName, LoadBalancer(cloud).


## 2. ClusterIP:
- tạo ra 1 IP và local DNS mà sẽ có thể truy cập ở bên trong cluster, không thể truy cập từ bên ngoài, dùng cho các pod trong cluster giao tiếp với nhau.
- IP nội bộ k8s đại diện cho tập các Pod (RS, RC)
- Traffic tới sẽ được cân bằng tải tới tập các Pod thuộc deployment.

## 3. NodePort:
- expose pod cho client bên ngoài có thể truy cập vào được, expose IP nội bộ bên trong Cluster ra bên ngoài.
- cũng tạo ra endpoint như ClusterIP để có thể truy cập được từ bên trong cluster bằng IP và DNS.
- Mapping 1 cặp IP:Port (internal) với 1 cặp IP:Port (external) để có thể truy cập từ bên ngoài internet và bên trong.

example.yaml:
```
apiVersion: v1
kind: Service
metadata:
  name: hello
spec:
  selector:
    app: hello-kube
  type: NodePort # type NodePort
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30123 # port of the worker node
```


## 4. ExternalName:
- 


## 5. LoadBalancer:
- Hỗ trợ trên môi trường cloud


