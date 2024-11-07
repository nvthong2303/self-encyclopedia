1. Giải thích về biến (variables) trong Python
- python là ngôn ngữ động, không cần khai báo type khi khai báo biến.
- biến được gán cho 1 giá trị hoặc đối tượng.

2. Python quản lý bộ nhớ như thế nào?
- Python sử dụng tham chiếu và bộ đếm để quản lý bộ nhớ
	- bộ đếm tham chiếu: theo dõi số lượng biến trỏ đến một đối tượng, khi bộ đếm đến tham chiếu của 1 đối tượng về 0, bộ nhớ được giải phóng.
	- garbage collector: cơ chế tự động thu gom tài nguyên khi không còn sử dụng, bao gồm xử lý các circular references.

3. Các kiểu dữ liệu cơ bản trong Python là gì?
- numbers:
	- int
	- float
	- complex
- sequences: chuỗi
	- str: string
	- list: ```[1,2,3]``` array có thể thay đổi
	- tuple: ```(1,2,3)``` array không thể thay đổi
- sets: tập hợp
	- set: ```{1,2,3}``` tập hợp không trùng lăp
	- frozen: ```frozenset([1, 2, 3])``` tập hợp không thể thay đổi
- mappings:
	- dict: ```{'a': 1, 'b': 2}```, ~ object trong js
- boolean:
- nonetype: None

4. So sánh giữa list và tuple trong Python? Khi nào nên sử dụng mỗi loại?
- list có thể thay đổi còn tuple thì không (sau khi khởi tạo)
- cú pháp [] và ()
- khi cần 1 ctdl có thể thay đổi, hoặc không thay đổi để đảm bảo dữ liệu.

5. Giải thích về dict trong Python ?
- không có thứ tự (< pythong 3.7) và có thứ tự (> python 3.7)
- key phải là kiểu dữ liệu ummutable: str, int, tuple
- value có thể nhận bất cứ kiểu dữ liệu nào

6. Giải thích về decorators trong Python.
- 1 tính năng trong python cho phép sửa đổi hoặc mở rộng chức năng của 1 hàm / lớp mà không thay đổi code ban đầu của nó.
- thường dùng để thêm các chức năng, kiểm tra, ...
- exp:
	```
	def my_decorator(func):
		def wrapper():
			print("Before function call")
			func()
			print("After function call")
		return wrapper

	@my_decorator
	def say_hello():
		print("Hello!")

	say_hello()
	```

7. Generator là gì và nó khác gì so với một hàm thông thường?
- generator là 1 hàm đặc biệt trong py, dùng ```yeld``` để trả về các gtri theo lazy evaluation.
- giúp tiếc kiệm bộ nhớ.
- exp
	```
	def my_generator():
		for i in range(5):
			yield i

	gen = my_generator()
	for value in gen:
		print(value)

	-> result:
	0
	1
	2
	3
	4
	```

8. Giải thích về context managers và cú pháp with trong Python ?
- context managers là cơ chế quản lý tài nguyên như tệp tin, kết nối mạng, csdl bằng cách đảm bảo rằng tài nguyên được khởi tạo và giải phóng đúng cách.
- exp:
	```
	with open('file.txt', 'r') as file:
    	content = file.read()
	```
