# -----------------------------------------------------------------------------
# Task 002
print('''
    Задача 002:
    ===========
Каждый следующий элемент ряда Фибоначчи получается при сложении двух
предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
\x1b[33m
Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона.
\x1b[0m
''')


# Способ 1. Механический. Перебор. пока Единственный


def fib_sum(limit):
    """
    Считает сумму положительных чисел Фибаначи, которые меньше указанного значения
    """
    u1 = 1
    u2 = 2
    summ = 2
    _u = u1 + u2
    while _u < limit:
        if _u % 2 == 0:
            summ += _u
        u1 = u2
        u2 = _u
        _u = u1 + u2
    return summ


x = 4000000

result = fib_sum(x)
print("{:,}".format(result))

# сгенерированный ряд
# >>> [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
#     1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025,
#     121393, 196418, 317811, 514229, 832040, 1346269,
#     2178309, 3524578]
