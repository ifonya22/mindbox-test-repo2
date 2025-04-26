import math

from .shape import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

        self._validate()

    def calculate_area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def _validate(self):
        sides = sorted([self.a, self.b, self.c])
        if sides[0] + sides[1] < sides[2]:
            raise ValueError("Треугольник не может существовать")

    def is_right_angled(self):
        lines = sorted([self.a, self.b, self.c])

        return lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2
