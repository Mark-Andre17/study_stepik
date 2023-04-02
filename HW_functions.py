# задание 1 "Меньшее из двух чётных чисел": Напишите функцию, которая возвращает меньшее из двух чисел, *если* оба
# эти числа чётные. Иначе возвращает большее из двух чисел, если одно или оба числа нечётные.
def get_some_number(a, b):
    new_list = [a, b]
    if new_list[0] % 2 == 0 and new_list[1] % 2 == 0:
        return min(new_list)
    else:
        return max(new_list)


print(get_some_number(102, 104))


# задание 2 Напишите функцию, которая получает на входе строку из двух слов, и возвращает True если оба слова
# начинаются с одной и той же буквы.
def get_boolean(string):
    new_list = string.split()
    return new_list[0][0].lower() == new_list[1][0].lower()


# задание 3 На входе два числа, функция возвращает True если сумма этих чисел равна 20, *или* если одно из чисел
# равно 20. В противном случае, возвращает False.

def make_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20


print(make_twenty(20, 20))

# Задание 4  Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени.


def old_macdonald(name):
    new_list = []
    for a, n in enumerate(name):
        if a == 0 or a == 3:
            new_list.append(n.upper())
        else:
            new_list.append(n)

    return ''.join(new_list)


print(old_macdonald('macdonald'))
