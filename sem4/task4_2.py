"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление
"""

def func(**kwargs):
    dct = {}
    for key, value in kwargs.items():
        if value.__hash__ == None:
            value = str(value)
        dct[value] = key
    return dct

print(func(a=6, b='World', c=3.1415, d=[0, 10, 3], e=(1, 2, 3)))