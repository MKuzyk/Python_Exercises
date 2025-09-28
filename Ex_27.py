'''Utwórz trzy listy (list) z następującą zawartością (plik 27_listy.txt):
v1=[1,3,5,7,9]
v2=[1,4,7,11,15]
v3=[1,2,3,4,5,6,7,8,9,20]
Potraktuj je jak zbiory, w których każdy element może wystąpić tylko jeden raz.
Przykładowo, po dodaniu do zbioru v1 liczby 5, zbiór nie uległby zmianie, gdyż 5
już tam jest. Dla podanych list/zbiorów wyświetl:
a) część wspólną zbiorów: v1 i v2 [2],
b) różnicę zbioru v3 i sumy zbiorów v1+v2 := v3–(v1+v2) [3],
c) sumę wszystkich zbiorów v1, v2 i v3 := v1+v2+v3 [2].
Wykonaj to zadanie jeszcze raz z wykorzystaniem zbiorów (set) [1].
Różnica zbioru A – B to takie elementy A, których nie ma w B. Suma zbiorów A + B
to wszystkie elementy z A i B (bez powtórzeń). Część wspólna A i B to tylko takie
elementy, którą są równocześnie w A i B.'''

v1=[1,3,5,7,9]
v2=[1,4,7,11,15]
v3=[1,2,3,4,5,6,7,8,9,20]

# a) część wspólną zbiorów: v1 i v2

czesc_wspolna=[]
for x in v1:
    if x in v2:
        czesc_wspolna.append(x)

# b) różnicę zbioru v3 i sumy zbiorów v1+v2 := v3–(v1+v2)

suma_v1_v2=[]

for x in v1+v2:
    if x not in suma_v1_v2:
        suma_v1_v2.append(x)

roznica=[]

for x in v3:
    if x not in suma_v1_v2:
        roznica.append(x)

# c) sumę wszystkich zbiorów v1, v2 i v3 := v1+v2+v3

suma_all=[]

for x in v1+v2+v3:
    if x not in suma_all:
        suma_all.append(x)

print("Część wspólna listy 1 i 2:", sorted(czesc_wspolna))
print("Różnica zbioru v3 i sumy zbiorów v1 i v2 to: ", sorted(roznica))
print("Suma zbiorów v1, v2, v3 to: ", sorted(suma_all))

print("Rozwiązanie z SET")

v1={1,3,5,7,9}
v2={1,4,7,11,15}
v3={1,2,3,4,5,6,7,8,9,20}

print("Część wspólna listy 1 i 2:", sorted(v1 & v2))
print("Różnica zbioru v3 i sumy zbiorów v1 i v2 to: ", sorted(v3 - (v1 | v2)))
print("Suma zbiorów v1, v2, v3 to: ", sorted(v1 | v2 | v3))