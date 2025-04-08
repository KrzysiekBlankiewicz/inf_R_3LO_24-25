def sigma1(lista, low, high):
    piwo = lista[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and lista[i] <= piwo:
            i =i+ 1
        while j >= low + 1 and lista[j] > piwo:
            j =j- 1
        if i < j:
                tym =lista[low]
                lista[low] = lista[j]
                lista[j] = tym
    tym =lista[low]
    lista[low] = lista[j]
    lista[j] = tym
    return j

def sigma2(lista, low, high):
    if low < high:
        index = sigma1(lista, low, high)
        sigma2(lista, low, index - 1)
        sigma2(lista, index + 1, high)

def szybek(lista):
    sigma2(lista, 0, len(lista) - 1)
    return lista

lista = [1,9,6,3,13]
print(szybek(lista))
