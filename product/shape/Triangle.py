from product.shape.Shape import Shape
from factory.calculator.AdvancedCalculatorFactory import AdvancedCalculatorFactory
from factory.calculator.BasicCalculatorFactory import BasicCalculatorFactory


class Triangle(Shape):
    def __init__(self, height, base, face_a, face_b) -> None:
        self._height = str(height)
        self._base = str(base)
        self._face_a = str(face_a)
        self._face_b = str(face_b)

    def area(self):
        expression = self._height + ' * ' + self._base + ' / 2'
        calculator = BasicCalculatorFactory(expression)

        calculator.calculate()
        result = calculator.get_result()
        self._area = result

    def perimeter(self):
        expression = self._face_a + ' + ' + self._base + ' + ' + self._face_b
        calculator = BasicCalculatorFactory(expression)
        calculator.calculate()
        result = calculator.get_result()

        self._perimeter = result
