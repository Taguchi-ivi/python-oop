# Repositoryパターン
from abc import abstractmethod, ABC
# あまり良くない例
#　最悪の方法（SQLをコードにベタ書き）
# class User:
#     def __init__(self, name: str):
#         self.name = name

# class UserApplicationService:
#     # ユーザーの新規作成を行うメソッド
#     def register_user(self, name: str) -> None:
#         user = User(name)

#         # データベースに接続する処理
#         query = f"INSERT INTO users (name) VALUES ('{user.name}')"
#         # クエリの検証・実行、データベースの開放処理
#         print("start sql query:", query)
# # 使用例
# user_application_service = UserApplicationService()
# user_application_service.register_user('ユーザー')

# 上記コードの問題点
# 1. register_userメソッドの責務は、ユーザー登録なのに、データベース操作の責務も持っている
# 2. データベースが変わったときにregister_userメソッドも変更しなければならない
# 3. データベースと密接合しているため、テストがしにくい

# Repositoryパターンを使った改善
# class User:
#     def __init__(self, name: str):
#         self.name = name
# # Repositoryパターン
# class SQLiteUserRepository:
#     def add(self, user: User) -> None:
#         # データベースに接続する処理
#         query = f"INSERT INTO users (name) VALUES ('{user.name}')"
#         # クエリの検証・実行、データベースの開放処理
# # ユーザーのユースケースを表現するクラス
# class UserApplicationService:
#     def __init__(self):
#         self.repository = SQLiteUserRepository()
#     def register_user(self, name: str) -> None:
#         user = User(name)
#         self.repository.add(user)
# # 使用例
# user_application_service = UserApplicationService()
# user_application_service.register_user('ユーザー')

# 改善点
# データベース操作をSQLiteUserRepositoryクラスで抽象化した
# その結果、ユーザー登録とデータベース操作の責務が分離された

# ただまだ問題点が残っている
# 1. UserApplicationService(上位モジュール)がSQLiteUserRepository(下位モジュール)に依存している
# 2. データベースを動的に切り替えることができず、テストがしづらい

# 更なる改善(DIPとDIを適用)
class User:
    def __init__(self, name: str):
        self.name = name
# リポジトリの抽象を用意
class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        pass

class SQLiteUserRepository(UserRepository):
    def add(self, user: User) -> None:
        # データベースに接続する処理
        query = f"INSERT INTO users (name) VALUES ('{user.name}')"
        # クエリの検証・実行、データベースの開放処理
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []
    def add(self, user: User) -> None:
        self.users.append(user)

# ユーザーのユースケースを表現するクラス
class UserApplicationService:
    def __init__(self, repository: UserRepository): # 抽象に依存、DIパターン
        self.repository = repository
    def register_user(self, name: str) -> None:
        user = User(name)
        self.repository.add(user)
# 使用例
sqlite_repo = SQLiteUserRepository()
user_application_service = UserApplicationService(sqlite_repo)
user_application_service.register_user('ユーザー')

# 改善点
# DIPを満たすようになった。UserApplicationServiceはUserRepositoryの抽象に依存している
# リポジトリをSQLiteとインクリメントで切り替えられるようになった
