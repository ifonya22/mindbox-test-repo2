from geometry_calculator.domain.entities.triangle import Triangle
from geometry_calculator.infrastructure.factories.shape_factory import ShapeFactory


class GeometryCalculator:
    @staticmethod
    def calculate_area(*args, **kwargs) -> float:
        """Вычисление площади фигуры

        Может принимать на вход объект наследованный от типа Shape
        или список/словарь аргументов для создания фигуры.

        Примеры:\n
        >>> GeometryCalculator.calculate_area(5)  # Круг\n
        >>> GeometryCalculator.calculate_area(radius=5)  # Круг\n
        >>> GeometryCalculator.calculate_area(3, 4, 5)  # Треугольник\n
        >>> GeometryCalculator.calculate_area(a=3, b=4, c=5)  # Треугольник\n
        """
        shape = ShapeFactory.create_shape(*args, **kwargs)
        return shape.calculate_area()

    @staticmethod
    def is_right_angled_triangle(*args, **kwargs) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным
        Примеры:
        >>> is_right_triangle(3, 4, 5)
        True
        >>> is_right_triangle(a=5, b=12, c=13)
        True
        >>> is_right_triangle(triangle_object)
        True
        """
        shape = ShapeFactory.create_shape(*args, **kwargs)
        if not isinstance(shape, Triangle):
            raise TypeError("Метод доступен только для треугольников")
        return shape.is_right_angled()
