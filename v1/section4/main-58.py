# 抽象クラス（インターフェース）を用意すれば、具象クラスに依存しなくなる
from abc import ABC, abstractmethod

class AbstractNotification(ABC):
    @abstractmethod
    def send(self, user_id: int) -> None:
        pass

class EmailNotification(AbstractNotification):
    def send(self, user_id: int) -> None:
        # メールで通知を送信
        print('メール')

class SMSNotification(AbstractNotification):
    def send(self, user_id: int) -> None:
        # SMSで通知を送信
        print('SMS')

class PushNotification(AbstractNotification):
    def send(self, user_id: int) -> None:
        # プッシュ通知を送信
        print('プッシュ通知')

# 通知機能のクライアントである notify関数は具象クラスに依存していない
def notify(user_id: int, notification: AbstractNotification): # AbstractNotificationのサブクラスだけ渡せる
    # 使う側、クライアント側も具象クラスに依存していない、抽象クラスに依存している
    # そのため、実装がどうなっているか知る必要がなくなり、影響を受けにくくなる
    notification.send(user_id)