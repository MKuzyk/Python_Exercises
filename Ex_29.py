'''Kasia postanowiła w 2022 roku zaznaczać dni, w których udało jej się pilnować diety,
jak również te, w których jej się to nie udało. Dla każdego dnia roku, numerowanego
od 1 do 365, utwórz dla Kasi listę i skopiuj do niej następujące wartości, gdzie
1 to wartość True, a 0 to wartość False (plik 29_dieta.txt).
1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,
0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,
1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,
0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,
0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,
0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,
1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,1,1,0,1,
0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0,
1,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1
Każda cyfra (0 lub 1) to kolejny dzień udany (1) lub nieudany (0). Utwórz odpowiednią
listę zawierającą wyżej wymienione dane. Odpowiedz na następujące pytania:
 Przez ile dni w roku Kasia odnosiła sukces dietetyczny? [1]
 Ile było okresów trwających przynajmniej pięć dni z rzędu, które stanowiły
porażkę dietetyczną? Podaj numer dnia w roku rozpoczynającym każdy
z okresów [4].
Dane z pliku nie muszą być w tym zadaniu odczytywane przez Pythona. Możesz je
ręcznie skopiować do listy'''

from pathlib import Path

sciezka = Path("C:/Users/Administrator/Desktop/Podyplomówka_Python/Książki/pliki/29_dieta.txt")


with sciezka.open("r", encoding="utf-8") as plik:
    # Wczytujemy całą linię z pliku
    linia = plik.read().strip()          # np. '1,1,0,1,...'
    # Dzielimy po przecinku i konwertujemy każdy element na int
    dane = [int(x) for x in linia.split(',')]

print(dane)

sukcesy = dane.count(1)
print("Dni sukcesu:", sukcesy)

porazki = []
i = 0
while i < len(dane):
    if dane[i] == 0:
        start = i  # numer indeksu początkowego
        length = 0
        while i < len(dane) and dane[i] == 0:
            length += 1
            i += 1
        if length >= 5:
            porazki.append(start + 1)  # +1 bo dni liczymy od 1
    else:
        i += 1

print("Okresy porażki zaczynają się w dniach:", porazki)