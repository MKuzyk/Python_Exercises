sequence = []

# Generujemy 100 elementów ciągu
n = 1
while len(sequence) < 100:
    sequence.extend([n] * n)
    n += 1

# Wyświetlamy pierwsze 100 elementów
print(sequence[:100])