import os
from colorama import init, deinit, Fore, Style   # Back
import time
import datetime
import math

init()

# cls + Шапка
os.system('cls')
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


# ищу простые числа
def next_simple(simple):
    ''' Возвращает следующее за переданным простое число'''
    # признак простоты числа
    num = simple
    is_ismple = False
    while not is_ismple:
        # перехожу к следующему числу
        num += 1
        # если не '1', '3', '7' или '9' на конце - не простое, дальше
        if (num % 2 == 0) or (num % 10 == 5):
            # if str(num)[-1] != '1' and str(num)[-1] != '3' and str(num)[-1] != '7' and str(num)[-1] != '9':
            continue
        devided = False
        for s in simple_nums:
            # if s == 1:
            #     continue
            if int(num / s) == num / s:
                # разделилось, не простое
                devided = True
                break
        is_ismple = not devided
    return num


start_time = time.time()
check_time = start_time
# print(Fore.RED + Style.BRIGHT + str(time.time()) + Style.RESET_ALL)
simple_nums = [2, 3, 5]
# lab_rat = 600851475143
lab_rat = 600851475143
# наибольший простой делитель
lagest_prime_factor = 1

# самый большой числитель может быть только квадратным корнем от делимого
limit = int(math.sqrt(lab_rat))
# в 4каком десятке тысяч мы сейчас
we_are_at = 0
while limit > simple_nums[-1]:
    if simple_nums[-1] / 10000 > we_are_at:
        we_are_at += 1
        tenth_time = time.time()
        delta_time = tenth_time - start_time
        str_time = str(datetime.timedelta(seconds=delta_time))
        print(Style.RESET_ALL + 'Спустя \x1b[31;1m{}\x1b[0m прошёл \x1b[32;1m{}\x1b[0m из {}'.format(str_time, simple_nums[-1], limit))
    # ищем следующее простое
    simple_nums.append(next_simple(simple_nums[-1]))
    # если испытуемый делится нацело
    if lab_rat % simple_nums[-1] == 0:
        # то на данный момент это наибольший простой делитель
        lagest_prime_factor = simple_nums[-1]
        point_time = time.time()
        delta_time = point_time - check_time
        check_time = point_time
        str_time = str(datetime.timedelta(seconds=delta_time))
        print(Style.RESET_ALL)
        print('\x1b[0mСпустя {} нашелся делитель \x1b[33;1m{}\x1b[0m'.format(str_time, lagest_prime_factor))


print("Ответ: " + Fore.GREEN + Style.BRIGHT + str(lagest_prime_factor) + Style.RESET_ALL)

end_time = time.time()
delta_time = end_time - start_time
print(Fore.RED + Style.BRIGHT + 'Работало ' + str(datetime.timedelta(seconds=delta_time)) + Style.RESET_ALL)
deinit()
