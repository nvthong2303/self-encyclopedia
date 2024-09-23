## 1: PV - PVC - Pod
Create a Persistent Volume called log-volume. It should make use of a storage class name manual. It should use RWX as the access mode and have a size of 1Gi. The volume should use the hostPath /opt/volume/nginx

Next, create a PVC called log-claim requesting a minimum of 200Mi of storage. This PVC should bind to log-volume.

Mount this in a pod called logger at the location /var/www/nginx. This pod should use the image nginx:alpine.

### answer:
#### create Persistent Volume:
```
apiVersion: v1
kind: PersistentVolume
metadata:
    name: log-volume
spec:
    capacity:
        storage: 1Gi
    storageClassName: manual
    accessModes:
        -   ReadWriteMany
    persistentVolumeReclaimPolicy: Recycle
    hostPath:
        path: /opt/volume/nginx
```
#### create PVC:
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
    name: log-claim
spec:
    resources:
        request:
            storage: 200Mi
    accessModes:
        -   ReadWriteMany
    storageClassName: manual
```
#### create Pod:
```
apiVerssion: v1
kind: Pod
metadata:
    name: logger
spec:
    containers:
        -   name: logger
            image: nginx:alpine
            volumeMounts:
                -   mountPath: /var/www/nginx
                    name: log
    volumes:
        -   name: log
            persistentVolumeClaim:
                claimName: log-claim
```



## 2: Pod - Service ClusterIP
We have deployed a new pod called secure-pod and a service called secure-service. Incoming or Outgoing connections to this pod are not working.
Troubleshoot why this is happening.

Make sure that incoming connection from the pod webapp-color are successful.

Important: Don't delete any current objects deployed.

### answer:
- Thêm phần thông tin port đc expose

## 3: ConfigMaps - Pod:
Create a pod called time-check in the dvl1987 namespace. This pod should run a container called time-check that uses the busybox image.
- Create a config map called time-config with the data TIME_FREQ=10 in the same namespace.
- The time-check container should run the command: while true; do date; sleep $TIME_FREQ;done and write the result to the location /opt/time/time-check.log.
- The path /opt/time on the pod should mount a volume that lasts the lifetime of this pod.

### answer:
- create namespace dvl1987: ```kubectl create namespace dvl1987```
#### create config map:
```
apiVersion: v1
kind: ConfigMap
metadata:
    name: time-config
    namespace: dvl1987
data:
    TIME_FREQ: 10
```
#### create pod:
```
apiVersion: v1
kind: Pod
metadata:
    name: time-check
    namespace: dvl1987
spec:
    containers:
        -   name: time-check
            image: busybox
            commamd:
                -   /bin/sh
                -   -c
                -   |
                    while true; do
                        date >> /opt/time/time-check.log;
                        sleep $TIME_FREQ;
                    done
            env:
                -   name: TIME_FREQ
                    valueFrom:
                        configMapKeyRef:
                            name: time-config
                            key: TIME_FREQ
            volumeMounts:
                -   name: time-volume
                    mountPath: /opt/time
    volumes:
        -   name: time-volume
            emptyDir: {}
```

## 4: Deployment - update - rollout:
Create a new deployment called nginx-deploy, with one single container called nginx, image nginx:1.16 and 4 replicas.
The deployment should use RollingUpdate strategy with maxSurge=1, and maxUnavailable=2.

Next upgrade the deployment to version 1.17.

Finally, once all pods are updated, undo the update and go back to the previous version.

### answer:
#### create deployment:
```
apiVersion: apps/v1
kind: Deployment
metadata:   
    name: nginx-deploy
    labels:
        app: nginx
spec:
    replicas: 4
    selector:
        matchLabels:
            app: nginx
    template:
        metadata:
            labels:
                app: nginx
        spec:
            -   name: nginx
                image: nginx:1.16
                ports:
                    -   containerPort: 80

```
#### update image:
- ```kubectl set image deployment/nginx-deploy nginx=nginx:1.17```
#### roll back:
- ```kubectl rollout undo deployment/nginx-deploy```


## 5: request CPU - limit:
Create a redis deployment with the following parameters:

Name of the deployment should be redis using the redis:alpine image. It should have exactly 1 replica.

The container should request for .2 CPU. It should use the label app=redis.

It should mount exactly 2 volumes.

a. An Empty directory volume called data at path /redis-master-data.

b. A configmap volume called redis-config at path /redis-master.

c. The container should expose the port 6379.


The configmap has already been created.

### answer:
### create deployment:
```
apiVersion: apps/v1
kind: Deployment
metadata:
    name: redis
    labels:
        app: redis
spec:
    replicas: 1
    selector:
        matchLabels:
            app: redis
    template:
        metadata:
            labels:
                app: redis
        spec:
            containers:
                -   name: redis
                    image: redis:alpine
                    resources:
                        requests:
                            cpu: "0.2"
                    ports:
                        -   containerPort: 6379
                    volumeMounts:
                        -   name: data
                            mountPath: /redis-master-data
                        -   name: redis-config
                            mountPath: /redis-master
            volumes:
                -   name: data
                    emptyDir: {}
                -   name: redis-config
                    configMap:
                        name: redis-config
```

