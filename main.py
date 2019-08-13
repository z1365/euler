import os


# cls + Шапка
os.system('cls')
print('{:*^80}'.format('  \x1b[33mПроект Эйлера\x1b[0m  '))
print('{:^80}'.format('\x1b[32mhttp://projecteuler.net/archives\x1b[0m'))

# Problem 1
print ('''
Задача 1:
=========
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
\x1b[33mFind the sum of all the multiples of 3 or 5 below 1000.\x1b[0m
''')

#все числа от 1 до 10 (не включая 10, судя по "дано" из проблемы)
def sum_natural(_from, _to):
    numberList = []
    for number in range(_from,_to):
        if number % 3 == 0 or number % 5 == 0:
            numberList.append(number)

    sum = 0
    for number in numberList:
        sum += number
    
    return sum
            
answer = sum_natural(1,1000)
# задача решена.
print("Задача решена.")
print("Ответ: \x1b[32m", answer , '\x1b[0m\n')



