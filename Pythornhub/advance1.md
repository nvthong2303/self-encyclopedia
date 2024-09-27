# Python advanced:

## Iterable / Iterator / Generator:
- trong python, có thể chia các datatype thành 2 nhóm:
    - sequence: string, list, ... cho phép truy cập đến các phần tử bằng index (từ 0 > length -1).
    - collection: set, dict, ... không thể truy cập bằng index.
- Iterable: dùng cho những đối tượng có thể lặp qua, có thể for, map(), filter(), sort().
- Iterator: đối tượng đại diện cho 1 luồng dữ liệu, có thể trả về từng phần tử một khi lặp qua. __iter__(): trả về chính nó, __next__(): trả về phần tử tiếp theo, khi hết trả về lỗi
- General: Generator là một kiểu đặc biệt của iterator, được tạo ra bởi hàm generator function (sử dụng từ khóa yield) hoặc generator expression. Generator function là một hàm trả về một iterator và thay vì sử dụng từ khóa return, nó sử dụng từ khóa yield để trả về từng phần tử mỗi lần nó được gọi. Sau mỗi lần yield, trạng thái của hàm được lưu lại để tiếp tục từ chỗ đó trong lần gọi tiếp theo. Generator expression là một cú pháp ngắn gọn tương tự như list comprehension nhưng tạo ra generator thay vì list. Generator giúp tiết kiệm bộ nhớ vì không lưu trữ toàn bộ dữ liệu trong bộ nhớ ngay lập tức, mà chỉ tạo ra phần tử khi cần.


## Intertools
- là một thư viện cung cấp các công cụ làm việc với các iterator, bao gồm các hàm thao tác và kết hợp với iterator, tối ưu hóa, đặc biệt khi xử lý với lazy avaluation.
- giúp tối ưu hiệu suất, hiệu quả bộ nhớ, linh hoạt.

### infinite iterators (lặp vô hạn):
- count
- cycle
- repeat

### combinatoric iterators (lặp tổ hợp):
- product
- permutations
- combinations
- combinations_with_replacement

### terminating iterators (lặp kết thúc):
- accumulate
- chain
- islice
- zip_longest

## Lambda function
- hàm ẩn danh, không có tên, tính toán đơn giản: ```lambda arguments: expression```
- dùng trong các hàm bậc cao: map(), filter(), reduce(), ...

## Exception handling
- try - except - else - finally
    ```
    try:
        # Đoạn mã có khả năng gây lỗi
    except ZeroDivisionError:
        print("Lỗi")
    else:
        # Thực thi khi không có lỗi
        print("Kết quả là", result)
    finally:
        # Thực thi dù có hay không có lỗi
        print("Khối lệnh finally luôn được chạy")
    ```

## Decorators
- Công cụ giúp thay đổi hành vi của một hàm / phương thức mà không làm thay đổi mã nguồn của hàm đó. Triển khai bằng cách sử dụng 1 hàm bọc lấy 1 hàm khác, Decorators thường nhận 1 hàm là input, và trả về 1 hàm
- exp: 
    ```
    def my_decorator(func):
        def wrapper():
            print("Something before the function is called.")
            func()
            print("Something after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
   ```

- truyền tham số vào Decorators:
    ```
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Trước khi gọi hàm.")
            result = func(*args, **kwargs)
            print("Sau khi gọi hàm.")
            return result
        return wrapper

    @my_decorator
    def say_hello(name):
        print(f"Xin chào, {name}!")

    say_hello("Thắng")

    ```

- Decorators lồng nhau: 
    ```
    def decorator_1(func):
        def wrapper():
            print("Decorator 1")
            func()
        return wrapper

    def decorator_2(func):
        def wrapper():
            print("Decorator 2")
            func()
        return wrapper

    @decorator_1
    @decorator_2
    def say_hello():
        print("Hello!")

    say_hello()
    ```

## Collections
- module cung cấp các kiểu dữ liệu đặc biệt được thiết kế để giải quyết một số bài toán phổ biến: list, tuple, dict, ...
- các method phổ biến:
    - namedtuple: tạo tuple có tên cho từng field, dễ dàng truy cập theo tên thay vì index
    - deque: tạo một queue 2 đầu, cho phép thêm, xóa các phần tử ở cả 2 đầu với độ phức tạp O(1).
    - Counter: 1 dict chuyên đếm số lần xuất hiện của mỗi phần tử trong một iterable.
    - OdererDict: 1 dict lưu trữ các phần tử theo thứ tự đi kèm, không như dict thông thường.
    - defaultDict: 1 dict cho phép gán giá trị mặc định cho các key không tồn tại
    - ChainMap: một lợp quản lý nhiều dict như 1 chuỗi ánh xạ đơn lẻ. 

## Generators

## Magic methods
- là các phương thức đặc biệt, có thể định nghĩa trong các lớp để cho phép các đối tượng của lớp tương tác với cú pháp hoặc method đặc biệt.
- thường có dạng __ name__, Ví dụ : __ init__, __ str__, __ repr__, ...
- cung cấp các phương thức để tích hợp hành vi phức tạp vào các object của lớp, giúp chúng hoạt động như các kiểu dữ liệu tiêu chuẩn, tăng tính linh hoạt, dễ sử dụng hoặc tạo ra các method tùy chỉnh cho object.

## Regular expression

