import datetime

class Logger:
    _instance = None

    # インスタンスを生成する前の処理
    # initはコンストラクタ(インスタンスを生成する処理)
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def output(self, content: str) -> None:
        now = datetime.datetime.now()
        print(f"{now}: {content}")


class Test:
    pass


if __name__ == "__main__":
    test1 = Test()
    test2 = Test()
    print("test: ", test1 == test2)

    # loggerは同じインスタンスを参照している、必ず1つのインスタンスしか生成されない
    logger1 = Logger()
    logger2 = Logger()

    print("logger: ", logger1 == logger2)

    logger1.output("logger1のログ")
    logger2.output("logger2のログ")