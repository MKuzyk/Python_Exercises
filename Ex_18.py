'''
Zadanie 18. [2:1,1] <abc> {~}
Pobieraj liczbę z klawiatury i wyświetlaj jej dwukrotność. Operację powtarzaj, dopóki
nie zostanie wpisana wartość pomiędzy 1 a 10 włącznie [1]. Oblicz sumę wyświetlonych
elementów z pominięciem tej liczby, która kończy pętlę. Wyświetl tę
sumę [1].
'''

list=[]
counter = 0
total = 0

while True:
    try:
        number = int(input("Provide a number except numbers from rang [1:10]! "))
        if not 1 <= number <= 10:
            list.insert(counter,number)
            list.insert(counter+1, number)
            counter=len(list)+1
            print(list)
            continue
        else:
            for numbers in list:
                total = sum(list)
            print("You entered the number invalid range !")
            print(f"Sum is:  {total}")
            break
    except ValueError:
        for numbers in list:
            total = sum(list)
        print(f"Sum is:  {total}")
        break


