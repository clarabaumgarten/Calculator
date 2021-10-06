from product.calculator.BasicCalculator import BasicCalculator
from factory.calculator.Factory import Factory


class BasicCalculatorFactory(Factory):
    def factory_method(self) -> float:
        return BasicCalculator(self._expression)
