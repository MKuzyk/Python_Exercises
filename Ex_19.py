'''
Wyświetl wszystkie liczby podzielne przez 6 ze zbioru od 0 do 1000 włącznie [1].
Ile ich było? Ile wśród tych liczb było takich, które zawierają cyfrę 7? Wyświetl oddzielnie
również te liczby i ich ilość [2].
'''

numbers = []
number =0

while number <= 1000:
    if  number % 6 == 0:
        numbers.append(number)
    number += 1

print(f'liczby ze zbioru od 0 do 1000 podzielne przez 6 to :'
      f'{numbers}')

counter = 0

for number in numbers:
    counter += 1
print(f'Iloąć liczb w zbiorze: {counter}')
print(f'Ilość liczb w zbiorze: {len(numbers)}')

numbers_7 = []
number_7 = 0

while number_7 < len(numbers):
    if '7' in str(numbers[number_7]):
        numbers_7.append(numbers[number_7])
    number_7 += 1

print(f'Liczby zawierające cyfrę 7 : {numbers_7}')
print(f'Ilość liczb zawierającą liczbę 7 to: {len(numbers_7)}')

