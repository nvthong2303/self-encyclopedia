# Redis Access Control List


## 1. Lấy danh sách ACL hiện tại: ACL LIST
## 2. Thêm mới User: ACL SETUSER {username}
    --> không truyền thêm gì, mặc định User ở trạng thái "off resetchannels", không có ý nghĩa, quyền hạn gì
## 3. Kích hoạt / Vô hiệu hóa User: ACL SETUSER {username} on / off
## 4. Thiết lập password cho User: ACL SETUSER {username} >{password1} > {password2}
    --> có thể thiết lập nhiều password cho 1 User
## 5. KeyPatterns: ACL SETUSER {username} ~cache:* ~data:*
## 6. Command Permission: ACL SETUSER {username} +GET +SET
    +command: cho phép User thực thi 1 lệnh cụ thể
    -command: cấm User thực thi 1 lệnh cụ thể
    +@category: cho phép User thao tác trên 1 danh mục
    -@category: cấm User thao tác trên 1 danh mục

    @all: tất cả các lệnh
    @read: các lệnh đọc
    @write: các lệnh ghi
    @admin: các lệnh quản trị
    @keyspace:
## 7. Lấy thông tin User: ACL GETUSER {username}
## 8. Xóa User: ACL DELUSER {username}




## 9. Kết hợp các lệnh lại:

    ACL SETUSER charlie on >charliepassword ~data:* +@read +@write -@admin

    ACL SETUSER dave on >davepassword +GET +SET +EXPIRE ~dave:*


    
    	

    	
    	


