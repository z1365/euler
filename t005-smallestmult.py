import termscreen
from colorama import init, deinit  # Style, Fore, Back
import prime_numbers

init()
termscreen.cls()
termscreen.intro()

# Task 005
print('''
Задача 005:
===========
\x1b[36;1m2520 \x1b[30mis the smallest number that can be divided by each of the numbers
from \x1b[35m1\x1b[30m to \x1b[35m10\x1b[30m without any remainder.
\x1b[0m
\x1b[36;1m2520\x1b[0m - самое маленькое число, которое делится без остатка на все числа
 от 1 до 10.\x1b[0m

\x1b[33mWhat is  the  smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?\n
\x1b[33;1mКакое самое маленькое число делится нацело на все числа от \x1b[35;1m1\x1b[0m to \x1b[35;1m20\x1b[0m ?
''')

# считать буду для 20
number = 20

# заполняю список простых чисел от 2 до анализируемого числа
# prime_num_list = prime_numbers.get_prime_numbers(number)
prime_num_list = [2, 3, 5]
# список слогаемых и их степеней
global_deviders = {}

for n in range(2, number + 1):
    # получил список степеней простых делителей
    deviders = prime_numbers.get_prime_deviders(n, prime_num_list)

    # анализирую количество простых делителей
    for d in deviders:
        # если делитель встретился впервые, завожу его
        if d not in global_deviders:
            global_deviders[d] = 0
        # смотрю, хватает ли элементарных делителей в глобальном словаре
        if global_deviders[d] < deviders[d]:
            # добавляю, если не хватает
            global_deviders[d] = deviders[d]
print('Словарь степеней простых множителей: {}'.format(global_deviders))

mlt = 1
for g in global_deviders:
    mlt *= g ** global_deviders[g]

print('Ответ: \x1b[32;1m{}\x1b[0m'.format(str(mlt)))
deinit()
