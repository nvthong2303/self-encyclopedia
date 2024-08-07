- Tại sao phải có Service ? Pods are ephemeral (phù du) có nghĩa là nó được sinh ra / loại bỏ bất cứ lúc nào, đồng nghĩa IP của nó cũng bị thay đổi.
--> Service sẽ tạo ra một single / constant point của một nhóm Pod, mỗi service chỉ có 1 IP và Port không đổi, Client sẽ mở kết nối đến service, connection đc forward đến 1 pod phía sau nó.


