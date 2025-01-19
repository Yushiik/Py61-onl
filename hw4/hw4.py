from itertools import count

from scipy.special import factorial
from unicodedata import digit
#1)	Напишите программу, которая проверяет последнюю цифру числа.
#Если последняя цифра числа 3, то вывести True иначе вывести False.
#print("Задание 1")
#a = int(input())
#if (a % 10) == 3:
#    print('True')
#else:
#   print('False')
#2)	Напишите программу, которая выводит True, если хотя бы одно из
# чисел number_1, number_2, number_3 отрицательно.
# Если нет вывести False. Числа вводятся с клавиатуры в одной строке.
#print("Задание 2")
#number_1, number_2, number_3 = map(int, input().split())
#if (number_1 < 0) or (number_2 < 0) or (number_3 < 0):
#    print("True")
#else:
#    print("False")
#3)	Верно ли что, целые number_1, number_2 имеют одинаковую четность.
#print("Задание 3")
#number_1 = int(input())
#number_2 = int(input())
#if ((number_1 % 2==0) == (number_2 % 2 ==0)):
#    print("True")
#else:
#    print("False")
#4)	Даны три стороны треугольника side_a, side_b, side_c.
# Выведите equilateral если треугольник равносторонний,
# isosceles если равнобедренный и scalene если разносторонний
#print("Задание 4")
#side_a = int(input())
#side_b = int(input())
#side_c = int(input())
#if side_a == side_b == side_c:
#    print("equilateral")
#elif side_a == side_b != side_c:
#    print("isoceles")
#elif side_a != side_b != side_a:
#    print("scalene")
#5)	Найти количество четных чисел среди заданных трех целых чисел.
#В ответе вывести количество четных чисел.
#print("Задание 5")
#a = int(input())
#b = int(input())
#c = int(input())
#count_ch = 0
#if a % 2 == 0:
#   count_ch += 1
#if b % 2 == 0:
#   count_ch += 1
#if c % 2 == 0:
#   count_ch += 1
#print("", count_ch)
#6)	Дано двузначное число.
# Определить является ли сумма его цифр двузначным числом.
#print("Задание 6")
#numb = int(input())
#if 10 <= numb <= 99:
#  x = numb // 10
#   y = numb % 10
#   digit_sum = x + y
#   if 10 <= digit_sum <= 99:
#      print("true")
#   else:
#      print("false")
#7)	Дано четырёхзначное число. Проверить, одинаковы ли все цифры в нём.
#print("Задание 7")
#n = input()
#if len(n) == 4 and n.isdigit():
#   if all(digit == n[0] for digit in n):
#      print("одинаковые")
#   else:
#      print("неодинаковые")
#8)	Напишите программу, принимающую на вход год и выводящую "Високосный",
# если в этом году действительно 366 дней, и "Не високосный" иначе.
# Год считается високосным, если его номер делится на 4, но не делится на 100
# или же делится на 400.
#print("Задание 8")
#year = int(input())
#if year % 4 != 0:
#   print("Год не високосный")
#elif year % 100 == 0:
#   if year % 400 == 0:
#      print("Год високосный")
#   else:
#      print("Год не високосный")
#else:
#   print("Год високосный")
#9)	Вывести на экран число "10" 20 раз столбиком.
#print("Задание 9")
#for i in range(20):
#   print("10")
#10)	Даны два числа start и stop.
# Составить программу вывода на экран всех чисел от start до stop.
#print("Задание 10")
#start = int(input())
#stop = int(input())
#for n in range(start, stop + 1):
#   print(n)
#11)	Выведите на экран в одну строку числа
# от 100 до  -100 включительно
#print("Задание 11")
#for n in range(100, -101, -1):
#   print(n, end=' ')
#12)	Найти сумму всех целых чисел от 100 до 500 включительно.
#print("Задание 12")
#total_sum = 0
#for n in range(100, 501):
#   total_sum += n
#print("суммa", total_sum)
#13)	Найти произведение всех целых чисел от 5 до 20 включительно
#print("Задание 13")
#a = 1
#for n in range(5, 21):
#   a *= n
#   print(a)
#14)	Дано натуральное число n. Вывести на экран факториал этого числа.
#print("Задание 14")
#n = int(input())
#factorial = 1
#for i in range(2, n+1):
#   factorial *= i
#   print(factorial)
