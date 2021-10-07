from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
    def show_metrics(self):
        print("Perímetro: ", self._perimeter)
        print("Área: ", self._area, '\n')

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area
