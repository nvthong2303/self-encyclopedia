# Cloud Computing

- Là mô hình truy cập qua mạng để lựa chọn và sử dụng tài nguyên để có thể tính toán thuận tiện và nhanh chóng, quản lý tài nguyên.
- Mô hình 5-4-3:
  - 5 đặc tính:
    - Repid Elasticity: Thu hồi và cấp phát tài nguyên nhanh chóng
    - Broad Network Access: Truy cập qua các chuẩn mạng
    - Measured Service: dịch vụ sử dụng đo đếm được
    - On-demand Self-service: khả năng tự phục vụ
    - Resource Pooling: chia sẻ tài nguyên
  - 4 mô hình dịch vụ:
    - Public Cloud: cho phép cá nhân / tổ chức thuê, dùng chung tài nguyên
    - Private Cloud: dùng cho doanh nghiệp, không chia sẻ ra bên ngoài
    - Hybrid Cloud: kết hợp 2 loại trên
  - 3 mô hình triển khai:
    - Infrastructure as a Service (IaaS): Hạ tầng như dịch vụ
    - Platform as a Service (PaaS): Nền tảng như dịch vụ
    - Software as a Service (SaaS): Phần mềm như dịch vụ

# Openstack

- Opensource cho Cloud Computing, hỗ trợ cả public cloud và private cloud.
- Các thành phần chính:
  #### Compute
  - **Nova** (Compute Service): thành phần cơ bản nhất, phức tạp nhất trong openstack, nó giao tiếp với các công cụ ảo hóa, quản lý các máy ảo thông qua API. Chạy ngầm trên máy chủ linux, với các công nghệ ảo hóa như KVM, Vmware, Hyper-V và các công nghệ container như LXC (Linux Containers) và LXD (Linux Daemon). ~ EC2, Hyper-v, KVM, Vmware, ...

  - **Zun** (Containers Service): thành phần quản lý container, cho phép triển khai container mà không cần quản lý cụm. ~ Docker, Podman, Rkt, ...

  #### Hardware lifecycle
  - **Ironic** (Bare MEtal Provisioning Service): cung cấp dịch vụ quản lý và triển khai máy vật lý trong openstack, cho phép triển khai các OS trực tiếp lên hardware mà không cần ảo hóa. ~ Foreman, Cobbler, ...

  - **Cyborg** (Lifecycle manager of accelerators): dịch vụ quản lý các tài nguyên GPU, FPGA, ...

  #### Storage
  - **Swift** (Object store): dịch vụ lưu trữ Object, phân tán, cho phép lưu trữ và truy cập dữ liệu dưới dạng object thông qua restapi. ~ S3, MinIO, ...

  - **Cinder** (Block Storage): dịch vụ cung cấp lưu trữ cho các instance, quản lý các volume, các snapshot của volume, cho phép attach/detach các volume vào instance. ~ EBS

  - **Manila** (Shared filesystems): cung cấp dịch vụ lưu trữ file system, hỗ trợ nhiều loại file khác nhau. ~ EFS, NFS, ...

  #### Networking
  - **Neutron** (Networking): cung cấp dịch vụ mạng cho Openstack, bao gồm quản lý private network, public network, router, NAT, firewall. ~ VPC, 
  - **Octavia** (Load balancer): cung cấp dịch vụ loadbalancer trong openstack. ~ ELB, 
  - **Designate** (DNS service): cung cấp dịch vụ quản lý DNS, tự động cập nhật khi tài nguyên thay đổi. ~ 

  #### Shared Service
  - **Keystone** (Identity service): chịu trách nhiệm về tất cả các authentication và authorization trong Openstack. ~ IAM, ...
  - **Placement** (Placement service): dịch vụ cung cấp API HTTP để theo dõi việc sử dụng và kiểm kê tài nguyên, giúp các dịch vụ khác quản lý và phân bổ tài nguyên một cách hiệu quả. ~ kube-scheduler, EC2-auto scaling, ...
  - **Glance** (Image service): chịu trách nhiệm đăng ký, lưu trữ và truy xuất images của các máy ảo. ~ dockerhub, ...
  - **Barbican** (Key management): dịch vụ quản lý key, cung cấp khả năng lưu trữ, quản lý an toàn dữ liệu secret. ~ KMS, Vault,, ...

  #### Orchestration
  - **Heat** (Orchestration): cung cấp dịch vụ theo yêu cầu với khả năng tự động scale tài nguyên. Heat điều phối tài nguyên cs hạ tầng dưới dạng code, cung cấp restAPI và queryAPI. Cung cấp dịch vụ auto-scaling. ~ Terraform, AWS CloudFormation, ...
  - **Mistral** (Workflow service): cung cấp dịch vụ tự động hóa workflow, có thể mô tả flow theo dạng tập hợp các task và task-relations, dưới dạng các file .yaml và Mistral quản lý, thực hiện chúng một cách chính xác, song song hoặc đông thời, HA. ~ AWS Step Functions, Apache Airflow, ...
  - **Zaqar** (Messaging Service): Message queue. ~ Kafka, RabbitMQ, SQS, ...
  - **Blazar** (Resource reservation service): dịch vụ đặt trước tài nguyên, cho phép người dùng đặt trước 1 lượng tài nguyên cụ thể, trong thời gian nhất định, có thể thuê dựa trên tài nguyên đã đặt trước. ~ Kube-Scheduler, AWS-Reserved Instance, ...
  - **Aodh** (Alarming Service): cho phép kích hoạt các hành động từ xa dựa trên các quy tắc đã xác định đối với dữ liệu mẫu hoặc sự kiện do Ceilometer thu thập. Cảnh báo dựa trên số liệu. ~ Cloud Watch Alert, ...
  

  #### Workload Provisioning
  - **Magnum** (Container Orchestration Engine Provisioning): công cụ điều phối container ~ docker swarm, k8s, ... dưới dạng tài nguyên trong openstack. Sử dụng Heat để sắp xếp image OS chứa Docker và K8s đồng thời chạy image đó trong VM hoặc máy vật lý. ~ K8s, DockerSwarm, Mesos, ...
  - **Trove** (Database as a Service): cung cấp database sql và no-sql dưới dạng dịch vụ. ~ RDS, GC SQL, ...
  

  #### Application lifecycle
  - **Masakari** (Instances High Availability Service): dịch vụ H/A cho các dịch vụ khác bằng cách tự động khôi phục sau thảm họa. ~ EC2 Auto Recovery, ...

  #### Web frontends
  - **Horizon** (Dashboard): ~ AWS Management Console, Google Cloud Console, Azure Portal. Cung cấp giao diện cho người dùng để quản lý openstack và tài nguyên
  - **Skyline** (Next generation dashboard (emerging technology)): ~ Datadog, New Relic, Prometheus, Grafana. Dịch vụ giám sát và phân tích hiệu suất tài nguyên và tối ưu hóa tài nguyên.

  #### Operation Tooling
  - **Senlin** (Cluster Service): dịch vụ quản lý cụm trong openstack, cho phép tạo, tự động hóa và quản lý các cụm tài nguyên.
  - **Murano** (Application Catalog): cung cấp 1 catalog ứng dụng để người dùng soạn và triển khai các môi trường tổng hợp ở mức trìu tượng hóa ứng dụng trong khi quản lý lifecylce của ứng dụng.
  - **Ceilometer** (Metering & Data Collection Service): cung cấp dịch vụ thu thập metrics, và log từ các thành phần khác trong openstack.
  - **Freezer** (Backup/Restore): cung cấp dịch vụ sao lưu và khôi phục dữ liệu.
  - **Watcher** (Resource Optimization): tối ưu hóa tài nguyên như Compute, Storage, Network.
  - **Vitrage** (Root Casuse Analysis): dịch vụ phân tích và xác định nguyên nhân các sự cố.
  - **Sahara** (Big Data Processing Framework Provisioning): dịch vụ xử lý data, hỗ trợ triển khai các cụm xử lý BigData như hadoop, spark.