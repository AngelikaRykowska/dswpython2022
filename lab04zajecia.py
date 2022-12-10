
lista = list(range(10))

for elem in lista:
    if elem % 2 == 0:
        print("#" * elem)


        #
        # for i in range(1,51):
        #     if i % 5 == 0:
        #         print(i, end=', ')

        # def zadanie_1():
        #     zdanie = input('Podaj jakies zdanie: \n')
        #     return zdanie.count(' ')
        #
        # if __name__ =="__main__":
        #     ile_spacji = zadanie_1()
        #     print(ile_spacji)

        # import sys
        # def zadanie_2():
        #
        #
        #     print('Podaj pierwsza liczbe: ')
        #     liczba_1 = sys.stdin.readline()
        #     print('Podaj druga liczbe: ')
        #     liczba_2 = sys.stdin.readline()
        #     wynik = int(liczba_1) * int(liczba_2)
        #     return wynik
        #
        #
        #
        # if __name__ =="__main__":
        #     sys.stdout.write(str(zadanie_2()))
        #

        # def zadanie_3():
        #     a = int(input('Podaj pierwsza liczbe:'))
        #     b = int(input('Podaj druga liczbe:'))
        #     c = int(input('Podaj trzecia liczbe:'))
        #
        #     if (a > 0 and a <= 10) and (a > b and b > c):
        #         print("spelnione sa dwa warunki")
        #     elif (a > 0 and a <= 10):
        #         print("spelniony jest tylko pierwszy warunek")
        #     elif (a > b and b > c):
        #         print("spelniony jest tylko drugi warunek")
        #     else:
        #         print("zaden warunek nie jest spelniony")
        #
        # if __name__ =="__main__":
        #     zadanie_3()

        # def zadanie_4():
        #     for i in range(1,51):
        #         if i % 5 == 0:
        #             print(i, end=', ')
        #
        # if __name__ =="__main__":
        #     zadanie_4()

        def zadanie_5():
            print('Podaj liczby, oddziel je spacja')
            lista_liczb = list()
            liczby = input()
            oddzielone = liczby.split(' ')
            for i in (0, len(oddzielone)):
                kwadraty = (oddzielone[i]) ** 2
                print('Kwadraty podanych liczb to', kwadraty)


        if __name__ == "__main__":
            zadanie_5()


        # def zadanie_6():
        #     lista = []
        #     print('Podaj liczby całkowite, które chcesz umieścić w pętli.')
        #     print('Wpisz "stop" aby zakończyć')
        #     while True:
        #         wejscie = input()
        #         if wejscie == 'stop':
        #             break
        #         lista.append(int(wejscie))
        #
        #     print("Twoja lista to", lista)
        #
        # if __name__ == "__main__":
        #     zadanie_6()

        # def zadanie_7():
        #     suma = 0
        #     liczba = input('Podaj liczbe wielocyfrową\n')
        #     for i in range(0, len(liczba)):
        #         suma = suma + int(liczba[i])
        #     print('Suma cyfr podanej liczby to', suma)
        #
        # if __name__ == "__main__":
        #     zadanie_7()

        # def zadanie_8():
        #     j = int(input("podaj ile wysokosci ma miec wieza ?"))
        #     if j >10 or j<0:
        #         print('Podana liczba jest wieksza od 10')
        #     else:
        #         for j in range(0, j):
        #             if j < 10:
        #                 print((j + 1) * "A")
        #
        #
        # if __name__ == "__main__":
        #     zadanie_8()

        #
        # for i in range(1,51):
        #     if i % 5 == 0:
        #         print(i, end=', ')

        # def zadanie_1():
        #     zdanie = input('Podaj jakies zdanie: \n')
        #     return zdanie.count(' ')
        #
        # if __name__ =="__main__":
        #     ile_spacji = zadanie_1()
        #     print(ile_spacji)

        # import sys
        # def zadanie_2():
        #
        #
        #     print('Podaj pierwsza liczbe: ')
        #     liczba_1 = sys.stdin.readline()
        #     print('Podaj druga liczbe: ')
        #     liczba_2 = sys.stdin.readline()
        #     wynik = int(liczba_1) * int(liczba_2)
        #     return wynik
        #
        #
        #
        # if __name__ =="__main__":
        #     sys.stdout.write(str(zadanie_2()))
        #

        # def zadanie_3():
        #     a = int(input('Podaj pierwsza liczbe:'))
        #     b = int(input('Podaj druga liczbe:'))
        #     c = int(input('Podaj trzecia liczbe:'))
        #
        #     if (a > 0 and a <= 10) and (a > b and b > c):
        #         print("spelnione sa dwa warunki")
        #     elif (a > 0 and a <= 10):
        #         print("spelniony jest tylko pierwszy warunek")
        #     elif (a > b and b > c):
        #         print("spelniony jest tylko drugi warunek")
        #     else:
        #         print("zaden warunek nie jest spelniony")
        #
        # if __name__ =="__main__":
        #     zadanie_3()

        # def zadanie_4():
        #     for i in range(1,51):
        #         if i % 5 == 0:
        #             print(i, end=', ')
        #
        # if __name__ =="__main__":
        #     zadanie_4()

        def zadanie_5():
            print('Podaj liczby, oddziel je spacja')
            lista_liczb = list()
            liczby = input()
            oddzielone = liczby.split(' ')
            for i in (0, len(oddzielone)):
                kwadraty = (oddzielone[i]) ** 2
                print('Kwadraty podanych liczb to', kwadraty)


        if __name__ == "__main__":
            zadanie_5()

        # def zadanie_6():
        #     lista = []
        #     print('Podaj liczby całkowite, które chcesz umieścić w pętli.')
        #     print('Wpisz "stop" aby zakończyć')
        #     while True:
        #         wejscie = input()
        #         if wejscie == 'stop':
        #             break
        #         lista.append(int(wejscie))
        #
        #     print("Twoja lista to", lista)
        #
        # if __name__ == "__main__":
        #     zadanie_6()

        # def zadanie_7():
        #     suma = 0
        #     liczba = input('Podaj liczbe wielocyfrową\n')
        #     for i in range(0, len(liczba)):
        #         suma = suma + int(liczba[i])
        #     print('Suma cyfr podanej liczby to', suma)
        #
        # if __name__ == "__main__":
        #     zadanie_7()

        # def zadanie_8():
        #     j = int(input("podaj ile wysokosci ma miec wieza ?"))
        #     if j >10 or j<0:
        #         print('Podana liczba jest wieksza od 10')
        #     else:
        #         for j in range(0, j):
        #             if j < 10:
        #                 print((j + 1) * "A")
        #
        #
        # if __name__ == "__main__":
        #     zadanie_8()
