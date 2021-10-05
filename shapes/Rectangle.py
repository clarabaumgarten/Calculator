from shapes.Shape import Shape
from factory.AdvancedCalculatorFactory import AdvancedCalculatorFactory
from factory.BasicCalculatorFactory import BasicCalculatorFactory


class Rectangle(Shape):
    def __init__(self, height, width) -> None:
        self._height = str(height)
        self._width = width

    def area(self):
        expression = self._height + ' * ' + self._width
        calculator = BasicCalculatorFactory(expression)
        calculator.calculate()
        result = calculator.get_result()

        self._area = result

    def perimeter(self):
        expression = '2 * ' + self._height + ' + 2 * ' + self._width
        calculator = BasicCalculatorFactory(expression)
        calculator.calculate()
        result = calculator.get_result()

        self._perimeter = result
