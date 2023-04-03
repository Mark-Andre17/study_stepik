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
#
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
        return 'Buzz'
