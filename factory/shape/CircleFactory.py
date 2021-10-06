from factory.shape.Factory import Factory
from product.shape.Circle import Circle


class CircleFactory(Factory):
    def __init__(self, raio) -> None:
        self._raio = raio
    
    def factory_method(self) -> None:
       return Circle(self._raio)
