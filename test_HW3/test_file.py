import pytest
from HW2.scr.Rectangle import Rectangle
from HW2.scr.Triangle import Triangle
from HW2.scr.Circle import Circle
from HW2.scr.Square import Square


class Test_square():

    @pytest.mark.parametrize(
        "side_a, area", [(1, 1), (5, 25), (2.2, 4.84)], ids=["one", "int", "float"]
    )
    def test_square_area(self, side_a, area):
        a = Square(side_a)
        assert round(a.get_area(), 2) == area, f"Площадь для квадрата со стороной {side_a} вычислена неверно"

    @pytest.mark.parametrize(
        "side_a, perimeter", [(1, 4), (2.2, 8.8)], ids=["int", "float"]
    )
    def test_square_perimeter(self, side_a, perimeter):
        a = Square(side_a)
        assert round(a.get_perimetr(), 2) == perimeter, f"Периметр для квадрата со стороной {side_a} вычислен неверно"

    @pytest.mark.parametrize(
        "side_a", [0, -6], ids=["zero", "negative"]
    )
    def test_square_wrong_var(self, side_a):
        with pytest.raises(ValueError):
            a = Square(side_a)

    def test_square_add_square(self, example_square):
        a = Square(10)
        assert a.add_area(example_square) == 200, "Площади квадратов суммируются неверно"

    def test_square_add_rectangle(self, example_rectangle):
        a = Square(10)
        assert a.add_area(example_rectangle) == 200, "Площади прямоугольников суммируются неверно"

    def test_square_add_triangle(self, example_triangle):
        a = Square(10)
        assert round(a.add_area(example_triangle), 1) == 109.9, "Площади треугольников суммируются неверно"

    def test_square_add_circle(self, example_circle):
        a = Square(10)
        assert round(a.add_area(example_circle), 2) == 414.16, "Площади окружностей суммируются неверно"

    def test_square_add_int(self):
        with pytest.raises(ValueError):
            a = Square(5)
            a.add_area(6)


class Test_rectangle():

    @pytest.mark.parametrize(
        "side_a, side_b, area", [(2, 2, 4), (2.2, 2.2, 4.84), (2.5, 2, 5)], ids=["int", "float", "float_and_int"]
    )
    def test_rectangle_area(self, side_a, side_b, area):
        a = Rectangle(side_a, side_b)
        assert round(a.get_area(), 2) == area, (f"Площадь для прямоугольника со сторонами {side_a} и {side_b} "
                                                f"вычислена неверно")

    @pytest.mark.parametrize(
        "side_a, side_b, perimeter", [(2, 2, 8), (2.2, 2.2, 8.8), (2.5, 2, 9)], ids=["int", "float", "float_and_int"]
    )
    def test_rectangle_perimeter(self, side_a, side_b, perimeter):
        a = Rectangle(side_a, side_b)
        assert round(a.get_perimetr(), 2) == perimeter, (f"Периметр для прямоугольника со сторонами {side_a} "
                                                         f"и {side_b}вычислен неверно")

    @pytest.mark.parametrize(
        "side_a, side_b", [(0, 0), (-5, -6), (0, 2), (-9, 2)], ids=["zero", "negative", "zero_and_normal",
                                                                    "negative_and_normal"]
    )
    def test_rectangle_wrong_var(self, side_a, side_b):
        with pytest.raises(ValueError):
            a = Rectangle(side_a, side_b)

    def test_rectangle_add_square(self, example_square):
        a = Rectangle(10, 10)
        assert a.add_area(example_square) == 200, "Площади квадратов суммируются неверно"

    def test_rectangle_add_rectangle(self, example_rectangle):
        a = Rectangle(10, 10)
        assert a.add_area(example_rectangle) == 200, "Площади прямоугольников суммируются неверно"

    def test_rectangle_add_triangle(self, example_triangle):
        a = Rectangle(10, 10)
        assert round(a.add_area(example_triangle), 1) == 109.9, "Площади треугольников суммируются неверно"

    def test_rectangle_add_circle(self, example_circle):
        a = Rectangle(10, 10)
        assert round(a.add_area(example_circle), 2) == 414.16, "Площади окружностей суммируются неверно"

    def test_rectangle_add_int(self):
        with pytest.raises(ValueError):
            a = Rectangle(5, 5)
            a.add_area(6)


