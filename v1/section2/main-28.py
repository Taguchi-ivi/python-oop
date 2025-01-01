
# pythonでは、アンダースコアで始まる名前はプライベートとして表現できる
# ただし、実際にはアクセスできる
# そのためname manglingよりもアンスコを1つにして、プライベートを表現することが多い
# name manglingの使い道としては、サブクラスで同じ名前の変数を使いたい場合などがある
class MyClass:
    __PI = 3.14 # name manglingにより、privateっぽくなるが、_MyClass__PIという名前に変換されている
    def __init__(self, value=0, r=1):
        self._value = value
        self.__r = r
        self._hight = 10
    def get_value(self):
        return self._value
    def _private_method(self):
        print('private method')

    @property
    def hight(self):
        return self._hight

    # setterを定義することで、プロパティを変更する前後に処理を挟むことができる
    @hight.setter
    def hight(self, value):
        if value < 0:
            raise ValueError('hight must be positive')
        self._hight = value

def main():
    try20()

# #20 - #28
def try20():
    # フールプルーフとアクセス制限
    my_class = MyClass(5, 2)

    # privateを表現できるが、実際にはアクセスできる
    print(my_class._value)
    my_class._private_method()

    # name manglingにより、privateっぽくなるが、_MyClass__PIという名前に変換されている
    # print(my_class.__PI) # AttributeError: 'MyClass' object has
    print(my_class._MyClass__PI) # これで呼び出せてしまう(name mangling)
    print(my_class._MyClass__r) # これで呼び出せてしまう(name mangling)

    # プロパティデコレータ(メソッドを属性に変換して呼び出し専用ぽくできる)
    print(my_class.hight) # 10 my_class.hight()が呼び出されている
    # my_class.hight = 20 # AttributeError: can't set attribute # setterがない場合、これはできない
    my_class._hight = 20 # これはできてしまうので、プライベートとしては弱い
    print(my_class.hight)

    # setterがある場合は、これで値を変更できる
    # 本来はメソッドを呼び出しているが、プロパティとして呼び出しているように見える
    # my_class.hight = -1 # ValueError: hight must be positive
    my_class.hight = 30
    print(my_class.hight)


if __name__ == '__main__':
    main()