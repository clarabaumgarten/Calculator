from product.shape.Shape import Shape
from factory.calculator.AdvancedCalculatorFactory import AdvancedCalculatorFactory
from factory.calculator.BasicCalculatorFactory import BasicCalculatorFactory


class Circle(Shape):
    _pi = '3.1415'

    def __init__(self, raio) -> None:
        self._raio = str(raio)

    def area(self):
        expression = self._raio + ' ** 2'
        calculator = AdvancedCalculatorFactory(expression)
        calculator.calculate()
        result = calculator.get_result()

        expression = self._pi + ' * ' + str(result)

        calculator = BasicCalculatorFactory(expression)

        calculator.calculate()
        result = calculator.get_result()

        self._area = result

    def perimeter(self):
        expression = '2 * ' + self._raio + ' * ' + self._pi
        calculator = BasicCalculatorFactory(expression)
        calculator.calculate()
        result = calculator.get_result()

        self._perimeter = result
