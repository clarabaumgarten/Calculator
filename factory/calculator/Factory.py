from abc import ABC, abstractmethod
from util.turnStringToNumber import turns_string_number_to_float


class Factory(ABC):
    def __init__(self, expression) -> None:
        expression = expression.split()
        self._expression = list(map(turns_string_number_to_float, expression))

    @abstractmethod
    def factory_method(self) -> float:
        pass

    def calculate(self) -> None:
        obj = self.factory_method()
        self._result = obj.calculate()
    
    def show_result(self) -> None:
        print("O resultado é: ", self._result)

    def get_result(self) -> float:
        return self._result
