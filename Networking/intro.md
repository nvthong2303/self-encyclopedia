# Networking

## Mô hình OSI / TCP-IP

### 1. Mô hình OSI
- mô hình tham chiếu cho mạng kết nối mở, đc koi là mô hình tiêu chuẩn dưới dạng phân cấp theo các tầng, các giao thức riêng biệt. Được tô 
- mặc dù internet hiện tại không còn tuân thủ tiêu chuẩn nghiêm ngặt của OSI . Nhưng mô hình OSI vẫn hữu ích.
- Mô hình OSI chia giao tiếp thành 7 lớp, lớp 1 -> 4 là cấp thấp. Từ lớp 5 -> 7 là lớp cấp cao

#### Lớp ứng dụng:
- Nhiệm vụ: cung cấp interface cho các ứng dụng, tương tác trực tiếp với các application.
- Giao thức phổ biến: HTTP, HTTPS, SMTP, FTP, POP, DHCP, DNS,...


#### Lớp trình bày:
- Nhiệm vụ: phiên dịch, định dạng, mã hóa/giải mã, nén/giải nén dữ liệu.
- Giao thức phổ biến: SSL/TLS. 

#### Lớp phiên:
- Nhiệm vụ: mở và đóng kết nối giữa 2 thiết bị. Đảm bảo kết nối đủ lâu để truyền tất cả dữ liệu, sau đó đóng kết nối. Đồng bộ việc kiểm tra (chỉ gửi lại từ gói tin bắt đầu lỗi, tránh gửi lại từ đầu, hạn chễ lãng phí tài nguyên ). Quản lý kết nối giữa 2 thiết bị
- Giao thức phổ biến: 

#### Lớp vận chuyển:
- Nhiệm vụ: Chịu trách nhiệm về giao tiếp đầu cuối giữa 2 thiết bị, bao gồm việc lấy dữ liệu từ lớp Phiên , chia nhỏ thành các Segmentation rồi chuyển tiếp đến lớp Mạng. Chịu trách nhiệm lắp ráp lại các phần từ lớp Mạng để chuyển tiếp lên lớp Phiên. Cũng kiểm soát luồng và kiểm soát lỗi, xác định tốc độ truyền để đảm bảo người gửi và người nhận kết nối vừa đủ, không quá chậm . Đảm bảo dữ liệu nhận được đầy đủ bằng cách gửi lại yêu cầu với những gói tin bị mất
- Giao thức phổ biến: TCP, UDP.

#### Lớp mạng:
- Nhiệm vụ: Chịu trách nhiệm định tuyến các gói tin từ nguồn đến đích thông qua một hay nhiều mạng. Xử lý địa chỉ IP, định tuyến và chuyển tiếp gói tin giữa các mạng khác nhau.
- Giao thức phổ biến: IP, ICMP, IGMP, RIP, ...

#### Lớp liên kết dữ liệu:
- Nhiệm vụ: Đảm bảo truyền dữ liệu đáng tin cậy thông qua một liên kết vật lý. Nó đóng gói dữ liệu vào các khung, phát hiện và sửa lỗi từ lớp Vật Lý. Cũng kiểm soát luồng và lỗi trong giao tiếp nội mạng.
- Giao thức phổ biến: Enthernet, Wifi, ...

#### Lớp vật lý:
- Nhiệm vụ: Bao gồm các thiết bị vật lý, dữ liệu sẽ được chuyển về dạng bit nhị phân để truyền giữa các thiết bị.
- Giao thức phổ biến:


### 2. Mô hình TCP/IP:
- Mô hình được sử dụng phổ biến, rộng rãi trên internet. 

#### Lớp Ứng dụng:
~ mô hình OSI (lớp Ứng dụng + lớp Trình bày + Lớp Phiên)
- Giao thức phổ biến: HTTP/HTTPS, FTP, SMTP, DNS, Telnet, SSH, DHCP, ...

#### Lớp Vận chuyển:
- Nhiệm vụ: Đảm bảo truyền tải dữ liệu một cách đáng tin cậy giữa các máy tính, xử lý việc phân chia dữ liệu thành các gói tin, kiểm tra lỗi và tái tạo dữ liệu. Cung cấp cơ chế kiểm soát luồng và quản lý lưu lượng.
- Giao thức phổ biến: TCP, UDP.

#### Lớp Mạng:
- Nhiệm vụ: Quản lý, định tuyến các gói tin qua mạng, đảm bảo chúng đưuọc chuyển đến đúng địa chỉ đích.
- Giao thức phổ biến: IP, RIP, ...

#### Lớp Liên kết (liên kết dữ liệu + vật lý ~ OSI):
- Nhiệm vụ: quản lý, xử lý việc truyền nhận các gói tin qua mạng, bao gồm phát hiện và sửa lỗi.
- Giao thức phổ biến:

## IP / Subnet / Submetmask

### 1. Địa chỉ IP:
- Địa chỉ IP gồm 32 bit nhị phân, chia thành 4 cụm 8 bit (octet). Chia thành 2 phần: phần network và host.
- 

### 2. SubnetMask:
- Subnet Mask là một giá trị được sử dụng trong mạng máy tính để xác định phạm vi địa chỉ IP thuộc phần mạng và phần host.


### 3. Subnet:
- là 1 phần của mạng lớn, tối ưu hóa việc quản lý địa chỉ IP và hiệu quả truyền tải gói tin, tăng bảo mật.
- Ví dụ:
    - trong VPC có 10.0.0.0/16 có 65536 địa chỉ (từ 10.0.0.0 đến 10.0.255.255)
    - chia cho 2 public subnet và 2 private subnet:
        - public subnet 1: 10.0.1.0/24 (dải: 10.0.1.0 đến 10.0.1.255)
        - public subnet 2: 10.0.2.0/24 (dải: 10.0.2.0 đến 10.0.2.255)
        - private subnet 1: 10.0.2.0/24 (dải: 10.0.3.0 đến 10.0.3.255)
        - private subnet 2: 10.0.2.0/24 (dải: 10.0.4.0 đến 10.0.4.255)
    - kết nối internet gateway:
        - internet gateway kết nối với vpc để cho phép các public subnet giao tiếp với internet, các tài nguyên trong public subnet sẽ nhận IP public và truy cập từ internet.
        - Nat gateway: đặt trong public subnet cho phép các tài nguyên trong private subnet ra ngoài internet, một chiều và bảo mật.

    - các thiết bị trong các subnet khác nhau sẽ không cùng dải IP mà chỉ có cùng subnet mới cùng dải IP.
    - các thiết bị trong các subnet khác nhau nhưng vẫn có thể ping tới nhau.



