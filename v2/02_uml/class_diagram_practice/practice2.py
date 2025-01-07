from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calc_area(self) -> int:
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def calc_area(self) -> int:
        return self.__width * self.__height

class Square(Shape):
    def __init__(self, length: int):
        self.__length = length

    def calc_area(self) -> int:
        return self.__length ** 2

class Client:
    def __init__(self, shape: Shape):
        self.__shape = shape
