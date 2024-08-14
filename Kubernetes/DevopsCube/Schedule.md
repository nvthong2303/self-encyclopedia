kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.0/manifests/tigera-operator.yaml# Scheduling
- Nhiệm vụ tính toán, tìm ra node phù hợp nhất để thực thi Pod, sau đó thông báo lại cho kubelet tại node đó để khởi tạo và chạy Pod.
- Các phương thức khai báo Pod:
    - static pod: chạy 1 pod trên 1 node cụ thể
    - nodeName: gán trực tiếp thông tin node muốn chạy pod trên đó
    - nodeSelector: chọn node theo label cụ thể
    - Tain/Toleration: đánh dấu đặc biệt, có tác dụng chỉ cho phép những Pod có tính chất (Toleration) chạy trên các node có Tain tương đương
    - Affinity: node / pod đó có label thỏa mãn điều kiện cho trước.
    - Resource request / limits: điều kiện node về tài nguyên như Ram, CPU, Disk, ...

- KubeScheduler gồm 2 giai đoạn chính:
    + filtering:
    + scoring:

- Hoạt động của scheduler:
    + Filtering và Scoring
    + Tim ra các node phù hợp nhất, nếu không có thì đưa pod vào hàng đợi schedule
    + Trong giai đoạn chấm điểm bằng các schedule-plugin (https://viblo.asia/p/k8s-basic-scheduling-lap-lich-tren-kubernetes-Yym40mQEJ91)
    + Chọn node có thứ hạng cao nhất.
