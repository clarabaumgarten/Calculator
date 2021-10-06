from factory.shape.Factory import Factory
from product.shape.Rectangle import Rectangle


class RectangleFactory(Factory):
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width
    
    def factory_method(self) -> None:
       return Rectangle(self._height, self._width)
