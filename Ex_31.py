'''Utwórz listę zawierającą kolejne liczby od 1 do 200. Wyświetl wszystkie podciągi
liczb sąsiednich składające się z sześciu liczb, których suma przekracza 800, ale nie
przekracza 1000 [2]. Ile ich jest? [1]'''

liczby = list(range(1, 201))

podciagi = [liczby[i:i+6] for i in range(len(liczby)-5)]

wynik = [p for p in podciagi if 800 < sum(p) <= 1000]

print("Podciągi spełniające warunek:")
for p in wynik:
    print(p)

print("Liczba takich podciągów:", len(wynik))

