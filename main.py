# задание 1 Написать команду которая выведет только те слова, которые начинаются на s
st = 'Print only the words that start with s in this sentence'
my_list = st.split()
for word in my_list:
    if word[0].lower == 's':
        print(word)
# задание 2 Распечатать все четные числа от 1 до 10
for number in range(11):
    if number % 2 == 0:
        print(number)
# задание 3 Используйте генератор списка , чтобы создать список чисел от 1 до 50 , которые делятся на 3
numbers = [num for num in range(51) if num % 3 == 0]
print(numbers)
# задание 4 Если длина слова в строке четная, напечатать слово и это слово имеет четную длину
new_st = 'Print every world in this sentence that has an even number of letters'
my_new_list = new_st.split()
for word in my_new_list:
    if len(word) % 2 == 0:
        print(f'{word}- это слово имеет четную длину')
# задание 5 Напишите программу, которая напечатает числа от 0 до 100. Но для тех чисел, которые делятся на 3
# написать вместо них слово "Fizz" для тех чисел которые делсятся на 5, пишем слово "Buzz", а также если число
# делится на 3 и на 5 , пишем слово "FizzBuzz"
number_list = []
for num in range(101):
    if num % 3 == 0 and num % 5 == 0:
        number_list.append('FizzBuzz')
    elif num % 5 == 0:
        number_list.append('Buzz')
    elif num % 3 == 0:
        number_list.append('Fizz')
    else:
        number_list.append(num)
print(number_list)
# задание 6 Используйте генератор списка, чтобы распечатать только первые буквы слов
new_string = 'Create a list of the first letters of every word in this string'
new_str_list = [word[0] for word in new_string.split()]
print(new_str_list)
