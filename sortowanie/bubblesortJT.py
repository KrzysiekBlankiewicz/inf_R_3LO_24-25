def bubblesort(lista):
    k = 0
    n = len(lista) - 1
    for j in range(n): 
        i = 0  
        while i < n - k:
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp 
            i += 1
        k += 1
    return lista

lista = [9, 2, 3, 4, 5, 6, 7, 8, 9]
print(bubblesort(lista))
