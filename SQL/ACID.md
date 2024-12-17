# Transaction:
- Có thể koi nó là 1 tập các query.
- Là một tiến trình xử lý có xác định điểm đầu và cuối, được chia nhỏ thành các operation (phép thực thi), được thực thi một cách tuần tự và độc lập.
- ACID là tính chất của transaction.
-


# ACID
## A - Atomicity:
- Tính nguyên tử: 1 transaction của database không thể phân chia và không thể rút gọn, sao cho tất cả các bước đều xảy ra hoặc không có gì xảy ra
	- Nếu một phần transaction bị lỗi thì transaction đó sẽ được rollback, dữ liệu sẽ không thay đổi.
	- Còn nếu không có lỗi gì xảy ra, transaction sẽ được commit, dữ liệu được cập nhât.
- Phương pháp:
	- Sử dụng DBMS tuân thủ ACID
	- triển khai 2pc (two-phase commit)
	- sử dụng transaction logs

## C - Consistentcy:
- Tính nhất quán: yêu cầu tất cả các transaction chỉ có thể thay đổi dữ liệu thoe những cách được cho phép
- sau khi thực hiện transaction, nếu có bất kỳ vi pham nào ràng buộc, nó phải bị hủy bỏ và hệ thống quay lại trạng thái ban đầu.
- Phương pháp:
	- Sử dụng DBMS tuân thủ ACID
	- kiểm tra tính hợp lệ của dữ liệu
	- Rollback và Recovery
	- sử dụng DB versioning
	- triển khai 2pc (two-phase commit)


## I - Isolation:
- Tính cô lập: đảm bảo các transaction được thực thi một cách độc lập, không phụ thuộc.
- 2 khái niệm:
	- Read phenomena (hiện tương đọc): những lỗi khi nhiều người đọc và ghi vào cùng một dòng
		- Dirty reads:
		- ...
	- Isolation levels (Cấp độ cô lập): chỉ ra các cấp độ cô lập một transaction nhằm khắc phục Read phenomena
		-
- Phương pháp:


## D - Durability:
- Tính bền vững: đảm bảo những transaction đã commit, kết quả của nó sẽ được lưu trữ vĩnh viễn, không thể mất mát kể cả khi hệ thống bị lỗi / mất điện / .../
