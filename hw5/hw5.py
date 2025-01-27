#1.	Дано число number. Вывести на экран числа 1, 4, 9, 16, 25, ... которые меньше number.
#print("Задание 1")
#number = int(input("Введите число: "))
#chisla = 1
#while number > chisla * chisla:
#    print(chisla * chisla)
#    chisla += 1
#2.	Дано число number. Определить первую цифру этого числа.
#print("Задание 2")
#number = int(input("Введите число: "))
#while number >=10:
#    number //= 10
#print("Превая цифра:", number)
#3.	Дано натуральное число number. Найти значение минимальной цифры в данном числе .
#print("Задание 3")
#number = int(input("Введите натуральное чило: "))
#min_digit = 9
#while number > 0:
#    digit = number % 10
#    if digit < min_digit:
#        min_digit = digit
#    number //= 10
#print(f"Минимальная цифра: {min_digit}")
# 4 задача на строки
#print("Задание 4")
#input_string = input("Введите строку: ")
##1
#print(input_string[2])
##2
#print(input_string[-2])
##3
#print(input_string[0:5])
##4
#print(input_string[:-2])
##5
#print(input_string[1::2])
##6
#print(input_string[2::2])
##7
#print(input_string[::-1])
##8
#print(input_string[::-2])
##9
#print(len(input_string))
#5.	Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.
#print("Задание 5")
#input_string = input("Введите строку из 2 слов = ")
#words = input_string.split()
#result_string = f"{words[1]} {words[0]}"
#print(result_string)
#6.	Проверить является ли строка палиндромом
#input_string = input("Введите строку: ")
#word_sting = ''.join(input_string.split()).lower()
#is_palindrome = word_sting == word_sting[::-1]
#if is_palindrome:
#    print("строка является палиндром")
#else:
#    print("строка не является палиндром")
#7.	Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз, выведите индекс
# её первого появления и количество букв f.Если буква f в данной строке
# не встречается, ничего не выводите.
#input_string = input("Введите строку ")
#first_index = -1
#f_count = 0
#for index in range(len(input_string)):
#    if input_string[index] == 'f':
#        f_count += 1
#        if f_count == 1:
#            first_index = index
#if f_count == 1:
#    print(first_index)
#elif f_count > 1:
#    print("Индекс", first_index,"Колчество", f_count)
#8.	Задано два списка. Найти наименьшие среди элементов первого списка,
# которые не входят во второй список.
#list1 = list(map(int, input("Введите элемнты первого списка через пробел ").split()))
#list2 = set(map(int, input("Введите элемнты второго списка через пробел ").split()))
#min_element = min((x for x in list1 if x not in list2), default=None)
#if min_element is not None:
#    print("Наименьший элемент из первого списка, который не входит во второй: ", min_element)
#else:
#    print("Все элементы первого списка входят во второй")
#9.	Задан список из k чисел. Определить количество инверсий в списке (т. е. таких пар элементов,
# в которых большее число находится слева от меньшего).
#numbers = list(map(int, input("Введите числа черрез пробел: ").split()))
#inversions = sum(1 for i in range(len(numbers))
#             for j in range(i + 1, len(numbers))
#             if numbers[i] > numbers[j])
#print("Количество инверсия в списке: ", inversions)
#10.	Программе подаётся на вход произвольная строка. Удалите из нее повторяющиеся символы
# (т. е. символы, встречающиеся в строке во второй или более раз) и выведите результат на экран.
# Задачу решить через список. Функцию set не использовать
#input_string = input("Введите строку: ")
#unique_chars = []
#for char in input_string:
#    if input_string.count(char) == 1:
#        unique_chars.append(char)
#result = ''.join(unique_chars)
#print("Результат:", result)