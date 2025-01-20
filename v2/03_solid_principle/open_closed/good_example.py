import math
from abc import ABC, abstractmethod

class IEmployee(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def get_bonus(self, base: int) -> int:
        pass

class JuniorEmployee(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.1)

class MiddleEmployee(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.5)

class SeniorEmployee(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 2)

class ExpertEmployee(IEmployee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 3)

if __name__ == "__main__":
    emp1 = JuniorEmployee("Yamada")
    emp2 = MiddleEmployee("Suzuki")
    emp3 = SeniorEmployee("Tanaka")
    emp4 = ExpertEmployee("Bob")

    base = 100
    print(emp1.get_bonus(base))
    print(emp2.get_bonus(base))
    print(emp3.get_bonus(base))
    print(emp4.get_bonus(base))