from Figure import Figure


class Rectangle(Figure):
    def __init__(self, side1, side2):
        if side1 <= 0 or side2 <= 0:
            raise ValueError("Значение стороны должно быть положительным числом больше 0")
        super().__init__()
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        s = self.side1*self.side2
        return s

    def get_perimetr(self):
        p = 2*(self.side1+self.side2)
        return p
