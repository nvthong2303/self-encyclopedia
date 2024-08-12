# POD

## Pod là gì ?
- Container là gì ? là nơi chúng ta đóng gói ứng dụng và các dependency của chúng (library, ...) một cách độc lập. Mỗi Container có một địa chỉ IP và có thể đính kèm disk hoặc CPU, ...
- Pod là đơn vị nhỏ nhất trong k8s đại diện cho 1 phiên bản duy nhất của ứng dụng. Đây là nơi k8s chạy các container. 1 Pod có thể chứa nhiều container, 1 pod đc nhận 1 IP duy nhất, các container bên trong có thể giao tiếp với nhau qua localhost:port của chúng.
- 



## Cheat sheet
- run pod:
    ```
    kubectl run {pod_name} \
    --image={image_name} \
    --restart=Never \
    --port=80 \
    --labels=app=web-server,environment=production \
    --annotations description="This pod runs the web server"
    ```

- get pod:
    ```
    kubectl get pods
    ```

- describe pod:
    ```
    kubectl describe pod {pod_name}
    ```

- delete pod:
    ```
    kubectl delete pod {pod_name}
    ```

- run file .yaml
    ```
    kubectl create -f nginx.yaml
    ```

- exec pod:
    ```
    kubectl exec -it  -- /bin/sh
    ```

- forward pord pod:
    ```
    kubectl port-forward pod/ 8080:80
    ```

## Pod Associate Objects:
- Trong thực tế, khi chạy các ứng dụng trên k8s không ai chạy các Pod riêng lẻ, bởi k8s tập chung vào việc mở rộng và duy trì tính HA cho các pod. Bản thân các pod cũng không thể tự động scale trực tiếp, nếu chạy một pod duy nhất nó sẽ có thể là 1 single point bị lỗi.
- K8s có nhiều loại Object khác nhau được liên kết với Pod cho các mục đích khác nhau:
    - Replicaset: Duy trì 1 bộ các replicas của Pod ổn định chạy tại bất kỳ thời điểm nào.
    - Deployment: Chạy các ứng dụng stateless như web-server, API, ...
    - StatefulSets: Chạy các ứng dụng stateful như database, distributed system, ...
    - Deamonsets: Chạy Pod trên tất cả các node (log, monitoring, ...)
    - Jobs: Xử lý hàng loại.
    - CronJobs: Công việc được lên lịch.



## Pod lifecycle:
- xem xét:
    - Pod Phases:

        | Phases | Mô tả |
        |-------|-------|
        | Pending | Pod tạo nhưng chưa chạy |
        | Running | Ít nhất 1 container trong Pod đang chạy hoặc 1 process đang start hoặc đang restart |
        | Succeeded | Tất cả các container đã chạy thành công |
        | Failed | Ít nhất 1 container lỗi |
        | Unknow | API-server không lấy được Pod status |

    - Pod Conditions: Pod status cung cấp trạng thái của pod, còn Pod condition cung cấp thông tin chi tiết về scheduling, readliness, initialization.
    - Container Status: 


## Tại sao k8s sử dụng Pod chứ k phải container ?
- 


