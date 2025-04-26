import pytest

from geometry_calculator.domain.entities.circle import Circle
from geometry_calculator.domain.entities.triangle import Triangle


class TestCircle:
    def test_circle_area(self):
        circle = Circle(5)
        assert circle.calculate_area() == pytest.approx(78.53981633974483)

    def test_circle_validation(self):
        with pytest.raises(ValueError, match="Радиус должен быть положительным"):
            Circle(-1)


class TestTriangle:
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.calculate_area() == pytest.approx(6.0)

    def test_triangle_validation(self):
        with pytest.raises(ValueError, match="Треугольник не может существовать"):
            Triangle(1, 2, 10)

    def test_right_triangle(self):
        assert Triangle(3, 4, 5).is_right_angled() is True
        assert Triangle(5, 12, 13).is_right_angled() is True
        assert Triangle(4, 5, 6).is_right_angled() is False
