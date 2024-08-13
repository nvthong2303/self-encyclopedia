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
  - Nova (Compute Service): thành phần cơ bản nhất, phức tạp nhất trong openstack, nó giao tiếp với các công cụ ảo hóa, quản lý các máy ảo thông qua API. Chạy ngầm trên máy chủ linux, với các công nghệ ảo hóa như KVM, Vmware, Hyper-V và các công nghệ container như LXC (Linux Containers) và LXD (Linux Daemon).
  - Zun (Containers Service):
  #### Hardware lifecycle
  - Ironic (Bare MEtal Provisioning Service):
  - Cyborg (Lifecycle manager of accelerators):
  #### Storage
  - Swift (Object store):
  - Cinder (Block Storage):
  - Manila (Shared filesystems):
  #### Networking
  - Neutron (Networking):
  - Octavia (Load balancer):
  - Designate (DNS service):
  #### Shared Service
  - Keystone (Identity service):
  - Placement (Placement service):
  - Glance (Image service):
  - Barbican (Key management):
  #### Orchestration
  - Heat (Orchestration):
  - Mistral (Workflow service):
  - Zaqar (Messaging Service):
  - Blazar (Resource reservation service):
  - Aodh (Alarming Service):
  #### Workload Provisioning
  - Magnum (Container Orchestration Engine Provisioning):
  - Trove (Database as a Service):
  #### Application lifecycle
  - Masakari (Instances High Availability Service):
  #### Web frontends
  - Horizon (Dashboard):
  - Skyline (Next generation dashboard (emerging technology)):
