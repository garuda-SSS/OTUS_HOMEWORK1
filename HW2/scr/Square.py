from Figure import Figure


class Square(Figure):
    def __init__(self, side1):
        self.side1 = side1

    def area(self):
        s = self.side1**2
        return s
