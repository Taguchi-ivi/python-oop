# Decoratorパターン
from abc import ABC, abstractmethod

# コーヒーインターフェース
class AbstractCoffee(ABC):
    @property
    @abstractmethod
    def cost(self) -> int:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

# ベースのコーヒークラス
class Coffee(AbstractCoffee):
    @property
    def cost(self) -> int:
        return 200

    @property
    def description(self) -> str:
        return 'コーヒー'

# me 追記してみた(変更に強い。水出しコーヒーもトッピングできる)
class WaterCoffee(AbstractCoffee):
    @property
    def cost(self) -> int:
        return 100

    @property
    def description(self) -> str:
        return '水出しコーヒー'

# コーヒーのトッピングデコレーター
# 二重承継を使って、抽象クラスを作成
class CoffeeDecorator(AbstractCoffee, ABC): # 抽象クラス（インスタンス化しない）
    def __init__(self, decorated_coffee: AbstractCoffee):
        self.decorated_coffee = decorated_coffee

    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost

    @property
    def description(self) -> str:
        return self.decorated_coffee.description

# トッピングの具体的なデコレータークラス
class CreamDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 50

    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、生クリーム'

class VanillaDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 70

    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、バニラアイス'

# me 追加してみた
class ChocolateDecorator(CoffeeDecorator):
    @property
    def cost(self) -> int:
        return self.decorated_coffee.cost + 60

    @property
    def description(self) -> str:
        return f'{self.decorated_coffee.description}、チョコレート'

# 基底クラスを引数に取ることで、具象クラスに依存しないかつ全ての具象クラスを扱える
def print_coffee(coffee: AbstractCoffee):
    print(f'{coffee.description} : {coffee.cost}円')


# 下記のようにすることで、具象クラスに依存しない
# トッピング追加によるclassの増加にも対応できる
coffee = Coffee()

# 上記のコードによって、coffeeを引数で渡すことも、coffee_with_creamを引数で渡すこともできる
# 同じ抽象クラスを承継しているものは、どれも同じように扱える(スイッチができる)
coffee_with_cream = CreamDecorator(coffee)
coffee_with_vanilla = VanillaDecorator(coffee)
coffee_with_cream_and_vanilla = VanillaDecorator(coffee_with_cream)
coffee_with_cream_and_vanilla_and_choco = ChocolateDecorator(coffee_with_cream_and_vanilla)
print_coffee(coffee)
print_coffee(coffee_with_cream)
print_coffee(coffee_with_vanilla)
print_coffee(coffee_with_cream_and_vanilla)
print_coffee(coffee_with_cream_and_vanilla_and_choco)

#                      MEMO
#            AbstractCoffee(抽象クラス)
#               /                  \
#       Coffee(具象クラス), CoffeeDecorator(抽象クラス)
#                            /                   \
#                  CreamDecorator(具象クラス), VanillaDecorator(具象クラス)