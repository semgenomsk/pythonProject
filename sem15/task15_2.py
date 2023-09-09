"""
Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c
"""

import logging
import math

if __name__ == '__main__':
    logging.basicConfig(filename='Log2.log',
                        filemode='a',
                        encoding='utf-8',
                        format='{levelname:<7} - {asctime} строка {lineno:>3d} : {msg}',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

# Для решения с другими коэффициентами  можно сделать запрос их из консоли
a = int(input("Ведите значения a = "))
b = int(input("Ведите значения b = "))
c = int(input("Ведите значения c = "))

# a = 5
# b = -10
# c = -400

discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
    logger.info(f'Итого: x1 = {x1} \nx2 = {x2}')
elif discr == 0:
    x = -b / (2 * a)
    print(f"x1 = x2 = {x}")
else:
    print("Корней нет")
    logger.error(f'Корней нет')
