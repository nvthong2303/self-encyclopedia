# Networking trong K8s:

## Basic networking (list topic devopscube recommend):
### 1. CIDR Notation & Type of IP Address
- tham khảo: https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking
- CIDR (Classless inter-domain routing) là phương pháp phân bổ địa chỉ IP nhằm cải thiện hiệu quả việc định tuyến trên internet.
- So sánh với IPv4 Address Classes. (Chưa hiểu) 
    - các khái niệm classfull addresses, classless addresses, subnet, netmask, ...
    - classless addresses (CIDR) khắc phục những hạn chế của classes IP addressing ? https://aws.amazon.com/what-is/cidr/
    - CIDR mang lại lợi tích gì ? https://aws.amazon.com/what-is/cidr/

- Type of IP Address:
    + Pod IP
    + Service IP
    + Node IP
    + Cluster IP
    + External IP
    

### 2. OSI layers
### 3. SSL / TLS: One way& Mutual TLS
### 4. Proxy
### 5. DNS
### 6. IPVS / IPTables / NFtables
### 7. Software Defined Networking (SDN)
### 8. Virtual interface
### 9. Overlay networking