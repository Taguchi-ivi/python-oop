# 値オブジェクトの演習②

# 値オブジェクトを使わずにいる上記コードはどのような問題があるか
# ┗ SRPの原則に違反している(責務が複数存在している ユーザー名のチェック、年齢のチェック、ユーザーの表現)
# ┗ ユーザー名と年齢のチェックがUserクラスに依存している

# Userクラスでユーザー名と年齢のチェックをする
class User:
    def __init__(self, name: str, age: int) -> None:
        # nameの文字数のチェック
        if name is None:
            raise ValueError('ユーザー名は、3文字以上20文字以内にしてください。')
        if not 3 <= len(name) <= 20:
            raise ValueError('ユーザー名は、3文字以上20文字以内にしてください。')
        # nameに使用不可の文字が使われていないことのチェック

        # ageの範囲のチェック
        if age is None:
            raise ValueError('年齢は、0歳以上150歳以下にしてください。')
        if not 0 <= age <= 150:
            raise ValueError('年齢は、0歳以上150歳以下にしてください。')

        self.name = name
        self.age = age



