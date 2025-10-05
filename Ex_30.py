'''Pewien kosmiczny Blob, okrążający swoją gwiazdę, postanowił zwiększyć swoją
masę. Na początku Blob ważył 1 kg i przez pierwsze dwa okrążenia swojej gwiazdy
nie udało mu się wzrosnąć. Ale przy trzecim okrążeniu Blob ważył tyle, ile wynosiła
suma wartości jego wagi z ostatnich dwóch okrążeń (waga przy pierwszym okrążeniu
i waga przy drugim okrążeniu). Od tego momentu wszystko potoczyło się
błyskawicznie. Kolejne okrążenie ponownie zaowocowało wagą Bloba równą sumie
wag z ostatnich dwóch okrążeń i ten schemat trwał już cały czas. Ile wynosiła waga
kosmicznego Bloba po trzynastym okrążeniu macierzystej gwiazdy? Przyjmij, że
dwa pierwsze okrążenia to waga 1 i 1.
Blob jeszcze wróci! Natrafisz na niego w innych zadaniach. Zachowaj czujność'''

waga = [1, 1]
for i in range(2, 13):
    waga.append(waga[i-1] + waga[i-2])

print("Waga Bloba po 13 okrążeniach:", waga[12])