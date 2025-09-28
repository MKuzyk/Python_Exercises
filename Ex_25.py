'''Pobieraj w pętli liczby całkowite z klawiatury, wkładaj je do listy V. Szczegółowe
postępowanie we wnętrzu pętli to następujące kroki:
1. Pobierz liczbę i wprowadź ją na koniec listy.
2. Pobierz liczbę i wprowadź ją na koniec listy (tak, takie samo polecenie
w ramach kroku pętli) [1].
3. Jeżeli iloczyn dwóch ostatnich liczb z listy nie przekracza 1000, wprowadź
również ten iloczyn do listy V i wróć do punktu 1., a jeżeli ten iloczyn przekroczył
wartość 1000, zakończ pętlę [1].
Pokaż listę po wyjściu z pętli.'''

list=[]

while True:

    data_1=int(input("Podaj liczbę: "))
    list.append(data_1)

    data_2 = int(input("Podaj liczbę: "))
    list.append(data_2)

    product=list[-1]*list[-2]
    if product<=1000:
        list.append(product)
    else:
        break

print("List after loop ended",list)

