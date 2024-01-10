from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        s = (self.r**2)*math.pi
        return s
