#  Cung cấp interface để tạo ra các instance liên quan hoặc phụ thuộc mà không cần chỉ định đến các lớp cụ thể của chúng.
#  Điều này giúp giảm sự phụ thuộc giữa các lớp và giúp dễ dàng thay đổi các lớp cụ thể mà không ảnh hưởng đến các lớp khác.
#  Abstract Factory Pattern thuộc nhóm Creational Pattern.

from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def has_legs(self) -> None:
        pass

    @abstractmethod
    def sit_on(self) -> None:
        pass


class Table(ABC):
    @abstractmethod
    def has_legs(self) -> None:
        pass

    @abstractmethod
    def put_on(self) -> None:
        pass


class ModernChair(Chair):
    def has_legs(self) -> None:
        print("Modern Chair has 4 legs.")

    def sit_on(self) -> None:
        print("Sitting on Modern Chair.")


class ModernTable(Table):
    def has_legs(self) -> None:
        print("Modern Table has 4 legs.")

    def put_on(self) -> None:
        print("Putting on Modern Table.")


class VictorianChair(Chair):
    def has_legs(self) -> None:
        print("Victorian Chair has 4 legs.")

    def sit_on(self) -> None:
        print("Sitting on Victorian Chair.")


class VictorianTable(Table):
    def has_legs(self) -> None:
        print("Victorian Table has 4 legs.")

    def put_on(self) -> None:
        print("Putting on Victorian Table.")


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class ModernFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        return ModernChair()

    @abstractmethod
    def create_table(self) -> Table:
        return ModernTable()


class VictorianFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        return VictorianChair()

    @abstractmethod
    def create_table(self) -> Table:
        return VictorianTable()


def Client_code(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    table = factory.create_table()

    chair.has_legs()
    chair.sit_on()
    table.has_legs()
    table.put_on()


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    Client_code(ModernFurnitureFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    Client_code(VictorianFurnitureFactory())
