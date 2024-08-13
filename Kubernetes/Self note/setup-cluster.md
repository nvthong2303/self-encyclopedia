deploy trên 3 VM: 10.60.65.90, 10.60.65.91, 10.60.65.92
user root

# Use Kubeadm:

## 1. Download & unpack containerd package
```
wget https://github.com/containerd/containerd/releases/download/v1.6.14/containerd-1.6.14-linux-amd64.tar.gz
```
==> result:
```
--2024-08-12 16:38:29--  https://github.com/containerd/containerd/releases/download/v1.6.14/containerd-1.6.14-linux-amd64.tar.gz
Resolving github.com (github.com)... 20.205.243.166
Connecting to github.com (github.com)|20.205.243.166|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/46089560/d90749e7-10b0-4e43-bf46-99a51edb0149?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240812T093830Z&X-Amz-Expires=300&X-Amz-Signature=059a5480e0390f2e89fa1435744a6cad9123a42a5c44b9d2e77f567b85efe22b&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=46089560&response-content-disposition=attachment%3B%20filename%3Dcontainerd-1.6.14-linux-amd64.tar.gz&response-content-type=application%2Foctet-stream [following]
--2024-08-12 16:38:30--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/46089560/d90749e7-10b0-4e43-bf46-99a51edb0149?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240812T093830Z&X-Amz-Expires=300&X-Amz-Signature=059a5480e0390f2e89fa1435744a6cad9123a42a5c44b9d2e77f567b85efe22b&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=46089560&response-content-disposition=attachment%3B%20filename%3Dcontainerd-1.6.14-linux-amd64.tar.gz&response-content-type=application%2Foctet-stream
Resolving objects.githubusercontent.com (objects.githubusercontent.com)... 185.199.111.133, 185.199.110.133, 185.199.109.133, ...
Connecting to objects.githubusercontent.com (objects.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 43434970 (41M) [application/octet-stream]
Saving to: ‘containerd-1.6.14-linux-amd64.tar.gz’

containerd-1.6.14-linux-amd64.tar.gz                 100%[=====================================================================================================================>]  41.42M  4.13MB/s    in 8.9s    

2024-08-12 16:38:39 (4.68 MB/s) - ‘containerd-1.6.14-linux-amd64.tar.gz’ saved [43434970/43434970]

```

```
sudo tar Cxzvf /usr/local containerd-1.6.14-linux-amd64.tar.gz
```
==> result:
```
bin/
bin/containerd-stress
bin/containerd-shim
bin/containerd-shim-runc-v1
bin/containerd-shim-runc-v2
bin/containerd
bin/ctr

```

## 2. Install runc
```
  wget https://github.com/opencontainers/runc/releases/download/v1.1.3/runc.amd64
  sudo install -m 755 runc.amd64 /usr/local/sbin/runc
```
==> result:
```
--2024-08-12 16:38:55--  https://github.com/opencontainers/runc/releases/download/v1.1.3/runc.amd64
Resolving github.com (github.com)... 20.205.243.166
Connecting to github.com (github.com)|20.205.243.166|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/36960321/49140741-ee77-4524-bbaf-70ec00fd6ffc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240812T093856Z&X-Amz-Expires=300&X-Amz-Signature=8b515e9ea1216d8daea3d45dee6434ae9849967aa5c308d871b25a6b5d8d4622&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=36960321&response-content-disposition=attachment%3B%20filename%3Drunc.amd64&response-content-type=application%2Foctet-stream [following]
--2024-08-12 16:38:57--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/36960321/49140741-ee77-4524-bbaf-70ec00fd6ffc?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240812T093856Z&X-Amz-Expires=300&X-Amz-Signature=8b515e9ea1216d8daea3d45dee6434ae9849967aa5c308d871b25a6b5d8d4622&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=36960321&response-content-disposition=attachment%3B%20filename%3Drunc.amd64&response-content-type=application%2Foctet-stream
Resolving objects.githubusercontent.com (objects.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.109.133, ...
Connecting to objects.githubusercontent.com (objects.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9423264 (9.0M) [application/octet-stream]
Saving to: ‘runc.amd64’

runc.amd64                                           100%[=====================================================================================================================>]   8.99M  4.02MB/s    in 2.2s    

2024-08-12 16:39:00 (4.02 MB/s) - ‘runc.amd64’ saved [9423264/9423264]
```

