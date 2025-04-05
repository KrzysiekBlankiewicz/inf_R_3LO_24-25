def selectsort(lista):
    n = len(lista)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if lista[j] < lista[mini]:
                mini = j
        temp = lista[i]
        lista[i] = lista[mini]
        lista[mini] = temp
    return lista


lista = [9, 2, 3, 4, 5, 6, 7, 8, 1]
print(selectsort(lista))
