from calculators.BasicCalculator import BasicCalculator
from factory.Factory import Factory


class BasicCalculatorFactory(Factory):
    def factory_method(self) -> float:
        return BasicCalculator(self._expression)
