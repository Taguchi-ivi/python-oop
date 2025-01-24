

# その他クラス群
class Product:
    def get_product(self, name: str) -> None:
        print(f'{name}の商品を取得しました')


class Payment:
    def make_payment(self, name: str) -> None:
        print(f'{name}の支払いを完了しました')

class Invoice:
    def send_invoice(self, name: str) -> None:
        print(f'{name}の請求書を送りました')


# Facadeクラス
class Order:
    def place_order(self, name: str) -> None:
        print("注文開始")
        product = Product()
        product.get_product(name)

        payment = Payment()
        payment.make_payment(name)

        invoice = Invoice()
        invoice.send_invoice(name)

        print('注文完了')

if __name__ == '__main__':
    order = Order()
    order.place_order('apple')