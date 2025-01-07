# 切り替えが可能になるので、テスト時のmockなどテストがしやすくなる

from abc import ABC, abstractmethod

class AbstractPayment(ABC):
    @abstractmethod
    def pay(self, amount: int) -> bool:
        pass

# 支払い機能のモック、テスト用としても機能する
class MockPayment(AbstractPayment):
    def pay(self, amount: int) -> bool:
        return True

# 具体的な支払い処理の実装の完成を待たずとも、クライアントの実装と動作確認を行える
class Order:
    def __init__(self, payment: AbstractPayment) -> None:
        self._payment = payment