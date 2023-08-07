"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла
"""


import os

def info_path(path):
    file_path, file_extension = os.path.splitext(path)
    dirc, file_name = os.path.split(file_path)
    return (dirc, file_name, file_extension)


print(info_path("D:\Общая папка\GeekBrains\погружение в Python\Установка среды разработки.rar"))