
def main():
    try12(0)
    try16()

# #12, #13, #14
def try12(num: int):
    # except部分には複数の例外を指定することができる
    # elseは例外が発生しなかった場合に実行される
    # elseは基本的にfinallyの前処理として書くことが多い(またtryを最小限にすることができる)
    # finallyは例外の有無にかかわらず最後に必ず実行される
    # キャッチする例外はなるべく具体的な方が望ましい
    try:
        check = int(num)
        print(1/ check)
    except ZeroDivisionError:
        print('Error: Division by zero')
    except ValueError:
        print('Error: Value error')
    except Exception as e:
        # Exceptionは全て。大元のオブジェクト。全ての例外はExceptionを継承している
        print('Error: ', e)

    # アンチパターン: 下記のようにすることで、全ての例外を握りつぶすことができる。
    # try:
    #     # 例外が発生する可能性のあるコード
    # except Exception:
    #     pass


# #16
def try16():
    # raiseとガード節を使って例外を発生させることができる
    # 下記をすることで不正値が入力された場合に、オブジェクトを生成することができないようにすることができる
    # 不正な値が渡されたら例外を発生させるようなメソッドをガード節という
    raise ValueError('制限がある場合はここにメッセージを入力してコンストラクタで例外を発生させる')

if __name__ == '__main__':
    main()