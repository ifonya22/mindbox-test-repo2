### Задание
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

* Юнит-тесты
* Легкость добавления других фигур
* Вычисление площади фигуры без знания типа фигуры в compile-time
* Проверку на то, является ли треугольник прямоугольным


### Билд
```bash
uv build
```
### Установка
```bash
uv add ../geometry-calculator/dist/geometry_calculator-0.1.0-py3-none-any.whl
```

### Тестирование
```bash
uv sync
uv run pytest
```