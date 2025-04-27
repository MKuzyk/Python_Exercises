'''
Zadanie 10.
Wyświetl w porządku rosnącym liczby całkowite od 1 do 100. Zrób to, wykorzystując
zarówno pętle for, jak i while.
'''

counter = 0

while counter < 100:
    counter += 1
    print(counter,end = ", ")

print()

for i in range(1,101):
    print(i, end = ", ")

