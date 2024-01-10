from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        if ((self.side1 < (self.side2+self.side3)) and (self.side2 < (self.side1+self.side3))
                and (self.side3 < (self.side2+self.side1))):
            p = (self.side1+self.side2+self.side3)/2
            s = math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
            return s
        else:
            raise ValueError("Нельзя построить трегольник по таким параметрам")
