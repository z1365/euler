import termscreen
from colorama import init, deinit  # Fore, Back, Style
import time
import datetime
import math
import prime_numbers

init()

termscreen.cls()
print('{:*^80}'.format('  \x1b[33;1mПроект Эйлера\x1b[0m  '))
print('{:^80}'.format('\x1b[32mhttp://projecteuler.net/archives\x1b[0m'))

# Task 003
print('''
Задача 003:
===========
\x1b[30;1mThe prime factors of 13195 are 5, 7, 13 and 29.\x1b[0m
Простыми делителями 13195 являются 5, 7, 13 и 29.

\x1b[33mWhat is the largest prime factor of the number '\x1b[36m600851475143\x1b[33m'?\x1b[0m
\x1b[33;1mНайти наибольший простой делитель для '\x1b[36;1m600851475143\x1b[33;1m'?\x1b[0m
''')

__version__ = "1.1.0"
start_time = time.time()
check_time = start_time
# print(Fore.RED + Style.BRIGHT + str(time.time()) + Style.RESET_ALL)
prime_numbers_list = [2, 3, 5]
# -- lab_rat = 600851475143
lab_rat = 600851475143
# наибольший простой делитель
lagest_prime_factor = 1

# самый большой числитель может быть только квадратным корнем от делимого
limit = int(math.sqrt(lab_rat))
# в 4каком десятке тысяч мы сейчас
we_are_at = 0
while limit > prime_numbers_list[-1]:
    # счётчик каждых 10 000 чисел, чтобы выводить на экран время прохождения
    if prime_numbers_list[-1] / 10000 > we_are_at:
        we_are_at += 1
        tenth_time = time.time()
        delta_time = tenth_time - start_time
        str_time = str(datetime.timedelta(seconds=delta_time))
        print('\x1b[0mСпустя \x1b[31;1m{}\x1b[0m прошёл \x1b[32;1m{:,}\x1b[0m из {:,}'
              .format(str_time, prime_numbers_list[-1], limit))
    # ищем следующее простое
    prime_numbers_list.append(prime_numbers.next_prime(prime_numbers_list[-1], prime_numbers_list))
    # если испытуемый делится нацело
    if lab_rat % prime_numbers_list[-1] == 0:
        # если второе слогаемое от деления тоже простое число
        # и при этом больше первого, то наибольший простой делитель
        # - второе слогаемое
        second_factor = int(lab_rat / prime_numbers_list[-1])
        if prime_numbers.is_prime(second_factor) and (second_factor > prime_numbers_list[-1]):
            lagest_prime_factor = second_factor
            limit = second_factor
            break
        else:
            lagest_prime_factor = prime_numbers_list[-1]

        point_time = time.time()
        delta_time = point_time - check_time
        check_time = point_time
        str_time = str(datetime.timedelta(seconds=delta_time))
        print('\x1b[0mСпустя {} нашелся делитель \x1b[33;1m{}\x1b[0m'.format(str_time, lagest_prime_factor))

print('Ответ: \x1b[32;1m{}\x1b[0m'.format(str(lagest_prime_factor)))

end_time = time.time()
delta_time = end_time - start_time
print('\x1b[32;1mРаботало {}'.format(str(datetime.timedelta(seconds=delta_time))))
deinit()