class Test_circle():

    @pytest.mark.parametrize(
        "rad, area", [(1, 3.14), (10, 314.16), (2.2, 15.21)], ids=["one", "int", "float"]
    )
    def test_circle_area(self, rad, area):
        a = Circle(rad)
        assert round(a.get_area(), 2) == area, f"Площадь для окружности с радиусом {rad} вычислена неверно"

    @pytest.mark.parametrize(
        "rad, perimeter", [(5, 31.42), (3.14, 19.73)], ids=["int", "float"]
    )
    def test_circle_perimeter(self, rad, perimeter):
        a = Circle(rad)
        assert round(a.get_perimetr(), 2) == perimeter, f"Периметр для окружности с радиусом {rad} вычислен неверно"

    @pytest.mark.parametrize(
        "rad", [0, -6], ids=["zero", "negative"]
    )
    def test_circle_wrong_var(self, rad):
        with pytest.raises(ValueError):
            a = Circle(rad)

    def test_circle_add_square(self, example_square):
        a = Circle(10)
        assert round(a.add_area(example_square), 2) == 414.16, "Площади квадратов суммируются неверно"

    def test_circle_add_rectangle(self, example_rectangle):
        a = Circle(10)
        assert round(a.add_area(example_rectangle), 2) == 414.16, "Площади прямоугольников суммируются неверно"

    def test_circle_add_triangle(self, example_triangle):
        a = Circle(10)
        assert round(a.add_area(example_triangle), 2) == 324.08, "Площади треугольников суммируются неверно"

    def test_circle_add_circle(self, example_circle):
        a = Circle(10)
        assert round(a.add_area(example_circle), 2) == 628.32, "Площади окружностей суммируются неверно"

    def test_circle_add_int(self):
        with pytest.raises(ValueError):
            a = Circle(5)
            a.add_area(6)


class Test_triangle():

    @pytest.mark.parametrize(
        "side_a, side_b, side_c, area", [(4, 5, 6, 9.9), (4.5, 5.5, 6.5, 12.2), (4, 5.5, 6.5, 11)],
        ids=["int", "float", "int_and_float"]
    )
    def test_triangle_area(self, side_a, side_b, side_c, area):
        a = Triangle(side_a, side_b, side_c)
        assert round(a.get_area(), 1) == area, (f"Площадь для треугольника со сторонами {side_a},{side_b} "
                                                f"и {side_c} вычислена неверно")

    @pytest.mark.parametrize(
        "side_a, side_b, side_c, perimeter", [(4, 5, 6, 15), (4.5, 5.5, 6.5, 16.5), (4, 5.5, 6.5, 16)],
        ids=["int", "float", "int_and_float"]
    )
    def test_triangle_perimeter(self, side_a, side_b, side_c, perimeter):
        a = Triangle(side_a, side_b, side_c)
        assert round(a.get_perimetr(), 2) == perimeter, (f"Периметр для треугольника со сторонами {side_a},{side_b} "
                                                         f"и {side_c} вычислен неверно")


    @pytest.mark.parametrize(
        "side_a, side_b, side_c", [(0, 0, 0), (-1, -5, -9), (7, -5, -9), (7, 0, 5),(11, 5, 5)],
        ids=["zero", "negative", "negative_and_normal", "zero_and_normal","oversize"]
    )
    def test_triangle_wrong_var(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            a = Triangle(side_a, side_b, side_c)

    def test_triangle_add_square(self, example_square):
        a = Triangle(4, 5, 6)
        assert round(a.add_area(example_square), 1) == 109.9, "Площади квадратов суммируются неверно"

    def test_triangle_add_rectangle(self, example_rectangle):
        a = Triangle(4, 5, 6)
        assert round(a.add_area(example_rectangle), 1) == 109.9, "Площади прямоугольников суммируются неверно"

    def test_triangle_add_triangle(self, example_triangle):
        a = Triangle(4, 5, 6)
        assert round(a.add_area(example_triangle), 1) == 19.8, "Площади треугольников суммируются неверно"

    def test_triangle_add_circle(self, example_circle):
        a = Triangle(4, 5, 6)
        assert round(a.add_area(example_circle), 2) == 324.08, "Площади окружностей суммируются неверно"

    def test_triangle_add_int(self):
        with pytest.raises(ValueError):
            a = Triangle(4, 5, 6)
            a.add_area(6)
