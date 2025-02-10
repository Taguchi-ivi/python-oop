# ディレクトリのツリー構造
from abc import ABC, abstractmethod

class Entry(ABC):
  def __init__(self, name: str) -> None:
    self.__name = name

  @property
  def name(self) -> str:
    return self.__name

  @abstractmethod
  def get_size(self) -> int:
    pass

  @abstractmethod
  def remove(self) -> None:
    pass


class File(Entry):
  def __init__(self, name: str, size: int) -> None:
    super().__init__(name)
    self.__size = size

  def get_size(self) -> int:
    return self.__size

  def remove(self) -> None:
    print(f'{self.name}を削除しました')

class Directory(Entry):
  def __init__(self, name: str) -> None:
    super().__init__(name)
    self.__children: list[Entry] = []

  def get_size(self) -> int:
    size = 0
    for child in self.__children:
      size += child.get_size()
    return size

  def remove(self) -> None:
    for child in self.__children:
      child.remove()
    print(f'{self.name}を削除しました')

  def add(self, child: Entry) -> None:
    self.__children.append(child)

# file, directoryどちらでも動作する
def client(entry: Entry) -> None:
  print(f'{entry.name}のサイズ: {entry.get_size()}')
  entry.remove()


if __name__ == '__main__':
  dir1 = Directory("design_pattern")
  dir2 = Directory("composite")
  file1 = File("composite.py", 100)
  file2 = File("practice.png", 150)

  dir2.add(file1)
  dir2.add(file2)
  dir1.add(dir2)

  client(dir1)