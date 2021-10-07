from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def make_figure():
        pass
    
    def total_area(self):
        metrics = list(map(lambda shape: shape.area(), self._shapes))
        total = 0
        for metric in metrics:
            total += metric

        return total

    def total_perimeter(self):
        metrics = list(map(lambda shape: shape.perimeter(), self._shapes))
        total = 0
        for metric in metrics:
            total += metric

        return total
