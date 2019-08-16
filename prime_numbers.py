def is_prime(num: int) -> bool:
    """ Возвращает True, если аргумент - простое число"""
    if (num % 2 == 0) or (num % 10 == 5):
        return False
    for s in range(3, num - 1):
        if num % s == 0:
            return False
    return True


def next_prime(previous_prime: int, prime_num_list: list) -> int:
    """ Возвращает следующее за переданным простое число"""
    # признак простоты числа
    num = previous_prime
    is_ismple = False
    while not is_ismple:
        # перехожу к следующему числу
        num += 1
        # если не '1', '3', '7' или '9' на конце - не простое, дальше
        if (num % 2 == 0) or (num % 10 == 5):
            continue
        devided = False
        for s in prime_num_list:
            # if s == 1:
            #     continue
            if num % s == 0:
                # разделилось, не простое
                devided = True
                break
        is_ismple = not devided
    return num


def get_prime_numbers(limit: int) -> list:
    """ Возвращает список всех простых чисел от 1 до указанного лимита """
    prime_num_list = [2, 3, 5]
    filled = False
    while not filled:
        if prime_num_list[-1] < limit:
            prime_num_list.append(next_prime(prime_num_list[-1], prime_num_list))
        else:
            filled = True
    return prime_num_list


def get_prime_deviders(number: int, prime_num_list: list) -> dict:
    """ Разложение числа на простые делители\n
    Возвращает словарь простых делителей.\n
    Ключи - простые делители,\n
    Значения - степени простых делителей\n

    :rtype: dict
    :param number: Раскладываемое на простые делители число
    :type number: int
    :param prime_num_list: Список простых чисел от 2 и до раскладываемого чила
    :type prime_num_list: list
    """
    prime_deviders = {}
    # индекс простого числа в списке простых чисел. Список начинается с 2
    devider_index = 0
    while number > 1:
        # если число делится нацело на текущее простое
        if number % prime_num_list[devider_index] == 0:
            # добавляю к счетчику этого простого числа еще 1
            # если простое встретилось впервые, заношу его в словарик
            if prime_num_list[devider_index] not in prime_deviders:
                prime_deviders[prime_num_list[devider_index]] = 0
            prime_deviders[prime_num_list[devider_index]] += 1

            # делю само число, чтобы двигаться дальше и сбрасываю делитель
            number = int(number / prime_num_list[devider_index])
            devider_index = 0
        # если число не делится нацело, перехожу к следующему простому числу
        else:
            devider_index += 1
            if len(prime_num_list) - 1 < devider_index:
                prime_num_list.append(next_prime(prime_num_list[devider_index-1], prime_num_list))
    return prime_deviders
