
def main():
    # ①
    try:
        x = int(input('Enter a number: '))
        result = 10 / x
        print("結果",result)
    except ZeroDivisionError:
        print("0で割ることはできません")
    except ValueError:
        print("数字を入力してください")

    # ②はだるいので考えて終わり

if __name__ == '__main__':
    main()