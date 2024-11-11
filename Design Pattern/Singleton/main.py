class SingletonMeta(type):
    """
    Meta class cho Singleton.
    Meta class sẽ kiểm soát cách lớp được khởi tạo
    """
    # dict lưu trữ các instance của lớp
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def some_business_logic(self):
        print("Singleton some_business_logic value :" + str(self.value))
        pass


if __name__ == "__main__":
    s1 = Singleton(1)
    s2 = Singleton(2)

    print(s1.value)
    print(s2.value)

    print(s1 is s2)
    s1.some_business_logic()
    s2.some_business_logic()
