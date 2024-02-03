import pytest
from HW2.scr.Rectangle import Rectangle
from HW2.scr.Triangle import Triangle
from HW2.scr.Circle import Circle
from HW2.scr.Square import Square


@pytest.fixture()
def example_square():
    return Square(10)


@pytest.fixture()
def example_rectangle():
    return Rectangle(10,10)


@pytest.fixture()
def example_triangle():
    return Triangle(4,5,6)


@pytest.fixture()
def example_circle():
    return Circle(10)

