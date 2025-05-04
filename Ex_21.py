'''
Pobierz pięć liczb z klawiatury. Jeżeli tworzą ciąg rosnący (zgodnie z kolejnością
pobierania), poinformuj o tym.
'''

list = []
counter = 1

while counter <= 5:
    number=float(input(f'Enter the {counter} number of five: '))
    list.append(number)
    counter += 1


if list[0]<list[1] and list[1]<list[2] and list[2]<list[3] and list[3]<list[4]:
    print('Numbers are sort ascending!')
    print(list)
else:
    print('Numbers are sort descending or randomly!')
    print(list)