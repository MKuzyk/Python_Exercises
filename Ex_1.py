'''
Pobierz z klawiatury trzy nieujemne liczby całkowite. Jeżeli któraś jest ujemna, powtórz
pobieranie. Następnie znajdź największą z nich [1]. Wyświetl sumę pozostałych
liczb tyle razy, ile wynosi wartość największej liczby [1].
'''

def get_non_negative_integer(number):
    while True:
        try:
            num = int(input(number))
            if num >= 0:
                return num
            else:
                print("Podaj liczbę nieujemną!")
        except ValueError:
            print("To nie jest liczba całkowita!")

# Pobieranie trzech liczb
num1 = get_non_negative_integer("Podaj pierwszą liczbę: ")
num2 = get_non_negative_integer("Podaj drugą liczbę: ")
num3 = get_non_negative_integer("Podaj trzecią liczbę: ")

# Znalezienie największej liczby
max_num = max(num1, num2, num3)

# Obliczenie sumy pozostałych liczb
sum_rest = (num1 + num2 + num3) - max_num

# Wyświetlenie sumy pozostałych liczb tyle razy, ile wynosi wartość największej liczby
for _ in range(max_num):
    print(sum_rest)
