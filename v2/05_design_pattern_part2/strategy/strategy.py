from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'{amount}をクレジットカードで支払います')

class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'{amount}を現金で支払います')

class ShoppingCart:
    def __init__(self) -> None:
        self.__total = 0
        self.__items = []
    def add_item(self, item: str, price: int) -> None:
        self.__total += price
        self.__items.append((item, price))
    def pay(self, payment_strategy: PaymentStrategy) -> None:
        payment_strategy.pay(self.__total)


if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item('りんご', 100)
    cart.add_item('みかん', 50)
    cart.add_item('バナナ', 150)

    payment_strategy1 = CreditCardPaymentStrategy()
    cart.pay(payment_strategy1)

    payment_strategy2 = CashPaymentStrategy()
    cart.pay(payment_strategy2)