# 銀行口座のクラス
# 修正前は#73などを参照
# 事前条件を満たす改善(ガード節を追加)
class BankAccount:
  def __init__(self) -> None:
    self._balance = 0

  def deposit(self, amount: int) -> None:
    if amount < 0:
      raise ValueError("事前条件: 入金額は0以上")
    self._balance += amount

  def withdraw(self, amount: int) -> None:
    if amount < 0:
      raise ValueError("事前条件: 入金額は0以上")
    if amount > self._balance:
      raise ValueError("事前条件: 引き出し額は現在の残高以下")
    self._balance -= amount

# 契約に違反した場合は、例外を発生させることで、契約に違反したまま処理が続くことを防ぐ
# そもそもamountを値オブジェクトにする方法ももちろんあり