#print("Задание1")
#def minimum(a, b):
#    return a if a < b else b

#num1 = float(input("Введите 1 число: "))
#num2 = float(input("Введите 2 число: "))

#print("Минимум: ", minimum(num1, num2))

#print("Задание 2")
#def minimum(a, b):
#    return a if a < b else b

#num1 = float(input("Введите первое число: "))
#num2 = float(input("Введите второе число: "))
#num3 = float(input("Введите третье число: "))
#num4 = float(input("Введите четвёртое число: "))

#min_first_two = minimum(num1, num2)
#min_last_two = minimum(num3, num4)
#final_min = minimum(min_first_two, min_last_two)

#print("Минимум из четырёх чисел:", final_min)

#print("Задание 3")
#import math

#def distance(x1, y1, x2, y2):
#    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

#x1 = float(input("Введите x1: "))
#y1 = float(input("Введите y1: "))
#x2 = float(input("Введите x2: "))
#y2 = float(input("Введите y2: "))

#result = distance(x1, y1, x2, y2)

#print("Расстояние между точками:", result)

#print("Задание 4")
#def is_prime(number):
#   if number <= 1:
#        return False
#    for i in range(2, int(number**0.5) + 1):
#        if number % i == 0:
#            return False
#    return True

#number = int(input("Введите натуральное число (больше 1): "))

#if is_prime(number):
#    print("YES")
#else:
#    print("NO")

#print("Задание 5")
#def fibonacci(n):
#    if n < 0:
#        raise ValueError("n должно быть неотрицательным")
#    elif n == 0:
#        return 0
#    elif n == 1:
#        return 1

#    a, b = 0, 1
#    for _ in range(2, n + 1):
#        a, b = b, a + b
#    return b
#n = int(input("Введите целое неотрицательное число n: "))
#result = fibonacci(n)

#print(f"{n}-е число Фибоначчи: {result}")

print("Задание 6")
def closest_mod_5(number):
    if number % 5 == 0:
        return number
    else:
        return number + (5 - number % 5)

number = int(input("Введите целое число: "))
result = closest_mod_5(number)
print("Наименьшее число, большее или равное", number, "и делящееся на 5:", result)