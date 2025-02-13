from abc import ABC, abstractmethod
import datetime


class Memento(ABC):
  @abstractmethod
  def get_memo(self) -> str:
    pass


class ConcreteMemento(Memento):
  def __init__(self, memo: str):
    self.__memo = memo
    self.__date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  def get_memo(self) -> str:
    return self.__memo

  def __str__(self):
    return f"{self.__date} / {self.get_memo()}"

class NotePad:
  def __init__(self, memo: str):
    self.__memo = memo

  def get_memo(self) -> str:
    return self.__memo

  def add_memo(self, memo: str):
    self.__memo = memo

  def save(self) -> Memento:
    print("memo saved")
    return ConcreteMemento(self.get_memo())

  def restore(self, memento: Memento):
    self.add_memo(memento.get_memo())

class CareTaker:
  def __init__(self, notepad: NotePad, mementos: list[Memento] = []):
    self.__notepad = notepad
    self.__mementos = mementos

  def backup(self):
    self.__mementos.append(self.__notepad.save())

  def undo(self):
    if not len(self.__mementos):
      print("スナップショットがありません")
      return
    memento = self.__mementos.pop() # 最後に保存したスナップショットを取り出す
    self.__notepad.restore(memento)

  def show_history(self):
    for memento in self.__mementos:
      print(memento)


if __name__ == "__main__":
  notepad = NotePad("first memo")
  caretaker = CareTaker(notepad)
  caretaker.backup()

  notepad.add_memo("second memo")
  caretaker.backup()

  notepad.add_memo("third memo")
  caretaker.backup()
  print(notepad.get_memo())

  caretaker.show_history()

  print("")
  caretaker.undo()
  print(notepad.get_memo())

  caretaker.undo()
  print(notepad.get_memo())

  caretaker.undo()
  print(notepad.get_memo())

  caretaker.show_history()