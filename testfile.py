var = 1
strin = 'test string'

tup = (1, 2, 3, 4)
lst = ['a', 'b', 'c', 'd']
dictio = {'imie': 'piotr', 'nazwisko': 'jankowiak'}
sett = set()

for item in lst:
    print(f"{item}")

i = 0
while i < 4:
    print(i)
    i += 1

# generator_liter = strin.__iter__()
# litera = generator_liter.__next__()

for letter in strin:
    print(f"twoja litera >> {letter}")

element_pierwszy = lst[0]

for klucz, wartosc in dictio.items():
    print(f"klucz> {klucz}, wartosc> {wartosc}")

test_file = open('plik_testowy', 'w')
for i in range(100):
    test_file.write(f"twoja liczba to {i}\n")
test_file.close()

input_file = open('plik_testowy', 'r')
for line in input_file:
    # print(f"twoja linia > {line}")
    if '59' in line:
        print(f"59 znajduje sie w linii {line}")

"""wypisz do pliku wszystkie kody pocztowe z zakresu
81-200
82-400
"""

var = "81200"

file = open('plik_testowy', 'w')
for i in range(81_200, 82_401, 1):
    strin = str(i)
    file.write(f"{strin[:2]}-{strin[2:]}\n")
file.close()

"""
1. wygeneruj liste randomowych liczb od 0 do 10 o dlugosci 1_000
len(twoja_lista) == 1_000
podpowiedz, biblioteka random
w google 'python3 random'
funkcja ktora generuje losowy int w podanym zakresie (od, do)

2. policz ile razy wystepuje dana liczba
{0:25, 1:26, 2:32, (...)}

"""

