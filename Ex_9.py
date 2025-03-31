'''
Pobierz liczbę całkowitą z klawiatury i wykonaj na niej poniższe operacje: jeżeli
liczba była ujemna, zmniejsz ją o 1; jeżeli liczba była dodatnia, zwiększ ją o 1; jeżeli
była zerem, pozostaw bez zmian; Wyświetl liczbę po zmianach [1]. Następnie określ
parzystość liczby po zmianach i wyświetl informację na ten temat za pomocą adekwatnego
komunikatu [1].
'''

def add_one(a):
    if a < 0:
        a-=1
        print(a)
        if a % 2 == 0:
            print(f"number {a} is an even number")
        else:
            print(f"number {a} is an odd number")
    elif a > 0:
        a+=1
        print(a)
        if a % 2 == 0:
            print(f"number {a} is an even number")
        else:
            print(f"number {a} is an odd number")
    else:
        print(a)


try:
    number = int(input("Enter integer numebr: "))
    add_one(number)
except:
    print("You didn't enter integer number!!")
    number = int(input("Enter integer numebr: "))
    add_one(number)

