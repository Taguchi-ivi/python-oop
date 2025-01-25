from __future__ import annotations # 現在戻り値の方としてクラスを指定することができないので、このimportを追加
from abc import ABC, abstractmethod
import copy


class ItemPrototype(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__review: list[str] = []

    def __str__(self):
        return f"{self.__name}: {self.__review}"

    def set_review(self, review: str) -> None:
        self.__review.append(review)

    @abstractmethod
    def create_copy(self) -> ItemPrototype:
        pass


class DeepCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.deepcopy(self)

class ShallowCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.copy(self)

class ItemManager:
    def __init__(self):
        self.items = {}

    def register_item(self, key: str, item: ItemPrototype) -> None:
        self.items[key] = item

    def create(self, key: str) -> ItemPrototype:
        if key in self.items:
            item = self.items.get(key)
            return item.create_copy()
        raise Exception("item not found")


if __name__ == "__main__":
    mouse = DeepCopyItem("mouse")
    keyboard = ShallowCopyItem("keyboard")

    manager = ItemManager()
    manager.register_item("mouse", mouse)
    manager.register_item("keyboard", keyboard)

    cloned_mouse = manager.create("mouse") # DeepCopy
    cloned_keyboard = manager.create("keyboard") # ShallowCopy

    cloned_mouse.set_review("good")
    cloned_keyboard.set_review("soso!")

    print("mouse original:", mouse)
    print("mouse cloned:", cloned_mouse)
    print("")
    print("keyboard original:", keyboard)
    print("keyboard cloned:", cloned_keyboard)