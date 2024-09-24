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
- 


## Collections
## Generators
## Magic methods
## Threading
## Regular expression

