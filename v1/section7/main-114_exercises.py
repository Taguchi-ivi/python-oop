# ちょっとした演習
from abc import ABC, abstractmethod

# 以下はDIPに違反している。
# DIを使ってFastSwimmingとSlowSwimmingをFishオブジェクト生成時に切り替える
# 元のコード
# class FastSwimming:
#     def swim(self) -> str:
#         return '速く泳ぎます'

# class SlowSwimming:
#     def swim(self) -> str:
#         return 'ゆっくり泳ぎます'

# class Fish:
#     def __init__(self) -> None:
#         self.swimming_behaviour = FastSwimming()

#     def swim(self) -> None:
#         print(f'魚が{self.swimming_behaviour.swim()}')

# 修正後
class SwimmingBehaviour(ABC):
    @abstractmethod
    def swim(self) -> str:
        pass

class FastSwimming(SwimmingBehaviour):
    def swim(self) -> str:
        return '速く泳ぎます'

class SlowSwimming(SwimmingBehaviour):
    def swim(self) -> str:
        return 'ゆっくり泳ぎます'

class Fish:
    def __init__(self, swimming_type: SwimmingBehaviour) -> None:
        self.swimming_behaviour = swimming_type

    def swim(self) -> None:
        print(f'魚が{self.swimming_behaviour.swim()}')