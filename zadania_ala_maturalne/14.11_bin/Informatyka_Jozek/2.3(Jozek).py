#file = open().readlines()

#for line in file:
    #line = line [0,-1]
file = ['11111', '111110010', '1110000', '1111100000', '10001111110111100000', '1111110000100000', '101']


def konwert_na_dz(biny):
    dziesietna = 0
    for i in range(0, len(biny)):
        if biny[i] == "1":
            dziesietna += 2 ** (len(biny) - i - 1)
    return dziesietna

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

najwieksza = 0
for j in range (0,len(file)):
    if konwert_na_dz(file[j]) > najwieksza:
        najwieksza = konwert_na_dz(file[j])

print(konwert_na_biny(najwieksza))