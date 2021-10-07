from factory.shape.CircleFactory import CircleFactory
from factory.shape.RectangleFactory import RectangleFactory
from factory.shape.TriangleFactory import TriangleFactory
from product.figure.Car import Car
from product.figure.Tree import Tree


if __name__ == "__main__":
    circle = CircleFactory('3')
    circle.show_metrics()


    rectangle = RectangleFactory('3', '2')
    rectangle.show_metrics()


    triangle = TriangleFactory('5', '4', '3', '3')
    triangle.show_metrics()


    car = Car()
    car.make_figure()
    print(car.total_area())
    print(car.total_perimeter())

    tree = Tree()
    tree.make_figure()
    print(tree.total_area())
    print(tree.total_perimeter())
