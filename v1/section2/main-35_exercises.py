# 元のクラス
# class User:
#     def __init__(self, name: str, age:str) -> None:
#         self.name = name
#         self.age = age

# ① nameとageがプライペートな変数になるように表現する
# class User:
#     def __init__(self, name: str, age:str) -> None:
#         self._name = name
#         self._age = age

# ② @propertyを使ってnameとageを取得できるようにする
# class User:
#     def __init__(self, name: str, age:str) -> None:
#         self._name = name
#         self._age = age
#     @property
#     def name(self):
#         return self._name
#     @property
#     def age(self):
#         return self._age

# ③ nameとageを変更可能な状態にする, nameは1-20文字, ageは0-150の範囲で設定可能
# コンストラクタにもガード節を追加すること
class User:
    def __init__(self, name: str, age:int) -> None:
        if not 1 <= len(name) <= 20:
            raise ValueError('nameは1-20文字で設定してください')
        if not 0 <= age <= 150:
            raise ValueError('ageは0-150の範囲で設定してください')
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        if not 1 <= len(name) <= 20:
            raise ValueError('nameは1-20文字で設定してください')
        self._name = name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age: int):
        if not 0 <= age <= 150:
            raise ValueError('ageは0-150の範囲で設定してください')
        self._age = age

def main():
    # ① nameとageがプライペートな変数になるように表現する
    # ② @propertyを使ってnameとageを取得できるようにする
    # ③ nameとageを変更可能な状態にする, nameは1-20文字, ageは0-150の範囲で設定可能
    pass

if __name__ == '__main__':
    main()