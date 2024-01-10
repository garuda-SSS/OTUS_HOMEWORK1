from abc import ABC, abstractmethod


class Figure(ABC):
    type_obj = "Figure"

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def add_area(self, another_figure):
        if hasattr(another_figure, "type_obj"):
            return self.area() + another_figure.area()
        else:
            raise ValueError("Это не геометрическая фигура")