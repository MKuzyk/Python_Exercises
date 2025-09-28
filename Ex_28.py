'''
Pobieraj w pętli jeden znak. Ignoruj znaki niebędące znakami cyfr (0 – 9). Przerwij
pętlę, gdy zbierzesz pięć znaków będących cyframi, np. '1', '4', '3', '5', '0'. Utwórz
zmienną całkowitą, która będzie liczbą utworzoną z tych cyfr. Dla podanego przykładu
byłaby to liczba całkowita: 14 350. Utwórz również liczbę w odwrotnej kolejności
cyfr. W obu przypadkach, gdy liczba zaczyna się od cyfr 0, należy je zignorować.
Na przykład 05341 to 5341. Wyświetl sumę obu powstałych liczb.
'''

lista_1=[]

while len(lista_1)<5:
    znak=input("Podaj znak: ")
    if znak.isdigit():
        lista_1.append(znak)
    else:
        print("To nie jest cyfra!")
print("Zebrane cyfry to: ",lista_1)

liczba = int("".join(lista_1))

print("Liczba utworzona z cyfr z listy to:",liczba)

liczba_odwrotna = int("".join(lista_1[::-1]))

print("Liczba utworzona z cyfr pobieranych w odwrotnej kolejności z listy to:",liczba_odwrotna)

print("Suma obu powstałych liczb to: ", liczba+liczba_odwrotna)






