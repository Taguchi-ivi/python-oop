# 銀行口座のクラス
# 契約による設計を意識していないコード
class BankAccount:
  def __init__(self) -> None:
    self._balance = 0
  def deposit(self, amount: int) -> None:
    self._balance += amount
  def withdraw(self, amount: int) -> None:
    self._balance -= amount

# 上記コードの問題点
# 入出金額を負の値にできてしまう
# 残高が0より小さくなる可能性がある
# 残高をクラスの外部から変更できる

# このような問題は銀行口座が持つ以下のルール反映されていないから
# 入出金額は0以上の整数値（事前条件）
# 残高以上の額を出金することはできない（事前条件）
# 入金・出金額と口座残高が整合性を保つ必要がある（事後条件）
# 残高は常に0以上の整数値（不変条件）
# 達人プログラマー: 事前をしっかりすることで、事後と不変を守る的な。