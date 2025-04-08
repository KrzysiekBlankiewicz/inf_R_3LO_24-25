def quicksort(lista):
    if len(lista) <= 1:
        return lista

    start = lista[0]  
    mniejsze = []
    wieksze = []

    for x in lista[1:]:
        if x <= start:
            mniejsze.append(x)
        else:
            wieksze.append(x)

    return quicksort(mniejsze) + [start] + quicksort(wieksze)
    
dane = [5, 3, 8, 4, 2, 7, 1, 10]
posortowane = quicksort(dane)
print(posortowane)
