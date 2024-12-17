# Chuẩn hóa dữ liệu:
- 2 mục đích chính:
	- giảm dữ liệu dư thừa
	- đảm bảo tính độc lập


## Chuẩn 1 (1NF):
- các cột chỉ chứa gtri nguyên tố, không chứa danh sách hoặc tập hợp
- mỗi hàng phải là duy nhất

## Chuẩn 2 (2NF):
- tất cả các cột không khóa đều phải phụ thuộc hoàn toàn vào khóa chính (không phụ thuộc 1 phần)
	- VD:
		```
		StudentID | Course     | Instructor  | Department
		----------|------------|-------------|-----------
		1         | Math       | Mr. A       | Science
		1         | Science    | Mr. B       | Science
		```
		- cột Department chỉ phụ thuộc vào Instructor, không phụ thuộc hoàn toàn vào StudentID, Course. Tách thành:
		```
		StudentID | Course     | Instructor
		----------|------------|------------
		1         | Math       | Mr. A
		1         | Science    | Mr. B
		```
		```
		Instructor  | Department
		------------|------------
		Mr. A       | Science
		Mr. B       | Science
		```

## Chuẩn 3 (3NF):
- không có phụ thuộc bắc cầu, một cột không khóa không phụ thuộc vào một cột không khóa khác.

## Chuẩn BCNF:
- mọi phụ thuộc hàm phải phụ thuộc vào superkey

## Chuẩn 4 (4NF):
- không phụ thuộc đa giá trị
