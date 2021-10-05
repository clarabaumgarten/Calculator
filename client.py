from factory.BasicCalculatorFactory import BasicCalculatorFactory
from factory.AdvancedCalculatorFactory import AdvancedCalculatorFactory
from shapes.Circle import Circle
from shapes.Rectangle import Rectangle
from shapes.Triangle import Triangle


if __name__ == "__main__":
    # expression = input("Digite uma expressão básica: ")
    
    # basic_cal = BasicCalculatorFactory(expression)
    # basic_cal.calculate()
    # basic_cal.show_result()

    # expression = input("\n\nDigite uma expressão avançada: ")

    # advanced_cal = AdvancedCalculatorFactory(expression)
    # advanced_cal.calculate()
    # advanced_cal.show_result()


    circle = Circle('5')
    circle.area()
    circle.perimeter()
    circle.show_metrics()


    rectangle = Rectangle('2', '8')
    rectangle.area()
    rectangle.perimeter()
    rectangle.show_metrics()


    triangle = Triangle('2', '8', '3', '3')
    triangle.area()
    triangle.perimeter()
    triangle.show_metrics()