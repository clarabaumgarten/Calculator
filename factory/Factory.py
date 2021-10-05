from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self, expression) -> None:
        self._expression = expression

    @abstractmethod
    def factory_method(self) -> float:
        pass

    def calculate(self) -> None:
        obj = self.factory_method()
        self._result = obj.calculate()
    
    def show_result(self) -> None:
        print("O resultado é: ", self._result)
