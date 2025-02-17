#class RangeSquared:
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end
#        self.current = start
from hw6.hw6 import result


#    def __iter__(self):
#        return self

#    def __next__(self):
#        if self.current < self.end:
#            square = self.current ** 2
#            self.current += 1
#            return square
#        else:
#            raise StopIteration

#for square in RangeSquared(1, 5):
#    print(square)

#def factorial_gen(n):
#    factorial = 1
#    for i in range(n + 1):
#        if i == 0:
#            yield 1  # Факториал 0 равен 1
#        else:
#            factorial *= i
#            yield factorial

#n = 5
#for fact in factorial_gen(n):
#    print(fact)

#def read_file_lines(filename):
#    with open(filename, 'r', encoding='utf-8') as file:
#        for line in file:
#            yield line.strip()

#filename = 'example.txt'  # Указать имя файла

#try:
#    for line in read_file_lines(filename):
#        print(line)
#except FileNotFoundError:
#    print(f"Файл '{filename}' не найден.")

#def calculate_complex_formula(a,b,c,d,e,f,g,h):
#    result = 0
#    # Условие для а
#    if a > 0:
#        result += b * c
#    else:
#        result += d / e # Предполагаем, что е не равно 0
#        # Условие для g и h
#    if g < h:
#        result += f*(g + h)
#    else:
#        result -= (d-f)/g # предпологаем, что g не равно 0
#    return result


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        greeting = self.get_greeting()
        print(greeting)

    def get_greeting(self):
        if self.age >= 18:
            return f"Привет, {self.name}! Добро пожаловать на сайт для взрослых."
        else:
            return f"Привет, {self.name}! Добро пожаловать на детский сайт."

user1 = User("Алекс", 25)
user1.greet()

user2 = User("Лиза", 12)
user2.greet()