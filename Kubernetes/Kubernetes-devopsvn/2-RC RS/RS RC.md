- đều là resource ra đời với mục đích quản lý các pods, chăc chắn số lượng pod nó quản lý và không thay đổi , keep running.
- RC sẽ tạo ra số lượng pod bằng với số ta chỉ định ở thuộc tính replicas và quản lý pod thông qua labels của pod
- nó sẽ giám sát và tự động restart container khi fail, nó luôn đảm bảo ứng dụng availablility nhất có thể, có thể tăng perfomance bằng cách chỉ định số lượng replicas.
- khi thay đổi template trong RC, nó sẽ không apply cho những thằng đang chạy, muốn cập nhật template mới phải xóa hết pod hoặc xóa cả RC

- RS tương tự RC, là phiên bản mới hơn, linh hoạt hơn ở phần label selector, trong khi label selector thằng RC chỉ có thể chọn pod giống hoàn toàn  thì thằng RS có thể sử dụng một số expression hoặc matching, regex, ...

- DaemonSets:  giống như 2 thằng trên, nhưng thằng RS thì pod có thể deploy ở bất cứ node nào và trong một node có thể chạy mấy pod cũng được. CÒn thằng DaemonSets này chỉ định mỗi node một pod duy nhất. --> không có thuộc tính replicas, sử dụng để logging hoặc monitoring.

