# IP Addressing

## Địa chỉ IP

### các loại địa chỉ IP

- IP v4 và IP v6
- IP publc và IP private
- IP loopback

- DHCP: cấp phát địa chỉ IP động cho các thiết bị trong mạng nội bộ tự động.

## Phân bổ địa chỉ IP

### Classful Networking:

- Classful Networking là một phương pháp cũ để phân bổ địa chỉ IP dựa trên các lớp cố định, mỗi lớp có kích thước và số lượng địa chỉ cụ thể:

  - Lớp A:
    - Phạm vi địa chỉ IP: 0.0.0.0 đến 127.255.255.255
    - Mặt nạ subnet mặc định: 255.0.0.0 (hoặc /8)
    - Số lượng địa chỉ IP: Khoảng 16 triệu địa chỉ (2^24 - 2 địa chỉ cho mạng và broadcast).
    - Ví dụ địa chỉ: 10.0.0.0 (Lớp A)

  - Lớp B:
    - Phạm vi địa chỉ IP: 128.0.0.0 đến 191.255.255.255
    - Mặt nạ subnet mặc định: 255.255.0.0 (hoặc /16)
    - Số lượng địa chỉ IP: Khoảng 65,536 địa chỉ (2^16 - 2 địa chỉ cho mạng và broadcast).
    - Ví dụ địa chỉ: 172.16.0.0 (Lớp B).

  - Lớp C:
    - Phạm vi địa chỉ IP: 192.0.0.0 đến 223.255.255.255
    - Mặt nạ subnet mặc định: 255.255.255.0 (hoặc /24)
    - Số lượng địa chỉ IP: Khoảng 256 địa chỉ (2^8 - 2 địa chỉ cho mạng và broadcast).
    - Ví dụ địa chỉ: 192.168.1.0 (Lớp C).

  - Lớp D:
    - Phạm vi địa chỉ IP: 224.0.0.0 đến 239.255.255.255
    - Chức năng: Được sử dụng cho multicast, không dành cho host.
    - Ví dụ địa chỉ: 224.0.0.1.

  - Lớp E:
    - Phạm vi địa chỉ IP: 240.0.0.0 đến 255.255.255.255
    - Chức năng: Được dành cho mục đích nghiên cứu và phát triển (Experimental), không được sử dụng cho các mạng thông thường.
    - Ví dụ địa chỉ: 240.0.0.1.

- Nhược điểm:
  - Lãng phí tài nguyên IP
  - Thiếu linh hoạt trong phân chia mạng
  - Bảng định tuyến lớn

### CIDR:

- CIDR (Classless Inter-Domain Routing) là một phương pháp phân bổ và định tuyến IP được sử dụng thay thế cho Classful Networking cho phép quản lý và phân bổ IP linh hoạt hơn, tối ưu hóa việc sử dụng tài nguyên.
- Khái niệm:
  - CIDR cho phép các mạng được định nghĩa không theo các lớp truyền thống (Class A, B, C) mà sử dụng một hệ thống phân chia linh hoạt hơn, dựa trên mặt nạ subnet (subnet mask).
  - CIDR sử dụng cú pháp /prefix_length để xác định phạm vi địa chỉ IP, trong đó prefix_length là số bit của phần mạng trong địa chỉ IP.
- Cú pháp:
  - Địa chỉ IP/PREFIX là cú pháp chính của CIDR. Ví dụ, 192.168.0.0/16:
    - 192.168.0.0 là địa chỉ mạng.
    - /16 là độ dài của phần mạng (prefix length), tức là 16 bit đầu tiên của địa chỉ IP dùng để xác định mạng.
- Lợi ích của CIDR:
  - Sử dụng hiệu quả địa chỉ IP: CIDR cho phép tạo các mạng con với kích thước chính xác theo nhu cầu, giảm lãng phí địa chỉ IP.
  - Giảm tải bảng định tuyến: CIDR cho phép gộp nhiều mạng con lại thành một mục duy nhất trong bảng định tuyến (route aggregation), giúp đơn giản hóa và tối ưu hóa định tuyến.
  - Tùy chỉnh linh hoạt: CIDR không bị ràng buộc bởi các lớp mạng cố định như Class A, B, C, cho phép tạo ra các mạng với kích thước khác nhau.


## SubNet:
