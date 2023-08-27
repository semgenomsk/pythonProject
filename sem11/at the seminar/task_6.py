"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""

class Rectangle:
    """ Rectangle - class прямоугольников"""

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        """ Вычисляет периметр"""
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """Вычисляет площадь"""
        return self.side_a * self.side_b

    def __add__(self, other):
        """ Метод сложения треугольников. Складываем периметры"""
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """Метод вычитания прямоугольников. Вычитаем периметры """
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        """Прямоугольники равны, когда равны их площади """
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        """Прямоугольники не равны, когда равны их площади не равны"""
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        """Метод возвращает истину, когда площадь левого треугольника больше площади правого"""
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        """Метод возвращает истину, когда площадь левого треугольника больше или равна площади правого"""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        """Метод возвращает истину, когда площадь левого треугольника меньше площади правого"""
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        """Метод возвращает истину, когда площадь левого треугольника меньше или равна площади правого"""
        return self.get_area() <= other.get_area()

    def __str__(self):
        """
        Метод вывода на печать для пользователей
        """
        res = f'Периметр прямоугольника = {self.get_area():.2f} '
        return res

rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)

print(f'площадь 1 прямоугольника = {rectangle1.get_area():.2f}')
print(f'площадь 2 прямоугольника = {rectangle2.get_area():.2f}')
# print(rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)