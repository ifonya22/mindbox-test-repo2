import pytest

from geometry_calculator.domain.entities.circle import Circle
from geometry_calculator.domain.entities.triangle import Triangle
from geometry_calculator.infrastructure.factories.shape_factory import ShapeFactory


class TestShapeFactory:
    def test_create_circle(self):
        circle = ShapeFactory.create_shape(5)
        assert isinstance(circle, Circle)
        assert circle.radius == 5

        circle = ShapeFactory.create_shape(radius=5)
        assert isinstance(circle, Circle)
        assert circle.radius == 5

    def test_create_triangle(self):
        triangle = ShapeFactory.create_shape(3, 4, 5)
        assert isinstance(triangle, Triangle)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5

        triangle = ShapeFactory.create_shape(a=3, b=4, c=5)
        assert isinstance(triangle, Triangle)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5

    def test_factory_invalid_args(self):
        with pytest.raises(ValueError):
            ShapeFactory.create_shape(1, 2)
        with pytest.raises(ValueError):
            ShapeFactory.create_shape(radius=5, a=3) 