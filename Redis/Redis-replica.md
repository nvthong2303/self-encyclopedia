## 1. Giới thiệu
- Tài liệu này trình bày redis replica (mirrored).
## 2. Phân loại, giải thích
#### Redis standalone
- Chỉ hoạt động trên 1 server duy nhất, nếu down thì không nhận request, available thấp.
#### Redis replication
- Bao gồm nhiều node redis kết nối với nhau, gồm 1 master và nhiều slave. Master nhận request read write, slave chỉ nhận request read. Các node thực hiện đồng bộ dữ liệu với nhau. Dữ liệu trên mỗi node là như nhau.
- Khi master down thì CÁC SLAVE CHỈ NHẬN REQUEST READ, redis giờ đây không thể nhận request write được nữa. Cách khắc phục là sửa lỗi master up, hoặc cấu hình thủ công bằng tay 1 slave để làm master.
#### Redis replication + Sentinel
- Bao gồm nhiều node redis kết nối với nhau, gồm 1 master và nhiều slave. Master nhận request read write, slave chỉ nhận request read. Các node thực hiện đồng bộ dữ liệu với nhau. Dữ liệu trên mỗi node là như nhau.
- Khi master down thì CÁC SLAVE SẼ TỰ ĐỘNG BẦU 1 MASTER MỚI, sẽ tiếp tục phục vụ request read write.
#### Redis replication + sharding (cluster)
- Bao gồm nhiều node redis kết nối với nhau, gồm NHIỀU master và nhiều slave. Master nhận request read write, slave chỉ nhận request read. Các node thực hiện đồng bộ dữ liệu với nhau. Dữ liệu trên mỗi node là 1 phần trong tập dữ liệu chung.
- Khi master down thì CÁC SLAVE SẼ TỰ ĐỘNG BẦU 1 MASTER MỚI, sẽ tiếp tục phục vụ request read write.
- Có kèm theo cơ chế di chuyển dữ liệu giữa các node.

- Tài liệu này nhắm đến mô hình  "Redis replication + Sentinel", còn "Redis replication + sharding (cluster)" trình bày ở Replication-sharding.

# 1 Redis replica
## 1.1

- Không được turn off persistence + auto restart. Làm vậy có thể bị mất hết dữ liệu. Cho dù có bật Sentinel hay không.
#### Tránh full resync
- Mỗi node có 1 offset thể hiện data version hiện tại của node đó. Master dựa vào đó để đồng bộ và gửi tới những data còn thiếu.
- Nếu version cách nhau quá lớn, backlog quá nhỏ không đủ lưu phiên bản đó, thì master sẽ phải thực hiện full resync cho node đó.
## 1.2 cấu hình replica redis.conf file

| Cấu hình   | Mặc định | Ý nghĩa      |
|---|---|---|
| replicaof   | (IP) (PORT) | ip và port của master    |
| masterauth   | (string) | password master     |
| masteruser   | (string) | user master      |
| replica-serve-stale-data | yes(no) | Có muốn slave phục vụ read với dữ liệu cũ khi master down không ? |
| replica-read-only  | yes(no) | Chỉ đọc ( chỉ slave hay tất cả? - Hình như chỉ slave)  |
| repl-diskless-sync   | no(yes) | Khi full (re)sync, muốn tạo rdb trên master rồi chuyển sang cho slave(no) hay là chuyển trực tiếp cho slave qua socket(yes) ?     |
| repl-diskless-sync-delay | 5(s)  | Delay mỗi lần chuyển rdb cho client   |
| repl-diskless-load  | disabled | ... Để disabled cho an toàn    |
| repl-ping-replica-period | 10(s) | Khoảng thời gian slave ping server   |
| repl-timeout   | 60(s) | Thời gian để xác nhận 1 node timeout   |
| repl-disable-tcp-nodelay | no(yes) | Giảm bandwidth đánh đổi với delay data trên slave lên tới 40ms ? (nên yes) |
| repl-backlog-size  | 1mb  | backlog dùng để slave khi reconnect sử dụng để sync nhanh chóng vs master (1mb thì được bao lâu event?) |
| repl-backlog-ttl  | 3600(ms) | Thời gian 1 backlog sẽ được giải phóng nếu ko cần dùng|
| replica-priority  | 100  | Số càng NHỎ càng dễ trở thành master, 0 là không bao giờ|
| min-replicas-to-write | 3  | Số node online tối thiểu để master chấp nhận write |
| min-replicas-max-lag  | 10(s) | Thời gian lag dữ liệu tối đa    |
| replica-announce-ip   |  | Sử dụng cho NAT      |
| replica-announce-port |  | //       |

