from factory.shape.RectangleFactory import RectangleFactory
from product.figure.Figure import Figure
from factory.shape.CircleFactory import CircleFactory
from factory.shape.RectangleFactory import RectangleFactory


class Car(Figure):
    _shapes = []

    def make_figure(self):
        self._shapes.append(CircleFactory('3'))
        self._shapes.append(CircleFactory('3'))
        self._shapes.append(RectangleFactory('3', '5'))
