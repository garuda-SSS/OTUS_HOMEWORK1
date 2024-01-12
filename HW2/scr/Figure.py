from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, another_figure):
        if not isinstance(another_figure, Figure):
            raise ValueError("Это не геометрическая фигура")
        return self.get_area() + another_figure.get_area()
