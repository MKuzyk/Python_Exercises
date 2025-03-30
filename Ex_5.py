'''
Masz takie wyrażenie: (((a1+a2)*a3)-a4)/a5 (elementy od a1 do a5 są typu zmiennoprzecinkowego:
float). Pobierz z klawiatury każdą ze zmiennych a1 do a5, oblicz
wartość wyrażenia i wyświetl wynik. Zwróć uwagę na wartość zmiennej a5. W przypadku,
gdy jej wartość będzie równa 0, nie wykonuj działania, tylko poinformuj o tym.
'''

def oblicz_wynik(a1,a2,a3,a4,a5):

    if a5==0:
        print("Piąta liczba musi być różna od zera / nie dziel przez 0")
    else:
        wynik =(((a1+a2)*a3)-a4)/a5
        print(f"Wynik wyrażenia to : {wynik}")

print("Obliczanie wyniku dla wyrażenia : (((a1+a2)*a3)-a4)/a5 ")


try:
    a1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
    a2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))
    a3 = float(input("Podaj trzecią liczbę zmiennoprzecinkową: "))
    a4 = float(input("Podaj czwartą liczbę zmiennoprzecinkową: "))
    a5 = float(input("Podaj piątą liczbę zmiennoprzecinkową: "))

    oblicz_wynik(a1,a2,a3,a4,a5)
except ValueError:
    print("Podano niepoprawną wartość. Wprowadź liczby zmiennoprzecinkowe.")


