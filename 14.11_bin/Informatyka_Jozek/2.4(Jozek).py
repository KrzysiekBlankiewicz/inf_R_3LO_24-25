

def XOR (a, b):  #jednak niepotrzebne, obliczylem recznie
    wieksza = 0
    mniejsza = 0
    if a > b:
        wieksza = a
        mniejsza = b
    else:
        wieksza = b
        mniejsza = a


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

def konwert_na_dz(biny):
    dziesietna = 0
    for i in range(0, len(biny)):
        if biny[i] == "1":
            dziesietna += 2 ** (len(biny) - i - 1)
    return dziesietna



print(konwert_na_dz("1111011"))


# print(konwert_na_biny(123)) = "1111011"
# 2D w 16 = (2*16 + 13*1) = 45
# print(konwert_na_biny(45)) = "101101"