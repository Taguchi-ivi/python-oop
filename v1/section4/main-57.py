# OCPを満たしていないコード
# class Notification:
#     def send(self, notification_type: str, user_id: int) -> None:
#         if notification_type == 'email':
#             # メールで通知を送信
#             print('メール')
#         elif notification_type == 'sms':
#             # SMSで通知を送信
#             print('SMS')

# notification = Notification()
# notification.send('sms', 123)

# OCPを満たす(抽象クラス)コード
from abc import ABC, abstractmethod

# 通知のインターフェース
class AbstractNotification(ABC):
    @abstractmethod
    def send(self, user_id: int) -> None:
        pass

# 具体的な通知
class EmailNotification(AbstractNotification):
    def send(self, user_id: int) -> None:
        # メールで通知を送信
        print('メール')

class SMSNotification(AbstractNotification):
    def send(self, user_id: int) -> None:
        # SMSで通知を送信
        print('SMS')

sms_notification = SMSNotification()
sms_notification.send(123)