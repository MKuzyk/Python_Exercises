'''
Pobierz liczbę całkowitą z klawiatury i sprawdź, czy jest podzielna: przez 3 i przez 5;
przez 3, ale nie przez 5; przez 5, ale nie przez 3; ani przez 3, ani przez 5. Właściwą
odpowiedź wyświetl na ekranie.
'''

def number(number):
    while True:
        try:
            num = int(input(number))
            if num % 3 == 0 and num % 5 == 0:
                print(f"{num} jest podzielna przez 3 i przez 5!")
            elif num % 3 == 0 and num % 5 != 0:
                print(f"{num} jest podzielna przez 3 ale nie przez 5!")
            elif num % 3 != 0 and num % 5 != 0:
                print(f"{num} nie jest podzielna przez 3 oraz nie przez 5!")
            return num
        except ValueError:
            print("To nie jest liczba całkowita!")

num = number("Podaj liczbę całkowita: ")