'''
Zadanie 12.
Wyświetl w porządku rosnącym liczby całkowite od –25 do 25 z pominięciem 0.
'''

for i in range (-25,26,1):
    if not i == 0:
        print(i, end = ",")