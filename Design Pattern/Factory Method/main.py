from abc import ABC, abstractmethod

# Interface cho sản phẩm
class Product(ABC):
    @abstractmethod
    def use(self) -> str:
        pass


# Cài đặt các sản phẩm cụ thể
# Các lớp triển khai cụ thể của Product, mỗi lớp cung cấp 1 cách sử dụng use() khác nhau
class ConcreteProductA(Product):
    def use(self) -> str:
        return "Sử dụng ConcreteProductA"
class ConcreteProductB(Product):
    def use(self) -> str:
        return "Sử dụng ConcreteProductB"


# Lớp creator cơ sở với phương thức factory
# là 1 abstract class, chứa phương thức factory_method() để tạo sản phẩm cụ thể
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        # Gọi phương thức factory để tạo sản phẩm
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.use()}"
        return result


# Các creator cụ thể tạo các sản phẩm cụ thể
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


# Sử dụng Factory Method
def client_code(creator: Creator) -> None:
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n{creator.some_operation()}")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorA.")
    client_code(ConcreteCreatorA())

    print("\nApp: Launched with the ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
