# ちょっとした演習
# インターフェースの分離の一例
from abc import ABC, abstractmethod

# 下記はISPに違反しているか

# ドキュメントの値オブジェクト
# class Document:
#     def __init__(self, content: str):
#         self.content = content
# # 複合機クラス
# class MultifunctionPrinter:
#     def print_document(self, document: Document) -> None:
#         print(f'プリントを開始します')
#         # プリントの処理

#     def copy_document(self, document: Document) -> None:
#         print(f'コピーを開始します')
#         # コピーの処理
# # クライアント
# class PrintClient:
#     def __init__(self, printer: MultifunctionPrinter):
#         self.printer = printer

#     def execute(self, document: Document) -> None:
#         self.printer.print_document(document)
# class CopyClient:
#     def __init__(self, printer: MultifunctionPrinter):
#         self.printer = printer

#     def execute(self, document: Document) -> None:
#         self.printer.copy_document(document)

# MultifunctionPrinterクラスは2種類のクライアントを持っている
# - プリントを行う
# - コピーを行う
# プリントとコピーしか行わないクライアントが存在するため、不要なメソッドが公開されておりISPに違反している

# インターフェースの分離の一例
# クライアントごとにインターフェースを分けて、次のように実装するのが望ましい
class Document:
    def __init__(self, content: str):
        self.content = content
# プリントの機能のみを提供するインターフェース
class PrintInterface(ABC):
    @abstractmethod
    def print_document(self, document: Document) -> None:
        pass

# コピーの機能のみを提供するインターフェース
class CopyInterface(ABC):
    @abstractmethod
    def copy_document(self, document: Document) -> None:
        pass

class MultifunctionPrinter(PrintInterface, CopyInterface):
    def print_document(self, document: Document) -> None:
        print(f'プリントを開始します')
        # プリントの処理

    def copy_document(self, document: Document) -> None:
        print(f'コピーを開始します')
        # コピーの処理
# クライアント
class PrintClient:
    def __init__(self, printer: MultifunctionPrinter):
        self.printer = printer

    def execute(self, document: Document) -> None:
        self.printer.print_document(document)
class CopyClient:
    def __init__(self, printer: MultifunctionPrinter):
        self.printer = printer

    def execute(self, document: Document) -> None:
        self.printer.copy_document(document)