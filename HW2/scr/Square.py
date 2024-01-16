from Figure import Figure


class Square(Figure):
    def __init__(self, side1):
        if side1 <= 0:
            raise ValueError("Значение стороны должно быть положительным числом больше 0")
        super().__init__()
        self.side1 = side1

    def get_area(self):
        s = self.side1**2
        return s

    def get_perimetr(self):
        p = self.side1*4
        return p
