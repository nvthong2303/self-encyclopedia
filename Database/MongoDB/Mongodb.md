# Các loại mô hỉnh triển khai MongoDB:

## 1. Standalone: ~ standalone bên redis:
Gồm 1 node duy nhất. 
handle: 
    start
    stop
    backup
    restore
    add / rm user
    update role connect

Replica-set (Cluster):
command start:

PRIMARY:
```
    docker run_url=https://ws-cloudops-taskmanager.ap
    -d
    --name mongo1
    --net mongo-net
    -e MONGODB_REPLICA_SET_MODE=primary
    -e MONGODB_REPLICA_SET_NAME=my-replica-set
    -e MONGODB_REPLICA_SET_KEY=replicasetkey123
    -e MONGODB_ROOT_PASSWORD=password123
    -e MONGODB_ADVERTISED_HOSTNAME=192.168.254.194 (current ip ~ primary ip)
    -p 27017:27017
    bitnami/mongodb:latest
```
SECONDARY:
```
    docker run
    -d
    --name mongo2
    --net mongo-net
    -e MONGODB_REPLICA_SET_MODE=secondary
    -e MONGODB_REPLICA_SET_NAME=my-replica-set
    -e MONGODB_REPLICA_SET_KEY=replicasetkey123
    -e MONGODB_INITIAL_PRIMARY_ROOT_PASSWORD=password123
    -e MONGODB_ADVERTISED_HOSTNAME=10.0.0.4 (current ip)
    -e MONGODB_INITIAL_PRIMARY_HOST=192.168.254.194 (primary ip)
    -p 27017:27017
    bitnami/mongodb:latest
```  

## 2. Replica-set 
- là phương pháp sao chép dữ liệu trên nhiều máy chủ (node), từ sẽ có được sự dư thừa và tăng tính H/A của dữ liệu với nhiều bản sao dữ liệu trên các node khác nhau. Vì vậy, nó sẽ tăng performance đọc. Tập hợp các node duy trì cùng một bản sao dữ liệu được gọi là replica servers hoặc MongoDB instances. Mục đích chính của mô hình Replica-set là tăng tính H/A cho MongoDB và dữ liệu được bảo toàn (sao lưu). Các tính chất:

- Gồm cụm N node khác nhau duy trì cùng một bản sao của tập dữ liệu.
    - Primary node nhận tất cả các hoạt động ghi và ghi lại tất cả các thay đổi đối với dữ liệu, tức là oplog.
    - Sau đó, các secondary node sẽ sao chép và áp dụng những thay đổi này theo quy trình không đồng bộ.
- Tất cả các secondary node được kết nối với các primary node. có một tín hiệu heartbeat từ các primary node.
- Nếu primary node ngừng hoạt động thì sencondary node đủ điều kiện sẽ giữ primary node mới.
    handle:
    ...
    add secondary node.
    add abiter.
- More:
    ***Arbiter***: 


## 3. Sharding:
- Sharding là phương pháp phân chia dữ liệu trên nhiều máy, từ đó đảm bảo khả năng xử lý, performance đọc ghi. Thường sử dụng cho tập dữ liệu lớn. 



## Path config, mount data trong container (bitnami):

config path trong container:

    /opt/bitnami/mongodb/conf/mongodb.conf
path data trong container:

    /bitnami/mongodb

## Infrastruture as a service Best Practices:



## Cách thực thi command trong module python/docker (cách execute tương tự bên redis agent):
```
mongosh mydatabase -quiet --eval '__command__'

mongosh -u root -p password123 -quiet --eval "db.getUsers()" (with authen)

mongosh -quiet --eval 'use admin' --eval 'db.getUsers()' (multiple command)
```
example: mongosh mydatabase --eval 'db.getUsers()'


Start MongoDB standalone:
- Cấu hình agent:
mode = standalone
root_user = root (default: root)
root_password = password123 (require )


Start MongoDB replicaset:
- Cấu hình agent:

mode = replica_set

mongo_role = primary / secondary / arbiter

root_user = root (default: root)
root_password = password123 (env: MONGODB_INITIAL_PRIMARY_ROOT_PASSWORD - dành cho các node secondary / arbiter và env: MONGODB_ROOT_PASSWORD - dành cho node primary)
replicaset_key = replicasetkey123 (Dài hơn 5 ký tự, không chừa ký tự đặc biệt và "-", cần cho tất cả các node, không có mặc định, env: MONGODB_REPLICA_SET_KEY)
replicaset_name = replicaset_name (default: replicaset)
ip_primary = 10.22.0.207 (IP node primary)
mode	config example
standalone	

```
[default]
socket_url=https://ws-cloudops-taskmanager.api-connect.io:8085/
datastore_manager=mongodb
datastore_version=7.0
encrypted_key=AB96h3etgbwawMzWRcpMmj0ik1Xd38sC
agent_id=55e509d5-14a2-4b49-b6f7-4e4ebed653f7
[mongodb]
mode=standalone
root_user=root
root_password=password


replica set	


Primary
[default]
socket_url=https://ws-cloudops-taskmanager.api-connect.io:8085/
datastore_manager=mongodb
datastore_version=7.0
encrypted_key=AB96h3etgbwawMzWRcpMmj0ik1Xd38sC
agent_id=55e509d5-14a2-4b49-b6f7-4e4ebed653f7
[mongodb]
mode=replica_set
mongo_role=primary
root_user=root
root_password = password
replicaset_key=replicasetKey
replicaset_name=replicasetName
ip_primary = 10.22.0.207 (taskmanager)
ip_address=x.x.x.x (taskmanager)

Secondary || Arbiter
[default]
socket_url=https://ws-cloudops-taskmanager.api-connect.io:8085/
datastore_manager=mongodb
datastore_version=7.0
encrypted_key=AB96h3etgbwawMzWRcpMmj0ik1Xd38sC
agent_id=55e509d5-14a2-4b49-b6f7-4e4ebed653f7
[mongodb]
mode = replica_set
mongo_role = secondary | arbiter
root_user=root
root_password=password
replicaset_key=${instance_id}
replicaset_name=replicaset
ip_primary = 10.22.0.207 (taskmanager)
ip_address=x.x.x.x (taskmanager)
```



