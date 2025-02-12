print("Task1")
#class fruits:

    #def __init__(self, apple, pear):
     #  self.apple = apple
     #   self.pear = pear

    #def desplay_info(self):
     #   print(f"apple: {self.apple}  pear: {self.pear}")

    #def changes_values(self, apple1, pear1):
    #   self.apple = apple1
    #    self.pear = pear1

    #def sum_values(self):
  #      return self.apple + self.pear

 #   def max_values(self):
 #       return max(self.apple, self.pear)

#basket = fruits(apple= int(input("Введите сколько яблок")),
 #               pear= int(input("Введите сколько груш")))
#basket.desplay_info()

#print(f"Сумма: {basket.sum_values()}")
#print(f"Наибольшее значение: {basket.max_values()}")

#print("Task2")
#class DecimalCounter:
#    def __init__(self, min_value=0, max_value=10, initial_value=0):
#        self.min_value = min_value
#        self.max_value = max_value
#        self.current_value = initial_value

#       if not (min_value <= initial_value <= max_value):
#            raise ValueError(f"Initial value {initial_value} must be between {min_value} and {max_value}")

#    def increment(self):
#        if self.current_value < self.max_value:
#            self.current_value += 1
#        else:
#            print("Cannot increment: reached maximum value.")

#    def decrement(self):
#        if self.current_value > self.min_value:
#            self.current_value -= 1
#        else:
#            print("Cannot decrement: reached minimum value.")

#    @property
#    def value(self):
#        return self.current_value

#if __name__ == "__main__":
#    counter1 = DecimalCounter()
#    print(f"Counter1 initial value: {counter1.value}")

#    counter1.increment()
#    print(f"Counter1 after increment: {counter1.value}")

#    print(f"Counter1 after decrement: {counter1.value}")

#    counter2 = DecimalCounter(min_value=0, max_value=5, initial_value=3)
#    print(f"Counter2 initial value: {counter2.value}")

#    for _ in range(3):
#        counter2.increment()
#        print(f"Counter2 after increment: {counter2.value}")
#   counter2.increment()

#    for _ in range(4):
#       counter2.decrement()
#        print(f"Counter2 after decrement: {counter2.value}")
#    counter2.decrement()


#class Product:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price

#    def __repr__(self):
#        return f"{self.name} (${self.price:.2f})"


#class Shop:
#    def __init__(self):
#        self.products = []

#   def add_product(self, product):
#        self.products.append(product)
#        print(f"Product '{product.name}' added to the shop.")

#    def remove_product(self, product_name):
#        for product in self.products:
#            if product.name == product_name:
#                self.products.remove(product)
#                print(f"Product '{product_name}' removed from the shop.")
#                return
#        print(f"Product '{product_name}' not found in the shop.")

#    def find_product(self, product_name):
#        found_products = [product for product in self.products if product_name.lower() in product.name.lower()]
#        return found_products

#    def list_products(self):
#        if not self.products:
#            print("No products available in the shop.")
#        else:
#            print("Products available in the shop:")
#            for product in self.products:
#                print(product)


#if __name__ == "__main__":
#    shop = Shop()

#    shop.add_product(Product("Apple", 0.99))
#    shop.add_product(Product("Banana", 0.59))
#    shop.add_product(Product("Orange", 0.79))

#    shop.list_products()

#    search_results = shop.find_product("apple")
#    print("Search results for 'apple':", search_results)

#    shop.remove_product("Banana")
#    shop.list_products()

#    shop.remove_product("Grapes")

#    shop.list_products()


#class MoneyBox:
#    def __init__(self, capacity):
#        self.capacity = capacity
#        self.current_amount = 0

#    def can_add(self, v):
#        return self.current_amount + v <= self.capacity

#    def add(self, v):
#        if self.can_add(v):
#            self.current_amount += v
#            print(f"Добавлено {v} монет. Текущее количество: {self.current_amount}.")
#        else:
#            print("Не хватает места в копилке для добавления монет.")

#    def __repr__(self):
#        return f"Копилка: {self.current_amount}/{self.capacity} монет."

#if __name__ == "__main__":
#    money_box = MoneyBox(10)
#    print(money_box)

#    money_box.add(5)
#    print(money_box)

#    if money_box.can_add(4):
#        money_box.add(4)
#    else:
#        print("Невозможно добавить 4 монеты.")

#   money_box.add(3)

#    print(money_box)