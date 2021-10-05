from calculators.AdvancedCalculator import AdvancedCalculator
from factory.Factory import Factory


class AdvancedCalculatorFactory(Factory):
    def factory_method(self) -> float:
        return AdvancedCalculator(self._expression)
