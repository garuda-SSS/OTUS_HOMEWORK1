from HW2.scr.Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Значение стороны должно быть положительным числом больше 0")
        if not ((side1 < (side2+side3)) and (side2 < (side1+side3))
                and (side3 < (side2+side1))):
            raise ValueError("Нельзя построить трегольник по таким параметрам")
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        p = (self.side1+self.side2+self.side3)/2
        s = math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
        return s

    def get_perimetr(self):
        per = self.side1+self.side2+self.side3
        return per
