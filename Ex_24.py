'''Pobieraj z klawiatury znaki (bez polskich ogonków i bez dużych liter) i wprowadzaj
je do listy według zasady: samogłoski zawsze na początku listy, pozostałe znaki na
końcu listy. Jeżeli pojawi się znak * lub #, nie wstawiaj ich, tylko usuń z listy pierwszy
znak (dla *) lub ostatni (dla #), o ile jest co usuwać. Zakończ pętlę pobierania i wstawiania,
gdy wprowadzony będzie znak ! (wykrzyknik).'''

list=[]
vowels = 'aeiouy'

while True:
    char=str(input("Podaj znak: "))
    if char == "!":
        break
    elif char =="*":
        if list:
            list.pop(0)
        else:
            print("List is empty, can't remove first element from the list")
    elif char == "#":
        if list:
            list.pop()
        else:
            print("List is empty, can't remove last element from the list")
    elif char in vowels:
        list.insert(0,char)
    else:
        list.append(char)

    print("Aktualna list: ",list)

print("Final list: ",list)
