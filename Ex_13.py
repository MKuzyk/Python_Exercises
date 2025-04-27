'''
Zadanie 13. [1] <abc> {!}
Wyświetl w porządku rosnącym liczby całkowite od 1 do 120, z pominięciem liczb
podzielnych równocześnie przez 11 i 5. Wyświetl informacje, ile liczb się wyświetliło,
a ile zostało pominiętych.
'''

count_display = 0
count_skipped = 0

for i in range (1,121):
    if not i % 11 == 0 and not i % 5 == 0:
        count_display += 1
        print(i, end = ", ")
    else:
        count_skipped += 1
print("/n")
print("Ilość liczb wyświetlonych:", count_display)
print("Ilość liczb pominiętych:", count_skipped)