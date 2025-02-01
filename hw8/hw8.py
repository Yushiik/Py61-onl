#print("Задание 1")
#lst = ["wqrwegf", "wqr", "dqwqs", "wqdqfd"]
#sorted_lst = sorted(lst, key = len, reverse = True)
#print(sorted_lst)

#print("Задание 2")
#lst = ["awseaad", "weaffre", "sawdaf", "edwrfrafrea"]
#sorted_lst = sorted(lst, key = lambda word: word.count('a') )
#print(sorted_lst)

#print("Задание 3")
#school = {"9a": 20, "9b": 19, "9c": 18, "9d": 17}
#а) именилось количество
#school["9a"] = 21
#б) добавили новый класс
#school["9e"] = 23
#в) уддаление класса
#del school["9b"]
#г) количество учащехся 9 классов
#total_students = sum(school.values())
#print("Общее количество учащихся 9 классов: ", total_students)

#print("Задание 4")
#def phone_book():
#    contacts = {}
#    while True:
#        entry = input("Введите имя и номер (или имя для поиска): ")
#        if entry == ".":
#            break
#        parts = entry.split()
#        if len(parts) == 2:
#            name, number = parts
#            contacts[name] = number
#            print(f"Контакт {name} добавлен/обновлён.")
#        elif len(parts) == 1:
#            name = parts[0]
#            number = contacts.get(name, None)
#            if number:
#                print(f"Номер {name}: {number}")
#            else:
#                print(f"Контакт {name} не найден.")
#        else:
#            print("Неверно. Попробуйте снова.")
#phone_book()

print("Задание 5")
def get_element(lst: list, index: int):
    try:
        return lst[index]
    except IndexError:
        raise IndexError("Ошибка: индекс вне диапазона")
my_list = [10, 20, 30, 40, 50]

print(get_element(my_list, 2))

print(get_element(my_list, 5))