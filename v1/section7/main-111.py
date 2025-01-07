# 下記は違反していない。全て抽象クラスに依存しているコード
# ストラテジーパターン
from abc import ABC, abstractmethod

class AbstractNotification(ABC): # 抽象クラス
    @abstractmethod
    def send(self, user_id: int) -> None:
        pass

class EmailNotification(AbstractNotification): # 具象クラス
    def send(self, user_id: int) -> None:
        # メールで通知を送信
        print('メール')

class SMSNotification(AbstractNotification): # 具象クラス
    def send(self, user_id: int) -> None:
        # SMSで通知を送信
        print('SMS')

def notify(user_id: int, notification: AbstractNotification):
    notification.send(user_id)

# 関係性
# notify -> AbstractNotification(notifyのインターフェース)
#                        ↑
#        EmailNotification, SMSNotification

# 上位モジュール: notify関数(とnotify関数が使うインターフェース)
# 下位モジュール: 具象クラス