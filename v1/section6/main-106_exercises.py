# 演習
from abc import ABC, abstractmethod

# ① ISPとはどのような原則か
# インターフェース分離の法則
# クライアントにクライアントが利用しないメソッドへの依存を強制しない
# これによってクライアントと疎結合することができる。
# クライアントが利用しなければいい話というわけではない。バカでもできる。潜在的な依存を生む可能性を潰すことが重要

# ② Hyrumの法則とはどのような経験則
# 公開されているといつの間にか使ってしまう的な。
# 公開していたらユーザーが暗黙的に使ってしまうもの

# ③ SRPとISPとの共通点と相違点と二つが必要な理由について考えてみてください
# 単一責任を全うする
# SRP: クラスの責務が高凝集になり、責務間が疎結合になる
# ISP: インターフェースが高凝集になり、クライアントと疎結合になる
# 必要な理由
# solidという単語になること。
# 単一責任をどうすればできるかをわかりやすくしてくれている


# ④ 音楽ストリーミングのサービスISPに違反しているか。していたら直せ
# 違反している
# 無料ユーザーと有料ユーザーで使用できる機能が違うのにメソッドが公開されてしまっている
# 修正前
# class AbstractMusicPlayer(ABC):
#     def __init__(self, playlist: list):
#         self.playlist = playlist
#     @abstractmethod
#     def play(self) -> None:
#         pass
#     @abstractmethod
#     def pause(self) -> None:
#         pass
#     @abstractmethod
#     def skip(self) -> None:
#         pass
# class FreeUserMusicPlayer(AbstractMusicPlayer):
#     def play(self) -> None:
#         print('広告表示')
#         print('再生します')
#         # 再生処理
#     def pause(self) -> None:
#         pass
#     def skip(self) -> None:
#         pass
# class PaidUserMusicPlayer(AbstractMusicPlayer):
#     def play(self) -> None:
#         print('再生します')
#         # 再生処理
#     def pause(self) -> None:
#         print('一時停止します')
#         # 一時停止処理
#     def skip(self) -> None:
#         print('スキップします')
#         # スキップ処理


# 修正後
class MusicPlayerInterface(ABC):
    def __init__(self, playlist: list):
        self.playlist = playlist
    @abstractmethod
    def play(self) -> None:
        pass
class PaidUserMusicPlayerInterface(MusicPlayerInterface):
    @abstractmethod
    def pause(self) -> None:
        pass
    @abstractmethod
    def skip(self) -> None:
        pass
class FreeUserMusicPlayer(MusicPlayerInterface):
    def play(self) -> None:
        print('広告表示')
        print('再生します')
        # 再生処理
class PaidUserMusicPlayer(PaidUserMusicPlayerInterface):
    def play(self) -> None:
        print('再生します')
        # 再生処理
    def pause(self) -> None:
        print('一時停止します')
        # 一時停止処理
    def skip(self) -> None:
        print('スキップします')
        # スキップ処理


# ⑤ ATMを表現したコードISPに違反しているか。していたら直せ
# それぞれでクライアントは1つだけの動作をする。全て公開されているため
# クライアントごとに一つのインターフェースを実装するべき
# 修正前
# class BankAccount:
#     def __init__(self):
#         pass
# class ATMInterface(ABC):
#     @abstractmethod
#     def withdraw_transaction(self, amount: int) -> None:
#         pass
#     @abstractmethod
#     def deposit_transaction(self, amount: int) -> None:
#         pass
#     @abstractmethod
#     def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
#         pass
# class ATM(ATMInterface):
#     def __init__(self, bank_account: BankAccount):
#         self.bank_account = bank_account
#     def withdraw_transaction(self, amount: int) -> None:
#         # 引き出し処理
#         print('出金成功')
#     def deposit_transaction(self, amount: int) -> None:
#         # 預け入れ処理
#         print('入金成功')
#     def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
#         # 振り込み処理
#         print('振込成功')

# 修正後
class BankAccount:
    def __init__(self):
        pass
# 利用目的ごとにインターフェースを分割
class WithdrawInterface(ABC):
    @abstractmethod
    def withdraw_transaction(self, amount: int) -> None:
        pass
class DepositInterface(ABC):
    @abstractmethod
    def deposit_transaction(self, amount: int) -> None:
        pass
class TransferInterface(ABC):
    @abstractmethod
    def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
        pass
# それらあを多重承継する具象クラス
class ATM(WithdrawInterface, DepositInterface, TransferInterface):
    def __init__(self, bank_account: BankAccount):
        self.bank_account = bank_account
    def withdraw_transaction(self, amount: int) -> None:
        # 引き出し処理
        print('出金成功')
    def deposit_transaction(self, amount: int) -> None:
        # 預け入れ処理
        print('入金成功')
    def transfer_transaction(self, to_bank_account: BankAccount, amount: int) -> None:
        # 振り込み処理
        print('振込成功')