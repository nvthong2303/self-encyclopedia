## Common

### 1. Giải thích về biến (variables) trong Python
- python là ngôn ngữ động, không cần khai báo type khi khai báo biến.
- biến được gán cho 1 giá trị hoặc đối tượng.
- có 2 kiểu dữ liệu chính: immutable và mutable
	- immutable: giá trị sau khi khởi tạo thì không thể thay đổi: str, int, float, tuple.
	- mutable: giá trị có thể thay đổi sau khi khởi tạo: list, dict, set


### 2. Python quản lý bộ nhớ như thế nào ?
- Python sử dụng tham chiếu và bộ đếm để quản lý bộ nhớ
	- bộ đếm tham chiếu: theo dõi số lượng biến trỏ đến một đối tượng, khi bộ đếm đến tham chiếu của 1 đối tượng về 0, bộ nhớ được giải phóng.
	- garbage collector: cơ chế tự động thu gom tài nguyên khi không còn sử dụng, bao gồm xử lý các circular references.
- từ khóa ```del``` dùng để xóa 1 biến hoặc 1 phần tử trong ctdl. giảm bộ đếm tham chiếu bộ nhớ.

### 3. Các kiểu dữ liệu cơ bản trong Python là gì ?
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

### 4. So sánh giữa list và tuple trong Python? Khi nào nên sử dụng mỗi loại ?
- list có thể thay đổi còn tuple thì không (sau khi khởi tạo)
- cú pháp [] và ()
- khi cần 1 ctdl có thể thay đổi, hoặc không thay đổi để đảm bảo dữ liệu.

### 5. Giải thích về dict trong Python ?
- không có thứ tự (< pythong 3.7) và có thứ tự (> python 3.7)
- key phải là kiểu dữ liệu ummutable: str, int, tuple
- value có thể nhận bất cứ kiểu dữ liệu nào

### 6. Giải thích về decorators trong Python.
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

### 7. Generator là gì và nó khác gì so với một hàm thông thường ?
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

### 8. Giải thích về context managers và cú pháp with trong Python ?
- context managers là cơ chế quản lý tài nguyên như tệp tin, kết nối mạng, csdl bằng cách đảm bảo rằng tài nguyên được khởi tạo và giải phóng đúng cách.
- exp:
	```
	with open('file.txt', 'r') as file:
    	content = file.read()
	```

### 9. Sự khác biệt giữa deepcopy và shallowcopy trong Python.
- shallowcopy: copy bằng cách tạo bản sao của đối tượng, nhưng vẫn trỏ tới cùng địa chỉ với bộ nhớ gốc, thay đổi thì đối tượng gốc cũng bị thay đổi.
- deepcopy: copy bằng cách tạo bản sao của đối tượng và các đối tượng con, đảm bảo mọi thứ độc lập, bản copy thay đổi không làm thay đổi bản gốc.
- exp
	```
	# shallowcopy
	import copy
	original = [[1, 2, 3], [4, 5, 6]]
	shallow_copy = copy.copy(original)
	shallow_copy[0][0] = 100

	# deepcopy
	deep_copy = copy.deepcopy(original)
	deep_copy[0][0] = 100
	```

### 10. Các công cụ quản lý môi trường ảo và version python ?
- Venv: module dùng để tạo môi trường ảo.
	```
	python3 -m venv myenv
	source myenv/bin/activate
	myenv\Scripts\activate
	```
- Pyvenv: công cụ thay thế virtualenv, sau bị venv thay thế.
- Virtualenv: công cụ ngoài, dùng để tạo môi trường ảo.
- Pyenv: công cụ quản lý version python
	```
	# Cài đặt một phiên bản Python mới
	pyenv install 3.9.1

	# Đặt phiên bản Python mặc định
	pyenv global 3.9.1

	# Đặt phiên bản Python cho một thư mục cụ thể
	pyenv local 3.8.5
	```
- Pipenv: công cụ quản lý kết hợp quản lý mt ảo và version.
	```
	# Cài đặt pipenv
	pip install pipenv

	# Tạo môi trường ảo và cài đặt gói
	pipenv install requests

	# Kích hoạt môi trường ảo
	pipenv shell

	# Cài đặt gói phát triển
	pipenv install --dev pytest

	# Cập nhật các gói
	pipenv update
	```
-

### 11. So Sánh array và list Trong Python ?
- list: ctdl mutable, có thể chứa các phần tử là các kiểu dữ liệu khác nhau.
- Array (module array): tương tự list nhưng chỉ chứa các phần tử cùng kiểu dữ liệu, tối ưu hóa bộ nhớ và linh hoạt hơn list.
	```
	import array

	# Tạo một array chứa các số nguyên
	my_array = array.array('i', [1, 2, 3, 4])
	my_array.append(5)
	print(my_array)
	```

### 12. Giải thích về các nguyên tắc của OOP trong Python?
- Encapsulation (tính đóng gói):
	- che dấu dữ liệu, thuộc tính và các thuộc tính, chỉ cung cấp một số phương thức để tương tác.
	- sử dụng ```_``` hoặc ```__``` để thể hiện private.
- Abstraction (trìu tượng):
	- tạo ra một lớp chứa các phương thức mà các lớp con cần phải implement, giúp trìu tượng hóa các phần phức tạp.
	- module abc
- Interhitance (kế thừa):
	- cho phép lớp con thừa kế các thuộc tính / method của lớp cha
- Polymorphism (đa hình):
	- cho phép cùng một phương thức có thể có các cách hoạt động khác nhau, tuy thuộc đối tượng thực thi.


### 13. Sự khác biệt giữa class method, instance method, và static method?
- class method: khai báo với @classmethod, tham số đầu tiên là cls đại diện cho class.
- instance method: method sử dụng dữ liệu của đối tượng, self là tham số đầu tiên của các method này.
- static method: khai báo với @staticmethod, không cần tham số, không thể truy cập các thuộc tính của lớp hay đối tượng.


### 14. Python có hỗ trợ Asynchronous Programming không ?
- có, thông qua module ```asyncio``` và từ khóa ```async``` và ```await```.
	```
	import asyncio

	async def my_async_function():
		await asyncio.sleep(1)
		print("Hello after 1 second!")

	# Chạy async function
	asyncio.run(my_async_function())
	```


### 15. Lazy evaluation là gì ?
- lazy evaluation là kỹ thuật trì hoãn việc tính toán cho đến khi cần kết quả, giúp tiếc kiệm tài nguyên và tăng hiệu suất trong python.
-

## Threading - Process

### 1. Python hỗ trợ đa luồng (multithreading) như thế nào?
- python hỗ trợ đa luồng thông qua module threading, tuy nhiên do GIL (global interpreter lock) chỉ có 1 luồng được thực thi tại 1 thời điểm.

### 2. Sự khác biệt giữa multithreading và multiprocessing trong Python?
-

###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


###


### ###


###


###


###


###


###


###


###


###


###


### ###


###


###


###


###


###


###


###


###


###


###
