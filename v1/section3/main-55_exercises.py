# #54
# SRPの演習 演習の回答を記載することが目的なので、エラーになってますが気にせず。

# ① SRPとはどのような原則か
# - 単一責任の原則。責任を一つにすること
# - 1つのクラスは1つの責務を持つようにする。関数やメソッドも同様に。
# - ただ、それによるデメリットもあり、過度に分割するとコード量が多くなり、可読性も悪くなる
# それを解決するために、Facadeパターンというものがある。Facadeパターンは、複数のクラスをまとめて1つのクラスにすること。

# ② 凝集度と結合度とは何か
# - 凝集度：クラス内でどのくらい関連したコードをまとめるか。高いほど良い。
# - 結合度: クラス間でどのくらい依存しているか。低いほどよい。
# - ソフトウェアの設計において、凝集度が高く、結合度が低いほど、保守性や拡張性が高くなる。

# ③ 下記のコードはSRPに違反しているか、改善が必要であれば改善すること
# - 違反している。calculate_discount, send_email, calculate_pointsの3つの責務がある。また値オブジェクトを使うこともできる
# 修正前
class Customer:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'名前: {self.name}、年齢: {self.age}'

    def calculate_discount(self, total_amount: int) -> None:
        if self.age >= 60:
            discount = total_amount * 0.1
        else:
            discount = total_amount * 0.05
        print(f'割引額: {discount}')

    def send_email(self) -> None:
        email_content = f'お客様のご購入ありがとうございます、{self.name}さん。'
        # メール送信の処理
        print('メールを送信しました。')

    def calculate_points(self, total_amount: int) -> None:
        points = total_amount // 10
        print(f'獲得ポイント: {points}')
# 改善後
# 記載しないが、それぞれのメソッドをクラスに分けて、責務を一つにする




# ④ スマートホームのシステムについて
# 複数のメソッドを一つにまとめること。その場合どのような変更を加えればよいか
# 変更前
class Light:
    def turn_on(self):
        print('電灯がオンになりました')

    def turn_off(self):
        print('電灯がオフになりました')

class AirConditioner:
    def turn_on(self):
        print('エアコンがオンになりました')

    def turn_off(self):
        print('エアコンがオフになりました')

class Curtain:
    def open(self):
        print('カーテンを開きました')

    def close(self):
        print('カーテンを閉じました')
# 変更後
class Light:
    def turn_on(self):
        print('電灯がオンになりました')

    def turn_off(self):
        print('電灯がオフになりました')

class AirConditioner:
    def turn_on(self):
        print('エアコンがオンになりました')

    def turn_off(self):
        print('エアコンがオフになりました')

class Curtain:
    def open(self):
        print('カーテンを開きました')

    def close(self):
        print('カーテンを閉じました')
class SmartHomeFacade:
    def __init__(self):
        self.light = Light()
        self.air_conditioner = AirConditioner()
        self.curtain = Curtain()

    def leave_home(self):
        self.light.turn_off()
        self.air_conditioner.turn_off()
        self.curtain.close()

    def come_home(self):
        self.light.turn_on()
        self.air_conditioner.turn_on()
        self.curtain.open()
smart_home = SmartHomeFacade()
smart_home.leave_home()
smart_home.come_home()

# ⑤ メールアドレスを表現する値オブジェクトを作成する
# 条件として@が含まれていること、@の前には少なくとも1文字以上、後ろには少なくとも2文字以上の文字列が入ること
class EmailAddress:
    def __init__(self, email: str):
        if '@' not in email:
            raise ValueError(f"無効なメールの形式です: {email}")
        local_part, domain_part = email.split('@')
        if len(local_part) < 1 or len(domain_part) < 2:
            raise ValueError(f"無効なメールの形式です: {email}")
        self.email = email