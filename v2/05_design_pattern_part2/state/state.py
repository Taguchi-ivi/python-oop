from __future__ import annotations
from abc import ABC, abstractmethod

class LightState(ABC):
    @abstractmethod
    def switch(self) -> LightState:
        pass


class OffState(LightState):
    def switch(self) -> LightState:
        print("Switching to On state")
        return OnState()

class OnState(LightState):
    def switch(self) -> LightState:
        print("Switching to Off state")
        return OffState()


class LightSwitch:
    def __init__(self):
        self.__state = OffState()

    def switch(self):
        self.__state = self.__state.switch()


if __name__ == "__main__":
    light_switch = LightSwitch()
    light_switch.switch()
    light_switch.switch()
    light_switch.switch()