Lấy danh sách db:
```
mongosh -quiet --eval "show dbs"
```

Lấy danh sách Collection của database:
```
mongosh -quiet --eval "use database_name" --eval "show collections"
```

Lấy danh sách user:
```
mongosh -quiet --eval "db.system.users.find()" (Chỉ execute trên node primary)
```

Thêm / Xóa User, Phân quyền trong MongoDB:

notes:  khi thêm user, user thao tác trên 1 db hay mọi db thì đều lưu tại admin, uri có dạng: mongodb://user_name:password@127.0.0.1:27017/dev-1?authSource=admin

Thêm user:
```
mongosh -quiet --eval 'db.createUser({ user: "__username__)", pwd: "__password__", roles: [] })'
mongosh admin --eval 'db.createUser({user: "admin", pwd: "admin", roles: [{role: "root", db: "admin"}]})'
mongosh admin --eval 'db.createUser({user: "user1", pwd: "password123", roles: [{role: "read", db: "users"}]})'
```

response: { ok: 1 } → thành công.

* Danh sách các role phổ biến: https://www.mongodb.com/docs/manual/reference/built-in-roles/
```
Role	description
read	Cho phép đọc dữ liệu trên 1 database.
readWrite	Cho phép đọc và ghi dữ liệu trên 1 database.
dbAdmin	Cho phép quản trị cơ sở dữ liệu, bao gồm việc tạo, xóa cơ sở dữ liệu, thống kê, indexing, ... trên 1 database.
userAdmin	Cho phép quản lý người dùng, bao gồm việc tạo, xóa người dùng và gán role trên 1 database.
dbOwner	Bao gồm quyền dbAdmin và userAdmin trên 1 database.
readAnyDatabase	Cho phép đọc dữ liệu từ mọi database. **
readWriteAnyDatabase	Cho phép đọc dữ và ghi liệu từ trên mọi database. **
userAdminAnyDatabase	~ userAdmin nhưng trên mọi database. **
dbAdminAnyDatabase	~ dbAdmin nhưng trên mọi database. **
root	Là role cao cấp nhất, cho phép người dùng thực hiện tất cả các hoạt động trên MongoDB. **
... more 	...
```

**: role phải đi kèm db là "admin"

Xóa user: Tương tự, thay createUser bằng dropUser() hoặc dropAllUsersFromDatabase
```
mongosh admin -quiet --eval 'db.dropUser("user05")'
```

response: { ok: 1 } → thành công.


Gán quyền / Xóa quyền user: 
```
mongosh admin -quiet --eval 'db.grantRolesToUser("user01", ["root"])'
mongosh admin -quiet --eval 'db.revokeRolesFromUser("user01", ["root"])'

mongosh admin -quiet --eval 'db.grantRolesToUser("user01", [{role: "read", db: "users"}])'
mongosh admin -quiet --eval 'db.revokeRolesFromUser("user01", [{role: "read", db: "users"}])'
```

response: { ok: 1 } → thành công.

Log activity:
Lấy các bộ lọc nhật ký có sẵn:
```
mongosh admin -quiet --eval 'db.adminCommand( { getLog: "*" } )' 
```

response: { names: [ 'global', 'startupWarnings' ], ok: 1 }

Lấy logs:
```
mongosh admin -quiet --eval 'db.adminCommand( { getLog: "global" } )'
```

response: totalLinesWritten: 778,
log: 
```
[
    '{"t":{"$date":"2023-11-02T07:08:39.591Z"},"s":"I", "c":"CONTROL", "id":5760901, "ctx":"main","msg":"Applied --setParameter options","attr":{"serverParameters":{"enableLocalhostAuthBypass":{"default":true,"value":true}}}}\n',
    '{"t":{"$date":"2023-11-02T07:08:39.591+00:00"},"s":"I", "c":"CONTROL", "id":20698, "ctx":"main","msg":"***** SERVER RESTARTED *****"}\n',
    '{"t":{"$date":"2023-11-02T07:08:39.593+00:00"},"s":"I", "c":"NETWORK", "id":4915701, "ctx":"main","msg":"Initialized wire specification","attr":{"spec":{"incomingExternalClient":{"minWireVersion":0,"maxWireVersion":21},"incomingInternalClient":{"minWireVersion":0,"maxWireVersion":21},"outgoing":{"minWireVersion":6,"maxWireVersion":21},"isInternalClient":true}}}\n',
    ... 678 more items
],
ok: 1
}
```
Backup data:
run trong container: mongodump --archive > /tmp/backup.dump
run ngoài máy host: docker cp database:/tmp/backup.dump /path_backup_file
// đẩy lên S3 


Restore:
// download từ S3
run ngoài máy host: docker cp /path_dump_file_restore database:/tmp
run trong container: mongorestore --archive=/tmp/backup.dump













