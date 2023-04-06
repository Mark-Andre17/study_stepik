# задание 1 "Меньшее из двух чётных чисел": Напишите функцию, которая возвращает меньшее из двух чисел, *если* оба
# эти числа чётные. Иначе возвращает большее из двух чисел, если одно или оба числа нечётные.


def get_some_number(a, b):
    new_list = [a, b]
    if new_list[0] % 2 == 0 and new_list[1] % 2 == 0:
        return min(new_list)
    else:
        return max(new_list)


# задание 2 Напишите функцию, которая получает на входе строку из двух слов, и возвращает True если оба слова
# начинаются с одной и той же буквы.

def get_boolean(string):
    new_list = string.split()
    return new_list[0][0].lower() == new_list[1][0].lower()


# задание 3 На входе два числа, функция возвращает True если сумма этих чисел равна 20, *или* если одно из чисел
# равно 20. В противном случае, возвращает False.

def make_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20


# Задание 4  Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени.


def old_macdonald(name):
    new_list = []
    for a, n in enumerate(name):
        if a == 0 or a == 3:
            new_list.append(n.upper())
        else:
            new_list.append(n)
    return ''.join(new_list)


# задание 5 На входе фраза, на выходе вернуть слова в обратном порядке

def reverse_string(string):
    new_list = string.split()
    return ' '.join(new_list[::-1])


# задание 6 на входе число n, вернуть True если n находится не далее чем на 10 от чисел 100 или 200.
def almost_there(number):
    return 90 <= number <= 110 or 190 <= number <= 210


# задание 7 На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3.


def return_boolean(my_list):
    for i in range(0, len(my_list) - 1):
        if my_list[i:i + 2] == [3, 3]:
            return True
    return False


# задание 8 На входе строка, вернуть строку где каждый символ исходной строки повторяется три раза.

def paper_doll(string):
    new_list = []
    for i in string:
        new_list.append(i * 3)
    return ''.join(new_list)


# задание 9 На входе три числа от 1 до 11. Если их сумма меньше или равна 21, то вернуть их сумму. Если сумма больше
# 21 *и* среди чисел есть 11, то уменьшить общую сумму на 10. И наконец, если сумма (в том числе после уменьшения)
# превышает 21, вернуть 'BUST'.


def blackjack(*arg):
    if sum(arg) > 21 and 11 in arg:
        return sum(arg) - 10
    elif sum(arg) <= 21:
        return sum(arg)
    else:
        return 'BUST'


# задание 10 Вернуть сумму чисел в массиве, кроме набора чисел который начинается с 6 и продолжается до 9 (для
# каждого числа 6 далее где-то будет число 9). Вернуть 0 если чисел нет.


def summer_69(some_list):
    start_index = 0
    end_index = 0
    for i, n in enumerate(some_list):
        if n == 6:
            start_index = i
        elif n == 9:
            end_index = i + 1
    del some_list[start_index:end_index]
    return sum(some_list)


# задание 11 Напишите функцию, которая берёт список чисел, и возвращает True, если в списке содержатся числа 0 0 7 в
# указанном порядке.

def spy_game(some_list):
    spy_list = [0, 0, 7]
    for elem in some_list:
        if elem == spy_list[0]:
            spy_list = spy_list[1:]
        if len(spy_list) == 0:
            return True
    return False


# задание 12 Напишите функцию, которая возвращает *количество* простых чисел, которые меньше или равны указанному числу.
def simple_numbers(num):
    all_numbers_list = list(range(num + 1))
    all_numbers_list[1] = 0
    number_list = []
    i = 2
    while i <= num:
        if all_numbers_list[i] != 0:
            number_list.append(all_numbers_list[i])
            for j in range(i, num + 1, i):
                all_numbers_list[j] = 0
        i += 1
    return len(number_list)


# задание 13(Необязательно)Напишите функцию, которая принимает на вход одну букву, и возвращает фигуру 5x5 для этой
# буквы.
def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


# задание 14 Найти больший делитель для 2 чисел

def get_divider(a, b):
    my_list = [i for i in range(1, a + b)]
    new_list = []
    for num in my_list:
        if a % num == 0 and b % num == 0:
            new_list.append(num)
    return f'максимальный делитель = {max(new_list)}\nВсе делители: {new_list}'


# задание 15 Дано: список dict-объектов вида вида {"key": "value"}, например [{"key1": "value1"}, {"k1": "v1",
# "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].
#
# Напишите функцию, которая удаляет дубликаты из этого списка. Для примера выше возвращаемое значение может быть
# равно [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}]. Обязательное условие:
# функция не должна иметь сложность O(n^2).

def delete_duplicates(some_list):
    new_list = []
    for i in some_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


