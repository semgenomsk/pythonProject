"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например, нельзя создавать
прямоугольник со сторонами отрицательной длины
"""

class BasedExep(Exception):
    pass


class Rectangle:

    def __init__(self, side_a, side_b=0):
        if side_b == 0:
            side_b = side_a
        try:
            if side_a <= 0 or side_b <= 0:
                raise ValueError(f"Длина сторон должна быть больше 0.")
        except ValueError as e:
            print(e)
        else:
            self._side_a = side_a
            self._side_b = side_b

class RectErr(BasedExep):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f"Отрицательные значения "

if __name__ == "__main__":
    rectangle1 = Rectangle(7, 3)
    rectangle2 = Rectangle(5.6, 10)