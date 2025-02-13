from __future__ import annotations
from abc import ABC, abstractmethod

class Mediator(ABC):
  @abstractmethod
  def register_user(self, user: User):
    pass

  @abstractmethod
  def send_message(self, msg: str, send_user: User):
    pass

class ChatRoom(Mediator):
  def __init__(self):
    self.__members = []

  def register_user(self, user: User):
    self.__members.append(user)

  def send_message(self, msg: str, send_user: User):
    for member in self.__members:
      if member != send_user:
        member.receive(msg)

class User(ABC):
  def __init__(self, mediator: Mediator, name: str):
    self._mediator = mediator
    self._name = name

  @abstractmethod
  def send(self, msg: str):
    pass

  @abstractmethod
  def receive(self, msg: str):
    pass

class ChatUser(User):
  def __init__(self, mediator: Mediator, name: str):
    super().__init__(mediator, name)

  def send(self, msg: str):
    print(f'{self._name}が送信: {msg}')
    self._mediator.send_message(f"{msg} from {self._name}", self)

  def receive(self, msg: str):
    print(f'{self._name}が受信: {msg}')


if __name__ == '__main__':
  chat_room = ChatRoom()

  yamada = ChatUser(chat_room, 'yamada')
  suzuki = ChatUser(chat_room, 'suzuki')
  tanaka = ChatUser(chat_room, 'tanaka')

  chat_room.register_user(yamada)
  chat_room.register_user(suzuki)
  chat_room.register_user(tanaka)

  yamada.send('こんにちは')
  tanaka.send('おはよう')