from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Значение радиуса должно быть положительным числом больше 0")
        super().__init__()
        self.r = r

    def get_area(self):
        s = (self.r**2)*math.pi
        return s

    def get_perimetr(self):
        p = 2*self.r*math.pi
        return p
