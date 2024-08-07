# Kubernetes

## Giới thiệu
## Các thành phần
### Pod:
Là thành phần cơ bản nhất để deploy và run 1 application trên k8s, được dùng để nhóm và chạy một hoặc nhiều Container lại với nhau trên cùng một server. Những container trong một pod chia sẻ chung tài nguyên.
Pod cung cấp các tính năng so với Container:
* nhóm tài nguyên của container
* kiểm tra container còn hoạt động không, nếu không thì restart
* chắc chắn ứng dụng trong container run mới gửi yêu cầu xử lý tới
* cung cấp lifecycle

#### sử dụng label để phân biệt, tổ chức và phân biệt các pod
gán label để phân biệt các pod.

#### namespace
Namespace là cách để chia tài nguyên của cluster, nhóm các repsource liên quan lại với nhau (~ sub-cluster).


### Replica Controller (RC):
Thành phần quản lý số lượng pod, duy trì số lượng bản sao của pod trong 1 cluster. Tự động tạo / hủy pod để duy trì số lượng pod mong muốn.

Selector Flexibility: Sử dụng bộ lựa chọn bình đẳng.
Label Matching: dùng matchLabels 

Cấu trúc: label, replica count, pod template.

Khi thay đổi template pod, nó sẽ không apply cho những pod hiện tại, mà muốn pod hiện tại cập nhập template mới thì cần xóa pod hoặc xóa cả rc.


### ReplicaSets (RS):
Thay thế RC, linh hoạt hơn, cung cấp các tính năng nâng cao hơn

Selector Flexibility: Sử dụng bộ lựa chọn linh hoạt hơn. 
Label Matching: dùng matchExpressions, linh hoạt hơn ở phần label selector

### DaemonSets:
Dùng DaemonSets để chạy chính xác một pod trên một worker node. Tương tự như RS, nó cũng giám sát và quản lý pod theo labels, nhưng RS có thể deploy pod ở bất cứ node nào, trong 1 node chạy mấy pod cũng được còn DaemonSets sẽ deploy tới mỗi thằng node một pod duy nhất, chắc chắn có bao nhiêu node sẽ có bấy nhiêu pod, không có thuộc tính replica. --> Ứng dụng trong Logging và Monitoring ở mỗi node 


### Services

#### ClusterIP:
Tạo ra một IP và local DNS mà có thể truy cập bên trong Cluster. Chỉ có thể truy cập được bên trong cluster. Có nghĩa là chỉ có các Pod trong cùng một cụm có thể truy cập lẫn nhau thông qua ClusterIP

#### NodePort
Cho phép truy cập từ bên ngoài cluster thông qua một port cụ thể  (30000 - 32767), Sử dụng địa chỉ IP của node để truy cập các Pod thuộc Service.


#### ExternalName
Service cho phép ánh xạ một tên miền bên ngoài với một service , không sử dụng Pod nào, thay vào đó sử dụng tên miền để truy cập tt vào một dịch vụ bên ngoài cluster.

#### LoadBalancer
Cung cấp cân bằng tải và khả năng truy cập từ bên ngoài cluster thông qua một IP public. Có thể truy cập từ bên trong và bên ngoài cluster.

#### Ingress resource
resource cho phép expose HTTP và HTTPS routes từ bên ngoài cluster tới service bên trong cluster (giúp gán 1 domain thật tới service bên trong cluster)



## Giới thiệu

