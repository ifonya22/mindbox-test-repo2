import pytest

from geometry_calculator.application.services.geometry_calculator import (
    GeometryCalculator,
)


class TestGeometryCalculator:
    def test_calculate_area_circle(self):
        radius = 5
        expected_area = 78.53981633974483
        assert GeometryCalculator.calculate_area(radius) == pytest.approx(expected_area)
        assert GeometryCalculator.calculate_area(radius=radius) == pytest.approx(expected_area)
        radius = 50
        expected_area = 7853.981633974483
        assert GeometryCalculator.calculate_area(radius) == pytest.approx(expected_area)
        assert GeometryCalculator.calculate_area(radius=radius) == pytest.approx(expected_area)

    def test_calculate_area_triangle(self):
        assert GeometryCalculator.calculate_area(3, 4, 5) == pytest.approx(6.0)
        assert GeometryCalculator.calculate_area(a=3, b=4, c=5) == pytest.approx(6.0)

    def test_is_right_triangle(self):
        assert GeometryCalculator.is_right_angled_triangle(3, 4, 5) is True
        assert GeometryCalculator.is_right_angled_triangle(a=5, b=12, c=13) is True
        assert GeometryCalculator.is_right_angled_triangle(4, 5, 6) is False

    def test_is_right_triangle_invalid_shape(self):
        with pytest.raises(TypeError, match="Метод доступен только для треугольников"):
            GeometryCalculator.is_right_angled_triangle(5)  # Circle
        with pytest.raises(TypeError, match="Метод доступен только для треугольников"):
            GeometryCalculator.is_right_angled_triangle(radius=5)  # Circle
