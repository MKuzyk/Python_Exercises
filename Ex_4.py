'''
Pobierz znak z klawiatury. Sprawdź, czy to samogłoska, spółgłoska, czy cyfra. Poinformuj
o tym, jaki to znak. Uwzględnij tylko małe litery alfabetu angielskiego i cyfry.
'''


def check_character(char):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    digits = "0123456789"

    if char in vowels:
        print(f"Znak '{char}' to samogłoska.")
    elif char in consonants:
        print(f"Znak '{char}' to spółgłoska.")
    elif char in digits:
        print(f"Znak '{char}' to cyfra.")
    else:
        print("Podano niepoprawny znak. Wprowadź małą literę lub cyfrę.")


# Pobranie znaku od użytkownika
char = input("Podaj jeden znak: ").strip()

if len(char) == 1:
    check_character(char)
else:
    print("Wprowadź tylko jeden znak!")
