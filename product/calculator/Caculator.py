from abc import ABC, abstractmethod


class Calculator(ABC):
    def __init__(self, expression) -> None:
        self._expression = expression
    
    @abstractmethod
    def calculate():
        pass
