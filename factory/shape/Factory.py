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
