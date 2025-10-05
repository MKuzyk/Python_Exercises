'''Skopiuj poniższą listę do swojego kodu lub skopiuj ją z pliku 32_lista.txt.
x=[2,7,1,1,4,9,3,2,1,4,1,9,6,1,3,0,1,2,3,6,8,5,6,9,3,0,8,1,8,8,7,0,7,8,5,0,2,2,3,7,1,7,
2,4,7,7,5,9,0,7,7,9,2,2,2,7,0,0,5,4,6,3,9,3,5,1,0,0,9,2,9,2,8,5,0,8,5,7,0,9,6,4,9,7,8,
8,6,5,4,3,2,5,8,9,4,6,8,7,9,9]
Wyświetl kolejne liczby określające odległość między kolejnymi wartościami 9.
Przyjmij, że sąsiadujące bezpośrednio dziewiątki dzieli odległość 0, dziewiątki rozdzielone
jedną liczbą (np. 9, 5, 9) dzieli odległość 1 itd.'''

import ast
from pathlib import Path

sciezka = Path("C:/Users/Administrator/Desktop/Podyplomówka_Python/Książki/pliki/32_lista.txt")

with sciezka.open("r", encoding="utf-8") as plik:
    zawartosc = plik.read().strip()

    if zawartosc.startswith("x ="):
        zawartosc = zawartosc[3:].strip()
    lista = ast.literal_eval(zawartosc)

print(lista)

indeksy_9 = [i for i, x in enumerate(lista) if x == 9]

# Oblicz odległości
odleglosci = [indeksy_9[i+1] - indeksy_9[i] - 1 for i in range(len(indeksy_9)-1)]

print("Indeksy 9:", indeksy_9)
print("Odległości między 9:", odleglosci)