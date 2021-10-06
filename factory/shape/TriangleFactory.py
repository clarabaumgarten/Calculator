from factory.shape.Factory import Factory
from product.shape.Triangle import Triangle


class TriangleFactory(Factory):
    def __init__(self, height, base, face_a, face_c) -> None:
        self._height = height
        self._base = base
        self._face_a = face_a
        self._face_c = face_c
    
    def factory_method(self) -> None:
       return Triangle(self._height, self._base, self._face_a, self._face_c)
