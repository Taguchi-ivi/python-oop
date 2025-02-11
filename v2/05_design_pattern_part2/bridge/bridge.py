from abc import ABC, abstractmethod

class MessageApp(ABC):
    @abstractmethod
    def send(self):
        pass

class Line(MessageApp):
    def send(self):
        print("LINEでメッセージを送信します")

class Twitter(MessageApp):
    def send(self):
        print("Twitterでメッセージを送信します")

class Facebook(MessageApp):
    def send(self):
        print("Facebookでメッセージを送信します")


class OS(ABC):
    def __init__(self):
        self._app = None

    def set_app(self, app: MessageApp):
        self._app = app

    @abstractmethod
    def send_message(self):
        pass

class IOS(OS):
    def send_message(self):
        print("iOSでメッセージを送信します")

        if self._app:
          self._app.send()
        else:
          raise Exception("アプリが設定されていません")

class Android(OS):
    def send_message(self):
        print("Androidでメッセージを送信します")

        if self._app:
          self._app.send()
        else:
          raise Exception("アプリが設定されていません")

if __name__ == "__main__":
    line = Line()
    twitter = Twitter()
    facebook = Facebook()

    ios = IOS()
    android = Android()

    ios.set_app(line)
    ios.send_message()

    android.set_app(facebook)
    android.send_message()