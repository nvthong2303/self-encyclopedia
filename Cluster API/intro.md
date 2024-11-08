# Cluster API
## Introduction:
- Công cụ đơn giản hóa việc quản lý vòng đời của cụm Kubernetes trên các hạ tầng khác nhau như AWS, Azure, GCP, ... hoặc on-premises.
- cho phép quản lý các cụm Kubernetes thông qua các API chuẩn k8s (triển khai, nâng cấp, quản lý cụm)
- Cluster API hoạt động như một operator trên Kubernetes

## Các thành phần:
- Gồm các thành phần chính:
	- Management Cluster: Cụm K8S dùng để quản lý các cụm K8S khác
	- Target Cluster: Các cụm K8S mà bạn muốn quản lý, mỗi cụm này được xem là 1 object trong API của K8S.
- các Controller cuả Cluster API nằm trên Management Cluster và quản lý vòng đời của các cụm bằng cách xử lý các custom resource definitions:
	- Cluster: Tài nguyên trung tâm, đại diện cho toàn cụm
	- Machine: Worker node
	- Machine Sets: Đảm bảo một tập hợp các worker node ổn định mọi thời điểm.
	- MachineDeployment: Quản lý vòng đời và khả năng mở rộng của một node group.

## Các tính năng:
- Các tính năng với cụm:
	- auto provisioning
	- auto upgrade
	- auto healing
	- auto scaling
	- auto discovering
	- native networking
	- event logging
- Quản lý theo CRD
- Hỗ trợ đa hạ tầng

## Cách hoạt động:
- Đầu tiên, cần 1 cụm kubernetes trước (cụm workload - dùng quản lý)
