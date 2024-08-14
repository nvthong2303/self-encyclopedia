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
- 

### 9. Attach configmap to pod.
### 10. Add Secret to pod.
### 11. multi-container pods (sidecar container pattern).
### 12. Init containers.
### 13. Ephemeral containers.
### 14. Static Pods.
### 15. Learn to troubleshoot Pods.
### 16. Pod Preemption & Priority.



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
