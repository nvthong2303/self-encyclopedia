# RC - RS - DS

## 1. ReplicationController
- Là một resources trong k8s dùng để tạo và quản lý Pod mà chắc chắn số lượng pod sẽ không thay đổi và kept running.
- RC sẽ tạo số lượng pod theo chỉ định và quản lý pod theo label
- Tại sao phải sử dụng RC ? Đầu tiên, Pod sẽ giám sát container và tự restart nó khi fail. Vậy trong trường hợp toàn bộ worker node fail ? pod sẽ không thể chạy được nữa và ứng dụng bị downtime. Vậy nên nếu chúng ta chạy k8s cluster với >1 worker node, RC sẽ giải quyết vấn đề này. RC sẽ luôn đảm bảo số lượng pod mà nó tạo ra không thay đổi, trong trường hợp cả worker node chứa pod fail, nó sẽ tạo ra pod ở worker node khác để đảm bảo số lượng.
- Đảm bảo ứng dụng availability nhất có thể, ngoài ra có thể đảm bảo performance ứng dụng khi có thể chỉ định số lượng replica trong RC để tạo ra nhiều pod cùng version.

example.yaml
```
apiVersion: v1
kind: ReplicationController
metadata:
  name: hello-rc
spec:
  replicas: 2 # number of the pod
  selector: # The pod selector determining what pods the RC is operating on
    app: hello-kube # label value
  template: # pod template
    metadata:
      labels:
        app: hello-kube # label value
    spec:
      containers:
      - image: 080196/hello-kube # image used to run container
        name: hello-kube # name of the container
        ports:
          - containerPort: 3000 # pod of the container
```

với:
- label selector: chỉ định pod nào đc RC giám sát
- replica count: số lượng pod được tạo
- pod template: config pod sẽ được tạo


- Khi thay đổi template của RC, nó sẽ không apply cho những thằng pod đang chạy hiện tại mà muốn cập nhập, phải xóa hết những pod hiện tại để RC tạo pod mới hoặc xóa cả RC đi tạo lại.

## 2. ReplicaSets
- Là 1 resource ra đời để thay thế RC, Tại sao lại thay thế ? về cơ bản thì RC và RS hoạt động tương tự nhau, nhưng RS sẽ linh hoạt hơn ở phần label selector (label selector ở RS cho phép dùng expression hoặc matching thay vì phải giống hoàn toàn của RC).

example.yaml
```
apiVersion: apps/v1 # change version API
kind: ReplicaSet # change resource name
metadata:
  name: hello-rs
spec:
  replicas: 2
  selector:
    matchLabels: # change here 
      app: hello-kube
  template:
    metadata:
      labels:
        app: hello-kube
    spec:
      containers:
      - image: 080196/hello-kube
        name: hello-kube
        ports:
          - containerPort: 3000
```

## 3. DaemonSets
- Là 1 resource khác của k8s, cũng giám sát và quản lý pod theo label (giống RC, RS) nhưng thay vì RS pod có thể được deploy ở bất cứ node nào thì DS đảm bảo mỗi worker node sẽ có 1 pod duy nhất. Và vì thế nó không có thuộc tính replica count

example.yaml:
```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ssd-monitor
spec:
  selector:
    matchLabels:
      app: ssd-monitor
  template:
    metadata:
      labels:
        app: ssd-monitor
    spec:
      nodeSelector:
        disk: ssd
      containers:
        - name: main
          image: luksa/ssd-monitor
```