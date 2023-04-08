# Задание 1 Напишите функцию, которая вычисляет объём сферы по заданному радиусу.
import math


def vol(radius):
    p = math.pi
    v = 4 / 3 * p * radius ** 3
    return v


# Задание 2 Напишите функцию, которая проверяет, содержится ли число в указанном диапазоне (включая верхнюю и нижнюю
# границы)

def run_check(num, start, end):
    for i in range(start, end + 1):
        if num == i:
            return f'{num} находится в диапазоне от {start} до {end}'


# Задание 3 Напишите функцию Python, которая принимает на вход строку, и вычисляет количество букв в верхнем регистре
# и в нижнем регистре.


def up_low(some_string):
    new_string = some_string.replace(',', '').replace('.', '').replace(' ', '').replace('?', '')
    upper_list = []
    lower_list = []
    for i in new_string:
        if i.isupper():
            upper_list.append(i)
        else:
            lower_list.append(i)
    return f'Количество символов в верхнем регистре:{len(upper_list)}\nКоличество символов в нижнем регистре:{len(lower_list)} '


# Задание 4 Напишите функцию Python, которая получает на входе список, и возвращает новый список, содержащий
# уникальные элементы из первого списка
def unique_list(some_list):
    return list(set(some_list))


# Задание 5 Напишите функцию Python, которая перемножает все числа в списке.

def multiply(some_list):
    return math.prod(some_list)


# Задание 6 Напишите функцию Python, которая проверяет входную строку, является ли эта строка палиндромом или нет.

def palindrome(some_string):
    if some_string[::-1] == some_string:
        return True
    else:
        return False

# Задание 7
