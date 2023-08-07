"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""

from fractions import Fraction
import math

num_first = input("Введите первую дробь в виде a/b: ")
num_second = input("Введите вторую дробь в виде a/b: ")

a = num_first.split('/')
b = num_second.split('/')
a = [int(x) for x in a]
b = [int(x) for x in b]

mult = [0, 0]
for i in range(0, len(a)):
    mult[i] = a[i] * b[i]
    i += 1
print(f"Произведение {num_first} и {num_second} = {'/'.join(str(x) for x in mult)}")

# Вычисляем НОК
lcm = (a[1] * b[1]) // math.gcd(a[1], b[1])
# Вычисляем дополнительные множители
add_mult_a = lcm // a[1]
add_mult_b = lcm // b[1]

summ = [0, 0]
summ[0] = a[0] * add_mult_a + b[0] * add_mult_b
summ[1] = lcm
print(f"Сумма {num_first} и {num_second} = {'/'.join(str(x) for x in summ)}")

a1 = Fraction(a[0], a[1])
b1 = Fraction(b[0], b[1])
print(f"Произведение, вычисленное при помощи Fraction {Fraction(a1 * b1)}")
print(f"Сумма, вычисленная при помощи Fraction {Fraction(a1 + b1)}")