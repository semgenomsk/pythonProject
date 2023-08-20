"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения
с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
"""

import csv
import json
import random
import math
import functools

# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def make_csv(file_csv):
    with open(file_csv, mode='w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(random.randint(100, 1001)):
            writer.writerow([random.randint(0, 101) for _ in range(3)])

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def decor_root_csv(func):
    @functools.wraps(func)
    def wrapper(filename):
        res = []
        with open(filename, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                res.append(func(a, b, c))
        return res

    return wrapper

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
def decor_res_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('log.json', 'a') as f:
            json.dump({'func': func.__name__, 'args': args, 'kwargs': kwargs, 'result': res}, f)
        return res

    return wrapper

@decor_root_csv
@decor_res_json
# функция нахождения корней квадратного уравнения
def equation_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a != 0:
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            print(f"x1 = {x1} \nx2 = {x2}")
        elif discr == 0:
            x = -b / (2 * a)
            print(f"x1 = x2 = {x}")
        else:
            print("Корней нет")

    else:
        print("Уравнение не является квадратным")

make_csv('multipliers.csv')
equation_roots('multipliers.csv')