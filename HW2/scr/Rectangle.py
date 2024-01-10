from Figure import Figure


class Rectangle(Figure):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        s = self.side1*self.side2
        return s
