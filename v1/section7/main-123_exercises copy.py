# 演習 ④ ~ ⑤
from abc import abstractmethod, ABC

# ④ 以下のコードはDIPに違反しているか、してたら理由を述べて改善する
# 違反している
# 理由: Carクラスが抽象クラスではなく、GasolineEngineクラスとNormalTiresクラスに依存しているため。
# 通常車はエンジンやタイヤは切り替え可能なので、ドメインルールを反映するためにDIPを適用するのが望ましい
# テストがしにくく、変更がしにくい。

# 修正前
# class GasolineEngine:
#     def start(self) -> None:
#         print('ガソリンエンジンが始動しました')
# class NormalTires:
#     def __init__(self) -> None:
#         self._pressure: int = 100
#     def is_inflated(self) -> bool:
#         if self._pressure >= 1:
#             return True
#         else:
#             print('タイヤに空気を入れてください')
#             return False
#     def use_air(self) -> None:
#         self._pressure -= 1
# class Car:
#     def __init__(self) -> None:
#         self.engine = GasolineEngine()
#         self.tires = NormalTires()
#     def start(self) -> None:
#         if self.tires.is_inflated():
#             self.engine.start()
#             self.tires.use_air()
#             print('車が発進しました')

# 修正後
class AbstractEngine(ABC):
    @abstractmethod
    def start(self) -> None:
        pass
class AbstractTires(ABC):
    @abstractmethod
    def is_inflated(self) -> bool:
        pass
    @abstractmethod
    def use_air(self) -> None:
        pass

class GasolineEngine(AbstractEngine):
    def start(self) -> None:
        print('ガソリンエンジンが始動しました')
class NormalTires(AbstractTires):
    def __init__(self) -> None:
        self._pressure: int = 100
    def is_inflated(self) -> bool:
        if self._pressure >= 1:
            return True
        else:
            print('タイヤに空気を入れてください')
            return False
    def use_air(self) -> None:
        self._pressure -= 1
class Car:
    def __init__(self, engine: AbstractEngine, tires: AbstractTires) -> None:
        self.engine = engine
        self.tires = tires
    def start(self) -> None:
        if self.tires.is_inflated():
            self.engine.start()
            self.tires.use_air()
            print('車が発進しました')
# 使い方の例
engine = GasolineEngine()
tires = NormalTires()
car = Car(engine, tires)
car.start()


# ⑤ 以下のコードはDIPに違反しているか、してたら理由を述べて改善する
# 違反している
# ユースケースが直接RDBUserRepositoryを参照しているため、ユースケースがRDBに依存している。
# それによってDBの変更があった場合、ユースケースにも変更が必要になるため、変更がしにくい。
# また、ユースケースがRDBUserRepositoryのインスタンスを生成しているため、テストがしにくい。
# 修正前
#　ユーザーを表現するクラス
# class User:
#     def __init__(self, id: int, name: str):
#         self.id = id
#         self.name = name
# # RDBへのアクセスを担当するクラス
# class RDBUserRepository:
#     def save(self, user: User) -> None:
#         print(f'Save {user.name} to the RDB')  # 疑似的なRDBへの保存処理
#     def get(self, id: int) -> User:
#         print(f'Get user from the RDB by id {id}')  # 疑似的なRDBからの取得処理
#         return User(id, 'user_name')
# # ユーザーに関するユースケースを実現するクラス
# class UserApplicationService:
#     def __init__(self):
#         self.user_repository = RDBUserRepository()
#     def create(self, id: int, name: str):
#         user = User(id, name)
#         self.user_repository.save(user)

# 修正後
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
# RDBへのアクセスを担当するクラス
class AbstractUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass
    @abstractmethod
    def get(self, id: int) -> User:
        pass
class RDBUserRepository(AbstractUserRepository):
    def save(self, user: User) -> None:
        print(f'Save {user.name} to the RDB')  # 疑似的なRDBへの保存処理
    def get(self, id: int) -> User:
        print(f'Get user from the RDB by id {id}')  # 疑似的なRDBからの取得処理
        return User(id, 'user_name')
# ユーザーに関するユースケースを実現するクラス
class UserApplicationService:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository
    def create(self, id: int, name: str):
        user = User(id, name)
        self.user_repository.save(user)