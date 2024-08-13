# Job

## 1. Job trong k8s:
- Trong quá trình vận hành, cần nhiều tác vụ chạy 1 lần hoặc theo định kỳ như backup database, report resource, ...
- K8s sinh ra resource Job
- Job tạo ra bên trong các Pod, các Pod tạo ra khi có các Job, sau khi kết thúc thì Job xóa, Pod cũng bị xóa theo. Nếu Pod chưa hoàn thành Job mà bị lỗi / xóa thì tạo Pod khác để thi hành tác vụ.

example.yaml:
```
apiVersion: batch/v1
kind: Job
metadata:
  name: myjob
spec:
  # Số lần chạy POD thành công
  completions: 10
  # Số lần tạo chạy lại POD bị lỗi, trước khi đánh dấu job thất bại
  backoffLimit: 3
  # Số POD chạy song song
  parallelism: 2
  # Số giây tối đa của JOB, quá thời hạn trên hệ thống ngắt JOB
  activeDeadlineSeconds: 120

  template:
    spec:
      containers:
      - name: busybox
        image: busybox
        command:
          - /bin/sh
          - -c
          - date; echo "Job executed"
      restartPolicy: Never
```


## 2. CronJob:
- Giống như trong linux, CronJob trong k8s cũng dùng để chạy các tác vụ tại một thời điểm cụ thể hoặc tại các khoảng thời gian được quy định.

example.yaml
```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: mycronjob
spec:
  # Một phút chạy một Job
  schedule: "*/1 * * * *"
  # Số Job lưu lại
  successfulJobsHistoryLimit: 3
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: busybox
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo "Job in CronJob"
          restartPolicy: Never
```