## 3. Download and install CNI plugins
```
  wget https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz
  sudo mkdir -p /opt/cni/bin
  sudo tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.1.1.tgz
```
==> result:
```
--2024-08-12 16:39:13--  https://github.com/containernetworking/plugins/releases/download/v1.1.1/cni-plugins-linux-amd64-v1.1.1.tgz
Resolving github.com (github.com)... 20.205.243.166
Connecting to github.com (github.com)|20.205.243.166|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://objects.githubusercontent.com/github-production-release-asset-2e65be/84575398/34412816-cbca-47a1-a428-9e738f2451d8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240812T093914Z&X-Amz-Expires=300&X-Amz-Signature=4931cd1d4bfec4a02cd69eb66e3a0f52820e2b0103a5a2baba1bee9ef50c0b42&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=84575398&response-content-disposition=attachment%3B%20filename%3Dcni-plugins-linux-amd64-v1.1.1.tgz&response-content-type=application%2Foctet-stream [following]
--2024-08-12 16:39:14--  https://objects.githubusercontent.com/github-production-release-asset-2e65be/84575398/34412816-cbca-47a1-a428-9e738f2451d8?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240812%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240812T093914Z&X-Amz-Expires=300&X-Amz-Signature=4931cd1d4bfec4a02cd69eb66e3a0f52820e2b0103a5a2baba1bee9ef50c0b42&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=84575398&response-content-disposition=attachment%3B%20filename%3Dcni-plugins-linux-amd64-v1.1.1.tgz&response-content-type=application%2Foctet-stream
Resolving objects.githubusercontent.com (objects.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to objects.githubusercontent.com (objects.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 36336160 (35M) [application/octet-stream]
Saving to: ‘cni-plugins-linux-amd64-v1.1.1.tgz’

cni-plugins-linux-amd64-v1.1.1.tgz                   100%[=====================================================================================================================>]  34.65M  2.80MB/s    in 15s     

2024-08-12 16:39:30 (2.34 MB/s) - ‘cni-plugins-linux-amd64-v1.1.1.tgz’ saved [36336160/36336160]

./
./macvlan
./static
./vlan
./portmap
./host-local
./vrf
./bridge
./tuning
./firewall
./host-device
./sbr
./loopback
./dhcp
./ptp
./ipvlan
./bandwidth
```

## 4. Configure containerd
- Create a containerd directory for the configuration file
- config.toml is the default configuration file for containerd
- Enable systemd group . Use sed command to change the parameter in config.toml instead of using vi editor
- Convert containerd into service:
```
  sudo mkdir /etc/containerd
  containerd config default | sudo tee /etc/containerd/config.toml
  sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml
  sudo curl -L https://raw.githubusercontent.com/containerd/containerd/main/containerd.service -o /etc/systemd/system/containerd.service
```
==> result:
```
[timeouts]
  "io.containerd.timeout.bolt.open" = "0s"
  "io.containerd.timeout.shim.cleanup" = "5s"
  "io.containerd.timeout.shim.load" = "5s"
  "io.containerd.timeout.shim.shutdown" = "3s"
  "io.containerd.timeout.task.state" = "2s"

[ttrpc]
  address = ""
  gid = 0
  uid = 0
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1251  100  1251    0     0   2141      0 --:--:-- --:--:-- --:--:--  2138
```

## 5. Start containerd service
```
sudo systemctl daemon-reload
sudo systemctl enable --now containerd
sudo systemctl status containerd 
```

## 6. kubelet,kubectl,kubeadm installation
```
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
sudo mkdir -p /etc/apt/keyrings/
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
```

## 7. Run kubeadm init and setup the control plane
```
  sudo kubeadm init
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
  kubectl get nodes
  kubectl get pods --all-namespaces
  kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
  kubectl get pods --all-namespaces
  kubectl get nodes
```


## Init Cluster
- Sửa file host (ở cả 3 node):
```
10.60.65.90	thong-test-kafka01
10.60.65.91	thong-test-kafka02
10.60.65.92	thong-test-kafka03
```

### Node master:
- Khởi tạo cụm k8s:
```
sudo kubeadm init --control-plane-endpoint=thong-test-kafka01
```
==> result:
```
sudo kubeadm join thong-test-kafka01:6443 --token 3tgtls.4psf3j5jvxkg67kc --discovery-token-ca-cert-hash sha256:3e954b79db731f4bea85a9c6cfce7b0f41506b893dea5ac9e339058b10171110
```
- Để tương tác với cụm với tư cách là người dùng thông thường, hãy thực hiện các lệnh sau, các lệnh này đã có sẵn ở đầu ra, chỉ cần sao chép và dán chúng.
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### Node Worker:
- Thêm node vào cụm (chạy trên các node worker):
```
sudo kubeadm join thong-test-kafka01:6443 --token 3tgtls.4psf3j5jvxkg67kc --discovery-token-ca-cert-hash sha256:3e954b79db731f4bea85a9c6cfce7b0f41506b893dea5ac9e339058b10171110
```

## notes:
- nếu ở node master ```kubectl get nodes``` mà bị:
```
E0812 16:28:30.977555  232613 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0812 16:28:30.977874  232613 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0812 16:28:30.979163  232613 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0812 16:28:30.979294  232613 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
E0812 16:28:30.980640  232613 memcache.go:265] couldn't get current server API group list: Get "http://localhost:8080/api?timeout=32s": dial tcp 127.0.0.1:8080: connect: connection refused
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```
- thì cần chạy (ở 2 node worker):
```
sudo rm /etc/containerd/config.toml
sudo systemctl restart containerd

```

# 