## 1.3
### INFO
- Hiện thông tin về tất cả thông số
### ROLE
- Thông tin ip,port, số đồng bộ master, slave

## 1.4
### Install redis 6.2.4
```
sudo add-apt-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get install redis
```
### Bật AOF cho master, còn slave thì không
(master - )
```
BGREWRITEAOF
CONFIG set appendonly yes
config set appendfsync everysec
config rewrite 
```
### Thêm 1 slave
(slave - service running - redis-cli)
```
config set replica-announce-ip [ip-nat]
config set replica-announce-port [port-nat]
config set masterauth [requirepass-master]
slaveof [ip-master] [port-master]
config rewrite
```
### Xóa slave (chuyển thành standalone node)
(slave - service running - redis-cli)
```
SLAVEOF NO ONE
CONFIG REWRITE
```

# 2 Sentinel
- Sentinel dùng để quản lý các node trong redis replica.
- Sentinel sẽ theo dõi master khi nó down, tiến hành bầu master mới và recover lại.
## 2.1 Cài đặt
### Tải
```
apt install redis-sentinel
systemctl status redis-sentinel
```
### Cho sentinel service chạy cùng với redis
```
systemctl stop redis-sentinel
```
- Sửa file service redis-server
```
vi /lib/systemd/system/redis-server.service

ExecStart=/usr/bin/redis-server /etc/redis/redis.conf --sentinel /etc/redis/sentinel.conf

systemctl daemon-reload

```
## 2.2 Cấu hình sentinel.conf

| Cấu hình           | Mặc định     | Ý nghĩa      |
|---|---|---|
| bind              | (ip) (ip)     | sentinel ip      |
| port              | 26379         | |
| daemonize           | no(yes)       | Nên bật yes cho daemon service   |
| logfile, pidfile    |              |       |
| sentinel announce-ip/port |          | Dùng để kết nối redis trong mạng NAT   |
| sentinel monitor    | <master-name> <ip> <redis-port> <quorum>| địa chỉ monitor master, quorum là số sentinel ít nhất đồng ý  |
| sentinel auth-pass  | <master-name> <password>      |password của master     |
| sentinel auth-user  | <master-name> <username>      |      |
| sentinel down-after-milliseconds      |<master-name> 30000(ms)| Thời gian để xem xét master là down |
| requirepass                 | (string)             | password của chính sentinel    |
| sentinel sentinel-pass       | (string)             | Nếu sentinel có pass thì khi kết nối vs nhau cần pass|
| sentinel failover-timeout     | <master-name> 180000(ms)| Xem cụ thể dưới    |
| sentinel notification-script |(master-name) (script) | Xem cụ thể dưới    |
| sentinel client-reconfig-script|(master-name) (script)| Xem cụ thể dưới    |
| sentinel deny-scripts-reconfig| yes(no)               | không cho thay đổi script khi chạy runtime  |
| sentinel rename-command       |                      | đổi câu lệnh để user ko dùng dc lệnh đó  |

- Thông số tương đối
```
sentinel down-after-milliseconds hoang 5000
sentinel failover-timeout hoang 20000
```
- Cấu hình trên chưa bao gồm ACL
#### failover-timeout
- Thời gian giữa 2 lần gọi failover trên các sentinel với cùng 1 master.
- Thời gian tối đa đợi replica cấu hình lại master để sync, trước khi force nó.
- Thời gian để hủy 1 lời gọi failover mà không thay đổi cấu hình (master, slave,...) gì cả.
- Thời gian tối đa đợi các sentinel khác đồng thuận một master mới.
- Mặc định là 3p.
#### notification-script
- Dùng để gọi script kiểm tra trạng thái sentinel với WARNING level
- Retries 10, running time max 60s.
- Return 1 nếu script thử lại sau, 2 nếu không được thửu lại.
```
sentinel notification-script mymaster /var/redis/notify.sh
```
#### client-reconfig-script
- Dùng để thay đổi master address (ip/port) trên client khi có sự thay đổi master. vd:
```
<master-name> <role> <state> <from-ip> <from-port> <to-ip> <to-port>
# <state> is currently always "failover"
# <role> is either "leader" or "observer"
```

## 2.3 Một số sentinel event
| Tên event  | Ý nghĩa       |
|---|---|
|+sdown | sentinel phát hiện master đã down   |
|+odown | Các sentinel đồng ý với nhau master đó đã down |
|-sdown | sentinel thấy có master đã up   |
|-odown | Các sentinel đồng ý master đã up   |
|switch-master <master name> <oldip> <oldport> <newip> <newport> | Đã đổi master |
|+tilt  | Trạng thái tilt mode     |
|-tilt  | Thoát trạng thái tilt mode    |
## 2.4 sentinel command
### SENTINEL + command
#### SENTINEL CONFIG GET <name>
- Lấy thông tin config
#### SENTINEL CONFIG SET <name> <value>

