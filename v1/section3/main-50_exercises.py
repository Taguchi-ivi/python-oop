# 値オブジェクトの演習①

# 値オブジェクトを使わずにいるコードはどのような問題があるか
# ┗　不正値チェックが分散する
# ┗　オブジェクト指向っぽくない、手続型のコードになっている
class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

# ユーザー作成時にチェックする
name: str = 'さとう'
age: int = 30

if name is None:
    raise ValueError('ユーザー名は、3文字以上20文字以内にしてください。')
elif not 3 <= len(name) <= 20:
    raise ValueError('ユーザー名は、3文字以上20文字以内にしてください。')
elif age is None:
    raise ValueError('年齢は、0歳以上150歳以下にしてください。')
elif not 0 <= age <= 150:
    raise ValueError('年齢は、0歳以上150歳以下にしてください。')
else:
    user = User(name, age)
