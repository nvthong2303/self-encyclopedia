# Roadmap & Resources
## Prerequisites To Learn Kubernetes

## Learn Kubernetes Architecture

## Kubernetes Cluster Setup

## Learn About Cluster Configurations

## Understand Kubeconfig File

## Understand Kubernetes Objects And Resources

## Learn About Pod & Associated Resources
- Định nghĩa tài nguyên bằng yaml:
    - Kind
    - Metadata
    - Annotations
    - Labels
    - Selectors

- hands-on tasks 
    - Deploy a pod
    - Deploy pod on the specific worker node
    - Add service to pod
    - Expose the pod Service using Nodeport
    - Expose the Pod Service using Ingress
    - Setup Pod resources & limits
    - Setup Pod with startup, liveness, and readiness probes.
    - Add Persistent Volume to the pod.
    - Attach configmap to pod
    - Add Secret to pod
    - multi-container pods (sidecar container pattern)
    - Init containers
    - Ephemeral containers
    - Static Pods
    - Learn to troubleshoot Pods
    - Pod Preemption & Priority
    - Pod Disruption Budget
    - Pod Placement Using a Node Selector
    - Pod Affinity and Anti-affinity
    - Container Life Cycle Hooks

### 1. Deploy a pod

### 2. Deploy pod on the specific worker node:
- đánh label cho node: ```kubectl label nodes thong-test-kafka02 node-role=worker02```
- apply .yaml:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
  nodeSelector:
    node-role: worker02
```

### 3. Add service to pod
- tạo pod:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
```
- tạo service:
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```
- gán label cho pod: ```kubectl label pod my-pod app=my-pod```
- kiểm tra service: ```kubectl exec -it <pod-name> -- curl http://my-service:80```

### 4. Expose the pod Service using Nodeport
- tạo pod:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
```
- tạo service NodePort:
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app: my-pod
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30007
```
- gán label cho pod: ```kubectl label pod my-pod app=my-pod```
- truy cập: ```http://192.168.1.100:30007```

### 5. Expose the Pod Service using Ingress
- tạo Pod và Service:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-app
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80

----
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```
- cài đặt Ingress Controller: ```kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml```
- tạo ingress resource:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: my-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```
- sửa file hosts ```<Ingress_Controller_IP> my-app.example.com```
- kiểm tra: ```http://my-app.example.com```

### 6. Setup Pod resources & limits
- tạo pod có giới hạn tài nguyên (yêu cầu tối thiểu request: Memories: 64Mi, cpu: 250m và limits: Memories: 128Mi, cpu: 500m)
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```
- request: dùng để schedule trên k8s, nếu node không đủ tài nguyên để đáp ứng yêu cầu này, pod sẽ không được schedule để chạy trên node đó.
- limits: bảo vệ cluster khỏi việc 1 container sử dụng quá nhiều tài nguyên.

### 7. Setup Pod with startup, liveness and readiness probes.
- startup, liveness và readiness probes là 3 cơ chế để kiểm tra giám sát trạng thái container.
    + startup probe: kiểm tra qtrinh khởi động container, dành cho các container cần thời gian dài để khởi động, nếu nó được kích hoạt nó sẽ thay thế liveness và readiness probes cho đến khi nó thành công, sau khi thành công liveness và readiness probes sẽ hoạt động bthg.
    + readiness probe: kiểm tra xem container có sẵn sàng phục vụ các yêu cầu hay không, nếu thất bại container sẽ bị loại khỏi các endpoint của service, k8s không gửi traffic đến nó cho đến khi hoạt động bình thường trở lại.
    + liveness probe: kiểm tra container có sống hay không, nếu có tức là nó đang hoạt động, nếu không k8s sẽ restart nó.

- tạo pod:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    ports:
    - containerPort: 80
    livenessProbe:
      httpGet:
        path: /healthz
        port: 80
      initialDelaySeconds: 10
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
    startupProbe:
      httpGet:
        path: /startup
        port: 80
      failureThreshold: 30
      periodSeconds: 10
```


### 8. Add Persistent Volume to the pod.
- tạo PV: 
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```
- tạo pvc:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```
- gắn pvc vào pod bằng path host: ```/mmt/data``` vào path ```/usr/share/nginx/html```:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    volumeMounts:
    - mountPath: "/usr/share/nginx/html"
      name: my-storage
  volumes:
  - name: my-storage
    persistentVolumeClaim:
      claimName: my-pvc
```

### 9. Attach configmap to pod.
- tạo config map: ```kubectl create configmap my-config --from-file=app-config.properties ```
- gắn vào pod:
```
# dạng env:
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: my-container
      image: nginx
      env:
        - name: CONFIG_SETTING1
          valueFrom:
            name: my-config
            key: setting1

# dạng volume:
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
    - name: my-container
      image: nginx
      volumeMounts:
        - mountPath: /etc/config
          name: config-volume
  volumes:
    - name: config-volume
      configMap:
        name: my-config
```

### 10. Add Secret to pod.
- tạo secret:
```
apiVersion: v1
kind: Secret
medata:
  name: my-secret
