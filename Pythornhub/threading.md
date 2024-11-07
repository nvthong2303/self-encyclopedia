# Threading

- Python là một ngôn ngữ đơn luồng nhưng có khả năng đa luồng.
- Module threading là module chuẩn, cung cấp các class, function làm việc với thread.

## Cơ chế đồng bộ trong Python:

### Lock:
- cơ chế đồng bộ cơ bản nhất của python, một lock gồm 2 trạng thái **locked** và **unlocker**, 2 phương thức là **acquire()** và **release()**:
    - nếu state là unlocked, gọi acquire() sẽ chuyển thành locked
    - nếu state là locked, gọi release() sẽ chuyển thành unlocked
    - nếu state là unlocked, gọi release() sẽ trả ra RuntimeError exception
    - nếu state là locked, gọi acquire() sẽ phải đợi block cho đến khi tiến trình khác gọi release()
- tại 1 thời điểm, chỉ có nhiều nhất 1 thread sở hữu lock.



### RLock (Reentrant Lock):
### Semaphore:
### Condition:
### Event:
### Barrier:
