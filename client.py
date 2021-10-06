from factory.shape.CircleFactory import CircleFactory
from factory.shape.RectangleFactory import RectangleFactory
from factory.shape.TriangleFactory import TriangleFactory


if __name__ == "__main__":
    circle = CircleFactory('5')
    circle.show_metrics()


    rectangle = RectangleFactory('2', '8')
    rectangle.show_metrics()


    triangle = TriangleFactory('2', '8', '3', '3')
    triangle.show_metrics()