# #1
# zdanie = input('Podaj jakies zdanie:')
# ilosc = 0
# for i in zdanie:
#     if i==" ":
#         ilosc=ilosc+1
# print ('Liczba spacji jest rowna: ', ilosc)

# #2 nie dziala
# import sys
# print('Podaj pierwsza liczbe: ')
# s1 = sys.stdin.readline()
# print('Podaj druga liczbe: ')
# s2 = sys.stdin.readline()
# wynik = (s1 * s2)
#
# sys.stdout.write(wynik)

# #3
# a = int(input('Podaj pierwsza liczbe:'))
# b = int(input('Podaj druga liczbe:'))
# c = int(input('Podaj trzecia liczbe:'))
#
# if (a > 0 and a <= 10) and (a > b and b > c):
#     print("spelnione dwa warunki")
# elif (a > 0 and a <= 10):
#     print("spelniony tylko pierwszy warunek")
# elif (a > b and b > c):
#     print("spelniony tylko drugi warunek")
# else:
#     print("zaden warunek nie jest spelniony")

# #4
# for i in range(1,51):
#     if i % 5 == 0:
#         print(i, end=', ')

# #6
# lista = []
# print('Podaj liczby całkowite, które chcesz umieścić w pętli.')
# print('Wpisz "stop" aby zakończyć')
# while True:
#     wejscie = input()
#     if wejscie == 'stop':
#         break
#     lista.append(int(wejscie))
#
# print("Twoja lista to", lista)

#7

# iloscWierszy = input()
# print(f"Twoja choinka będzie wysoka na {iloscWierszy} wierszy")
# iloscGwiazdek = 1
# iloscSpacji = iloscWierszy-1
# print("Nie wolno kopiować kodu z PDF!")
# # Pierwsza pętla to wysokość choinki:
# for kazdyElement in range(iloscWierszy):


# j = int(input("podaj ile wysokosci ma miec wieza ?"))
#
# for j in range(0, j):
#     if j < 10:
#         print((j+1) * "A")



# liczba = [1,2,3,4,5]
# for i in range (0,5):
#     print (liczba [i]**3)