#### SENTINEL CKQUORUM <master name>
- Kiểm tra xem sentinel này đã kết nối với các sentinel khác hay chưa.
#### SENTINEL FLUSHCONFIG
- Ghi đè cấu hình sentinel vào .conf file
#### SENTINEL FAILOVER <master name>
- Force a failover as if the master was not reachable, and without asking for agreement to other Sentinels (however a new version of the configuration will be published so that the other Sentinels will update their configurations).
- (Cảm giác không ổn định lắm)
#### SENTINEL GET-MASTER-ADDR-BY-NAME <master name>
- Master hiện tại là ip nào ?
#### SENTINEL INFO-CACHE
#### SENTINEL MASTER <master name>
- Lấy info về master
#### SENTINEL MASTERS/REPLICA <master name>/ SENTINELS <master name>
- Lấy thông tin về các master (thường chỉ có 1 thôi)/replica/sentinels
#### SENTINEL SET
- Cấu hình monitor
#### SENTINEL MONITOR/ SENTINEL REMOVE
- Monitor sentinel / Dừng ngay cái hành động đó lại.
#### SENTINEL PENDING-SCRIPTS
- Thông tin các pending scripts.
#### SENTINEL SIMULATE-FAILURE (crash-after-election|crash-after-promotion|help)
- Test sentinel crash
#### SENTINEL RESET <pattern>
- Có thể hiểu như reset lại toàn bộ sentinel.
#### SENTINEL ACL/AUTH/CLIENT/COMMAND/HELLO/INFO/PING/ROLE/SHUTDOWN
- Tương tự redis command.

## 2.5

### quorum và trigger failover
- quorum <number>:Với một lượng nhất định sentinel đồng ý rằng master đã down thì mới cho phép trigger failover.
- Tuy nhiên vẫn cần quá bán sentinel để đồng thuận một master mới.
- quorum > quá bán sentinel: Phát hiện khi có lượng lớn sentinel không kết nối được.
- quorum < quá bán sentinel: (recommended) Phát hiện master down nhanh hơn -> bầu chọn nhanh hơn.

### tilt mode
- Xảy ra khi thời gian bị sai (>2s)
- Khi sentinel vào mode này:
- It stops acting at all.
- SENTINEL is-master-down-by-addr  trả về thông tin không chính xác.
- Nếu sau 30s bình thường trở lại vì sẽ thoát mode này.
## 2.6
### Thêm 1 master để monitor

```
SENTINEL MONITOR <name> <ip> <port> <quorum>
```
### Xóa 1 master đang monitor

```
SENTINEL REMOVE <name> 
```
### Thêm 1 sentinel vào group
- Đơn giản là dùng SENTINEL MONITOR (bên trên) thôi.
### Xóa 1 sentinel khỏi group
- Stop service sentinel đó.
- (Trên từng sentinel khác)
```
SENTINEL RESET * 
```
  - * có thể là master name cụ thể
- (check)
```
SENTINEL MASTER mastername
```
### Xóa 1 replica (old master)
- Thực hiện tương tự xóa 1 sentinel (tắt service, SENTINEL RESET *)

### Thoát khỏi -BUSY state
- Do Lua script bị treo gây timeout
- Nếu script đó thực hiện READ ops, gửi SCRIPT KILL để kill scipt đó.
- Nếu script đó thực hiện WRITE ops, gửi SHUTDOWN NOSAVE, kill redis process tránh việc ghi dữ liệu nửa vời.

## Độ ổn định dữ liệu khi write
- Dữ liệu write ổn định nếu up/down master mới không quá gần nhau.
- Dữ liệu write không ổn định nếu sử dụng SENTINEL FAILOVER "service-name", hoặc up/down các master node khác nhau liên tục.
## 3 Giảm thiểu tối đa write lost?
- Có 2 cách sau:
- Sử dụng replica đồng bộ với nhau theo một có chế đồng thuận chung.
- Sử dụng cơ chế cho phép gộp các db với dữ liệu khác nhau.
- 2 cách trên nằm ngoài mục tiêu của redis, tuy nhiên có thể cài bằng một proxy layer lớp bên trên để quản lý. Tham khảo Soundcloud Roshi (<https://github.com/soundcloud/roshi>) hoặc Netflix dynomite (<https://github.com/Netflix/dynomite>)
