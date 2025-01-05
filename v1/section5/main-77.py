# 銀行口座のクラス
# 修正前は#73などを参照
# 不変条件を満たす改善(propertyを使う)
class BankAccount:
  def __init__(self) -> None:
    self._balance = 0

  # クラス外部から変更されないようにする(もどき)
  @property
  def balance(self) -> int:
    return self._balance

  def deposit(self, amount: int) -> None:
    if amount < 0:
      raise ValueError("事前条件: 入金額は0以上")

    new_balance = self._balance + amount
    self._check_invariant(new_balance)
    self._balance += new_balance

  def withdraw(self, amount: int) -> None:
    if amount < 0:
      raise ValueError("事前条件: 入金額は0以上")
    if amount > self._balance:
      raise ValueError("事前条件: 引き出し額は現在の残高以下")

    new_balance = self._balance - amount
    self._check_invariant(new_balance)
    self._balance += new_balance

  # 不変条件を確認するメソッド
  def _check_invariant(self, new_balance):
    if new_balance < 0:
      raise ValueError("不変条件: 残高は0以上")

# 上記を見てもわかるように、事前条件が保証されていれば不変条件は不要になる(冗長)
# ガード節で組み込むというよりテストケースとして確認されるが基本。コードにするほどではない。あまり価値がない。

# 契約による設計を意識すると、コードがより正確・頑健になる