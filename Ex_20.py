'''
Utwórz listę i wstaw do niej dziesięć dowolnych liczb całkowitych. Utwórz drugą
listę, która na początku zawiera liczby parzyste z pierwszej listy, a potem pozostałe.
Wyświetl obie listy w oddzielnych wierszach.
'''

list_1 = []
list_2 = []
i = 1
count=int(input(f'How many numbers you would like to input in to the list?'))

while i <=count:
    try:
        number = int(input(f'Provide {i} integer number: '))
        list_1.append(number)
        i+=1
    except ValueError:
        print('This is not an integer number! Try again!')

for number in list_1:
    if number % 2 == 0:
        list_2.append(number)

for number in list_1:
    if number not in list_2:
        list_2.append(number)

print(f'List with elements : {list_1}')
print(f'List with even numbers at the beginning: {list_2}')
