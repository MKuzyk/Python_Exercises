'''
Pobierz pięć liczb całkowitych z klawiatury i wyświetl informację, ile spośród nich
było parzystych, a ile nieparzystych.
'''

def Liczby_calkowite(n):
    lista = []
    parzyste = []
    nieparzyste = []

    for i in range(n):
        try:
            liczba= int(input(f"Podaj {i+1} liczbę całkowitą:"))
            lista.append(liczba)
            if liczba % 2 ==0:
                parzyste.append(liczba)
            else:
                nieparzyste.append(liczba)
        except ValueError:
            print("Podano niepoprawną wartość. Wprowadź tylko liczby całkowite.")
            return Liczby_calkowite(n)
    # Wyświetlenie wyników
    print(f"Lista wszystkich liczb: {lista}\nIlość pobranych liczb wynosi {len(lista)}")
    print(f"Lista liczb parzystych: {parzyste}\nIlość liczb parzystych to: {len(parzyste)}")
    print(f"Lista liczb nieparzystych: {nieparzyste}\nIlość liczb nieparzystych to: {len(nieparzyste)}")



Liczby_calkowite(5)




