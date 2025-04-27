'''
Zadanie 16. [3:1,2] <abc> {!}
Odgadnij wzór ciągu na podstawie pierwszych sześciu elementów [1], a następnie
wyświetl jego sto elementów. Początek ciągu: 100, 99, 97, 94, 90, 85, … Ile wynosi
ostatni (setny) element ciągu? [2]
'''

list = []
current_value = 100
step = 1

for i in range(100):
    list.append(current_value)
    current_value -=step
    step +=1

last_element = list[-1]

print(list)
print(f"Ostatni element ciągu to : {last_element}")