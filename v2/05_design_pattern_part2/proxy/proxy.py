from abc import ABC, abstractmethod

class Server(ABC):
    @abstractmethod
    def handle(self, user_id: str):
        pass

class RealServer(Server):
    def handle(self, user_id: str):
        print(f"{user_id}の処理を実行中")

class Proxy(Server):
    def __init__(self, server: Server) -> None:
        self.__server = server

    def _authorize(self, user_id: str):
        authorized_user_ids = ["1", "2", "3"]
        if user_id not in authorized_user_ids:
            raise PermissionError("権限がありません")

    def handle(self, user_id: str):
        self._authorize(user_id)

        print("処理を開始します")
        self.__server.handle(user_id)
        print("処理が完了しました")


if __name__ == "__main__":
    server = RealServer()
    proxy = Proxy(server)

    proxy.handle("1")
    # proxy.handle("4")  # PermissionError: 権限がありません