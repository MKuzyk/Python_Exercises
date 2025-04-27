'''
Zadanie 15. [3:1,2] <abc> {!}
Odgadnij wzór ciągu na podstawie pierwszych dziesięciu elementów [1], a następnie
wyświetl jego sto elementów [2]. Początek ciągu: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, …
'''

list = []
n = 1

while len(list) <= 100:
    for _ in range(n):
        list.append(n)
    n += 1

print(list)