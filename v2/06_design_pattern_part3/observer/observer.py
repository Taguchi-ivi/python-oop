from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, name: str) -> None:
        pass

class StoreObserver(Observer):
    def update(self, name: str) -> None:
        print(f'{name}が入荷されました。仕入れが可能です')

class PersonalObserver(Observer):
    def update(self, name: str) -> None:
        print(f'{name}が入荷されました。購入が可能です')


class ItemSubject(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for obs in self.__observers:
            obs.update(self.__name)

    @abstractmethod
    def restock(self) -> None:
        pass


class TvGameSubject(ItemSubject):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__in_stock = False

    def restock(self) -> None:
        print('TVゲームが入荷されました')
        self.__in_stock = True
        self.notify()


if __name__ == '__main__':
    store = StoreObserver()
    person = PersonalObserver()

    tv_game = TvGameSubject('スーパーマリオ')
    tv_game.attach(store)
    tv_game.attach(person)
    tv_game.restock()
