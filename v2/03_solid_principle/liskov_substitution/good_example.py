from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> int:
        pass

class Rectangle(Shape):
    def __init__(self) -> None:
        self._width = 0
        self._height = 0

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int):
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int):
        self._height = height

    def get_area(self) -> int:
        return self._width * self._height

class Square(Shape):
    def __init__(self) -> None:
        self._length = 0

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int):
        self._length = length

    def get_area(self) -> int:
        return self._length ** 2


def f(s: Shape) -> None:
    print(s.get_area())


if __name__ == "__main__":
    r1 = Rectangle()
    r1.width = 3
    r1.height = 4
    f(r1)

    r2 = Square()
    r2.length = 4
    f(r2)