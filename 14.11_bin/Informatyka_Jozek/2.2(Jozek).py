#file = open().readlines()

#for line in file:
    #line = line [0,-1]

file = ['11111', '111110010', '1110000', '1111100000', '10001111110111100000', '1111110000100000', '101']


def algorytm_bin(binarna):
    ile_blokow = 1
    pocz = 0
    if binarna[0] == "1":
        pocz = 1
    if binarna[0] == "0":
        pocz = 0
    aktualna = pocz
    for i in binarna:
        if i == "1" and aktualna == 0:
            ile_blokow += 1
            aktualna = 1
        if i == "0" and aktualna == 1:
            ile_blokow += 1
            aktualna = 0
    return ile_blokow

wynik = 0
for j in range (0,len(file)):
    if algorytm_bin(file[j]) <3:
        wynik +=1

print(wynik)