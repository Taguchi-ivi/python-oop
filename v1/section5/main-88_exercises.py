from abc import ABC, abstractmethod
# 演習問題

# ① LSPとは
# リスコフの置換原則
# 派生型と基本型は置換可能でなくてはならない。切り替えが可能な状態にするべき
# OCPを活用するために、承継をうまく使うための原則

# ② 基本型を派生型で置換できないのはどのような場合か
# 派生型で、基本型よりも事前条件を強める
# 派生型で、基本型よりも事後条件を弱める
# 派生型で、基本型の不変条件に違反する
# 派生型で、基本型にない例外が発生する（1と同じ）

# ③ 商品を表現するProductクラスについて
# ルール
# 名前は1文字以上20文字以内
# 価格は1円以上
# 割引率は5~50%
# 次のコードを改善してください。新しいクラスは定義しないものとする
# 修正前
# class Product:
#     def __init__(self, name: str, price: int) -> None:
#         self._name = name
#         self._price = price
#     def discount(self, discount_percent: int) -> None:
#         self._price = self._price * (100 - discount_percent) // 100
#     def change_name(self, new_name: str) -> None:
#         self._name = new_name

# 修正後
class Product:
    def __init__(self, name: str, price: int) -> None:
        if not 1 <= len(name) <= 20:
            raise ValueError("nameは1文字以上20文字以内")
        if price < 1:
            raise ValueError("priceは1円以上")
        self._name = name
        self._price = price
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    def discount(self, discount_percent: int) -> None:
        if not 5 <= discount_percent <= 50:
          raise ValueError("5-50%の間")
        new_price = self._price * (100 - discount_percent) // 100
        if new_price < 1:
            raise ValueError("priceは1円以上")
        self._price = new_price
    def change_name(self, new_name: str) -> None:
        if not 1 <= len(new_name) <= 20:
            raise ValueError("nameは1文字以上20文字以内")
        self._name = new_name


# ④ 次のコードはLSPに違反しているか、している場合は理由を述べて改善してください。
# 違反している
#   派生型で引数が多くなっている。 => 派生型で事前条件を強めている。置換できなくなる
#   クライアント(ShoppingCart)から見ても、apply_discountがうまく使えない
# 修正前
# class CouponStrategy(ABC):
#     @abstractmethod
#     def apply_discount(self, price: int) -> int:
#         pass
# class PercentageDiscountCoupon(CouponStrategy):
#     def __init__(self, percentage: int):
#         self.percentage = percentage

#     def apply_discount(self, price: int) -> int:
#         return int(price * (1 - self.percentage / 100))
# class QuantityDiscountCoupon(CouponStrategy):
#     def apply_discount(self, price: int, items_count: int) -> int:
#         if items_count >= 10:
#             return int(price * 0.9)
#         return price
# class ShoppingCart:
#     def __init__(self, discount_strategy: CouponStrategy):
#         self.items = []
#         self.discount_strategy = discount_strategy
#     def add_item(self, item_name: str, price: int):
#         self.items.append((item_name, price))
#     def calculate_total(self) -> int:
#         total = sum(price for _, price in self.items)
#         return self.discount_strategy.apply_discount(total)

# 修正後
# ⑤ 新しいクラスもうまく活用すること
# ④の問題点は、1つの派生型でしか使わない引数を全ての派生型で実装するように強制してしまっている点。
#    ある派生型に固有の引数が増えるたびに、全ての派生型の引数を変更する必要が出てしまう
#    有効なデザインパターン(パラメータオブジェクトパターン)
class DiscountParameters:
    def __init__(self, items: list):
        self._items = items
    @property
    def total_price(self) -> int:
        return sum(price for _, price in self._items)
    @property
    def item_count(self) -> int:
        return len(self._items)
class CouponStrategy(ABC):
    @abstractmethod
    def apply_discount(self, context: DiscountParameters) -> int:
        pass
class PercentageDiscountCoupon(CouponStrategy):
    def __init__(self, percentage: int):
        self.percentage = percentage

    def apply_discount(self, context: DiscountParameters) -> int:
        return int(context.total_price * (1 - self.percentage / 100))
class QuantityDiscountCoupon(CouponStrategy):
    def apply_discount(self, context: DiscountParameters) -> int:
        if context.item_count >= 10:
            return int(context.total_price * 0.9)
        return context.total_price
class ShoppingCart:
    def __init__(self, discount_strategy: CouponStrategy):
        self.items = []
        self.discount_strategy = discount_strategy
    def add_item(self, item_name: str, price: int):
        self.items.append((item_name, price))
    def calculate_total(self) -> int:
        context = DiscountParameters(self.items)
        return self.discount_strategy.apply_discount(context)


# null オブジェクトパターン
# 修正前(できないことはないが、バグを起こしやすいのでNoneを取り除きたい)
# class ShoppingCart:
#     def __init__(self, discount_strategy: CouponStrategy = None):
#         self.items = []
#         self.discount_strategy = discount_strategy
#     def add_item(self, item_name: str, price: int):
#         self.items.append((item_name, price))
#     def calculate_total(self) -> int:
#         context = DiscountParameters(self.items)
#         if self.discount_strategy is not None:
#             return self.discount_strategy.apply_discount(context)
#         return context.total_price
# Null Object(他の派生型と同じインターフェースを持ったNoneの表現)
class NoCoupon(CouponStrategy):
    def apply_discount(self, context):
        return context.total_price