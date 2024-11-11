# Builder là một mẫu thiết kế thuộc nhóm Creational Pattern.
# Nó cho phép tách rời việc xây dựng một đối tượng phức tạp
# ra khỏi việc biểu diễn nó, cho phép cùng quá trình xây dựng
# có thể tạo ra các biểu diễn khác nhau.
from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.doors = 0
        self.windows = 0
        self.roof = False
        self.garage = False

    def description(self):
        print(f"This house has {self.doors} doors, {self.windows} windows, roof: {self.roof}, garage: {self.garage}")


# Builder interface
class HouseBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_doors(self, number: int) -> None:
        pass

    @abstractmethod
    def set_windows(self, number: int) -> None:
        pass

    @abstractmethod
    def set_roof(self) -> None:
        pass

    @abstractmethod
    def set_garage(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> House:
        pass

# Concrete Builder


class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.house = House()

    def set_doors(self, number: int) -> None:
        self.house.doors = number

    def set_windows(self, number: int) -> None:
        self.house.windows = number

    def set_roof(self, roof: bool) -> None:
        self.house.roof = roof

    def set_garage(self, garage: bool) -> None:
        self.house.garage = garage

    def get_result(self) -> House:
        result = self.house
        self.reset()
        return result

# Director


class Director():
    def set_builder(self, builder: HouseBuilder):
        self._builder = builder

    def build_simple_house(self) -> None:
        self._builder.set_doors(1)
        self._builder.set_windows(2)
        self._builder.set_roof(True)

    def build_luxury_house(self) -> None:
        self._builder.set_doors(4)
        self._builder.set_windows(8)
        self._builder.set_roof(True)
        self._builder.set_garage(True)


def client_code(director: Director) -> None:
    builder = ConcreteHouseBuilder()
    director.set_builder(builder)

    print("Simple house:")
    director.build_simple_house()
    builder.get_result().description()

    print("Luxury house:")
    director.build_luxury_house()
    builder.get_result().description()


if __name__ == "__main__":
    director = Director()
    client_code(director)
