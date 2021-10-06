from product.calculator.AdvancedCalculator import AdvancedCalculator
from factory.calculator.Factory import Factory


class AdvancedCalculatorFactory(Factory):
    def factory_method(self) -> float:
        return AdvancedCalculator(self._expression)
