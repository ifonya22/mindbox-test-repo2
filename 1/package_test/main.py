from geometry_calculator import Circle, GeometryCalculator, Triangle


def main():
    print(GeometryCalculator.calculate_area(radius=5))  # По ключевому слову
    print(GeometryCalculator.calculate_area(5))  # По позиционному аргументу
    print(GeometryCalculator.calculate_area(a=3, b=4, c=5))  # Треугольник по ключевым словам
    print(GeometryCalculator.calculate_area(3, 4, 5))  # Треугольник по позиционным аргументам

    circle = Circle(5)
    triangle = Triangle(3, 4, 5)
    print(GeometryCalculator.calculate_area(circle))  # Явно заданный круг
    print(GeometryCalculator.is_right_triangle(triangle))  # Явно заданный треугольник


if __name__ == "__main__":
    main()