type: Opaque
data:
  username: admin
  password: 123456
```
- gán vào pod:
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    volumeMounts:
    - name: srt
      mountPath: "/srt"
      readOnly: true
  volumes:
  - name: srt
    secret:
      secretName: my-secret
```

### 11. multi-container pods (sidecar container pattern).
- pattern phổ biến, sử dụng các container phụ trợ (sidecar container) trong cùng Pod với main container, thường cung cấp các service hỗ trợ cho main container như logging, monitoring, proxy, hoặc catching.
```
apiVersion: v1
kind: Pod
metadata:
  name: sidecar-container
spec:
  containers:
  - name: sidecar-container
    image: busybox
    command: ["/bin/sh"]
    args: ["-c", "while true; do echo  $(date -u) 'This is just an echo from simple Sidecar Container' >> /var/log/index.html; sleep 5;done"]
    resources: {}
    volumeMounts:
    - name: shared-logs
      mountPath: /var/log
    
  - name: main-container
    image: nginx
    resources: {}
    ports:
    - containerPort: 80
    volumeMounts:
    - name: shared-logs
      mountPath: /usr/share/nginx/html
  
  volumes:
  - name: shared-log
    emptyDir: {}
  
  dnsPolicy: Default
```


### 12. Init containers.
- Init container là container đặc biệt trong k8s, chạy trước các container chính (cùng Pod), dùng để thực hiện các tác vụ chuẩn bị cho container chính.
```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  initContainers:
  - name: init-service
    image: busybox
    command: ["sh", "-c", "echo Preparing data ... && sleep 10 && echo Done."]
  containers:
  - name: my-app
    image: nginx
    ports:
    - containerPorts: 80
```

### 13. Ephemeral containers.
- Ephameral là một tính năng đặc biệt trong k8s, dùng để debug và khắc phục sự cố trong các Pod, mà không cần can thiệp cấu hình hay khởi động lại Pod.
- Ephameral Pod là tạm thời, không tồn tại lâu dài và cũng không được khai báo trong các spec ban đầu của Pod, không thể restart.

- Thêm ephameral Pod:
```
kubectl debug -it nginx-pod --image=busybox --target=nginx-container
```

### 14. Static Pods.
- Là loại pod đặc biệt, được kubelet quản lý chứ k phải apiserver, thường dùng để triển khai các thành phần cơ sở trên các node: kube-apiserver, kube-schedule, kube-controller-manager, ...
- Tự động restart khi có sự cố, được khai báo trong bằng các file cấu hình đặt trong ```/etc/kubernetes/manifests```.
- Không có đối tượng Pod, nhưng apiserver sẽ tạo ra 1 mirror pod để có thể quan sát.


### 15. Learn to troubleshoot Pods.
```
# get pod
kubectl get pods

# describe pod
kubectl describe pod <pod-name>

# check logs
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container-name>

# check container state

# exec to container bash
kubectl exec -it <pod-name> -- /bin/sh
kubectl exec -it <pod-name> -- ping google.com

# check probes (liveness, readness, startup)
```


### 16. Pod Preemption & Priority.
- đây là 2 tính năng trong k8s cho phép đánh priority để đảm bảo tài nguyên cho các ứng dụng quan trọng hơn khi tài nguyên bị giới hạn.
- Pod Priority: thiết lập **PriorityClass** với value rồi gán cho Pod để đánh priority cho Pod đó. Pod có priority cao sẽ đc ưu tiên xử lý trước.
- Pod Preemption: là qtrinh node loại bỏ các pod có priority thấp nhường tài nguyên cho các pod có priority cao hơn.
  + cách hoạt động: khi tài nguyên bị giới hạn, k8s sẽ tìm các pod có priority thấp để giải phóng nhường tài nguyên cho các pod có priority cao. Thông báo tới các Pod này và có thời gian ngắn để giải phóng tài nguyên trc khi bị loại bỏ.

### 17. Pod Disruption Budget.


### 18. Pod Placement Using a Node Selector.


### 19. Pod Affinity and Anti-affinity.


### 20. Container Life Cycle Hooks.



## Learn Pod Dependent Objects
- Replicaset
- Deployment
- Daemonsets
- Statefulset
- Jobs & Cronjobs


## Learn Ingress & Ingress Controllers

## Learn End-to-end Microservices Application Deployment on Kubernetes

## Learn About Securing Kubernetes Cluster

## Learn About Kubernetes Configuration Management Tools

## Learn About Kubernetes Operator Pattern

## Learn Important Kubernetes Configurations

## Learn Kubernetes Best Practicesc
 
## The Best Resources to Learn Kubernetes Online

## Real-World Kubernetes Case Studies
- List of Kubernetes User Case StudiesOfficial Case Studies
- How OpenAI Scaled Kubernetes to 7,500 NodesBlog
- Testing 500 Pods Per NodeBlog
- Dynamic Kubernetes Cluster Scaling at AirbnbBlog
- Scaling 100 to 10,000 pods on Amazon EKSBlog
