from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

class Movable(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Airplane(Vehicle, Movable, Flyable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self):
        print("start!")

    def stop(self):
        print("stop!")

    def fly(self):
        print("fly!")

class Car(Vehicle, Movable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self):
        print("start!")

    def stop(self):
        print("stop!")

if __name__ == "__main__":
    v1 = Airplane("AirBus", "white")
    v2 = Car("Prius", "black")

    v1.fly()
    v2.start()