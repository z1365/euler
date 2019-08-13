import os


# cls + Шапка
os.system('cls')
print('{:*^80}'.format('  \x1b[33mПроект Эйлера\x1b[0m  '))
print('{:^80}'.format('\x1b[32mhttp://projecteuler.net/archives\x1b[0m'))

# Problem 1
print('''
Задача 1:
=========
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

\x1b[33mFind the sum of all the multiples of 3 or 5 below 1000.\x1b[0m
''')
# область
x = 999

# все числа от 1 до x (не включая x, судя по "дано" из проблемы)
# Способ 1. Перебор.
print('Способ 1. Перебор.')


def sum_natural(_from, _to):
    for number in range(_from, _to):
        if number % 3 == 0 or number % 5 == 0:
                sum += number
        return sum


answer = sum_natural(1, x+1)
# задача решена.
print("Ответ: \x1b[32m", answer, '\x1b[0m\n')

# Способ 2. Формула.
# Сумма первых n членов арифметической прогресии Sn = (n / 2) * (a1 + an)
# разность арифметической прогрессии - d
# Соотвественно, сумма для d=3: S3n = (n3 / 2) * (3 + a3n)
# Sresult = S3 + S5 - S15 (В месте пересечения членов прогрессии мы посчитали
# членов S15 два раза, сначала в S3, потом в S5. Вычтем 1 раз.)

# Формула n-го члена: an = a1 + (n - 1) * d

print('Способ 2. Формула.')


# разность  прогрессий
d3 = 3
d5 = 5
d15 = 15
# последний член прогрессии в области
a3n = int(x/d3) * d3
a5n = int(x/d5) * d5
a15n = int(x/d15) * d15
# поскольку дано, что область начинается с 1, то a1 = d
a31 = d3
a51 = d5
a151 = d15

# количество членов прогрессий
n3 = (a3n - a31)/d3 + 1
n5 = (a5n - a51)/d5 + 1
n15 = (a15n - a151)/d15 + 1

# суммы членов прогрессий
s3 = (n3/2) * (a31 + a3n)
s5 = (n5/2) * (a51 + a5n)
s15 = (n15/2) * (a151 + a15n)
answer = int(s3 + s5 - s15)

# можно выразить через x и d3, d5 и d15
# sr = (((int(x/d3) * d3 - d3)/d3 + 1) / 2) * (d3 + int(x/d3) * d3) + \
#         (((int(x/d5) * d5 - d5)/d5 + 1) /2) * (d5 + int(x/d5) * d5) - \
#         (((int(x/d15) * d15 - d15)/d15 + 1) / 2) * (d15 + int(x/d15) * d15)

print('Ответ: \x1b[32m', answer, '\x1b[0m')
