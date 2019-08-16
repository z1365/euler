import termscreen
from colorama import init, deinit  # Style, Fore, Back
import time
import datetime

init()
termscreen.cls()
print('{:*^80}'.format('  \x1b[33;1mПроект Эйлера\x1b[0m  '))
print('{:^80}'.format('\x1b[32mhttp://projecteuler.net/archives\x1b[0m'))

# Task 004
print('''
Задача 004:
===========
\x1b[30;1mA palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
\x1b[0m
Полиндромы это числа, которые читаются одинаково как слева направо, так и справа налево.
Наибольший полиндром, полученный произведением двухчисленных числителей: 9009 = 91 х 99.

\x1b[33mFind the largest palindrome made from the product of two 3-digit numbers.
\x1b[33;1mНайти наибольший полиндром, полученный путем произведения трёх-цифровых числителей.
''')
print('\x1b[0m')

start_time: float = time.time()
largest_polindrome: int = 0
for first in range(100, 1000):
    for second in range(10, 1000):
        testing = first * second
        s1: str = str(testing)
        s2: str = s1[::-1]
        if s1 == s2:
            if largest_polindrome < testing:
                largest_polindrome = testing

print('Ответ: \x1b[32;1m{}\x1b[0m'.format(str(largest_polindrome)))
end_time = time.time()
delta_time = end_time - start_time
print('\x1b[31;1mРаботало {}\x1b[0m'.format(str(datetime.timedelta(seconds=delta_time))))
deinit()
