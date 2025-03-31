'''
Pobierz z klawiatury dwie liczby (float) i znak działania (jeden z tych: *, +, –, /).
W zależności od znaku wykonaj na pobranych dwóch liczbach odpowiednie
i możliwe działania i poinformuj o wyniku [1]. Zwróć uwagę na dzielenie przez 0!
Przykładowo, dla pobranej liczby 3 i 9,5 oraz znaku + zwróć sumę 3 + 9,5 równą 12,5.
Sprawdź też operację przy zamianie liczb miejscami [1]. Jeżeli wynik różni się od
wcześniejszego, wyświetl oba wyniki. Jeżeli jest taki sam, wyświetl go tylko jeden
raz. Na przykład dla liczb 5 i 2 oraz znaku / (dzielenie) trzeba wyświetlić 5/2 i 2/5,
ponieważ dają różny wynik.
'''


def math_operation(a,b,c):
    if c == '+':
        result = a+b
        print(f"{a} {c} {b} = {result}!")
    elif c=='-':
        result=a-b
        result_2=b-a
        if result!=result_2:
            print(f"{a} {c} {b} = {result}")
            print(f"{b} {c} {a} = {result_2}")
        else:
            print(f"{a} {c} {b} ={result}")
    elif c=='/':
        if a !=0 and b!=0:
            result=a/b
            result_2=b/a
            if result != result_2:
                print(f"{a} {c} {b} = {result}")
                print(f"{b} {c} {a} = {result_2}")
            else:
                print(f"{a} {c} {b} = {result}")
        elif a==0 and b!=0:
            result=a/b
            print(f"{a} {c} {b} = {result}")
        elif b==0 and a!=0:
            result=b/a
            print(f"{b} {c} {a} = {result}")
        else:
            print("Check if a = 0 and b = 0 / You can't divide by 0 !!")
    elif c=='*':
        result=a*b
        print(f"{a} {c} {b} = {result}")
    return

try:
    numebr_1 = float(input("Provide first (a) float number: "))
    number_2 = float(input("Provide second (b) float number: "))
    operation_sign = input("Provide one operation sign: multiplication (*) / division (/) / subtraction (-) / addition(+): ")
    print(f"You enter numbers a = {numebr_1}, b ={number_2}")
    math_operation(numebr_1,number_2,operation_sign)
except ValueError:
    print("You enter incorrect values or operation sign!!")