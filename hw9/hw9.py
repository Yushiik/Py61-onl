#print("Задание 1,2")
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#with open('input.txt', 'w') as file:
#    file.write(' '.join(map(str, numbers)))
#    with open('input.txt', 'r') as file:
#        numbers = list(map(int, file.read().strip().split()))
#    product = 1
#    for number in numbers:
#        product *= number
#    with open('output.txt', 'w') as file:
#        file.write(str(product))
#print(product)

#print("Задание 3")
#from datetime import datetime, timedelta
#
#stock = [
#    {"name": "Table", "quantity": 100, "unit_price": 450, "arrival_date": "2024-09-10"},
#    {"name": "Board", "quantity": 1000, "unit_price": 2590, "arrival_date": "2024-12-28"},
#    {"name": "Chfir", "quantity": 800, "unit_price": 2500, "arrival_date": "2025-01-12"},
#]

#current_date = datetime.now()
#for item in stock:
#    total_cost = item["quantity"] * item["unit_price"]
#    arrival_date = datetime.strptime(item["arrival_date"], "%Y-%m-%d")
#
#    if (current_date - arrival_date > timedelta(days=30)) and (total_cost > 1000000):
#        print(f"Наименование: {item['name']}, Количество: {item['quantity']}, "
#              f"Цена: {item['unit_price']}, Дата поступления: {item['arrival_date']}")

#print("Задание 4")

#print("Задание 5,6")
#import json
#import csv
#
#data = {
#    12345: ("Алексей", 30),
#    23456: ("Мария", 25),
#    34567: ("Иван", 40),
#   45678: ("Светлана", 35),
#    56789: ("Дмитрий", 28)
#}
#json_data = {str(key): value for key, value in data.items()}
#
#with open('data.json', 'w', encoding='utf-8') as json_file:
#    json.dump(json_data, json_file, ensure_ascii=False, indent=4)
#with open('data.json', 'r', encoding='utf-8') as json_file:
#    json_data = json.load(json_file)
#print("Данные успешно записаны в файл data.json")
#print(json_data)
#with open('data.csv', 'w', encoding='utf-8', newline='') as csv_file:
#    csv_writer = csv.writer(csv_file, delimiter=';')
#
#    csv_writer.writerow(['ID', 'Name', 'Age'])
#
#    for key, value in json_data.items():
#        name, age = value
#        csv_writer.writerow([f'person {key}', name, age])
#
#print("Данные успешно записаны в файл data.csv")