def konwert_na_biny(dz):
    binarna = ""
    while dz != 0:
        x = dz % 2
        dz = (dz - x) / 2
        if x == 0:
            binarna = "0" + binarna
        if x == 1:
            binarna = "1" + binarna
    return binarna

def algorytm(dziesietna):
    binarna = konwert_na_biny(dziesietna)
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



print(algorytm(67))
print(algorytm(245))