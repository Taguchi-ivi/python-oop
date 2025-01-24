from abc import ABC, abstractmethod

class CreditCard(ABC):
    def __init__(self, owner: str) -> None:
        self.__owner = owner

    @property
    def owner(self) -> str:
        return self.__owner

    @abstractmethod
    def get_card_type(self) -> str:
        pass

    @abstractmethod
    def get_annual_charge(self) -> int:
        pass

class PlatinumCard(CreditCard):
    def get_card_type(self) -> str:
        return "プラチナム"

    def get_annual_charge(self) -> int:
        return 30000

class GoldCard(CreditCard):
    def get_card_type(self) -> str:
        return "プラチナム"

    def get_annual_charge(self) -> int:
        return 30000

class CreditCardFactory(ABC):
    @abstractmethod
    def create_credit_card(self, owner: str) -> CreditCard:
        pass

    @abstractmethod
    def register_credit_card(self, credit_card: CreditCard) -> None:
        pass

    def create(self, owner: str) -> CreditCard:
        credit_card = self.create_credit_card(owner)
        self.register_credit_card(credit_card)
        return credit_card

credit_card_database: list[CreditCard] = []

class PlatinumCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        return PlatinumCard(owner)

    def register_credit_card(self, credit_card: CreditCard) -> None:
        credit_card_database.append(credit_card)

class GoldCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        return GoldCard(owner)

    def register_credit_card(self, credit_card: CreditCard) -> None:
        credit_card_database.append(credit_card)


if __name__ == "__main__":
    platinum_card_factory = PlatinumCardFactory()
    platinum_card = platinum_card_factory.create("tanaka")
    print(platinum_card.get_card_type())

    gold_card_factory = GoldCardFactory()
    gold_card = gold_card_factory.create("suzuki")
    print(gold_card.get_card_type())

    print(credit_card_database)
