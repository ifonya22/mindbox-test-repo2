from geometry_calculator.domain.entities.circle import Circle
from geometry_calculator.domain.entities.shape import Shape
from geometry_calculator.domain.entities.triangle import Triangle


class ShapeFactory:
    @classmethod
    def create_shape(cls, *args, **kwargs) -> Shape:
        if len(args) == 1 and isinstance(args[0], Shape):
            return args[0]

        shape_creators = [
            (cls._create_circle, 1, ["radius"]),
            (cls._create_triangle, 3, ["a", "b", "c"]),
        ]

        for creator, arg_count, keywords in shape_creators:
            if cls._matches_arguments(arg_count, keywords, *args, **kwargs):
                return creator(*args, **kwargs)

        allowed_combinations = """
            Возможные комбинации аргументов:
            - Circle: (radius) или (radius=...)
            - Triangle: (a, b, c) или (a=..., b=..., c=...)
            """
        raise ValueError(f"Неверные аргументы.{allowed_combinations}")

    @staticmethod
    def _matches_arguments(arg_count, keywords, *args, **kwargs):
        if len(args) == arg_count and not kwargs:
            return True
        if len(kwargs) == arg_count and all(k in keywords for k in kwargs):
            return True
        return False

    @staticmethod
    def _create_circle(*args, **kwargs) -> Circle:
        radius = args[0] if args else kwargs["radius"]
        return Circle(radius)

    @staticmethod
    def _create_triangle(*args, **kwargs) -> Triangle:
        if args:
            return Triangle(*args)
        return Triangle(kwargs["a"], kwargs["b"], kwargs["c"])
