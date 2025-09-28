'''
Pobieraj liczby z klawiatury i wkładaj je do listy pod warunkiem, że taka liczba
jeszcze w liście nie istnieje. Jeżeli istnieje, zignoruj ją i pobieraj dalej. Zakończ pobieranie,
gdy lista będzie zawierała dziesięć liczb [2].
Zrób to samo zadanie z wykorzystaniem zbioru (set) [1].
'''

list =[]

while len(list)<10:
    number = int(input("Podaj liczbę: "))
    if number not in list:
        list.append(number)
    else:
        print("Number is already in the list!")


print("Gotowa lista: ",list)