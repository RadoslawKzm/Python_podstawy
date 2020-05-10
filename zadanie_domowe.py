"""
1. wygeneruj liste randomowych liczb od 0 do 10 o dlugosci 1_000
len(twoja_lista) == 1_000
podpowiedz, biblioteka random
w google 'python3 random'
funkcja ktora generuje losowy int w podanym zakresie (od, do)

2. policz ile razy wystepuje dana liczba
{0:25, 1:26, 2:32, (...), 10:26}

3. wypisz do pliku wyniki
liczba > 0, wystapila > 26
liczba > 1, wystapila > 31
(...)
liczba > 10, wystapila > 25

"""

from random import randint

"""Punkt pierwszy 
tworzymy liste 1_000 liczba losowych z zakresu od 0-9
podalem ci 2 rozwiazania ktore sa torzsame czyli sa identyczne jesli chodzi o wynik ale drugie rozwiazanie jest szybsze
wszystko wytlumacze na kolejnych zajeciach
drugi sposob to list comprehention
"""

lista_liczb = []
for liczba in range(1_000):
    lista_liczb.append(randint(0,9))

lista_liczb_randomowych = [randint(0,9) for liczba in range(1_000)]

"""punkt drugi
liczymy ile razy dana liczba wystapila
dalem trzy przyklady jak to mozna policzyc trzeci to uzycie dedykowanej funkcji counter z biblioteki collections
sa 3 printy zeby pokazac ze sa to te same wartosci
"""
slownik_liczb = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for liczba in lista_liczb_randomowych:
    if liczba == 0:
        slownik_liczb[liczba] += 1
    if liczba == 1:
        slownik_liczb[liczba] += 1
    if liczba == 2:
        slownik_liczb[liczba] += 1
    if liczba == 3:
        slownik_liczb[liczba] += 1
    if liczba == 4:
        slownik_liczb[liczba] += 1
    if liczba == 5:
        slownik_liczb[liczba] += 1
    if liczba == 6:
        slownik_liczb[liczba] += 1
    if liczba == 7:
        slownik_liczb[liczba] += 1
    if liczba == 8:
        slownik_liczb[liczba] += 1
    if liczba == 9:
        slownik_liczb[liczba] += 1

slownik_liczb_2 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for liczba in lista_liczb_randomowych:
    slownik_liczb_2[liczba] += 1

from collections import Counter as col_counter
licznik = col_counter(lista_liczb_randomowych)
slownik_licznik = dict(licznik)

print(slownik_liczb == slownik_liczb_2)
print(slownik_liczb == slownik_licznik)
print(slownik_liczb_2 == slownik_licznik)

"""Punkt trzeci do pliku
pierwsze wpisywanie do pliku jest takie jakie znamy
drugie to uzycie lepszego podejscia tj. context manager daje ci to wszystko zebys mogl doczytac
na koncu sortujemy wszystko
"""
file = open('wyniki', 'w')
for klucz, wartosc in slownik_licznik.items():
    file.write(f"liczba > {klucz}, wystapila > {wartosc}\n")
file.close()

with open('wyniki_2', 'w') as output:
    for klucz, wartosc in slownik_licznik.items():
        output.write(f"liczba > {klucz}, wystapila > {wartosc}\n")

#posortujmy wyniki
posortowany_slownik = {k: slownik_licznik[k] for k in sorted(slownik_licznik)}

with open('wyniki_3', 'w') as output:
    for klucz, wartosc in posortowany_slownik.items():
        output.write(f"liczba > {klucz}, wystapila > {wartosc}\n")
