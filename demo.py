sequence = []

# Początkowa wartość
current_value = 100
decrement = 1

# Generujemy 100 elementów ciągu
for i in range(100):
    sequence.append(current_value)
    current_value -= decrement
    decrement += 1  # Zwiększamy spadek o 1 w każdej iteracji

# Ostatni (setny) element ciągu
last_element = sequence[-1]

# Wyświetlamy pierwsze 100 elementów
print(sequence)

# Wyświetlamy ostatni element
print(f"Ostatni (setny) element ciągu: {last_element}")