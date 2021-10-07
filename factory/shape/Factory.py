from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def factory_method():
        pass
    
    def show_metrics(self):
        obj = self.factory_method()
        obj.area()
        obj.perimeter()
        obj.show_metrics()

    def area(self):
        obj = self.factory_method()
        obj.area()
        return obj.get_area()

    def perimeter(self):
        obj = self.factory_method()
        obj.perimeter()
        return obj.get_perimeter()
