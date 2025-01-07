# 下記は上位モジュールが下位モジュールに依存している。違反している例

# 関係性
# 上位モジュールである注文処理（process_order）が
#  - ユーザーの有効性チェック
#  - 在庫チェック
#  - 支払い処理
#  - 在庫更新処理
# といった、データベースアクセスや外部サービスの利用などを伴う、下位モジュールから構成されている

# eコマースの注文処理
def validate_user(user_name: str):
    # ユーザーの有効性をチェック
    pass

def check_stock(product_name: str):
    # 在庫をチェック
    pass

def make_payment(user_name: str, product_name: str):
    # 支払いを処理
    pass

def update_stock(product_name: str) -> None:
    # 在庫を更新
    pass

def process_order(user_name: str, product_name: str) -> str:
    if not validate_user(user_name):
        return '無効なユーザーです。'
    if not check_stock(product_name):
        return '在庫切れです。'
    if not make_payment(user_name, product_name):
        return '購入額が足りません。'

    update_stock(product_name)
    return '注文処理が完了しました。'