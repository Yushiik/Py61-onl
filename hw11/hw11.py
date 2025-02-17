#class bank_account:
#    def __init__(self, balance: float = 0):
#        self.__balance = balance
#        self.daily_limit = 5000
#        self.withdrawals_today = 0
#        self.max_withdrawals = 3
import time


#    def deposit(self, amount: float):
#        if amount > 0:
#            self.__balance += amount
#            print(f"Пополнено: {amount}. Текущий баланс {self.__balance}")

#    def withdraw(self, amount: float):
#        if amount > self.__balance:
#            print("Недостаточно средств")
#            return
#        if self.withdrawals_today + amount > self.daily_limit:
#            print("Привышен лимит операций на сегодня.")
#            return
#        self.__balance -= amount
#        self.withdrawals_today += amount
#        self.daily_limit += 1
#        print(f"Снято: {amount}. Текущий баланс: {self.__balance}")

#    def reset_daily_limit(self):
#        self.withdrawn_today = 0
#        self.transaction_count = 0
#        print("Суточные лимиты и счетчик транзакций сброшены.")

#    def get_balance(self):
#        return self.__balance
#account = bank_account(10000)
#while True:
#        action = input("Введите действие (deposit, withdraw, balance, reset, exit): ").strip()
#        if action == 'deposit':
#            amount = float(input("Введите сумму для пополнения: "))
#            account.deposit(amount)

#        elif action == 'withdraw':
#            amount = float(input("Введите сумму для снятия: "))
#           account.withdraw(amount)

#        elif action == 'balance':
#            print(f"Текущий баланс: {account.get_balance()}")

#        elif action == 'reset':
#            account.reset_daily_limit()

#        elif action == 'exit':
#            print("Выход из программы.")
#            break

#        else:
#            print("Неизвестное действие. Попробуйте снова.")
#import time
#class Animal:
#    def __init__(self, name: str, age: int):
#        self.name = name
#        self.age = age
#        self.hunger = 100  # 100 - сыт, 0 - голоден
#        self.is_hunger = False

#    def make_sound(self):
#        pass

#    def eat(self):
#        self.hunger = 100
#        self.is_hunger = False
#        print(f"{self.name} накормлен")

#    def check_hunger(self):
#        if self.hunger < 50:
#            self.is_hunger = True
#            print(f"{self.name} гоолоден")
#        else:
#            self.hunger += -10

#class Lion(Animal):
#    def make_sound(self):
#        return "Рев!"
#    def hunt(self):
#        print(f"{self.name} ищет добычу")

#class Elephant(Animal):
#    def make_sound(self):
#        return "трууууу"
#    def trumpet(self):
#        print(f"{self.name} трубит")

#class Penguin(Animal):
#    def make_sound(self):
#        return "шлеп-шлеп"
#    def swim(self):
#        print(f"{self.name} плывет")
#animals = []
#while True:
#    animal_type = input("Введите тип животного (lion, elephant, penguin) или 'exit' для выхода: ").strip()

#    if animal_type == 'exit':
#        break

#    name = input("Введите имя животного: ")
#    age = int(input("Введите возраст животного: "))

#    if animal_type == 'lion':
#        animals.append(Lion(name, age))
#    elif animal_type == 'elephant':
#        animals.append(Elephant(name, age))
#    elif animal_type == 'penguin':
#        animals.append(Penguin(name, age))
#    else:
#        print("Неизвестный тип животного. Попробуйте снова.")

#while True:
#    for animal in animals:
#        print(f"{animal.name} (Возраст: {animal.age}) издает звук: {animal.make_sound()}")
#        animal.check_hunger()
#    if animal.is_hunger:
#        animal.eat()
#    time.sleep(1)

class Temperature:
    def __init__(self, celsius):
        self._celsius = None
        self.set_temperature(celsius)

    def set_temperature(self, celsius):
        if celsius < -273.15:
            raise ValueError("Температура не может быть ниже -273.15°C.")
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15
try:
    temp = Temperature(int(input("Введите значение: ")))
    print(f"Температура в Цельсиях: {temp.celsius}°C")
    print(f"Температура в Фаренгейтах: {temp.fahrenheit}°F")
    print(f"Температура в Кельвинах: {temp.kelvin} K")

    temp.set_temperature(-300)
except ValueError as e:
    print(e)