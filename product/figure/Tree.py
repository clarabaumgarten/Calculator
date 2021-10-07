from factory.shape.RectangleFactory import RectangleFactory
from product.figure.Figure import Figure
from factory.shape.TriangleFactory import TriangleFactory


class Tree(Figure):
    _shapes = []

    def make_figure(self):
        self._shapes.append(RectangleFactory('3', '2'))
        self._shapes.append(TriangleFactory('5', '4', '3', '3'))
