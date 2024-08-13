# StatefulSets
- Đã có Pod, RC, RS, Deployment để deploy các ứng dụng stateless application (các ứng dụng không lưu trữ bất cứ thứ gì, khi restart hoặc xóa đi tạo lại hoạt động bình thường mà không bị ảnh hưởng bởi yếu tố bên ngoài, không ảnh hưởng đến người dùng )
- Stateful application ? Nó là những ứng dụng yêu cầu lưu trữ trạng thái của chính nó, dữ liệu, ... . Ví dụ: các loại Database, ....

## 1. Hạn chế khi dùng RS để deploy stateful application:
tham khảo tại:  https://viblo.asia/p/kubernetes-series-bai-9-statefulsets-deploying-replicated-stateful-applications-07LKXkXp5V4



## 2. StatefulSets:
- là một resource tương tự RS, khác ở chỗ Pod của SS được định danh chính xác và mỗi thằng sẽ có một stable network identify. Mỗi Pod được tạo sẽ được gán với 1 index, nó sẽ dùng để định dạnh cho Pod.
- Khi một Pod bị fail, thằng SS sẽ tạo ra 1 Pod mới thay thê Pod cũ như RS nhưng Pod mới này sẽ có tên, hostname như Pod cũ.

## 3. StatefulSets scale Pod:
- Khi scale up, SS sẽ tạo ra 1 Pod mới có index tiếp theo index hiện tại. Tương tự khi scale down.
- 

## 4. Storage trong SS:
- tương tự như cách scale up, khi tạo pod, thì storage ứng với nó cũng được đánh index tương tự, nên khi scale up hoặc down thì vẫn giữ nguyen storage mà không cần tạo mới và không xóa storage khi scale down.
- SS làm việc với PVC bằng cách tạo PVC cho mỗi Pod, gắn nó và đánh index nó vào Pod tương ứng.




