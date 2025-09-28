'''Utwórz listę zawierającą następujące cyfry (można skopiować z pliku 26_lista.txt):
v=[1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9]
Znajdź w liście i wyświetl wszystkie podciągi trójelementowe (trzy kolejne cyfry
listy), które tworzą ciągi niemalejące [2]. Znajdź przynajmniej jeden najdłuższy
podciąg niemalejący [4]. Policz liczbę wystąpień każdej liczby w liście [1].'''

from collections import Counter

list=[1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9]

print("Trójelementowe podciągi niemalejące: a<=b<=c")

for i in range(len(list)-2):
    a,b,c=list[i],list[i+1],list[i+2]
    if a<=b<=c:
        print([a,b,c])

longest_list=[]
actual=[list[0]]

for i in range(1,len(list)):
    if list[i] >= list[i-1]:
        actual.append(list[i])
    else:
        if len(actual) > len(longest_list):
            longest_list=actual
        actual=[list[i]]

if len(actual) > len(longest_list):
    actual=longest_list

print("Najdłuższy podciąg niemalejący: ",longest_list)

element_count=Counter(list)

print("liczba wystąpień każdej cyfry: ")

for number, count in sorted(element_count.items()):
    print(f"{number}: {count}")