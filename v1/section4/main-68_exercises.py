# 演習問題
from abc import ABC, abstractmethod

# ① OCP(オープンクローズド)の原則とは何か
# 最も重要な原則の一つ
# 拡張に対して開いていて、修正に対して閉じているべき
# 既存コードを変更せずに、新しい機能を追加できるようにする
# 基底クラスを作り、そこから派生クラスを作る。それによって、新しい機能を追加する

# ② 以下の対立する2つの要素に対して、一般的に変更されづらいのはどちらか
# - 抽象クラス vs 具象クラス
#   抽象クラス
# - 実装 vs インターフェース
#   インターフェース
# 組み込み機能 vs 自作機能
#   組み込み機能

# ③ 以下のコードはOCPを違反しているか。違反している場合は理由を述べて修正せよ
# 違反している。 単一責任の原則を違反している。支払い方法が追加されると、payメソッドの修正が必要になる
# 修正前
class Payment:
    def pay(self, amount: int, method: str) -> None:
        if method == 'cash':
            # 現金決済の処理
            print(f'{amount}円を現金で支払いました。')
        elif method == 'credit_card':
            # クレジットカード決済の処理
            print(f'{amount}円をクレジットカードで支払いました。')
        elif method == 'QRPay':
            # QRコード決済の処理
            print(f'{amount}円をQRコードで支払いました。')
        else:
            raise ValueError('利用できない決済方法です。')
# 修正後(strategyパターン)
class AbstractPayment(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass
class CashPayment(AbstractPayment):
    def pay(self, amount: int) -> None:
        print(f'{amount}円を現金で支払いました。')
class CreditCardPayment(AbstractPayment):
    def pay(self, amount: int) -> None:
        print(f'{amount}円をクレジットカードで支払いました。')
class QRPayPayment(AbstractPayment):
    def pay(self, amount: int) -> None:
        print(f'{amount}円をQRコードで支払いました。')


# ④あるカラオケ店の料金計算システムを考えてみる
# 利用時間は1時間単位
# 基本料金は1時間あたり700円
# 学生は料金が基本料金の80%になる
# 会員は料金が基本料金の90%になる
# 学生割引と会員割引は併用できる
# 料金を計算する関数
# SOLID原則の観点から見た時の問題点を指摘
# 問題点: 割引の方法が増るたびに、関数の修正が必要になる。変更に弱く、バグを生みやすい
# 修正前
def calculate_fee(hours: int, is_student: bool, is_member: bool) -> int:
    base_rate: int = 700
    discount_rate: float = 1.0

    if is_student and is_member:
        discount_rate = 0.8 * 0.9
    elif is_student:
        discount_rate = 0.8
    elif is_member:
        discount_rate = 0.9

    total_fee: int = int(hours * base_rate * discount_rate)
    return total_fee
# 使用例
hours: int = 2
is_student: bool = True
is_member: bool = True
fee: int = calculate_fee(hours, is_student, is_member)
print(f'カラオケの料金は: {fee}円')

# 修正後
# 部屋料金のインターフェース
class AbstractRoomFee(ABC):
    @abstractmethod
    def get_cost(self, hours: int) -> int:
        pass
# 基本料金
class BaseRoomFee(AbstractRoomFee):
    def get_cost(self, hours: int) -> int:
        return 700 * hours # 1時間あたり700円
class RoomFeeDecorator(AbstractRoomFee, ABC):
    def __init__(self, decorated_fee: AbstractRoomFee):
        self._decorated_fee = decorated_fee
    @abstractmethod
    def get_cost(self, hours: int) -> int:
        pass
class StudentDiscountDecorator(RoomFeeDecorator):
    def get_cost(self, hours: int) -> int:
        base_cost = self._decorated_fee.get_cost(hours)
        return int(base_cost * 0.8) # 学生は料金が基本料金の80%になる
class MemberDiscountDecorator(RoomFeeDecorator):
    def get_cost(self, hours: int) -> int:
        base_cost = self._decorated_fee.get_cost(hours)
        return int(base_cost * 0.9) # 会員は料金が基本料金の90%になる
class SeniorDiscountDecorator(RoomFeeDecorator):
    def get_cost(self, hours: int) -> int:
        base_cost = self._decorated_fee.get_cost(hours)
        return int(base_cost * 0.7) # シニアは料金が基本料金の70%になる

# クライアント(使用例)
def calculate_fee_fix(hours: int, fee: AbstractRoomFee):
    print(f'カラオケの料金は: {fee.get_cost(hours)}円')

# test
calculate_fee_fix(2, BaseRoomFee()) # 基本料金
calculate_fee_fix(2, StudentDiscountDecorator(BaseRoomFee())) # 学生割引
calculate_fee_fix(2, MemberDiscountDecorator(BaseRoomFee())) # 会員割引
calculate_fee_fix(2, StudentDiscountDecorator(MemberDiscountDecorator(BaseRoomFee()))) # 学生割引と会員割引



# ⑤ ④に部屋料金が70%になるシニアデコレータを追加する
# 上部に追加する
