'''
Zadanie 11. [1] <abc> {!}
Wyświetl w porządku malejącym liczby całkowite od 10 do 100 z wyłączeniem 10,
pomijając podzielne przez 7.
'''

for i in range (100,10, -1):
    if not i % 7 == 0:
        print(i, end = ", ")