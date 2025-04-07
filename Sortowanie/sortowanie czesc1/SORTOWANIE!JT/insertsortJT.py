def insertsort(lista):
    for i in range(1, len(lista)):
        k = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > k:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = k
    return lista

lista = [9, 2, 3, 4, 5, 6, 7, 8, 1]
print(insertsort(lista))
