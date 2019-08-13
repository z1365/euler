import os


# cls + Шапка
os.system('cls')
print('{:*^80}'.format('  \x1b[33mПроект Эйлера\x1b[0m  '))
print('{:^80}'.format('\x1b[32mhttp://projecteuler.net/archives\x1b[0m'))
print()

# Problem 1
print (''' Задача 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
''')

#все числа от 1 до 10 (не включая 10, судя по "дано" из проблемы)
print('\nВоссоздал дано:')
numberList = []
for number in range(1,10):
    if number % 3 == 0 or number % 5 == 0:
        numberList.append(number)
print (numberList)

#проверяю сумму
sum = 0
for number in numberList:
    sum += number
print ('сумма: ', sum, '\n')


