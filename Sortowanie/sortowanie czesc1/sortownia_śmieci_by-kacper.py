def bubel(lista):
    nig = len(lista)
    for i in range(nig):
        for j in range(0, nig - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(bubel([1,5,2,3,8,10,7]))

def wstawanie_jedynek(lista):
    for i in range(1, len(lista)):
        sigma = lista[i]
        j = i - 1
        while j >= 0 and sigma < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = sigma
    return lista

print(wstawanie_jedynek([1,5,2,3,8,10,7]))

def wolosc_wyboru(lista):
    n = len(lista)
    for i in range(n):
        mina = i
        for j in range(i+1, n):
            if lista[j] < lista[mina]:
                mina = j
        lista[i], lista[mina] = lista[mina], lista[i]
    return lista

print(wolosc_wyboru([1,5,2,3,8,10,7]))

