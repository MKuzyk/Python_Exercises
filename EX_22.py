'''
Pobieraj liczby z klawiatury i wkładaj je do listy [1]. Pobieranie ma się zakończyć,
gdy zostanie wprowadzona dwa razy z rzędu taka sama liczba [1].
'''

list=[]
counter = 1

while True:
    number = float(input(f'Enter the {counter} number: '))
    if number in list:
        break
    else:
        list.append(number)
        counter += 1

print(list)