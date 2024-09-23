## 1: Auto Restart Container:
We have deployed a few pods in this cluster in various namespaces. Inspect them and identify the pod which is not in a Ready state. Troubleshoot and fix the issue.

Next, add a check to restart the container on the same pod if the command ls /var/www/html/file_check fails. This check should start after a delay of 10 seconds and run every 60 seconds.

You may delete and recreate the object. Ignore the warnings from the probe.

### answer:
#### troubleShooting:

#### auto restart container:
```
apiVersion: v1
kind: Pod
metadata:   
    name: name_
    namespace: ns_
spec:
    containers:
        -   name: name_
            image: image_
            livenessProbe:
                exec:
                    command:
                        -   /bin/sh
                        -   -c
                        -   ls /var/www/html/file_check
                    initialDelaySeconds: 10
                    periodSeconds: 60

```

## 2: CronJob:
Create a cronjob called dice that runs every one minute. Use the Pod template located at /root/throw-a-dice. The image throw-dice randomly returns a value between 1 and 6. The result of 6 is considered success and all others are failure.

The job should be non-parallel and complete the task once. Use a backoffLimit of 25.

If the task is not completed within 20 seconds the job should fail and pods should be terminated.

You don't have to wait for the job completion. As long as the cronjob has been created as per the requirements.

### answer:
#### create cronjob:
```
apiVersion: batch/v1
kind: CronJob
metadata:
    name: dice
spec:
    schedule: "* * * * *"
    jobTemplate:
        spec:
            backofflimit: 25
            activeDeadlineSeconds: 20
            completions: 1
            parallelism: 1
            template:
                spec:
                    containers:
                        -   name: throw-dice
                            image: throw-dice
                    restartPolicy: Never
```

## 3: Pod:
Create a pod called my-busybox in the dev2406 namespace using the busybox image. The container should be called secret and should sleep for 3600 seconds.

The container should mount a read-only secret volume called secret-volume at the path /etc/secret-volume. The secret being mounted has already been created for you and is called dotfile-secret.

Make sure that the pod is scheduled on controlplane and no other node in the cluster.

### answer:
- create namespace: ```kubectl create namespace dev2406```
#### create pod:
```
apiVersion: v1
kind: Pod
metadata:
    name: my-busybox
    namespace: dev2406
spec:
    containers:
        -   name: secret
            image: busybox
            command: ["sleep", "3600"]
            volumeMounts:
                -   name: secret-volume
                    mountPath: /etc/secret-volume
                    readOnly: true
    volumes:
        -   name: secret-volume
            secret:
                secretName: dotfile-secret
    nodeSelector:
        kubernetes.io/hostname: controlplane
```

## 4: Ingress:
Create a single ingress resource called ingress-vh-routing. The resource should route HTTP traffic to multiple hostnames as specified below:
- The service video-service should be accessible on http://watch.ecom-store.com:30093/video
- The service apparels-service should be accessible on http://apparels.ecom-store.com:30093/wear

To ensure that the path is correctly rewritten for the backend service, add the following annotation to the resource:
    nginx.ingress.kubernetes.io/rewrite-target: /
Here 30093 is the port used by the Ingress Controller

### answer
- create Ingress resource:
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
    name: ingress-vh-routing
    annotations:
        nginx.ingress.kubernetes.io/rewrite-target: /
spec:
    rules:
        -   host: watch.ecom-store.com
            http:
                paths:
                -   path: /video
                    pathType: Prefix
                    backend:
                        service:
                            name: video-service
                            port:
                                number: 80
        -   host: apparels.ecom-store.com
            http:
                paths:
                -   path: /wear
                    pathType: Prefix
                    backend:
                        service:
                            name: apparels-service
                            port:
                                number: 80
    ingressClassName: nginx
```


## 5
A pod called dev-pod-dind-878516 has been deployed in the default namespace. Inspect the logs for the container called log-x and redirect the warnings to /opt/dind-878516_logs.txt on the controlplane node

### answer:
- ssh to controlplane.
- get logs: ```kubectl logs -f dev-pod-dind-878516 -c log -x -n default | grep "warning" > /opt/dind-878516_logs.txt```
