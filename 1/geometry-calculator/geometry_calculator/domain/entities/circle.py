import math

from .shape import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        self._validation()

    def calculate_area(self) -> float:
        return math.pi * self.radius**2

    def _validation(self):
        if self.radius <= 0:
            raise ValueError("Радиус должен быть положительным")
