'''
Zadanie 14. [2:1,1] <abc> {!}
Odgadnij wzór ciągu na podstawie pierwszych ośmiu elementów [1], a następnie
wyświetl jego sto elementów [1]. Początek ciągu: 3, 1, 2, 1, 3, 1, 2, 1, …
'''

List = [3, 1, 2, 1]
List_1 = []

for i in range (100):
    List_1.append(List[i%4])
print(List_1)





