from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def press(self) -> None:
        pass


class Checkbox(ABC):
    @abstractmethod
    def switch(self) -> None:
        pass


class CUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsButton(Button):
    def press(self) -> None:
        print("Windows button is pressed")

class WindowsCheckbox(Checkbox):
    def switch(self) -> None:
        print("Windows checkbox is switched")

class WindowsCUIFactory(CUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacButton(Button):
    def press(self) -> None:
        print("Mac button is pressed")

class MacCheckbox(Checkbox):
    def switch(self) -> None:
        print("Mac checkbox is switched")

class MacCUIFactory(CUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def run(factory: CUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.press()
    checkbox.switch()

if __name__ == "__main__":
    run(WindowsCUIFactory())
    run(MacCUIFactory())