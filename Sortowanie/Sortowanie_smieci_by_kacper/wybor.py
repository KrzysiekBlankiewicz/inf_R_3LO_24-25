def selekcja_naturalna(lista):
    
    for x in range(len(lista)):
        mina = x
        for j in range(x+1, len(lista)):
            if lista[j] < lista[mina]:
                mina = j
        tym = lista[x]
        lista[x] = lista[mina]
        lista[mina] = tym
    return lista

posortowana = selekcja_naturalna([1,9,6,3,13])
print(posortowana)
