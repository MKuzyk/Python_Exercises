'''
Pobraną z klawiatury liczbę całkowitą zweryfikuj pod kątem parzystości. Wyświetl
adekwatny komunikat, gdy jest lub nie jest parzysta.
'''

def get_odd_or_even_number(number):
    while True:
        try:
            num = int(input(number))
            if num % 2 == 0:
                print(f"{num} jest liczbą parzystą.")
            else:
                print(f"{num} jest liczbą nieparzystą.")
            return num
        except ValueError:
            print("To nie jest liczba całkowita!")

num = get_odd_or_even_number("Podaj liczbę całkowita: ")