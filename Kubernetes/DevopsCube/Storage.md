# Storage

## 1. Volume
- tương tự khái niệm volume trong docker

## 2. PersistantVolume (PV)
- Là phân vùng dùng để lưu trữ, được cấp phát trên một hệ thống lưu trữ nhất định, được thực hiện thủ công với admin hoặc qua StorageClass.
- PV sẽ không thuộc về 1 namespace nào, trong k8s tồn tại 2 loại resource: **namesapce resource** và **cluster resource**. 
- Là resource của k8s (khác với tài nguyên của namespace như Pod, RS, RC, ...), tương tự như node.
- Đc sử dụng như một Volume Plugins, vòng đời của nó độc lập với Pod, khi tạo PV, admin chỉ cần quan tâm tới size, access_mode của nó.
- Các loại access_mode:
    - ReadWriteOnce (RWO): có thể được mount bởi một node, volome này có thể được truy cập bởi nhiều Pod với điều kiện các Pod này cùng chạy trên đó.
    - ReadOnlyMany (ROX): được mount dưới dạng ReadOnly bởi nhiều node.
    - ReadWriteMany (RWX): được mount dưới dạng ReadWrite bởi nhiều node.
    - ReadWriteOncePod (RWOP): được mount dưới dạng ReadOnly bởi 1 pod.

PV.yaml
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mongodb-pv
spec:
  capacity:
    storage: 10Gi # size of the storage
  accessModes: # access mode
    - ReadWriteOnce # can be mounted by a single wokrer node for reading and writing
    - ReadOnlyMany # can be mounted by a multiple wokrer node for reading only
  persistentVolumeReclaimPolicy: Retain
  gcePersistentDisk:
    pdName: mongodb
    fsType: ext4
```

## 3. PersistantVolumeClaim (PVC)
- PVC là 1 phân vùng lưu trữ, tiêu thụ sử dụng tài nguyên PV, tương tự như Pod trong Node.
- Pod yêu cầu tài nguyên nhất định về CPU, Memory mà Node cần cấp phát cho nó.

PVC.yaml
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongodb-pvc
spec:
  resources:
    requests:
      storage: 10Gi # request 10Gi storage
  accessModes:
    - ReadWriteOnce # only allow one node can be read and write
  storageClassName: ""
```

## Gán PV cho PVC (Binding)
- Khi một PVC được yêu cầu, với size và access_mode nhất định, ban đầu nó ở trạng thái **Unbound**, Controller của cluster sẽ tìm PV nào "match" với yêu cầu này, và gán nó lại với nhau. lúc này trạng thái của PVC sẽ là **Bound**. Còn nếu 1 PV được tạo động thì nó được gán luôn cho PVC đó.

## Cơ chế Reclaiming
- thuộc tính **persistentVolumeReclaimPolicy** có 3 giá trị: Retain, Recyvle và Delete
    - Retain: khi PVC xóa, PV vẫn tồn tại và ở trạng thái **release**, tuy nhiên vẫn chưa ready cho các PVC khác nên dữ liệu bên trong còn nguyên. Admin có thể thu hồi lại dung lượng của volume bằng cách xóa PV.
    - Recycle: khi PVC xóa, PV vẫn ở đó nhưng dữ liệu đã mất, trạng thái sẽ là available để có thể bind PVC khác.
    - Delete: khi PVC xóa, xóa luôn PV và dữ liệu được lưu trữ.

## 4. StorageClass
- Là tài nguyên của cluster resource, tương tự PV hoặc node.
- Cách mà administrator setup trước PV hoặc PVCs gọi là pre provisioning, còn cách tự động gọi là Dynamic provisioning. Để tự động, cần sử dụng StorageClass.
- Đây là resource tự động tạo PV, chỉ cần tạo SC 1 lần thay vì config và tạo 1 đống PV.


## 5. Provisioner
- Mỗi StorageClass có một Provisioner định nghĩa plugin nào sử dụng để tạo ra các PV tương ứng.