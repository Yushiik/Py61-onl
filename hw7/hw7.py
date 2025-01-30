#print("Задание 1")
#list_nechet = [i for i in range(10,100) if i%2 == 1]
#print(list_nechet)

#print("Задание 2")
#list_stp2 = [i**2 for i in range(1, 11)]
#print(list_stp2)

#print("Задание 3")
#list_chisla3 = [i for i in range(100, 1000) if i%5 == 0 or i%3 == 0]
#print(list_chisla3)

#print("Задание 4")
#numb = input("Введите 3 числа: ")
#start, end, stp = map(int, numb.split())
#list_numb = [i**stp for i in range(start, end+1)]
#print(list_numb)

#print("Задание 5")
#def even_fr(i):
#    if i%10 == 0:
#        return True
#    return False
#list_numb = [i for i in range(1, 101)]
#print(list(filter(even_fr, list_numb)))

#print("Задание 6")
#words = ["awerga", "assawa", "cwefwas", "sdwergfa", "asdefrfa", "wrefwdqa"]
#filt_words = [word for word in words if word.count('a') >= 2]
#print(filt_words)

#print("Задание 7")
#words = ["awerga", "assawa", "cwefwas", "sdwergfa", "asdefrfa", "wrefwdqa"]
#upper_words = [s.upper() for s in words]
#print(upper_words)

print("Задание 8")
words = ["aw12erga", "ass34awa", "cwef56was", "sdwerg78fa"]
cleaned_word = [''.join(i for i in a if not i.isdigit()) for a in words]
print(cleaned_word)