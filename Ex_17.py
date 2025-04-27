'''
Zadanie 17. [2:1,1] <abc> {!}
Odgadnij wzór ciągu na podstawie pierwszych dziesięciu elementów [1], a następnie
wyświetl jego sto elementów [1]. Początek ciągu: 6, 2, 8, 3, 10 ,4, 12, 5, 14, 6, …
'''

sequence = []

# Generujemy 100 elementów ciągu
for i in range(100):
    if i % 2 == 0:  # Parzyste indeksy (1, 3, 5, 7, ...)
        sequence.append(6 + (i // 2) * 2)
    else:  # Nieparzyste indeksy (2, 4, 6, 8, ...)
        sequence.append(2 + (i // 2))

# Wyświetlamy pierwsze 100 elementów
print(sequence)

# Ostatni (setny) element ciągu
last_element = sequence[-1]
print(f"Ostatni (setny) element ciągu: {last_element}")